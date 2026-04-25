"""
Unit tests for llm_utils.py — scoring, tokenisation, JSON parsing.
Network calls to OpenRouter are mocked.
"""
from __future__ import annotations

import json
import pytest
from unittest.mock import patch, MagicMock

import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

import llm_utils


# ── Tokenisation ────────────────────────────────────────────────────────

class TestTokenisation:
    def test_lowercase_only(self):
        t = llm_utils._tokens("Hello WORLD 123")
        assert all(x.islower() or x.isdigit() for x in t)

    def test_non_alphanumeric_split(self):
        t = llm_utils._tokens("foo@bar!baz-qux")
        # punctuation removed; all tokens are pure alphanumeric
        assert all(tok.isalnum() for tok in t)

    def test_empty_string(self):
        assert llm_utils._tokens("") == ()
        assert llm_utils._tokens(None) == ()

    def test_cached_identical_output(self):
        a = llm_utils._tokens("hello world")
        b = llm_utils._tokens("hello world")
        assert a == b


# ── _token_score ────────────────────────────────────────────────────────

class TestTokenScore:
    def _item(self, title="", excerpt="", building_type="", content=""):
        return {"title": title, "excerpt": excerpt, "building_type": building_type, "content": content}

    def test_exact_phrase_bonus(self):
        item = self._item(title="Demand Ventilation", excerpt="Reduce outdoor air",
                          building_type="Office", content="...")
        # Query matching the full phrase in content should get +8
        score = llm_utils._token_score("reduce outdoor air", item)
        assert score >= 8.0

    def test_title_token_match_bonus(self):
        item = self._item(title="Heat Recovery", excerpt="Waste heat reclaim",
                          building_type="Hospital", content="...")
        score = llm_utils._token_score("heat", item)
        assert score > 0

    def test_building_type_match_bonus(self):
        item = self._item(title="ERV", excerpt="Energy recovery",
                          building_type="Office", content="...")
        score = llm_utils._token_score("office HVAC", item)
        assert score > 6.0  # building type bonus

    def test_zero_for_empty_query(self):
        item = self._item(title="Title", excerpt="Excerpt", building_type="Office", content="Body")
        assert llm_utils._token_score("", item) == 0.0

    def test_query_token_cap(self):
        """Each token contributes at most 4 * 2.0 = 8.0 per token (phrase bonus is separate)."""
        item = self._item(content="xyz123 " * 100)  # no 'xyz123' phrase match possible
        score = llm_utils._token_score("xyz123", item)
        # 'xyz123' in content gives +8 phrase bonus; token 'xyz123' capped at 4 hits * 2.0 = 8.0; title bonus = 0
        assert score == 16.0


# ── _score_ecms ────────────────────────────────────────────────────────

class TestScoreEcms:
    def _item(self, id_, title, score_anchor=0):
        return {"id": id_, "title": title, "excerpt": "", "building_type": "", "content": ""}

    def test_descending_order(self):
        ecms = [
            self._item("a", "Alpha"),
            self._item("b", "Bravo"),
            self._item("c", "Charlie"),
        ]
        scored = llm_utils._score_ecms("bravo", ecms)
        ids = [item["id"] for item, _ in scored]
        assert ids[0] == "b"

    def test_fallback_order_when_no_match(self):
        ecms = [
            self._item("x", "Xray"),
            self._item("y", "Yankee"),
        ]
        scored = llm_utils._score_ecms("zzz", ecms)
        ids = [item["id"] for item, _ in scored]
        assert set(ids) == {"x", "y"}


# ── _extract_json_array ─────────────────────────────────────────────────

class TestExtractJsonArray:
    def test_plain_json_array(self):
        result = llm_utils._extract_json_array('["a:b", "c:d"]')
        assert result == ["a:b", "c:d"]

    def test_dict_with_ids_key(self):
        result = llm_utils._extract_json_array('{"ids": ["x:y", "z:w"]}')
        assert result == ["x:y", "z:w"]

    def test_json_array_in_markdown_fence(self):
        result = llm_utils._extract_json_array(
            'Here is the list:\n```json\n["id1", "id2"]\n```'
        )
        assert result == ["id1", "id2"]

    def test_bare_array_syntax_in_text(self):
        result = llm_utils._extract_json_array('Use ["a:b","c:d"] please')
        assert result == ["a:b", "c:d"]

    def test_empty_string_raises(self):
        with pytest.raises(llm_utils.LLMError, match="Empty"):
            llm_utils._extract_json_array("")

    def test_malformed_raises(self):
        with pytest.raises(llm_utils.LLMError, match="Could not parse"):
            llm_utils._extract_json_array("not json at all {{{{[[[")


class TestMessageTextFromChoice:
    def test_string_content(self):
        choice = {"message": {"content": '["id1", "id2"]'}}
        assert llm_utils._message_text_from_choice(choice) == '["id1", "id2"]'

    def test_list_content(self):
        choice = {
            "message": {
                "content": [
                    {"type": "text", "text": '["id1", '},
                    {"type": "text", "text": '"id2"]'},
                ]
            }
        }
        assert llm_utils._message_text_from_choice(choice) == '["id1", "id2"]'


# ── _subset_index ──────────────────────────────────────────────────────

class TestModelCatalogHelpers:
    def test_is_text_generation_model_true_for_text_to_text(self):
        model = {
            "architecture": {
                "modality": "text+image->text",
                "input_modalities": ["text", "image"],
                "output_modalities": ["text"],
            }
        }
        assert llm_utils._is_text_generation_model(model) is True

    def test_is_text_generation_model_false_for_non_text_output(self):
        model = {
            "architecture": {
                "modality": "text->image",
                "input_modalities": ["text"],
                "output_modalities": ["image"],
            }
        }
        assert llm_utils._is_text_generation_model(model) is False

    def test_sort_model_ids_prefers_free_models(self):
        models = ["openai/gpt-4o-mini", "google/gemma-3-12b-it:free", "anthropic/claude-3-haiku"]
        assert llm_utils._sort_model_ids(models) == [
            "google/gemma-3-12b-it:free",
            "anthropic/claude-3-haiku",
            "openai/gpt-4o-mini",
        ]

    @patch("llm_utils.st.session_state", {"openrouter_available_models": ["openai/gpt-4o-mini", "deepseek/deepseek-chat"]})
    def test_candidate_models_for_request_uses_live_session_models(self):
        assert llm_utils._candidate_models_for_request("google/gemma-3-12b-it:free") == [
            "google/gemma-3-12b-it:free",
            "openai/gpt-4o-mini",
            "deepseek/deepseek-chat",
        ]


class TestFetchAvailableModels:
    @patch("llm_utils.requests.get")
    def test_returns_sorted_text_models(self, mock_get):
        response = MagicMock()
        response.status_code = 200
        response.json.return_value = {
            "data": [
                {
                    "id": "openai/gpt-4o-mini",
                    "architecture": {
                        "modality": "text->text",
                        "input_modalities": ["text"],
                        "output_modalities": ["text"],
                    },
                },
                {
                    "id": "google/gemma-3-12b-it:free",
                    "architecture": {
                        "modality": "text->text",
                        "input_modalities": ["text"],
                        "output_modalities": ["text"],
                    },
                },
                {
                    "id": "black-forest-labs/flux-1",
                    "architecture": {
                        "modality": "text->image",
                        "input_modalities": ["text"],
                        "output_modalities": ["image"],
                    },
                },
            ]
        }
        mock_get.return_value = response

        result = llm_utils.fetch_available_models("test-key")

        assert result == ["google/gemma-3-12b-it:free", "openai/gpt-4o-mini"]

    @patch("llm_utils.requests.get")
    def test_raises_on_rejected_key(self, mock_get):
        response = MagicMock()
        response.status_code = 401
        response.json.return_value = {"error": {"message": "Invalid API key"}}
        mock_get.return_value = response

        with pytest.raises(llm_utils.LLMError, match="Invalid API key"):
            llm_utils.fetch_available_models("bad-key")


class TestSubsetIndex:
    def _item(self, id_, title, excerpt, building_type="Office"):
        return {"id": id_, "title": title, "excerpt": excerpt, "building_type": building_type}

    def test_includes_id(self):
        items = [self._item("office:vav", "VAV", "Variable air volume")]
        idx = llm_utils._subset_index(items)
        assert "office:vav" in idx

    def test_truncates_long_excerpt(self):
        items = [self._item("x:y", "T", "word " * 300)]
        idx = llm_utils._subset_index(items, max_chars_per_item=60)
        # Should be truncated to ~60 chars
        assert len(idx) < 300

    def test_separator_between_items(self):
        items = [
            self._item("a:1", "One", "First"),
            self._item("b:2", "Two", "Second"),
        ]
        idx = llm_utils._subset_index(items)
        assert "\n\n---\n\n" in idx


# ── _candidate_subset_for_query ────────────────────────────────────────

class TestCandidateSubsetForQuery:
    def _item(self, id_, title, building_type="Office"):
        return {"id": id_, "title": title, "excerpt": "", "building_type": building_type, "content": ""}

    def test_returns_top_n(self):
        ecms = [self._item(str(i), f"ECM {i}") for i in range(30)]
        result = llm_utils._candidate_subset_for_query("ECM", ecms, top_n=5)
        assert len(result) == 5

    def test_all_positive_when_matches_exist(self):
        ecms = [
            self._item("1", "Heat Pump"),
            self._item("2", "Heat Recovery"),
            self._item("3", "Chiller"),
        ]
        result = llm_utils._candidate_subset_for_query("heat", ecms)
        ids = [e["id"] for e in result]
        assert "1" in ids
        assert "2" in ids


# ── recommend_ecms / search_ecms graceful fallback ───────────────────────

class TestRecommendEcmsFallback:
    """When the LLM call fails, both functions should return a deterministic fallback."""

    def _item(self, id_, title="Title", building_type="Office"):
        return {"id": id_, "title": title, "excerpt": "Excerpt", "building_type": building_type, "content": "Body text."}

    @patch("llm_utils._call")
    def test_recommend_falls_back_to_subset(self, mock_call):
        mock_call.side_effect = llm_utils.LLMError("Network error")
        ecms = [self._item(str(i)) for i in range(10)]
        profile = {"building_type": "Office"}
        result = llm_utils.recommend_ecms(profile, ecms)
        assert len(result[0]) == 5
        assert all(isinstance(r, str) for r in result[0])

    @patch("llm_utils._call")
    def test_search_falls_back_to_subset(self, mock_call):
        mock_call.side_effect = llm_utils.LLMError("Network error")
        ecms = [self._item(str(i)) for i in range(10)]
        result = llm_utils.search_ecms("HVAC", ecms)
        assert len(result[0]) == 5
        assert all(isinstance(r, str) for r in result[0])


class TestCallModelFallback:
    @patch("llm_utils.get_api_key", return_value="test-key")
    @patch("llm_utils._check_rate_limit")
    @patch("llm_utils.requests.post")
    def test_retries_with_default_model_when_selected_model_is_invalid(self, mock_post, _mock_rate, _mock_key):
        invalid = MagicMock()
        invalid.status_code = 404
        invalid.json.return_value = {"error": {"message": "No endpoints found for model"}}

        ok = MagicMock()
        ok.status_code = 200
        ok.raise_for_status.return_value = None
        ok.json.return_value = {"choices": [{"message": {"content": '["ecm-1", "ecm-2"]'}}]}

        mock_post.side_effect = [invalid, ok]

        result = llm_utils._call("system", "user", model="stale/model")

        assert result == ["ecm-1", "ecm-2"]
        assert mock_post.call_args_list[0].kwargs["json"]["model"] == "stale/model"
        assert mock_post.call_args_list[1].kwargs["json"]["model"] == llm_utils.OPENROUTER_MODEL

    @patch("llm_utils.get_api_key", return_value="test-key")
    @patch("llm_utils._check_rate_limit")
    @patch("llm_utils._candidate_models_for_request", return_value=["bad/model", "openai/gpt-4o-mini", "deepseek/deepseek-chat"])
    @patch("llm_utils.requests.post")
    def test_retries_across_multiple_live_models_when_provider_fails(self, mock_post, _mock_candidates, _mock_rate, _mock_key):
        bad = MagicMock()
        bad.status_code = 400
        bad.json.return_value = {"error": {"message": "Provider returned error"}}

        good = MagicMock()
        good.status_code = 200
        good.raise_for_status.return_value = None
        good.json.return_value = {"choices": [{"message": {"content": '["ecm-1"]'}}]}

        mock_post.side_effect = [bad, good]

        result = llm_utils._call("system", "user", model="bad/model")

        assert result == ["ecm-1"]
        assert mock_post.call_args_list[0].kwargs["json"]["model"] == "bad/model"
        assert mock_post.call_args_list[1].kwargs["json"]["model"] == "openai/gpt-4o-mini"
