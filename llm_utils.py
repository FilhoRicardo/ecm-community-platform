
from __future__ import annotations

import os
import re
from collections import Counter
from typing import Any

import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
# Quality default for ranking shortlists. If you want lower latency, switch to:
# nvidia/nemotron-3-nano-30b-a3b:free
OPENROUTER_MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ── User-provided key (set via Settings page) ──────────────────────────────────
def get_api_key() -> str:
    """Return user-provided key from session state, falling back to env var."""
    # st may not be imported here; import lazily at call site via st.session_state
    _st = None
    try:
        import streamlit as st
        _st = st
    except ImportError:
        return OPENROUTER_API_KEY
    user_key = _st.session_state.get("openrouter_api_key", "")
    return user_key or OPENROUTER_API_KEY


class LLMError(RuntimeError):
    pass


def _tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", (text or "").lower())


def _token_score(query: str, item: dict[str, Any]) -> float:
    qset = set(_tokens(query))
    if not qset:
        return 0.0
    haystack = " ".join(
        [
            item.get("title", ""),
            item.get("excerpt", ""),
            item.get("building_type", ""),
            item.get("content", "")[:1600],
        ]
    ).lower()
    counts = Counter(_tokens(haystack))
    score = 0.0
    title_tokens = set(_tokens(item.get("title", "")))

    for tok in qset:
        score += min(counts.get(tok, 0), 4) * 2.0
    score += len(qset & title_tokens) * 4.0

    lowered_query = query.lower().strip()
    if lowered_query and lowered_query in haystack:
        score += 8.0
    for bt in ["office", "school", "retail", "grocery", "hospital", "warehouse", "lodging", "healthcare"]:
        if bt in lowered_query and bt in item.get("building_type", "").lower():
            score += 6.0
    return score


def _subset_index(items: list[dict[str, Any]], max_chars_per_item: int = 420) -> str:
    blocks: list[str] = []
    for item in items:
        excerpt = re.sub(r"\s+", " ", item.get("excerpt", ""))
        blocks.append(
            f"ID: {item['id']}\n"
            f"Building Type: {item['building_type']}\n"
            f"Title: {item['title']}\n"
            f"Summary: {excerpt[:max_chars_per_item]}"
        )
    return "\n\n---\n\n".join(blocks)


def _extract_json_array(text: str) -> list[str]:
    text = text.strip()
    if not text:
        raise LLMError("Empty model response.")
    try:
        parsed = json.loads(text)
        if isinstance(parsed, list):
            return [str(x) for x in parsed]
        if isinstance(parsed, dict) and isinstance(parsed.get("ids"), list):
            return [str(x) for x in parsed["ids"]]
    except Exception:
        pass

    match = re.search(r"\[[\s\S]*\]", text)
    if match:
        parsed = json.loads(match.group(0))
        if isinstance(parsed, list):
            return [str(x) for x in parsed]
    raise LLMError("Could not parse returned ECM IDs.")


def _call(system_prompt: str, user_prompt: str, max_tokens: int = 160) -> list[str]:
    # Resolve key: user-provided session key takes priority over env var
    api_key = OPENROUTER_API_KEY
    try:
        import streamlit as st
        user_key = st.session_state.get("openrouter_api_key", "")
        if user_key:
            api_key = user_key
    except ImportError:
        pass

    if not api_key:
        raise LLMError("No OpenRouter API key configured. Set OPENROUTER_API_KEY in .env or via Settings.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "ECM Community Platform",
    }
    payload: dict[str, Any] = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0,
        "max_tokens": max_tokens,
    }
    try:
        resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        content = data["choices"][0]["message"]["content"]
        return _extract_json_array(content)
    except Exception as exc:
        raise LLMError(f"OpenRouter request failed or returned an invalid response: {exc}") from exc


def _candidate_subset_for_query(query: str, ecms: list[dict[str, Any]], top_n: int = 18) -> list[dict[str, Any]]:
    ranked = sorted(ecms, key=lambda item: (_token_score(query, item), item["title"].lower()), reverse=True)
    positive = [item for item in ranked if _token_score(query, item) > 0]
    return (positive or ranked)[:top_n]


def _candidate_subset_for_profile(profile: dict[str, Any], ecms: list[dict[str, Any]], top_n: int = 18) -> list[dict[str, Any]]:
    building_type = str(profile.get("building_type", "")).strip().lower()
    profile_text = " ".join(
        [
            str(profile.get("building_type", "")),
            str(profile.get("location", "")),
            str(profile.get("heating_system", "")),
            str(profile.get("ventilation_mode", "")),
            str(profile.get("cooling_system", "")),
            str(profile.get("utility_summary", "")),
        ]
    )
    same_type = [item for item in ecms if item.get("building_type", "").lower() == building_type]
    pool = same_type if same_type else ecms
    ranked = sorted(pool, key=lambda item: (_token_score(profile_text, item), item["title"].lower()), reverse=True)
    positive = [item for item in ranked if _token_score(profile_text, item) > 0]
    return (positive or ranked)[:top_n]


def _profile_text_from_typology(typology_data: dict[str, Any], building_type: str) -> str:
    """Build a compact text block from NABERS-aligned typology inputs."""
    if not typology_data:
        return ""

    lines = []
    for key, val in typology_data.items():
        if val is None or val == "" or val == 0:
            continue
        label = key.replace("_", " ").replace(" m2", " m²").replace(" m3", " m³").replace(" kwh", " kWh").replace(" pct", "%").title()
        lines.append(f"{label}: {val}")
    return "; ".join(lines)


def recommend_ecms(profile: dict[str, Any], ecms: list[dict[str, Any]]) -> list[str]:
    subset = _candidate_subset_for_profile(profile, ecms, top_n=18)

    # Build full profile text including typology data
    typology_block = ""
    if profile.get("typology_data"):
        typology_block = _profile_text_from_typology(profile["typology_data"], profile.get("building_type", ""))
        if typology_block:
            typology_block = f"Typology data: {typology_block}\n"

    profile_text = (
        f"Building Type: {profile.get('building_type')}\n"
        f"Location / Climate Zone: {profile.get('location')}\n"
        f"Heating System: {profile.get('heating_system')}\n"
        f"Ventilation Mode: {profile.get('ventilation_mode')}\n"
        f"Cooling System: {profile.get('cooling_system')}\n"
        f"{typology_block}"
        f"Context summary: {profile.get('utility_summary', '')}"
    )
    system = (
        "You rank Energy Conservation Measures for one building. "
        "Return ONLY a JSON array of exactly 5 ECM IDs from the provided shortlist. "
        "Favor practical, building-type-relevant measures that clearly match climate, HVAC type, ventilation mode, and likely utility pain points. "
        "No prose."
    )
    user = f"Rank the best 5 ECMs for this building profile.\n\n{profile_text}\n\nUse only IDs from this shortlist:\n{_subset_index(subset)}"

    try:
        ids = _call(system, user)
        valid = [ecm_id for ecm_id in ids if ecm_id in {item['id'] for item in subset}]
        if valid:
            return valid[:5]
    except LLMError:
        pass
    return [item["id"] for item in subset[:5]]


def search_ecms(query: str, ecms: list[dict[str, Any]]) -> list[str]:
    subset = _candidate_subset_for_query(query, ecms, top_n=18)
    system = (
        "You rank ECM IDs against a user query. "
        "Return ONLY a JSON array of exactly 5 ECM IDs from the provided shortlist. "
        "Favor direct relevance, actionable application, building-type fit, and strong keyword match. "
        "No prose."
    )
    user = f"User query:\n{query}\n\nChoose the best 5 ECM IDs from this shortlist:\n{_subset_index(subset)}"
    try:
        ids = _call(system, user)
        valid = [ecm_id for ecm_id in ids if ecm_id in {item['id'] for item in subset}]
        if valid:
            return valid[:5]
    except LLMError:
        pass
    return [item["id"] for item in subset[:5]]
