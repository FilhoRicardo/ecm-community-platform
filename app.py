
from __future__ import annotations

import re
from typing import Any

import requests
import streamlit as st
from dotenv import load_dotenv
from markdown import markdown

from db_utils import DBError, get_vote_score_map, record_vote, upsert_ecm_metadata
from ecm_utils import USER_FACING_BUILDING_TYPES, load_ecms
from llm_utils import LLMError, OPENROUTER_MODEL, fetch_available_models, get_model, recommend_ecms, search_ecms

load_dotenv()
st.set_page_config(page_title="ECM Community Platform", page_icon="⚡", layout="wide")

HEATING_OPTIONS = ["Gas Furnace", "Heat Pump", "Electric Baseboard", "Boiler", "District Heating", "Other"]
VENT_OPTIONS = ["Natural", "Mechanical ERV/HRV", "Mixed Mode", "None"]
COOLING_OPTIONS = ["Central AC", "Mini-Split", "Evaporative", "District Cooling", "None"]

# ASHRAE/IECC Climate Zones with NOAA-derived HDD65 / CDD50 estimates
# Sources: NOAA nClimGrid data, ASHRAE 90.1-2019 Table B-4, EIA CBECS
# HDD = Heating Degree Days (base 65°F), CDD = Cooling Degree Days (base 50°F)
CLIMATE_ZONES = {
    "1A — Very Hot Humid (Miami, FL)":              {"hdd": 200,   "cdd": 5000, "examples": "Miami, Honolulu, Manila"},
    "2A — Hot Humid (Houston, TX)":                  {"hdd": 1500,  "cdd": 4000, "examples": "Houston, New Orleans, Tampa"},
    "2B — Hot Dry (Phoenix, AZ)":                    {"hdd": 1500,  "cdd": 4500, "examples": "Phoenix, Las Vegas, Dubai"},
    "3A — Warm Humid (Atlanta, GA)":                 {"hdd": 3000,  "cdd": 2500, "examples": "Atlanta, Shanghai, Sydney"},
    "3B — Warm Dry (Las Vegas, NV)":                 {"hdd": 3000,  "cdd": 3000, "examples": "Las Vegas, Tehran, Beijing"},
    "3C — Warm Marine (San Francisco, CA)":           {"hdd": 3000,  "cdd": 1000, "examples": "San Francisco, Lisbon, Melbourne"},
    "4A — Mixed Humid (Baltimore, MD)":              {"hdd": 5000,  "cdd": 1500, "examples": "Baltimore, Philadelphia, Nanjing"},
    "4B — Mixed Dry (Albuquerque, NM)":              {"hdd": 5000,  "cdd": 1500, "examples": "Albuquerque, Denver, Madrid"},
    "4C — Mixed Marine (Seattle, WA)":               {"hdd": 5000,  "cdd": 500,  "examples": "Seattle, Portland OR, Vancouver"},
    "5A — Cold Humid (Chicago, IL)":                 {"hdd": 7000,  "cdd": 800,  "examples": "Chicago, Boston, New York"},
    "5B — Cold Dry (Denver, CO)":                    {"hdd": 7000,  "cdd": 800,  "examples": "Denver, Minneapolis, Warsaw"},
    "5C — Cold Marine (Portland, OR)":               {"hdd": 6000,  "cdd": 600,  "examples": "Portland OR, Belfast, Zurich"},
    "6A — Very Cold Humid (Minneapolis, MN)":        {"hdd": 9000,  "cdd": 400,  "examples": "Minneapolis, Toronto, Harbin"},
    "6B — Very Cold Dry (Helena, MT)":               {"hdd": 9000,  "cdd": 400,  "examples": "Helena, Billings, Ulaanbaatar"},
    "7 — Frigid (Duluth, MN)":                       {"hdd": 11000, "cdd": 200,  "examples": "Duluth, Fairbanks, Murmansk"},
    "8 — Subarctic (Fairbanks, AK)":                {"hdd": 14000, "cdd": 50,   "examples": "Fairbanks, Barrow, Yakutsk"},
    "Not Sure / Manual Entry":                        {"hdd": None,  "cdd": None, "examples": ""},
}
CLIMATE_ZONE_OPTIONS = list(CLIMATE_ZONES.keys())

# Typology-specific input schemas (NABERS-aligned inputs)
# Note: HDD/CDD are handled at the top-level form via ASHRAE climate zone selector.
# Only building-specific fields go here.
TYPOLOGY_SCHEMAS = {
    "Office (Zero Energy)": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "renewable_pct":    {"label": "Renewable energy purchased (%)", "type": "number", "default": 0},
        "nla_m2":           {"label": "Net Leasable Area (m²)", "type": "number", "default": 0},
        "weekly_hours":     {"label": "Weekly operating hours", "type": "number", "default": 40},
        "computer_count":   {"label": "Computer count", "type": "number", "default": 0},
    },
    "Office": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "renewable_pct":    {"label": "Renewable energy purchased (%)", "type": "number", "default": 0},
        "nla_m2":           {"label": "Net Leasable Area (m²)", "type": "number", "default": 0},
        "weekly_hours":     {"label": "Weekly operating hours", "type": "number", "default": 40},
        "computer_count":   {"label": "Computer count", "type": "number", "default": 0},
    },
    "K-12 (50%)": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "renewable_pct":     {"label": "Renewable energy (%)", "type": "number", "default": 0},
        "floor_area_m2":     {"label": "Total floor area (m²)", "type": "number", "default": 0},
        "student_count":     {"label": "Student count", "type": "number", "default": 0},
        "weekly_hours":      {"label": "Weekly operating hours", "type": "number", "default": 40},
    },
    "K-12 (Zero Energy)": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "renewable_pct":     {"label": "Renewable energy (%)", "type": "number", "default": 0},
        "floor_area_m2":     {"label": "Total floor area (m²)", "type": "number", "default": 0},
        "student_count":     {"label": "Student count", "type": "number", "default": 0},
        "weekly_hours":      {"label": "Weekly operating hours", "type": "number", "default": 40},
    },
    "Highway Lodging": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "annual_water_m3":   {"label": "Annual water consumption (m³)", "type": "number", "default": 0},
        "guest_rooms":       {"label": "Number of guest rooms", "type": "number", "default": 0},
        "star_rating":       {"label": "Hotel star rating", "type": "select", "options": ["1★", "2★", "3★", "4★", "5★"], "default": "3★"},
        "laundry_rooms":    {"label": "Number of laundry-serviced rooms", "type": "number", "default": 0},
        "pool_area_m2":     {"label": "Area of heated swimming pools (m²)", "type": "number", "default": 0},
        "weekly_hours":     {"label": "Weekly operating hours (reception)", "type": "number", "default": 168},
    },
    "Small Warehouse / Self-Storage": {
        "annual_energy_kwh":   {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "conditioned_area_m2": {"label": "Conditioned floor area (m²)", "type": "number", "default": 0},
        "non_conditioned_area_m2": {"label": "Non-conditioned floor area (m²)", "type": "number", "default": 0},
        "cold_store_m3":       {"label": "Cold store volume (m³)", "type": "number", "default": 0},
        "weekly_hours":        {"label": "Weekly operating hours", "type": "number", "default": 40},
    },
    "Retail (Medium / Big Box)": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "annual_water_m3":   {"label": "Annual water consumption (m³)", "type": "number", "default": 0},
        "gla_m2":            {"label": "Gross Leasable Area (m²)", "type": "number", "default": 0},
        "tenancy_type":      {"label": "Primary tenancy type", "type": "select", "options": ["Fashion/Apparel", "Electronics", "Groceries", "Department Store", "Mixed-Use"], "default": "Mixed-Use"},
        "operating_hours":   {"label": "Daily operating hours", "type": "number", "default": 12},
        "food_court_seats":  {"label": "Food court seats", "type": "number", "default": 0},
    },
    "Grocery": {
        "annual_energy_kwh":   {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "annual_water_m3":     {"label": "Annual water consumption (m³)", "type": "number", "default": 0},
        "refrigerated_cases":  {"label": "Linear meters of refrigerated display cases", "type": "number", "default": 0},
        "cold_store_m3":       {"label": "Cold storage volume (m³)", "type": "number", "default": 0},
        "floor_area_m2":       {"label": "Total floor area (m²)", "type": "number", "default": 0},
        "operating_hours":     {"label": "Daily operating hours", "type": "number", "default": 14},
    },
    "Small Healthcare": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "annual_water_m3":   {"label": "Annual water consumption (m³)", "type": "number", "default": 0},
        "floor_area_m2":     {"label": "Total floor area (m²)", "type": "number", "default": 0},
        "weekly_hours":      {"label": "Weekly operating hours", "type": "number", "default": 80},
        "bed_count":         {"label": "Number of patient beds", "type": "number", "default": 0},
    },
    "Large Hospitals": {
        "annual_energy_kwh": {"label": "Annual energy consumption (kWh)", "type": "number", "default": 0},
        "annual_water_m3":   {"label": "Annual water consumption (m³)", "type": "number", "default": 0},
        "floor_area_m2":     {"label": "Total floor area (m²)", "type": "number", "default": 0},
        "weekly_hours":      {"label": "Weekly operating hours", "type": "number", "default": 168},
        "bed_count":         {"label": "Number of patient beds", "type": "number", "default": 0},
        "operating_rooms":   {"label": "Number of operating rooms", "type": "number", "default": 0},
    },
}


def build_typology_form(building_type: str) -> dict[str, Any]:
    """Render the typology-specific fields and return the values as a dict."""
    schema = TYPOLOGY_SCHEMAS.get(building_type, {})
    if not schema:
        st.info(f"No specific form fields for '{building_type}' yet.")
        return {}

    values: dict[str, Any] = {}
    with st.container(border=True):
        st.markdown("##### Building-Specific Data")
        cols = st.columns(2)
        for i, (key, field) in enumerate(schema.items()):
            col = cols[i % 2]
            with col:
                if field["type"] == "number":
                    values[key] = st.number_input(
                        field["label"],
                        value=field.get("default", 0),
                        step=1,
                        key=f"typo_{key}",
                    )
                elif field["type"] == "text":
                    values[key] = st.text_input(
                        field["label"],
                        value=field.get("default", ""),
                        key=f"typo_{key}",
                    )
                elif field["type"] == "slider":
                    values[key] = st.slider(
                        field["label"],
                        min_value=field["min"],
                        max_value=field["max"],
                        value=field.get("default", field["min"]),
                        key=f"typo_{key}",
                    )
                elif field["type"] == "select":
                    options = field["options"]
                    default = field.get("default")
                    default_index = options.index(default) if default in options else 0
                    values[key] = st.selectbox(
                        field["label"],
                        options=options,
                        index=default_index,
                        key=f"typo_{key}",
                    )
    return values


def typology_summary(building_type: str, values: dict[str, Any]) -> str:
    """Build a human-readable summary string from the typology inputs."""
    if not values:
        return "No specific data provided."

    lines = []
    for key, val in values.items():
        if val is None or val == "":
            continue
        label = key.replace("_", " ").title()
        lines.append(f"{label}: {val}")
    return "; ".join(lines)


@st.cache_resource
def _cached_load_ecms():
    ecms = load_ecms()
    return ecms, {item["id"]: item for item in ecms}


ECMS, ECM_BY_ID = _cached_load_ecms()

# Warm up DB index on startup (idempotent)
upsert_ecm_metadata(
    [
        {
            "id": item["id"],
            "filename": item["filename"],
            "title": item["title"],
            "building_type": item["building_type"],
        }
        for item in ECMS
    ]
)


def init_state() -> None:
    defaults = {
        "page": "Recommendations",
        "selected_ecm_id": ECMS[0]["id"] if ECMS else None,
        "recommendation_ids": [],
        "search_ids": [],
        "openrouter_api_key": "",
        "openrouter_model": OPENROUTER_MODEL,
    }
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)


def score_lookup() -> dict[str, int]:
    return get_vote_score_map()


def apply_css() -> None:
    st.markdown(
        '''
        <style>
        :root {
            --bg: #0d1117;
            --bg2: #111827;
            --card: #161b22;
            --card2: #1b2230;
            --border: #2a3240;
            --text: #e6edf3;
            --muted: #9aa4b2;
            --accent: #7aa2ff;
        }
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(70, 115, 188, 0.10), transparent 22%),
                linear-gradient(180deg, #0c1016, var(--bg));
            color: var(--text);
        }
        .block-container {
            max-width: 100%;
            padding-top: 0.9rem;
            padding-bottom: 1rem;
        }
        h1,h2,h3,h4,h5,h6,p,li,label,div,span { color: var(--text); }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #10161e, #0c1016);
            border-right: 1px solid var(--border);
        }
        .about-panel {
            background: linear-gradient(180deg, #151b24, #10161e);
            border: 1px solid var(--border);
            border-radius: 14px;
            padding: 1rem 1.1rem;
        }
        .about-panel h4 { margin-top: 0; margin-bottom: 0.4rem; font-size: 1.05rem; }
        .about-panel ol, .about-panel ul { padding-left: 1.1rem; margin: 0.4rem 0; }
        .about-panel li { margin-bottom: 0.3rem; line-height: 1.45; }

        .hero {
            background: linear-gradient(180deg, #151b24, #10161e);
            border: 1px solid var(--border);
            border-radius: 18px;
            padding: 1rem 1.15rem;
            margin-bottom: 0.9rem;
        }
        .hero-title { font-size: 1.15rem; font-weight: 800; }
        .hero-sub { color: var(--muted); font-size: 0.93rem; margin-top: 0.2rem; }

        .rail-title { font-weight: 800; margin-bottom: 0.45rem; }
        .muted { color: var(--muted); }

        .note-title {
            font-size: 1.35rem;
            font-weight: 800;
            line-height: 1.22;
            margin-bottom: 0.15rem;
        }
        .note-meta {
            color: var(--muted);
            font-size: 0.9rem;
            margin-bottom: 0.9rem;
        }
        .score-pill {
            display: inline-block;
            margin-left: 0.45rem;
            padding: 0.15rem 0.5rem;
            border-radius: 999px;
            border: 1px solid var(--border);
            color: var(--muted);
            font-size: 0.78rem;
        }

        .note-html h1, .note-html h2, .note-html h3 {
            margin-top: 1rem;
            margin-bottom: 0.45rem;
            padding-bottom: 0.2rem;
            border-bottom: 1px solid rgba(255,255,255,0.06);
        }
        .note-html p, .note-html li {
            line-height: 1.62;
            font-size: 0.98rem;
        }
        .note-html ul { margin-top: 0.2rem; }
        .note-html table {
            width: 100%;
            border-collapse: collapse;
            margin: 0.8rem 0 1rem 0;
            font-size: 0.92rem;
        }
        .note-html th, .note-html td {
            border: 1px solid var(--border);
            padding: 0.45rem 0.55rem;
            text-align: left;
        }
        .note-html th { background: rgba(255,255,255,0.04); }

        div[data-testid="stButton"] > button {
            border-radius: 12px;
            border: 1px solid var(--border);
            background: linear-gradient(180deg, #1b2330, #141b26);
            color: var(--text);
            min-height: 2.65rem;
        }
        div[data-testid="stButton"] > button:hover {
            border-color: #4d607f;
            color: white;
        }
        div[data-testid="stTextArea"] textarea,
        div[data-testid="stTextInput"] input,
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div,
        div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {
            background: #0f141b !important;
            color: var(--text) !important;
            border-color: var(--border) !important;
        }
        </style>
        ''',
        unsafe_allow_html=True,
    )


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter and [[wiki-link]] metadata tags from ECM content."""
    lines = content.splitlines()
    if lines and lines[0].strip() == "---":
        # Skip to end of frontmatter
        end = None
        for i, line in enumerate(lines[1:], start=1):
            if line.strip() == "---":
                end = i
                break
        if end is not None:
            lines = lines[end + 1:]
    text = "\n".join(lines)
    # Strip Obsidian [[wiki-links]] used as metadata tags
    text = re.sub(r'\[\[[^\]]*\|([^\]]*)\]\]', r'\1', text)  # [[Display Text|target]] → target
    text = re.sub(r'\[\[([^\]]*)\]\]', r'\1', text)          # [[target]] → target
    return text.lstrip("\n")


def sanitize_html(html: str) -> str:
    """Strip dangerous tags and attributes to prevent XSS when rendering ECM markdown."""
    # Remove script tags and their contents
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove style tags and their contents
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove event handler attributes (on*="...")
    html = re.sub(r'\bon\w+\s*=\s*(["\'][^"\']*["\']|[^\s>]*)', '', html, flags=re.IGNORECASE)
    # Remove iframes
    html = re.sub(r'<iframe[^>]*>.*?</iframe>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove forms
    html = re.sub(r'<form[^>]*>.*?</form>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove javascript: URIs in href/src
    html = re.sub(r'(href|src)\s*=\s*(["\']?)javascript:', r'\1=\2#', html, flags=re.IGNORECASE)
    return html


def render_note_html(markdown_text: str) -> str:
    clean = strip_frontmatter(markdown_text)
    html = markdown(clean, extensions=["tables", "fenced_code", "sane_lists"], output_format="html5")
    html = sanitize_html(html)
    return f"<div class='note-html'>{html}</div>"


def set_selected(ecm_id: str) -> None:
    st.session_state["selected_ecm_id"] = ecm_id



def render_left_rail(items: list[dict[str, Any]], key_prefix: str, scores: dict[str, int]) -> None:
    with st.container(border=True):
        st.markdown("<div class='rail-title'>ECMs</div>", unsafe_allow_html=True)
        if not items:
            st.info("No ECMs to show.")
            return
        selected_id = st.session_state.get("selected_ecm_id")
        for item in items:
            if st.button(item["title"], key=f"{key_prefix}::pick::{item['id']}", use_container_width=True):
                set_selected(item["id"])
                st.rerun()
            if item["id"] == selected_id:
                st.caption(f"{item['building_type']} · score {scores.get(item['id'], 0)}")


def render_feedback(item: dict[str, Any], key_prefix: str, scores: dict[str, int]) -> None:
    with st.container(border=True):
        st.subheader("Feedback")
        st.caption("Downvotes require a reason. Comments are stored in SQLite.")
        st.markdown(f"**Net score:** {scores.get(item['id'], 0)}")
        reason = st.text_area(
            "Comment / reason",
            key=f"{key_prefix}::reason::{item['id']}",
            height=240,
            placeholder="Required for thumbs down. Optional for thumbs up.",
            label_visibility="collapsed",
        )
        c1, c2 = st.columns(2)
        with c1:
            if st.button("👍 Upvote", key=f"{key_prefix}::up::{item['id']}", use_container_width=True):
                try:
                    record_vote(item["id"], item["title"], "thumbs_up", reason)
                    st.success("Saved.")
                    st.rerun()
                except DBError as exc:
                    st.error(str(exc))
        with c2:
            if st.button("👎 Downvote", key=f"{key_prefix}::down::{item['id']}", use_container_width=True):
                if not reason.strip():
                    st.error("Please enter a reason for thumbs down.")
                else:
                    try:
                        record_vote(item["id"], item["title"], "thumbs_down", reason)
                        st.success("Saved.")
                        st.rerun()
                    except DBError as exc:
                        st.error(str(exc))


def render_note(item: dict[str, Any], scores: dict[str, int]) -> None:
    with st.container(border=True):
        st.markdown(
            f"<div class='note-title'>{item['title']}<span class='score-pill'>score {scores.get(item['id'], 0)}</span></div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='note-meta'>{item['building_type']} · {item['filename']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(render_note_html(item["content"]), unsafe_allow_html=True)


def render_workspace(items: list[dict[str, Any]], key_prefix: str, scores: dict[str, int]) -> None:
    if not items:
        return
    ids = {item["id"] for item in items}
    selected_id = st.session_state.get("selected_ecm_id")
    if selected_id not in ids:
        selected_id = items[0]["id"]
        set_selected(selected_id)
    selected = ECM_BY_ID[selected_id]

    col_left, col_mid, col_right = st.columns([1.15, 2.8, 1.1], gap="medium")
    with col_left:
        render_left_rail(items, key_prefix, scores)
    with col_mid:
        render_note(selected, scores)
    with col_right:
        render_feedback(selected, key_prefix, scores)



def recommendation_page(scores: dict[str, int]) -> None:
    st.header("Building Profile → Top 5 ECM Recommendations")

    # Two-column layout: form on the left, About panel on the right.
    col_form, col_about = st.columns([2.6, 1], gap="medium")

    with col_about:
        render_about_panel()

    with col_form:
        # Climate zone lives OUTSIDE the form so selecting a zone triggers a rerun
        # that refreshes HDD/CDD. Widgets inside st.form don't rerun until submit.
        cz_col, hdd_col, cdd_col = st.columns([3, 1, 1])
        with cz_col:
            climate_zone = st.selectbox(
                "Climate Zone (ASHRAE/IECC)",
                options=CLIMATE_ZONE_OPTIONS,
                index=CLIMATE_ZONE_OPTIONS.index(st.session_state.get("profile_climate_zone", "Not Sure / Manual Entry")),
                key="profile_climate_zone",
            )
        # Reload HDD/CDD from the zone defaults whenever the selection changes.
        # Must write to session_state BEFORE the number_input widgets render,
        # otherwise Streamlit's widget-state precedence keeps the old values.
        if st.session_state.get("_loaded_zone_for_hdd_cdd") != climate_zone:
            zone_data = CLIMATE_ZONES.get(climate_zone, {})
            st.session_state["profile_hdd"] = zone_data.get("hdd") if zone_data.get("hdd") is not None else 0
            st.session_state["profile_cdd"] = zone_data.get("cdd") if zone_data.get("cdd") is not None else 0
            st.session_state["_loaded_zone_for_hdd_cdd"] = climate_zone
        with hdd_col:
            hdd = st.number_input(
                "HDD (heating)",
                min_value=0,
                max_value=20000,
                step=1,
                key="profile_hdd",
            )
        with cdd_col:
            cdd = st.number_input(
                "CDD (cooling)",
                min_value=0,
                max_value=10000,
                step=1,
                key="profile_cdd",
            )

        with st.form("recommendation_form", border=True):
            c1, c2 = st.columns(2)
            with c1:
                building_type = st.selectbox("Building Type", USER_FACING_BUILDING_TYPES, key="profile_building_type")
            with c2:
                location = st.text_input("Location", placeholder="e.g. Denver, CO")

            c_heat, c_vent, c_cool = st.columns(3)
            with c_heat:
                heating = st.selectbox("Heating System", HEATING_OPTIONS)
            with c_vent:
                ventilation = st.selectbox("Ventilation Mode", VENT_OPTIONS)
            with c_cool:
                cooling = st.selectbox("Cooling System", COOLING_OPTIONS)

            typo_values = build_typology_form(building_type)

            submitted = st.form_submit_button("Generate Top 5", use_container_width=False)

        st.caption(f"Model: `{get_model()}`")

    if submitted:
        try:
            full_values = {**typo_values, "hdd": hdd, "cdd": cdd, "climate_zone": climate_zone}
            summary = typology_summary(building_type, full_values)
            profile = {
                "building_type": building_type,
                "location": location or "Not specified",
                "climate_zone": climate_zone,
                "hdd": hdd,
                "cdd": cdd,
                "heating_system": heating,
                "ventilation_mode": ventilation,
                "cooling_system": cooling,
                "utility_summary": summary,
                "typology_data": full_values,
            }
            id_set, used_fallback, error_msg = recommend_ecms(profile, ECMS)
            valid = [ecm_id for ecm_id in id_set if ecm_id in ECM_BY_ID][:5]
            if valid:
                st.session_state["recommendation_ids"] = valid
                set_selected(valid[0])
                if used_fallback:
                    detail = error_msg or "Reason unknown."
                    st.warning(
                        f"LLM ranking unavailable — showing keyword-scored matches instead.\n\n**Reason:** {detail}"
                    )
            else:
                st.warning("No strong ECM matches were returned.")
        except ValueError as exc:
            st.error(str(exc))
        except LLMError as exc:
            st.error(str(exc))

    items = [ECM_BY_ID[ecm_id] for ecm_id in st.session_state.get("recommendation_ids", []) if ecm_id in ECM_BY_ID]
    if items:
        render_workspace(items, "rec", scores)


def browser_page(scores: dict[str, int]) -> None:
    st.header("ECM Browser")
    c1, c2, c3 = st.columns([1.6, 1.0, 1.4])
    with c1:
        filters = st.multiselect("Building Type Filter", USER_FACING_BUILDING_TYPES, default=USER_FACING_BUILDING_TYPES)
    with c2:
        sort_by = st.selectbox("Sort", ["Name", "Vote Score"])
    with c3:
        local_filter = st.text_input("Local Filter", placeholder="Title or keyword")

    items = [
        item
        for item in ECMS
        if item["building_type"] in filters
        and (
            not local_filter
            or local_filter.lower() in item["title"].lower()
            or local_filter.lower() in item["excerpt"].lower()
            or local_filter.lower() in item["content"].lower()
        )
    ]
    if sort_by == "Vote Score":
        items = sorted(items, key=lambda item: (scores.get(item["id"], 0), item["title"].lower()), reverse=True)
    else:
        items = sorted(items, key=lambda item: item["title"].lower())

    if items:
        render_workspace(items, "browser", scores)
    else:
        st.info("No ECMs match the current filter.")


def search_page(scores: dict[str, int]) -> None:
    st.header("Natural Language Search")
    query = st.text_input("Search", placeholder="e.g. reduce heating costs in a cold climate office")
    run = st.button("Run Search")
    if run:
        if not query.strip():
            st.error("Enter a query.")
        else:
            try:
                id_set, used_fallback, error_msg = search_ecms(query, ECMS)
                valid = [ecm_id for ecm_id in id_set if ecm_id in ECM_BY_ID][:5]
                st.session_state["search_ids"] = valid
                if valid:
                    set_selected(valid[0])
                    if used_fallback:
                        detail = error_msg or "Reason unknown."
                        st.warning(
                            f"LLM ranking unavailable — showing keyword-scored matches instead.\n\n**Reason:** {detail}"
                        )
                else:
                    st.warning("No strong ECM matches found.")
            except LLMError as exc:
                st.error(str(exc))

    items = [ECM_BY_ID[ecm_id] for ecm_id in st.session_state.get("search_ids", []) if ecm_id in ECM_BY_ID]
    if items:
        render_workspace(items, "search", scores)
    else:
        st.caption("The model is only used to rank ECM IDs. There is no chatbot interface.")


# ── OpenRouter sidebar config ──────────────────────────────────────────────────

OPENROUTER_API_BASE = "https://openrouter.ai/api/v1"
RECOMMENDED_MODELS = [
    "google/gemma-3-12b-it:free",
    "meta-llama/llama-3.2-3b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "openai/gpt-oss-20b:free",
    "anthropic/claude-3-haiku",
    "anthropic/claude-3.7-sonnet",
    "openai/gpt-4o-mini",
    "deepseek/deepseek-chat",
]


def _validate_api_key(api_key: str) -> tuple[bool, str]:
    """Return (ok, detail). detail is the OpenRouter response on failure."""
    try:
        models = fetch_available_models(api_key)
        return True, f"Loaded {len(models)} live models."
    except LLMError as exc:
        return False, str(exc)


@st.cache_data(ttl=300, show_spinner=False)
def _load_live_models(api_key: str) -> tuple[list[str], str | None]:
    """Fetch current models from OpenRouter and cache briefly per key."""
    try:
        return fetch_available_models(api_key), None
    except LLMError as exc:
        return [], str(exc)


def render_sidebar() -> None:
    """LLM configuration lives in the left sidebar — visible from every page."""
    with st.sidebar:
        st.markdown("### ⚙️  LLM Configuration")
        st.caption("Used to rank ECMs. Your key stays in this browser session only.")
        st.markdown("[Get a free key →](https://openrouter.ai/keys)")

        api_key_input = st.text_input(
            "OpenRouter API Key",
            value=st.session_state.get("openrouter_api_key", ""),
            type="password",
            placeholder="sk-or-v1-...",
            key="sidebar_api_key_input",
        )
        # Persist on every keystroke so users don't lose their key by forgetting
        # to click Validate.
        st.session_state["openrouter_api_key"] = api_key_input

        live_models: list[str] = []
        live_models_error: str | None = None
        if api_key_input.strip():
            live_models, live_models_error = _load_live_models(api_key_input.strip())
            st.session_state["openrouter_available_models"] = live_models
        else:
            st.session_state["openrouter_available_models"] = []

        if st.button("Validate key", use_container_width=True, key="sidebar_validate_btn"):
            if not api_key_input:
                st.error("Enter a key first.")
            else:
                ok, detail = _validate_api_key(api_key_input)
                if ok:
                    st.success("Key accepted by OpenRouter.")
                else:
                    st.error(f"Rejected: {detail}")

        if st.session_state.get("openrouter_api_key"):
            st.caption("✅ Key set in this session.")
            if live_models:
                st.caption(f"Loaded {len(live_models)} live models from OpenRouter for this key.")
            elif live_models_error:
                st.caption("Unable to load live models for this key.")
        else:
            st.caption("⚠️ No key set — using server key if available, else keyword fallback.")

        st.markdown("---")
        st.markdown("### 🧠  Model")
        model_options = live_models or RECOMMENDED_MODELS.copy()
        current = st.session_state.get("openrouter_model", OPENROUTER_MODEL)
        if live_models:
            if current not in model_options:
                fallback_model = OPENROUTER_MODEL if OPENROUTER_MODEL in model_options else model_options[0]
                st.session_state["openrouter_model"] = fallback_model
                current = fallback_model
                st.info(f"Selected model was unavailable. Switched to `{fallback_model}`.")
        elif current not in model_options:
            model_options.insert(0, current)
        st.selectbox(
            "Model",
            options=model_options,
            index=model_options.index(current),
            key="openrouter_model",
            label_visibility="collapsed",
        )
        st.caption(f"Default: `{OPENROUTER_MODEL}`")
        if live_models_error:
            st.warning(f"Live model refresh failed. Using fallback list.\n\n**Reason:** {live_models_error}")


def render_about_panel() -> None:
    """Short explanation of what the app does — shown alongside the recommendation form."""
    st.markdown(
        """
        <div class='about-panel'>
            <h4>What this does</h4>
            <p class='muted'>
                ECM Community Platform helps you discover Energy Conservation
                Measures (ECMs) ranked for your specific building.
            </p>
            <ol>
                <li>Pick a building type and climate zone — HDD/CDD auto-fill from ASHRAE/IECC defaults.</li>
                <li>Add HVAC systems and any NABERS-aligned operational data you have.</li>
                <li>Generate the top 5 ECMs ranked by an LLM against the 100+ measures in the library.</li>
                <li>Read each ECM in the centre pane; upvote the helpful ones, downvote with a reason.</li>
            </ol>
            <p class='muted'>
                No LLM key? You'll still get the top keyword-scored matches — just less tailored.
                Configure your OpenRouter key in the left sidebar.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    init_state()
    apply_css()
    render_sidebar()

    st.markdown(
        "<div class='hero'><div class='hero-title'>ECM Community Platform</div>"
        "<div class='hero-sub'>Discover and rank Energy Conservation Measures for your building. "
        "Configure your LLM key in the left sidebar.</div></div>",
        unsafe_allow_html=True,
    )

    page = st.segmented_control(
        "View",
        options=["Recommendations", "Browser", "Search"],
        default=st.session_state.get("page", "Recommendations"),
        key="page",
    )

    scores = score_lookup()
    if page == "Recommendations":
        recommendation_page(scores)
    elif page == "Browser":
        browser_page(scores)
    else:
        search_page(scores)


if __name__ == "__main__":
    main()
