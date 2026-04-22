"""Tests for ecm_utils — ECM loading, path traversal guard, ID uniqueness."""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest

import ecm_utils


class TestLoadEcms:
    """Tests that use a patched ECM_ROOT via tmp_ecm_root fixture."""

    def test_loads_all_valid_files(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        assert len(items) == 2

    def test_ids_are_unique(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        ids = [item["id"] for item in items]
        assert len(ids) == len(set(ids)), "Duplicate ECM IDs found"

    def test_ecm_id_contains_full_filename(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        for item in items:
            assert ".md" in item["id"], f"ID '{item['id']}' should contain .md extension"

    def test_ecm_id_format(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        for item in items:
            assert ":" in item["id"]
            slug, filename = item["id"].split(":", 1)
            assert slug in ecm_utils.BUILDING_TYPE_LABELS
            assert filename.endswith(".md")

    def test_content_and_excerpt_present(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        for item in items:
            assert item["content"]
            assert item["excerpt"]
            assert len(item["excerpt"]) <= 320

    def test_title_extracted_from_markdown(self, tmp_ecm_root):
        items = ecm_utils.load_ecms()
        titles = [item["title"] for item in items]
        assert "Test Office ECM" in titles


class TestPathTraversalGuard:
    def test_symlink_outside_ecm_root_is_rejected(self, tmp_ecm_root):
        """A symlink pointing outside ECM_ROOT should be skipped (not traversed)."""
        # Create a real file outside tmp_ecm_root
        outside = Path(tempfile.gettempdir()) / "ecm_audit_secret.txt"
        outside.write_text("secret", encoding="utf-8")
        try:
            # Create a symlink inside office_zero_energy pointing to the secret file
            symlink = tmp_ecm_root / "office_zero_energy" / "traversal.md"
            symlink.symlink_to(outside)

            items = ecm_utils.load_ecms()
            ids = [item["id"] for item in items]
            # The symlink should be skipped, not read
            assert not any("traversal" in i for i in ids)
        finally:
            outside.unlink(missing_ok=True)

    def test_double_dot_path_component_rejected(self, tmp_ecm_root):
        """Files with '..' in the path should not appear in results."""
        items = ecm_utils.load_ecms()
        for item in items:
            assert ".." not in item["filename"]
            assert ".." not in item["id"]


class TestSlugify:
    def test_slugify_strips_punctuation(self):
        assert ecm_utils.slugify("Hello, World!") == "hello_world"

    def test_slugify_handles_empty_string(self):
        assert ecm_utils.slugify("   ") == "ecm"


class TestExcerptFromContent:
    def test_excerpt_skips_frontmatter(self):
        text = (
            "---\ntags: ['test']\n---\n# Title\n\n"
            "This is the actual content that should appear in the excerpt."
        )
        excerpt = ecm_utils.excerpt_from_content(text)
        assert "frontmatter" not in excerpt.lower()
        assert "Title" not in excerpt

    def test_excerpt_skips_headings(self):
        text = "# Heading\n\nParagraph content here."
        excerpt = ecm_utils.excerpt_from_content(text)
        assert "Heading" not in excerpt
        assert "Paragraph" in excerpt

    def test_excerpt_truncates(self):
        long_text = " ".join(["word"] * 200)
        excerpt = ecm_utils.excerpt_from_content(long_text)
        assert len(excerpt) <= 320
