"""Length converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class LengthConverter(FactorConverter):
    category = Category.LENGTH
    base_unit = "meter"
    units = {
        "millimeter": UnitInfo("millimeter", "Millimeter", "mm"),
        "centimeter": UnitInfo("centimeter", "Centimeter", "cm"),
        "meter": UnitInfo("meter", "Meter", "m"),
        "kilometer": UnitInfo("kilometer", "Kilometer", "km"),
        "inch": UnitInfo("inch", "Inch", "in"),
        "foot": UnitInfo("foot", "Foot", "ft"),
        "yard": UnitInfo("yard", "Yard", "yd"),
        "mile": UnitInfo("mile", "Mile", "mi"),
        "nautical_mile": UnitInfo("nautical_mile", "Nautical Mile", "nmi"),
    }
    factors = {
        "millimeter": 0.001,
        "centimeter": 0.01,
        "meter": 1.0,
        "kilometer": 1000.0,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
        "nautical_mile": 1852.0,
    }
