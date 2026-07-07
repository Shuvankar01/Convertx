import math

from app.converters.fuel_economy import FuelEconomyConverter

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