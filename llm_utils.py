from __future__ import annotations

import json
import os
import re
import time
from collections import Counter
from functools import lru_cache
from threading import Lock
from typing import Any

import requests
import streamlit as st

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# ── Rate limiting (per-process, thread-safe) ───────────────────────────────────
# NOTE: Under multi-process WSGI (e.g. gunicorn --workers N), each worker
# maintains its own counter. For true per-instance rate limiting across all
# workers, use a shared Redis counter instead.
_RATE_LIMIT_WINDOW_SECS = 60
_RATE_LIMIT_MAX_CALLS = 20
_rate_limit_calls: list[float] = []
_rate_limit_lock = Lock()


def _check_rate_limit() -> None:
    """Reject or sleep if more than _RATE_LIMIT_MAX_CALLS within the time window."""
    now = time.time()
    with _rate_limit_lock:
        global _rate_limit_calls
        # Evict expired entries
        _rate_limit_calls = [t for t in _rate_limit_calls if now - t < _RATE_LIMIT_WINDOW_SECS]
        if len(_rate_limit_calls) >= _RATE_LIMIT_MAX_CALLS:
            oldest = _rate_limit_calls[0]
            sleep_secs = _RATE_LIMIT_WINDOW_SECS - (now - oldest)
            if sleep_secs > 0:
                time.sleep(sleep_secs)
            # After sleeping, prune again
            _rate_limit_calls = [t for t in _rate_limit_calls if now - t < _RATE_LIMIT_WINDOW_SECS]
        _rate_limit_calls.append(now)


# ── User-provided key (set via Settings page) ──────────────────────────────────
def get_api_key() -> str:
    """Return user-provided key from session state, falling back to env var."""
    user_key = st.session_state.get("openrouter_api_key", "")
    return user_key or OPENROUTER_API_KEY


def get_model() -> str:
    """Return user-selected model from session state, falling back to default."""
    return st.session_state.get("openrouter_model", OPENROUTER_MODEL)


class LLMError(RuntimeError):
    pass


@lru_cache(maxsize=1024)
def _tokens(text: str) -> tuple[str, ...]:
    """Tokenize text into lowercase alphanumeric tokens. Cached for performance."""
    return tuple(re.findall(r"[a-z0-9]+", (text or "").lower()))


def _token_score(query: str, item: dict[str, Any], query_tokens: tuple[str, ...] | None = None) -> float:
    """Score a single ECM against a query. query_tokens optional to avoid re-tokenizing."""
    qset = query_tokens or _tokens(query)
    if not qset:
        return 0.0
    haystack = " ".join(
        [
            item.get("title", ""),
            item.get("excerpt", ""),
            item.get("building_type", ""),
            item.get("content", "")[:1200],   # capped at 1200 chars for scoring
        ]
    ).lower()
    counts = Counter(_tokens(haystack))
    score = 0.0
    title_tokens = set(_tokens(item.get("title", "")))

    for tok in qset:
        score += min(counts.get(tok, 0), 4) * 2.0
    score += len(set(qset) & title_tokens) * 4.0

    lowered_query = query.lower().strip()
    if lowered_query and lowered_query in haystack:
        score += 8.0
    for bt in ("office", "school", "retail", "grocery", "hospital", "warehouse", "lodging", "healthcare"):
        if bt in lowered_query and bt in item.get("building_type", "").lower():
            score += 6.0
    return score


def _score_ecms(query: str, ecms: list[dict[str, Any]]) -> list[tuple[dict[str, Any], float]]:
    """Score all ECMs once, returning (item, score) pairs sorted descending."""
    q_tokens = _tokens(query)
    scored = [(item, _token_score(query, item, q_tokens)) for item in ecms]
    scored.sort(key=lambda x: (x[1], x[0]["title"].lower()), reverse=True)
    return scored


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


def _call(system_prompt: str, user_prompt: str, max_tokens: int = 160, model: str | None = None) -> list[str]:
    """Call OpenRouter with rate limiting, retry logic and user-configured model/key."""
    api_key = get_api_key()
    if not api_key:
        raise LLMError("No OpenRouter API key configured. Set OPENROUTER_API_KEY in .env or via Settings.")

    # Rate limit check before making the request
    _check_rate_limit()

    model = model or get_model()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "ECM Community Platform",
    }
    payload: dict[str, Any] = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "temperature": 0,
        "max_tokens": min(max_tokens, 160),   # cap to prevent runaway completions
    }

    # Retry with exponential backoff on 5xx errors
    for attempt in range(3):
        try:
            resp = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)
            if resp.status_code >= 500:
                raise resp.raise_for_status()
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return _extract_json_array(content)
        except requests.exceptions.HTTPError as exc:
            if attempt == 2:
                raise LLMError(f"OpenRouter request failed after 3 attempts: {exc}") from exc
            time.sleep(min(2 ** attempt, 4))
        except Exception as exc:
            if attempt == 2:
                raise LLMError(f"OpenRouter request failed or returned an invalid response: {exc}") from exc
            time.sleep(min(2 ** attempt, 4))


def _candidate_subset_for_query(query: str, ecms: list[dict[str, Any]], top_n: int = 18) -> list[dict[str, Any]]:
    """Score all ECMs once and return the top_n that have positive scores, or top_n fallback."""
    scored = _score_ecms(query, ecms)
    positive = [item for item, score in scored if score > 0]
    return (positive or [item for item, _ in scored])[:top_n]


def _candidate_subset_for_profile(profile: dict[str, Any], ecms: list[dict[str, Any]], top_n: int = 18) -> list[dict[str, Any]]:
    """Pre-filter by building type, then score. Avoids full-list sort when type filter is effective."""
    building_type = str(profile.get("building_type", "")).strip().lower()
    same_type = [item for item in ecms if item.get("building_type", "").lower() == building_type]
    pool = same_type if same_type else ecms

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
    scored = _score_ecms(profile_text, pool)
    positive = [item for item, score in scored if score > 0]
    return (positive or [item for item, _ in scored])[:top_n]


_MAX_PROFILE_TEXT_CHARS = 800   # prevent unbounded prompt growth


def _profile_text_from_typology(typology_data: dict[str, Any], building_type: str) -> str:
    """Build a compact text block from NABERS-aligned typology inputs (capped)."""
    if not typology_data:
        return ""

    lines = []
    for key, val in typology_data.items():
        if val is None or val == "" or val == 0:
            continue
        label = key.replace("_", " ").replace(" m2", " m²").replace(" m3", " m³").replace(" kwh", " kWh").replace(" pct", "%").title()
        lines.append(f"{label}: {val}")
    text = "; ".join(lines)
    # Cap to prevent unbounded LLM prompt growth
    return text[:_MAX_PROFILE_TEXT_CHARS]


def recommend_ecms(profile: dict[str, Any], ecms: list[dict[str, Any]]) -> tuple[list[str], bool]:
    """
    Return (list_of_ecm_ids, used_fallback).
    used_fallback is True when the LLM call failed and keyword-sorted results were returned.
    """
    subset = _candidate_subset_for_profile(profile, ecms, top_n=18)

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
            return valid[:5], False
    except LLMError:
        pass
    return [item["id"] for item in subset[:5]], True


def search_ecms(query: str, ecms: list[dict[str, Any]]) -> tuple[list[str], bool]:
    """
    Return (list_of_ecm_ids, used_fallback).
    used_fallback is True when the LLM call failed and keyword-sorted results were returned.
    """
    # Cap query to prevent abuse
    query = query[:500]
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
            return valid[:5], False
    except LLMError:
        pass
    return [item["id"] for item in subset[:5]], True
