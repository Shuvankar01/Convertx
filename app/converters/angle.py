"""Angle converter."""
from __future__ import annotations

import math

from app.converters.base import FactorConverter, UnitInfo
from app.core.enums import Category


class AngleConverter(FactorConverter):
    category = Category.ANGLE
    base_unit = "radian"
    units = {
        "degree": UnitInfo("degree", "Degree", "°"),
        "radian": UnitInfo("radian", "Radian", "rad"),
    }
    factors = {
        "degree": math.pi / 180.0,
        "radian": 1.0,
    }
