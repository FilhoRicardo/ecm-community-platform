"""Tests for llm_utils — token scoring, candidate selection, and fallback logic."""
from __future__ import annotations

import pytest

import llm_utils


class TestTokenScore:
    def test_exact_phrase_match_boosts_score(self):
        ecm = {
            "title": "LED Lighting Controls",
            "excerpt": "Replace halogen with LED fixtures",
            "building_type": "Office",
            "content": "Replace halogen lamps with LED fixtures and add occupancy sensors.",
        }
        score = llm_utils._token_score("LED lighting", ecm)
        assert score > 0

    def test_title_match_boosts_score_more(self):
        ecm_title = {
            "title": "DHW Heat Pump",
            "excerpt": "Install a heat pump for domestic hot water",
            "building_type": "Office",
            "content": "Install a heat pump for domestic hot water.",
        }
        ecm_no_title = {
            "title": "Generic HVAC Upgrade",
            "excerpt": "Install a heat pump for domestic hot water",
            "building_type": "Office",
            "content": "Install a heat pump for domestic hot water.",
        }
        score_title = llm_utils._token_score("heat pump DHW", ecm_title)
        score_no_title = llm_utils._token_score("heat pump DHW", ecm_no_title)
        assert score_title > score_no_title

    def test_empty_query_returns_zero(self):
        ecm = {"title": "Test", "excerpt": "", "building_type": "Office", "content": ""}
        assert llm_utils._token_score("", ecm) == 0.0

    def test_building_type_match_boosts_score(self):
        ecm = {
            "title": "ERV Controls",
            "excerpt": "Install energy recovery ventilation",
            "building_type": "Highway Lodging",
            "content": "Install energy recovery ventilation in the guestroom corridors.",
        }
        score_bt = llm_utils._token_score("lodging ventilation", ecm)
        ecm_other = {**ecm, "building_type": "Office"}
        score_other = llm_utils._token_score("lodging ventilation", ecm_other)
        assert score_bt > score_other


class TestCandidateSubsetQuery:
    def test_returns_up_to_top_n(self):
        ecms = [
            {"id": f"ecm_{i}", "title": f"ECM {i}", "excerpt": "", "building_type": "Office", "content": ""}
            for i in range(30)
        ]
        subset = llm_utils._candidate_subset_for_query("ECM", ecms, top_n=5)
        assert len(subset) == 5

    def test_positive_scores_preferred(self):
        ecms = [
            {"id": "pos", "title": "LED lighting energy", "excerpt": "", "building_type": "Office", "content": "LED"},
            {"id": "neg", "title": "Generic", "excerpt": "", "building_type": "Office", "content": ""},
        ]
        subset = llm_utils._candidate_subset_for_query("LED", ecms, top_n=2)
        ids = [e["id"] for e in subset]
        assert "pos" in ids

    def test_fallback_when_no_positive_scores(self):
        ecms = [
            {"id": f"ecm_{i}", "title": f"ECM {i}", "excerpt": "", "building_type": "Office", "content": ""}
            for i in range(5)
        ]
        subset = llm_utils._candidate_subset_for_query("xyzzy nonsense", ecms, top_n=3)
        assert len(subset) == 3   # returns top_n even with zero keyword scores


class TestCandidateSubsetProfile:
    def test_filters_by_building_type(self):
        ecms = [
            {"id": "office_1", "title": "Office ECM", "excerpt": "", "building_type": "Office", "content": ""},
            {"id": "grocery_1", "title": "Grocery ECM", "excerpt": "", "building_type": "Grocery", "content": ""},
        ]
        profile = {"building_type": "Office", "location": "", "heating_system": "", "ventilation_mode": "", "cooling_system": "", "utility_summary": ""}
        subset = llm_utils._candidate_subset_for_profile(profile, ecms, top_n=5)
        ids = [e["id"] for e in subset]
        assert "office_1" in ids

    def test_fallback_to_all_ecms_when_no_type_match(self):
        ecms = [
            {"id": "ecm_1", "title": "ECM", "excerpt": "", "building_type": "Office", "content": ""},
        ]
        profile = {"building_type": "Unknown Type", "location": "", "heating_system": "", "ventilation_mode": "", "cooling_system": "", "utility_summary": ""}
        subset = llm_utils._candidate_subset_for_profile(profile, ecms, top_n=5)
        assert len(subset) == 1


class TestRecommendEcmsReturnsFallbackFlag:
    def test_returns_tuple_of_ids_and_fallback_bool(self):
        ecms = [
            {"id": "o:ECM_A.md", "title": "A", "excerpt": "", "building_type": "Office", "content": ""},
            {"id": "o:ECM_B.md", "title": "B", "excerpt": "", "building_type": "Office", "content": ""},
        ]
        profile = {
            "building_type": "Office",
            "location": "",
            "heating_system": "",
            "ventilation_mode": "",
            "cooling_system": "",
            "utility_summary": "",
            "typology_data": {},
        }
        # Without a valid API key the LLM call will fail and fall back
        result = llm_utils.recommend_ecms(profile, ecms)
        assert isinstance(result, tuple)
        assert len(result) == 2
        ids, used_fallback = result
        assert isinstance(ids, list)
        assert isinstance(used_fallback, bool)
        # Fallback should be True since no API key is set in tests
        assert used_fallback is True
        assert len(ids) == 2   # fallback returns all from subset


class TestSearchEcms:
    def test_query_length_capped(self):
        ecms = [
            {"id": f"e{i}", "title": "Test", "excerpt": "", "building_type": "Office", "content": ""}
            for i in range(5)
        ]
        long_query = "a" * 1000
        ids, used_fallback = llm_utils.search_ecms(long_query, ecms)
        # Should not crash; query is capped at 500 chars internally
        assert isinstance(ids, list)


class TestRateLimitImport:
    def test_rate_limit_function_exists(self):
        assert hasattr(llm_utils, "_check_rate_limit")
        assert callable(llm_utils._check_rate_limit)
