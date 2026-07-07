"""ORM model registry."""
from app.db.models.favorite import FavoriteConversion
from app.db.models.history import ConversionHistory
from app.db.models.settings import AppSettings

__all__ = ["ConversionHistory", "FavoriteConversion", "AppSettings"]
