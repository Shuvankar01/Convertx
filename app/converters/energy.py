"""Energy converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class EnergyConverter(FactorConverter):
    category = Category.ENERGY
    base_unit = "joule"
    units = {
        "joule": UnitInfo("joule", "Joule", "J"),
        "kilojoule": UnitInfo("kilojoule", "Kilojoule", "kJ"),
        "calorie": UnitInfo("calorie", "Calorie", "cal"),
        "kilocalorie": UnitInfo("kilocalorie", "Kilocalorie", "kcal"),
        "watt_hour": UnitInfo("watt_hour", "Watt-hour", "Wh"),
        "kilowatt_hour": UnitInfo("kilowatt_hour", "Kilowatt-hour", "kWh"),
    }
    factors = {
        "joule": 1.0,
        "kilojoule": 1000.0,
        "calorie": 4.184,
        "kilocalorie": 4184.0,
        "watt_hour": 3600.0,
        "kilowatt_hour": 3_600_000.0,
    }
