"""Weight / mass converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class WeightConverter(FactorConverter):
    category = Category.WEIGHT
    base_unit = "gram"
    units = {
        "milligram": UnitInfo("milligram", "Milligram", "mg"),
        "gram": UnitInfo("gram", "Gram", "g"),
        "kilogram": UnitInfo("kilogram", "Kilogram", "kg"),
        "metric_ton": UnitInfo("metric_ton", "Metric Ton", "t"),
        "ounce": UnitInfo("ounce", "Ounce", "oz"),
        "pound": UnitInfo("pound", "Pound", "lb"),
        "stone": UnitInfo("stone", "Stone", "st"),
    }
    factors = {
        "milligram": 0.001,
        "gram": 1.0,
        "kilogram": 1000.0,
        "metric_ton": 1_000_000.0,
        "ounce": 28.349523125,
        "pound": 453.59237,
        "stone": 6350.29318,
    }
