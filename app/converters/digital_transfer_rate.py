"""Digital transfer rate converter (decimal SI, base = bits per second)."""
from __future__ import annotations

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class DigitalTransferRateConverter(FactorConverter):
    category = Category.DIGITAL_TRANSFER_RATE
    base_unit = "bps"
    units = {
        "bps": UnitInfo("bps", "Bits / second", "bps"),
        "Kbps": UnitInfo("Kbps", "Kilobits / second", "Kbps"),
        "Mbps": UnitInfo("Mbps", "Megabits / second", "Mbps"),
        "Gbps": UnitInfo("Gbps", "Gigabits / second", "Gbps"),
    }
    factors = {
        "bps": 1.0,
        "Kbps": 1_000.0,
        "Mbps": 1_000_000.0,
        "Gbps": 1_000_000_000.0,
    }
