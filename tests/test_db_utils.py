"""
Unit tests for db_utils.py.
Uses a temporary SQLite database to avoid touching the real votes.db.
"""
from __future__ import annotations

import sqlite3
import tempfile
import pytest
from pathlib import Path
from unittest.mock import patch

import sys
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

import db_utils


@pytest.fixture
def fresh_db(tmp_path):
    """
    Patch DB_PATH to a temp file and reset the module-level _db_initialized flag
    so each test starts with a clean slate.
    """
    db_file = tmp_path / "test_votes.db"

    # Patch the global DB_PATH and reset init flag inside the module
    import db_utils as m
    original_path = m.DB_PATH
    original_init = m._db_initialized
    m.DB_PATH = db_file
    m._db_initialized = False

    yield db_file, m

    # Restore
    m.DB_PATH = original_path
    m._db_initialized = original_init


# ── init_db ─────────────────────────────────────────────────────────────

class TestInitDb:
    def test_creates_votes_and_ecm_metadata_tables(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()

        with sqlite3.connect(db_file) as conn:
            conn.row_factory = sqlite3.Row
            tables = [row["name"] for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()]
        assert "votes" in tables
        assert "ecm_metadata" in tables

    def test_idempotent_init(self, fresh_db):
        """Calling init_db twice must not raise."""
        db_file, m = fresh_db
        m.init_db()
        m.init_db()  # must not fail


# ── record_vote ─────────────────────────────────────────────────────────

class TestRecordVote:
    def test_thumbs_up(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        m.record_vote("office_zero_energy:demand_ventilation", "Demand Ventilation", "thumbs_up")

        with sqlite3.connect(db_file) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT * FROM votes WHERE ecm_id = ?", (
                "office_zero_energy:demand_ventilation",
            )).fetchone()
        assert row is not None
        assert row["vote"] == "thumbs_up"

    def test_thumbs_down_requires_reason(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        with pytest.raises(ValueError, match="reason is required"):
            m.record_vote("office_zero_energy:demand_ventilation", "DV", "thumbs_down")

    def test_thumbs_down_with_reason(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        m.record_vote("office_zero_energy:demand_ventilation", "DV", "thumbs_down", "Too expensive")

        with sqlite3.connect(db_file) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute("SELECT * FROM votes WHERE ecm_id = ?", (
                "office_zero_energy:demand_ventilation",
            )).fetchone()
        assert row["vote"] == "thumbs_down"
        assert row["reason"] == "Too expensive"

    def test_vote_updates_net_score(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        m.record_vote("k12_50:roof_ insulation", "Roof Insulation", "thumbs_up")
        m.record_vote("k12_50:roof_ insulation", "Roof Insulation", "thumbs_down", "Not cost-effective")

        with sqlite3.connect(db_file) as conn:
            conn.row_factory = sqlite3.Row
            score = conn.execute(
                "SELECT net_vote_score FROM ecm_metadata WHERE ecm_id = ?",
                ("k12_50:roof_ insulation",)
            ).fetchone()

        assert score is not None
        assert score["net_vote_score"] == 0  # +1 -1


# ── get_vote_score_map ──────────────────────────────────────────────────

class TestGetVoteScoreMap:
    def test_empty_when_no_votes(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        assert m.get_vote_score_map() == {}

    def test_score_map_reflects_votes(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()
        m.record_vote("grocery:night_cover", "Night Cover", "thumbs_up")
        m.record_vote("grocery:night_cover", "Night Cover", "thumbs_up")
        m.record_vote("grocery:night_cover", "Night Cover", "thumbs_down", "Too expensive")

        scores = m.get_vote_score_map()
        assert scores["grocery:night_cover"] == 1  # +2 -1


# ── upsert_ecm_metadata ─────────────────────────────────────────────────

class TestUpsertEcmMetadata:
    def test_insert_and_update(self, fresh_db):
        db_file, m = fresh_db
        m.init_db()

        records = [{
            "id": "large_hospitals:heat_recovery",
            "filename": "large_hospitals/heat_recovery.md",
            "title": "Heat Recovery",
            "building_type": "Large Hospitals",
        }]
        m.upsert_ecm_metadata(records)

        with sqlite3.connect(db_file) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT * FROM ecm_metadata WHERE ecm_id = ?",
                ("large_hospitals:heat_recovery",)
            ).fetchone()
        assert row["ecm_title"] == "Heat Recovery"
