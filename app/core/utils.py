"""Shared helpers."""
from __future__ import annotations

import math
from decimal import Decimal


def format_number(value: float, precision: int | str = 4) -> str:
    """Format a number for display.

    ``precision`` may be an int (fixed decimals) or "auto" for smart formatting
    that strips insignificant trailing zeros and avoids scientific notation for
    reasonable magnitudes.
    """
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "—"

    if precision == "auto" or precision is None:
        if value == 0:
            return "0"
        magnitude = abs(value)
        if magnitude >= 1e12 or magnitude < 1e-6:
            return f"{value:.6g}"
        text = f"{value:.10f}".rstrip("0").rstrip(".")
        return text or "0"

    try:
        p = int(precision)
    except (TypeError, ValueError):
        p = 4
    p = max(0, min(p, 12))
    text = f"{value:.{p}f}"
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text or "0"


def safe_float(raw: str | float | int | None) -> float:
    """Parse a possibly-messy user string into a float."""
    if raw is None:
        raise ValueError("Value is required")
    if isinstance(raw, (int, float)):
        return float(raw)
    cleaned = str(raw).strip().replace(",", "")
    if not cleaned:
        raise ValueError("Value is required")
    try:
        return float(Decimal(cleaned))
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"'{raw}' is not a valid number") from exc
