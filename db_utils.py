from __future__ import annotations

import os
import sqlite3
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable

import pandas as pd

# Configurable data directory via environment variable (Fix #10)
ECM_DATA_DIR = os.getenv("ECM_DATA_DIR", str(Path(__file__).resolve().parent))
DB_PATH = Path(ECM_DATA_DIR) / "votes.db"

_init_lock = threading.Lock()
_db_initialized = False


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    # Enable WAL mode for better concurrent-read performance
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def _column_names(conn: sqlite3.Connection, table_name: str) -> set[str]:
    rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
    return {row["name"] for row in rows}


def init_db() -> None:
    global _db_initialized
    # Thread-safe init: use lock to prevent races under multi-process WSGI
    with _init_lock:
        if _db_initialized:
            return
        _db_initialized = True

        with get_connection() as conn:
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS votes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ecm_id TEXT NOT NULL,
                    ecm_name TEXT NOT NULL,
                    vote TEXT NOT NULL CHECK (vote IN ('thumbs_up', 'thumbs_down')),
                    reason TEXT,
                    timestamp TEXT NOT NULL
                )
                '''
            )
            conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS ecm_metadata (
                    ecm_id TEXT PRIMARY KEY,
                    ecm_filename TEXT,
                    ecm_title TEXT NOT NULL,
                    building_type TEXT,
                    net_vote_score INTEGER NOT NULL DEFAULT 0
                )
                '''
            )

            cols = _column_names(conn, "ecm_metadata")
            if "ecm_filename" not in cols:
                conn.execute("ALTER TABLE ecm_metadata ADD COLUMN ecm_filename TEXT")
            if "ecm_title" not in cols:
                conn.execute("ALTER TABLE ecm_metadata ADD COLUMN ecm_title TEXT")
                conn.execute("UPDATE ecm_metadata SET ecm_title = title WHERE title IS NOT NULL")
            if "building_type" not in cols:
                conn.execute("ALTER TABLE ecm_metadata ADD COLUMN building_type TEXT")
            if "net_vote_score" not in cols:
                conn.execute("ALTER TABLE ecm_metadata ADD COLUMN net_vote_score INTEGER NOT NULL DEFAULT 0")

            # Add missing indexes (CREATE INDEX IF NOT EXISTS is safe to call on every init)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_votes_ecm_id ON votes(ecm_id)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_ecm_metadata_building_type ON ecm_metadata(building_type)")

            # Migration: add reason column to votes if missing (Fix #3)
            vote_cols = _column_names(conn, "votes")
            if "reason" not in vote_cols:
                conn.execute("ALTER TABLE votes ADD COLUMN reason TEXT")

            conn.commit()


def upsert_ecm_metadata(records: Iterable[Dict[str, Any]]) -> None:
    init_db()
    with get_connection() as conn:
        for rec in records:
            conn.execute(
                '''
                INSERT INTO ecm_metadata (
                    ecm_id, ecm_filename, ecm_title, building_type, net_vote_score
                )
                VALUES (?, ?, ?, ?, COALESCE((SELECT net_vote_score FROM ecm_metadata WHERE ecm_id = ?), 0))
                ON CONFLICT(ecm_id) DO UPDATE SET
                    ecm_filename = excluded.ecm_filename,
                    ecm_title = excluded.ecm_title,
                    building_type = excluded.building_type
                ''',
                (rec["id"], rec["filename"], rec["title"], rec["building_type"], rec["id"]),
            )
        conn.commit()


def record_vote(ecm_id: str, ecm_name: str, vote: str, reason: str | None = None) -> None:
    if vote == "thumbs_down" and not (reason or "").strip():
        raise ValueError("A reason is required for thumbs down votes.")
    init_db()
    timestamp = datetime.now(timezone.utc).isoformat()
    try:
        with get_connection() as conn:
            conn.execute(
                '''
                INSERT INTO votes (ecm_id, ecm_name, vote, reason, timestamp)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (ecm_id, ecm_name, vote, reason, timestamp),
            )
            delta = 1 if vote == "thumbs_up" else -1
            conn.execute(
                '''
                INSERT INTO ecm_metadata (ecm_id, ecm_title, net_vote_score)
                VALUES (?, ?, ?)
                ON CONFLICT(ecm_id) DO UPDATE SET
                    net_vote_score = COALESCE(ecm_metadata.net_vote_score, 0) + excluded.net_vote_score,
                    ecm_title = COALESCE(ecm_metadata.ecm_title, excluded.ecm_title)
                ''',
                (ecm_id, ecm_name, delta),
            )
            conn.commit()
    except sqlite3.OperationalError as exc:
        raise LLMError(f"Database error while recording vote: {exc}") from exc


# Re-export LLMError from llm_utils for backwards compatibility
from llm_utils import LLMError  # noqa: E402, F401


def get_vote_score_map() -> dict[str, int]:
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT ecm_id, COALESCE(net_vote_score, 0) AS net_vote_score FROM ecm_metadata"
        ).fetchall()
    return {row["ecm_id"]: int(row["net_vote_score"]) for row in rows}


def get_votes_df() -> pd.DataFrame:
    init_db()
    with get_connection() as conn:
        rows = conn.execute(
            '''
            SELECT id, ecm_id, ecm_name, vote, reason, timestamp
            FROM votes
            ORDER BY timestamp DESC, id DESC
            '''
        ).fetchall()
    return pd.DataFrame([dict(row) for row in rows])
