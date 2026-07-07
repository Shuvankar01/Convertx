"""Domain enums shared across the app."""
from __future__ import annotations

from enum import Enum


class Category(str, Enum):
    LENGTH = "length"
    WEIGHT = "weight"
    TEMPERATURE = "temperature"
    AREA = "area"
    VOLUME = "volume"
    TIME = "time"
    SPEED = "speed"
    DATA_STORAGE = "data_storage"
    PRESSURE = "pressure"
    ENERGY = "energy"
    POWER = "power"
    ANGLE = "angle"
    FREQUENCY = "frequency"
    FUEL_ECONOMY = "fuel_economy"
    DIGITAL_TRANSFER_RATE = "digital_transfer_rate"

    @property
    def label(self) -> str:
        return {
            "length": "Length",
            "weight": "Weight / Mass",
            "temperature": "Temperature",
            "area": "Area",
            "volume": "Volume",
            "time": "Time",
            "speed": "Speed",
            "data_storage": "Data Storage",
            "pressure": "Pressure",
            "energy": "Energy",
            "power": "Power",
            "angle": "Angle",
            "frequency": "Frequency",
            "fuel_economy": "Fuel Economy",
            "digital_transfer_rate": "Digital Transfer Rate",
        }[self.value]

    @property
    def icon(self) -> str:
        """Lucide icon name used in the UI."""
        return {
            "length": "ruler",
            "weight": "scale",
            "temperature": "thermometer",
            "area": "square",
            "volume": "beaker",
            "time": "clock",
            "speed": "gauge",
            "data_storage": "hard-drive",
            "pressure": "wind",
            "energy": "zap",
            "power": "battery-charging",
            "angle": "triangle",
            "frequency": "activity",
            "fuel_economy": "fuel",
            "digital_transfer_rate": "wifi",
        }[self.value]


class Theme(str, Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"
