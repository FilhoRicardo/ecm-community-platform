"""Pytest configuration and shared fixtures."""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

import pytest

# Ensure the project root is on sys.path so imports work from tests/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary data directory with votes.db initialised."""
    os.environ["ECM_DATA_DIR"] = str(tmp_path)
    # Patch DB_PATH to use the temp dir for the test
    import db_utils
    db_utils.DB_PATH = tmp_path / "votes.db"
    db_utils._db_initialized = False   # reset flag so init_db re-runs in this tmp dir
    db_utils.init_db()
    yield tmp_path
    # Cleanup — reset module state
    db_utils._db_initialized = False


@pytest.fixture
def tmp_ecm_root(tmp_path):
    """
    Create a fake ECM directory structure and point ecm_utils.ECM_ROOT at it.
    Since load_ecms() is decorated with @st.cache_resource (streamlit caching),
    it can't be cleared here. Tests that need a different ECM_ROOT must call
    load_ecms() again after patching ECM_ROOT — but the streamlit cache won't
    re-run outside a Streamlit context. For unit tests we work around this by
    patching the module-level ECMS/ECM_BY_ID directly in app.py, or by using
    a fresh Python subprocess. Here we keep the real ECM_ROOT for path-traversal
    tests that only verify the guard logic without reloading.
    """
    import ecm_utils
    original = ecm_utils.ECM_ROOT
    ecm_utils.ECM_ROOT = tmp_path
    # Build a minimal structure
    (tmp_path / "office_zero_energy").mkdir(parents=True)
    (tmp_path / "grocery").mkdir(parents=True)
    (tmp_path / "office_zero_energy" / "ECM_Test_Office.md").write_text(
        "# Test Office ECM\n\nSome content.", encoding="utf-8"
    )
    (tmp_path / "grocery" / "ECM_Test_Grocery.md").write_text(
        "# Test Grocery ECM\n\nSome content.", encoding="utf-8"
    )
    yield tmp_path
    ecm_utils.ECM_ROOT = original


@pytest.fixture
def sample_ecms():
    """Minimal ECM records mirroring what load_ecms() produces."""
    return [
        {
            "id": "office_zero_energy:ECM_Daylight_Harvesting_Controls_Office.md",
            "filename": "office_zero_energy/ECM_Daylight_Harvesting_Controls_Office.md",
            "title": "Daylight Harvesting Controls",
            "building_type": "Office (Zero Energy)",
            "building_slug": "office_zero_energy",
            "content": "# Daylight Harvesting Controls\n\nInstall daylight-responsive lighting controls...",
            "excerpt": "Install daylight-responsive lighting controls to reduce electric lighting energy.",
        },
        {
            "id": "grocery:ECM_Condenser_Optimization_Grocery.md",
            "filename": "grocery/ECM_Condenser_Optimization_Grocery.md",
            "title": "Condenser Heat Recovery",
            "building_type": "Grocery",
            "building_slug": "grocery",
            "content": "# Condenser Heat Recovery\n\nRecover waste heat from refrigeration condensers...",
            "excerpt": "Recover waste heat from refrigeration condensers for domestic hot water.",
        },
    ]
