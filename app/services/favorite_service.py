"""Favorite service."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.db.models.favorite import FavoriteConversion
from app.repositories.favorite_repository import FavoriteRepository


class FavoriteService:
    def __init__(self, db: Session) -> None:
        self.repo = FavoriteRepository(db)

    def list(self) -> list[FavoriteConversion]:
        return self.repo.list_all()

    def is_favorite(self, category: str, from_unit: str, to_unit: str) -> bool:
        return self.repo.find(category, from_unit, to_unit) is not None

    def toggle(
        self, category: str, from_unit: str, to_unit: str, label: str | None = None
    ) -> bool:
        """Toggle the favorite status of a pair. Returns True if now favorited."""
        existing = self.repo.find(category, from_unit, to_unit)
        if existing:
            self.repo.delete(existing.id)
            return False
        self.repo.add(
            FavoriteConversion(
                category=category,
                from_unit=from_unit,
                to_unit=to_unit,
                label=label,
            )
        )
        return True

    def delete(self, fav_id: int) -> None:
        self.repo.delete(fav_id)
