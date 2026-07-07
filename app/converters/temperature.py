"""Temperature converter (dedicated formulas)."""
from __future__ import annotations

from app.converters.base import BaseConverter, UnitInfo
from app.core.enums import Category


class TemperatureConverter(BaseConverter):
    category = Category.TEMPERATURE
    units = {
        "Celsius": UnitInfo("Celsius", "Celsius", "°C"),
        "Fahrenheit": UnitInfo("Fahrenheit", "Fahrenheit", "°F"),
        "Kelvin": UnitInfo("Kelvin", "Kelvin", "K"),
    }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        self.ensure_unit(from_unit)
        self.ensure_unit(to_unit)
        if from_unit == to_unit:
            return value
        # Normalize to Celsius.
        if from_unit == "Celsius":
            c = value
        elif from_unit == "Fahrenheit":
            c = (value - 32.0) * 5.0 / 9.0
        else:  # Kelvin
            c = value - 273.15

        if to_unit == "Celsius":
            return c
        if to_unit == "Fahrenheit":
            return c * 9.0 / 5.0 + 32.0
        return c + 273.15  # Kelvin

    def formula(self, from_unit: str, to_unit: str) -> str:
        table = {
            ("Celsius", "Fahrenheit"): "°F = °C × 9/5 + 32",
            ("Fahrenheit", "Celsius"): "°C = (°F − 32) × 5/9",
            ("Celsius", "Kelvin"): "K = °C + 273.15",
            ("Kelvin", "Celsius"): "°C = K − 273.15",
            ("Fahrenheit", "Kelvin"): "K = (°F − 32) × 5/9 + 273.15",
            ("Kelvin", "Fahrenheit"): "°F = (K − 273.15) × 9/5 + 32",
        }
        if from_unit == to_unit:
            return "Same unit — value is unchanged."
        return table.get((from_unit, to_unit), "")
