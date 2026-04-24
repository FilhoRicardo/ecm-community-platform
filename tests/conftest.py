"""
Pytest configuration and shared fixtures for the ECM Community Platform test suite.
"""
from __future__ import annotations

import os
import sqlite3
import tempfile
from pathlib import Path
from typing import Generator
from contextlib import contextmanager

import pytest


# ── Temporary data directory ────────────────────────────────────────────

@contextmanager
def _tmpdir():
    d = tempfile.mkdtemp()
    yield Path(d)
    # cleanup
    import shutil
    shutil.rmtree(d, ignore_errors=True)


# ── ECM_ROOT fixture ────────────────────────────────────────────────────

@pytest.fixture
def sample_ecm_root(tmp_path) -> Path:
    """
    Creates a minimal ecms/ directory tree that mimics the real structure.
    Returns the root Path. Caller can inject .md files directly into
    sub-folders to test load_ecms() parsing, frontmatter stripping, etc.
    """
    ecms = tmp_path / "ecms"
    # Pre-create all known building-slug folders
    for slug in [
        "office_zero_energy",
        "highway_lodging",
        "small_healthcare",
        "zero_k12",
        "med_big_box_retail",
        "large_hospitals",
        "k12_50",
        "grocery",
        "small_warehouse",
    ]:
        (ecms / slug).mkdir(parents=True)
    return ecms


# ── DB fixture ──────────────────────────────────────────────────────────

@pytest.fixture
def tmp_db(tmp_path) -> Path:
    """Point DB_PATH at a temp file and reset module-level state."""
    db = tmp_path / "test_votes.db"
    return db
