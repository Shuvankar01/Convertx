"""Fuel economy converter (uses inverse relationships for L/100km)."""
from __future__ import annotations

from app.converters.base import BaseConverter, UnitInfo
from app.core.enums import Category
from app.core.exceptions import InvalidValueError

# Reference constants.
KM_PER_MILE = 1.609344
LITERS_PER_US_GALLON = 3.785411784
LITERS_PER_UK_GALLON = 4.54609


class FuelEconomyConverter(BaseConverter):
    category = Category.FUEL_ECONOMY
    units = {
        "km_per_l": UnitInfo("km_per_l", "Kilometers / Liter", "km/L"),
        "mpg_us": UnitInfo("mpg_us", "Miles / US Gallon", "mpg (US)"),
        "mpg_uk": UnitInfo("mpg_uk", "Miles / UK Gallon", "mpg (UK)"),
        "l_per_100km": UnitInfo("l_per_100km", "Liters / 100 km", "L/100km"),
    }

    # Convert every unit to a canonical "km per liter" scalar, then back out.
    def _to_kml(self, value: float, unit: str) -> float:
        if unit == "km_per_l":
            return value
        if unit == "mpg_us":
            return value * KM_PER_MILE / LITERS_PER_US_GALLON
        if unit == "mpg_uk":
            return value * KM_PER_MILE / LITERS_PER_UK_GALLON
        if unit == "l_per_100km":
            if value == 0:
                raise InvalidValueError("L/100km cannot be zero")
            return 100.0 / value
        raise InvalidValueError(f"Unknown unit '{unit}'")

    def _from_kml(self, kml: float, unit: str) -> float:
        if unit == "km_per_l":
            return kml
        if unit == "mpg_us":
            return kml * LITERS_PER_US_GALLON / KM_PER_MILE
        if unit == "mpg_uk":
            return kml * LITERS_PER_UK_GALLON / KM_PER_MILE
        if unit == "l_per_100km":
            if kml == 0:
                raise InvalidValueError("Cannot convert 0 km/L to L/100km")
            return 100.0 / kml
        raise InvalidValueError(f"Unknown unit '{unit}'")

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        self.ensure_unit(from_unit)
        self.ensure_unit(to_unit)
        return self._from_kml(self._to_kml(value, from_unit), to_unit)

    def formula(self, from_unit: str, to_unit: str) -> str:
        if from_unit == to_unit:
            return "Same unit — value is unchanged."
        if "l_per_100km" in (from_unit, to_unit):
            return "L/100km ↔ km/L uses an inverse relationship: L/100km = 100 / (km/L)."
        return "Converted through canonical km/L, then to the target unit."
