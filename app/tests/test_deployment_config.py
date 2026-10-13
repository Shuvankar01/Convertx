"""Deployment-safety regression tests.

These guard the few things that silently break when the app is started from a
different working directory or on a read-only filesystem (Vercel Functions).
"""
from __future__ import annotations

import sqlite3
import tempfile
from pathlib import Path

import pytest

from app.config import BASE_DIR, default_database_url, get_settings
from app.converters.registry import all_categories, get_converter


def test_all_fifteen_categories_are_registered():
    assert len(all_categories()) == 15


@pytest.mark.parametrize("category", all_categories(), ids=lambda c: c.value)
def test_every_category_exposes_units_and_a_formula(category):
    converter = get_converter(category)
    units = converter.unit_keys()
    assert len(units) >= 2, f"{category.value} needs at least two units"
    for unit in units:
        assert converter.label_for(unit)
        assert converter.symbol_for(unit)
    assert converter.formula(units[0], units[0])


def test_template_and_static_dirs_are_absolute_and_present():
    """Relative template/static paths break once the CWD is not the repo root."""
    settings = get_settings()
    for directory in (settings.templates_dir, settings.static_dir):
        assert directory.is_absolute()
        assert Path(directory).is_dir()


def test_static_assets_referenced_by_templates_exist():
    static_dir = get_settings().static_dir
    for asset in ("css/app.css", "js/app.js", "icons/favicon.svg"):
        assert (static_dir / asset).is_file(), asset


def test_default_database_url_points_at_a_writable_location():
    """A read-only project directory must not be used for SQLite storage."""
    url = default_database_url()
    assert url.startswith("sqlite:///")

    path = Path(url.removeprefix("sqlite:///"))
    assert path.is_absolute()
    assert path.parent.is_dir()

    # Prove we can actually open the file for writing.
    with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".probe"):
        pass


def test_base_dir_points_at_the_app_package():
    assert (BASE_DIR / "main.py").is_file()
    assert (BASE_DIR / "__init__.py").is_file()


def test_sqlite_driver_is_available():
    """No extra driver package should be needed for the default SQLite URL."""
    with sqlite3.connect(":memory:") as conn:
        conn.execute("select 1")