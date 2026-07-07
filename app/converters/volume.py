"""Volume converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class VolumeConverter(FactorConverter):
    category = Category.VOLUME
    base_unit = "liter"
    units = {
        "milliliter": UnitInfo("milliliter", "Milliliter", "mL"),
        "liter": UnitInfo("liter", "Liter", "L"),
        "cubic_meter": UnitInfo("cubic_meter", "Cubic Meter", "m³"),
        "teaspoon": UnitInfo("teaspoon", "Teaspoon (US)", "tsp"),
        "tablespoon": UnitInfo("tablespoon", "Tablespoon (US)", "tbsp"),
        "cup": UnitInfo("cup", "Cup (US)", "cup"),
        "pint": UnitInfo("pint", "Pint (US)", "pt"),
        "quart": UnitInfo("quart", "Quart (US)", "qt"),
        "gallon": UnitInfo("gallon", "Gallon (US)", "gal"),
    }
    factors = {
        "milliliter": 0.001,
        "liter": 1.0,
        "cubic_meter": 1000.0,
        "teaspoon": 0.00492892159375,
        "tablespoon": 0.01478676478125,
        "cup": 0.2365882365,
        "pint": 0.473176473,
        "quart": 0.946352946,
        "gallon": 3.785411784,
    }
