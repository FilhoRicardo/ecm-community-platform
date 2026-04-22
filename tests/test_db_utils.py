"""Tests for db_utils — vote recording, score lookup, and init_db."""
from __future__ import annotations

import pytest

import db_utils


class TestInitDb:
    def test_creates_tables(self, tmp_data_dir):
        db_utils.init_db()
        with db_utils.get_connection() as conn:
            tables = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        table_names = {r["name"] for r in tables}
        assert "votes" in table_names
        assert "ecm_metadata" in table_names

    def test_init_db_idempotent(self, tmp_data_dir):
        db_utils.init_db()
        db_utils.init_db()   # must not raise
        with db_utils.get_connection() as conn:
            count = conn.execute("SELECT COUNT(*) FROM ecm_metadata").fetchone()[0]
        assert count == 0   # empty after init

    def test_concurrent_init_safe(self, tmp_data_dir):
        """Verify threading.Lock prevents races (call init_db from multiple threads)."""
        import threading
        errors = []

        def init_in_thread():
            try:
                db_utils.init_db()
            except Exception as exc:
                errors.append(exc)

        threads = [threading.Thread(target=init_in_thread) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        assert len(errors) == 0


class TestRecordVote:
    def test_thumbs_up_increments_score(self, tmp_data_dir):
        db_utils.record_vote("ecm1", "Test ECM", "thumbs_up")
        scores = db_utils.get_vote_score_map()
        assert scores["ecm1"] == 1

    def test_thumbs_down_decrements_score(self, tmp_data_dir):
        db_utils.record_vote("ecm2", "Test ECM", "thumbs_up")
        db_utils.record_vote("ecm2", "Test ECM", "thumbs_down", reason="not relevant")
        scores = db_utils.get_vote_score_map()
        assert scores["ecm2"] == 0

    def test_thumbs_down_without_reason_raises(self, tmp_data_dir):
        with pytest.raises(ValueError, match="reason is required"):
            db_utils.record_vote("ecm3", "Test ECM", "thumbs_down")

    def test_reason_stored(self, tmp_data_dir):
        db_utils.record_vote("ecm4", "Test ECM", "thumbs_down", reason="too generic")
        df = db_utils.get_votes_df()
        row = df[df["ecm_id"] == "ecm4"].iloc[0]
        assert row["reason"] == "too generic"

    def test_multiple_votes_accumulate(self, tmp_data_dir):
        for _ in range(3):
            db_utils.record_vote("ecm5", "Test ECM", "thumbs_up")
        for _ in range(2):
            db_utils.record_vote("ecm5", "Test ECM", "thumbs_down", reason="a reason")
        scores = db_utils.get_vote_score_map()
        assert scores["ecm5"] == 1   # 3 up - 2 down


class TestGetVotesDf:
    def test_returns_dataframe(self, tmp_data_dir):
        db_utils.record_vote("x", "X", "thumbs_up")
        df = db_utils.get_votes_df()
        assert len(df) == 1
        assert "ecm_id" in df.columns
        assert "vote" in df.columns
        assert "reason" in df.columns
        assert "timestamp" in df.columns


class TestUpsertEcmMetadata:
    def test_upsert_inserts_new(self, tmp_data_dir):
        db_utils.upsert_ecm_metadata([
            {"id": "new_ecm", "filename": "path.md", "title": "New ECM", "building_type": "Office"},
        ])
        scores = db_utils.get_vote_score_map()
        assert "new_ecm" in scores

    def test_upsert_idempotent(self, tmp_data_dir):
        db_utils.upsert_ecm_metadata([
            {"id": "idem", "filename": "a.md", "title": "A", "building_type": "Office"},
        ])
        db_utils.upsert_ecm_metadata([
            {"id": "idem", "filename": "b.md", "title": "B", "building_type": "Grocery"},
        ])
        # Should not raise; second upsert updates metadata but score stays 0
        scores = db_utils.get_vote_score_map()
        assert scores["idem"] == 0
