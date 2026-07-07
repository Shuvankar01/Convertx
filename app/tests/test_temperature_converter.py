"""Temperature converter correctness tests."""
from __future__ import annotations

import math

from app.converters.temperature import TemperatureConverter

t = TemperatureConverter()


def approx(a, b, tol=1e-9):
    return math.isclose(a, b, rel_tol=tol, abs_tol=tol)


def test_celsius_to_fahrenheit_freezing_point():
    assert approx(t.convert(0.0, "Celsius", "Fahrenheit"), 32.0)


def test_celsius_to_fahrenheit_boiling_point():
    assert approx(t.convert(100.0, "Celsius", "Fahrenheit"), 212.0)


def test_fahrenheit_to_celsius():
    assert approx(t.convert(32.0, "Fahrenheit", "Celsius"), 0.0)
    assert approx(t.convert(212.0, "Fahrenheit", "Celsius"), 100.0)


def test_celsius_to_kelvin_absolute_zero():
    assert approx(t.convert(-273.15, "Celsius", "Kelvin"), 0.0)


def test_kelvin_to_fahrenheit_roundtrip():
    x = t.convert(300.0, "Kelvin", "Fahrenheit")
    back = t.convert(x, "Fahrenheit", "Kelvin")
    assert approx(back, 300.0, tol=1e-6)


def test_same_unit():
    assert t.convert(25.0, "Celsius", "Celsius") == 25.0
