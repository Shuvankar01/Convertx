"""Conversion service unit tests."""
from __future__ import annotations

import math

import pytest

from app.core.enums import Category
from app.services.conversion_service import ConversionService


svc = ConversionService()


def approx(a: float, b: float, tol: float = 1e-6) -> bool:
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def test_length_km_to_mile():
    r = svc.convert(Category.LENGTH, 1.0, "kilometer", "mile", include_comparisons=False)
    assert approx(r.result, 0.6213711922373339)


def test_weight_kg_to_pound():
    r = svc.convert(Category.WEIGHT, 1.0, "kilogram", "pound", include_comparisons=False)
    assert approx(r.result, 2.2046226218487757)


def test_same_unit_returns_input():
    r = svc.convert(Category.LENGTH, 42.0, "meter", "meter", include_comparisons=False)
    assert r.result == 42.0


def test_data_storage_gb_to_mb_decimal_convention():
    r = svc.convert(Category.DATA_STORAGE, 1.0, "GB", "MB", include_comparisons=False)
    assert approx(r.result, 1000.0)


def test_comparisons_exclude_source_unit():
    r = svc.convert(Category.LENGTH, 5.0, "kilometer", "meter")
    assert all(c.unit != "kilometer" for c in r.comparisons)
    assert any(c.unit == "meter" for c in r.comparisons)


def test_invalid_unit_raises():
    from app.core.exceptions import UnknownUnitError

    with pytest.raises(UnknownUnitError):
        svc.convert(Category.LENGTH, 1.0, "meter", "not-a-unit", include_comparisons=False)
