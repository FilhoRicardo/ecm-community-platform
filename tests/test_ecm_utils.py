"""
Unit tests for ecm_utils.py — pure functions only (no I/O, no network).
"""
from __future__ import annotations

import pytest

import sys
from pathlib import Path
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from ecm_utils import (
    slugify,
    first_markdown_title,
    excerpt_from_content,
)


# ── slugify ──────────────────────────────────────────────────────────────

class TestSlugify:
    def test_strip_and_lowercase(self):
        assert slugify("  Hello World  ") == "hello_world"

    def test_multiple_separators_collapse(self):
        assert slugify("one---two   three") == "one_two_three"

    def test_non_alphanumeric_replaced(self):
        assert slugify("foo@bar!baz") == "foo_bar_baz"

    def test_empty_string_returns_ecm(self):
        assert slugify("   ") == "ecm"
        assert slugify("") == "ecm"

    def test_preserves_underscores(self):
        assert slugify("zero_energy_building") == "zero_energy_building"


# ── first_markdown_title ────────────────────────────────────────────────

class TestFirstMarkdownTitle:
    def test_finds_h1(self):
        content = "# My Title\n## Section\nBody"
        assert first_markdown_title(content, "fallback") == "My Title"

    def test_skips_lower_headings(self):
        content = "## Not a title\n# Yes Title\nBody"
        assert first_markdown_title(content, "fallback") == "Yes Title"

    def test_strips_leading_hash_whitespace(self):
        content = "#   Spaced Title  \nBody"
        assert first_markdown_title(content, "fallback") == "Spaced Title"

    def test_falls_back_when_no_h1(self):
        content = "## Subtitle\nSome text"
        assert first_markdown_title(content, "my fallback") == "my fallback"

    def test_empty_content(self):
        assert first_markdown_title("", "empty") == "empty"

    def test_only_frontmatter(self):
        content = "---\nkey: value\n---\n# Real Title"
        assert first_markdown_title(content, "fallback") == "Real Title"


# ── excerpt_from_content ────────────────────────────────────────────────

class TestExcerptFromContent:
    def test_strips_frontmatter(self):
        content = "---\ntitle: Foo\n---\n# Title\nSome body text"
        result = excerpt_from_content(content)
        assert "---" not in result
        assert "title" not in result

    def test_strips_h1_h2(self):
        content = "## Not a title\n# Yes Title\nSome text"
        result = excerpt_from_content(content)
        # All headings are stripped; only body text remains
        assert "#" not in result
        assert "Some text" in result

    def test_max_len(self):
        content = "# Title\n" + "word " * 200
        result = excerpt_from_content(content, max_len=80)
        assert len(result) <= 80

    def test_empty_content(self):
        assert excerpt_from_content("") == ""
        assert excerpt_from_content("   \n\n  ") == ""

    def test_preserves_body_lines(self):
        content = "# Title\nLine one.\nLine two."
        result = excerpt_from_content(content)
        assert "Line one" in result
        assert "Line two" in result

    def test_collapses_whitespace(self):
        content = "# Title\nWord1    Word2\n\n\nWord3"
        result = excerpt_from_content(content)
        assert "  " not in result
