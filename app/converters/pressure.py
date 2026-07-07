"""Pressure converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class PressureConverter(FactorConverter):
    category = Category.PRESSURE
    base_unit = "pascal"
    units = {
        "pascal": UnitInfo("pascal", "Pascal", "Pa"),
        "kilopascal": UnitInfo("kilopascal", "Kilopascal", "kPa"),
        "bar": UnitInfo("bar", "Bar", "bar"),
        "psi": UnitInfo("psi", "Pound / in²", "psi"),
        "atmosphere": UnitInfo("atmosphere", "Atmosphere", "atm"),
    }
    factors = {
        "pascal": 1.0,
        "kilopascal": 1000.0,
        "bar": 100_000.0,
        "psi": 6894.757293168,
        "atmosphere": 101_325.0,
    }
