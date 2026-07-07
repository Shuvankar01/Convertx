"""Frequency converter."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class FrequencyConverter(FactorConverter):
    category = Category.FREQUENCY
    base_unit = "hertz"
    units = {
        "hertz": UnitInfo("hertz", "Hertz", "Hz"),
        "kilohertz": UnitInfo("kilohertz", "Kilohertz", "kHz"),
        "megahertz": UnitInfo("megahertz", "Megahertz", "MHz"),
        "gigahertz": UnitInfo("gigahertz", "Gigahertz", "GHz"),
    }
    factors = {
        "hertz": 1.0,
        "kilohertz": 1_000.0,
        "megahertz": 1_000_000.0,
        "gigahertz": 1_000_000_000.0,
    }
