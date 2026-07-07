"""Power converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class PowerConverter(FactorConverter):
    category = Category.POWER
    base_unit = "watt"
    units = {
        "watt": UnitInfo("watt", "Watt", "W"),
        "kilowatt": UnitInfo("kilowatt", "Kilowatt", "kW"),
        "horsepower": UnitInfo("horsepower", "Horsepower (mech)", "hp"),
    }
    factors = {
        "watt": 1.0,
        "kilowatt": 1000.0,
        "horsepower": 745.6998715822702,
    }
