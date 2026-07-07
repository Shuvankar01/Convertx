"""Pytest fixtures — use an isolated in-memory SQLite DB for tests."""
from __future__ import annotations

import os
import tempfile

# Point CONVERTX to a temp SQLite file before app imports read settings.
_tmp_db = tempfile.NamedTemporaryFile(suffix=".sqlite", delete=False)
_tmp_db.close()
os.environ["CONVERTX_DATABASE_URL"] = f"sqlite:///{_tmp_db.name}"

import pytest
from fastapi.testclient import TestClient

from app.db.session import init_db
from app.main import app


@pytest.fixture(scope="session", autouse=True)
def _setup_db():
    init_db()
    yield


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
