"""Area converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class AreaConverter(FactorConverter):
    category = Category.AREA
    base_unit = "square_meter"
    units = {
        "square_millimeter": UnitInfo("square_millimeter", "Square Millimeter", "mm²"),
        "square_centimeter": UnitInfo("square_centimeter", "Square Centimeter", "cm²"),
        "square_meter": UnitInfo("square_meter", "Square Meter", "m²"),
        "square_kilometer": UnitInfo("square_kilometer", "Square Kilometer", "km²"),
        "square_foot": UnitInfo("square_foot", "Square Foot", "ft²"),
        "square_yard": UnitInfo("square_yard", "Square Yard", "yd²"),
        "acre": UnitInfo("acre", "Acre", "ac"),
        "hectare": UnitInfo("hectare", "Hectare", "ha"),
    }
    factors = {
        "square_millimeter": 1e-6,
        "square_centimeter": 1e-4,
        "square_meter": 1.0,
        "square_kilometer": 1_000_000.0,
        "square_foot": 0.09290304,
        "square_yard": 0.83612736,
        "acre": 4046.8564224,
        "hectare": 10_000.0,
    }
