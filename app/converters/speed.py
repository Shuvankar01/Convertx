"""Speed converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class SpeedConverter(FactorConverter):
    category = Category.SPEED
    base_unit = "meter_per_second"
    units = {
        "meter_per_second": UnitInfo("meter_per_second", "Meter / second", "m/s"),
        "kilometer_per_hour": UnitInfo("kilometer_per_hour", "Kilometer / hour", "km/h"),
        "mile_per_hour": UnitInfo("mile_per_hour", "Mile / hour", "mph"),
        "knot": UnitInfo("knot", "Knot", "kn"),
    }
    factors = {
        "meter_per_second": 1.0,
        "kilometer_per_hour": 1000.0 / 3600.0,
        "mile_per_hour": 1609.344 / 3600.0,
        "knot": 1852.0 / 3600.0,
    }
