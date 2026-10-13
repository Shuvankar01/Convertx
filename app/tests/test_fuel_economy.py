import math

import pytest

from app.converters.fuel_economy import (
    KM_PER_MILE,
    LITERS_PER_UK_GALLON,
    LITERS_PER_US_GALLON,
    FuelEconomyConverter,
)
from app.core.exceptions import InvalidValueError, UnknownUnitError

fe = FuelEconomyConverter()


def test_mpg_us_to_kml_reasonable():
    # 30 mpg (US) ≈ 12.7543112229 km/L using project constants
    assert math.isclose(
        fe.convert(30.0, "mpg_us", "km_per_l"),
        12.75431122290816,
        rel_tol=1e-9,
    )


def test_mpg_uk_vs_mpg_us_differs():
    us = fe.convert(30.0, "mpg_us", "km_per_l")
    uk = fe.convert(30.0, "mpg_uk", "km_per_l")
    assert us > uk


# ---------------------------------------------------------------------------
# Reference relationships, derived from the constants the converter declares.
#
#   1 mile       = KM_PER_MILE km
#   1 US gallon  = LITERS_PER_US_GALLON L
#   1 UK gallon  = LITERS_PER_UK_GALLON L
#
# km/L -> mpg(US) is kml * L_per_US_galon / km_per_mile
# 1 mpg (US) is therefore exactly 1.20095 mpg (UK), because a UK gallon is
# ~20% larger than a US gallon.
# ---------------------------------------------------------------------------


def test_mpg_uk_to_kml_reasonable():
    assert math.isclose(
        fe.convert(30.0, "mpg_uk", "km_per_l"),
        30.0 * KM_PER_MILE / LITERS_PER_UK_GALLON,
        rel_tol=1e-12,
    )


def test_kml_to_mpg_us():
    assert math.isclose(
        fe.convert(10.0, "km_per_l", "mpg_us"),
        10.0 * LITERS_PER_US_GALLON / KM_PER_MILE,
        rel_tol=1e-12,
    )


def test_kml_to_mpg_uk():
    assert math.isclose(
        fe.convert(10.0, "km_per_l", "mpg_uk"),
        10.0 * LITERS_PER_UK_GALLON / KM_PER_MILE,
        rel_tol=1e-12,
    )


def test_mpg_us_to_mpg_uk_ratio():
    # A UK gallon holds more litres than a US gallon, so the same distance
    # covers more UK gallons: 30 mpg (US) ≈ 36.03 mpg (UK).
    assert math.isclose(
        fe.convert(30.0, "mpg_us", "mpg_uk"),
        30.0 * LITERS_PER_UK_GALLON / LITERS_PER_US_GALLON,
        rel_tol=1e-12,
    )


def test_mpg_uk_to_mpg_us_ratio():
    assert math.isclose(
        fe.convert(30.0, "mpg_uk", "mpg_us"),
        30.0 * LITERS_PER_US_GALLON / LITERS_PER_UK_GALLON,
        rel_tol=1e-12,
    )


def test_mpg_pair_is_invertible():
    assert math.isclose(
        fe.convert(fe.convert(30.0, "mpg_us", "mpg_uk"), "mpg_uk", "mpg_us"),
        30.0,
        rel_tol=1e-12,
    )


@pytest.mark.parametrize("value", [5.0, 12.5, 30.0])
def test_l_per_100km_is_inverse_of_kml(value):
    assert math.isclose(
        fe.convert(fe.convert(value, "km_per_l", "l_per_100km"), "l_per_100km", "km_per_l"),
        value,
        rel_tol=1e-12,
    )


def test_l_per_100km_to_kml():
    # 8 L/100km is the classic "50 mpg-ish" figure and equals 12.5 km/L.
    assert math.isclose(fe.convert(8.0, "l_per_100km", "km_per_l"), 12.5, rel_tol=1e-12)


def test_kml_to_l_per_100km():
    assert math.isclose(fe.convert(12.5, "km_per_l", "l_per_100km"), 8.0, rel_tol=1e-12)


@pytest.mark.parametrize("unit", ["km_per_l", "mpg_us", "mpg_uk"])
def test_same_unit_conversion_is_identity(unit):
    assert fe.convert(12.5, unit, unit) == 12.5


@pytest.mark.parametrize(
    ("from_unit", "to_unit"),
    [
        ("l_per_100km", "km_per_l"),
        ("l_per_100km", "mpg_us"),
        ("l_per_100km", "mpg_uk"),
        ("km_per_l", "l_per_100km"),
        ("mpg_us", "l_per_100km"),
        ("mpg_uk", "l_per_100km"),
    ],
)
def test_zero_is_rejected_for_inverse_units(from_unit, to_unit):
    with pytest.raises(InvalidValueError):
        fe.convert(0.0, from_unit, to_unit)


@pytest.mark.parametrize(
    ("from_unit", "to_unit"),
    [
        ("not_a_unit", "km_per_l"),
        ("km_per_l", "not_a_unit"),
    ],
)
def test_unknown_unit_raises(from_unit, to_unit):
    with pytest.raises(UnknownUnitError):
        fe.convert(1.0, from_unit, to_unit)