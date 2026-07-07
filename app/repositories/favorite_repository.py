"""Data access for favorite conversion pairs."""
from __future__ import annotations

from sqlalchemy import delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.models.favorite import FavoriteConversion


class FavoriteRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def list_all(self) -> list[FavoriteConversion]:
        stmt = select(FavoriteConversion).order_by(FavoriteConversion.created_at.desc())
        return list(self.db.execute(stmt).scalars())

    def find(
        self, category: str, from_unit: str, to_unit: str
    ) -> FavoriteConversion | None:
        stmt = select(FavoriteConversion).where(
            FavoriteConversion.category == category,
            FavoriteConversion.from_unit == from_unit,
            FavoriteConversion.to_unit == to_unit,
        )
        return self.db.execute(stmt).scalar_one_or_none()

    def add(self, fav: FavoriteConversion) -> FavoriteConversion:
        try:
            self.db.add(fav)
            self.db.commit()
            self.db.refresh(fav)
            return fav
        except IntegrityError:
            self.db.rollback()
            existing = self.find(fav.category, fav.from_unit, fav.to_unit)
            assert existing is not None
            return existing

    def delete(self, fav_id: int) -> None:
        self.db.execute(delete(FavoriteConversion).where(FavoriteConversion.id == fav_id))
        self.db.commit()

    def delete_pair(self, category: str, from_unit: str, to_unit: str) -> None:
        self.db.execute(
            delete(FavoriteConversion).where(
                FavoriteConversion.category == category,
                FavoriteConversion.from_unit == from_unit,
                FavoriteConversion.to_unit == to_unit,
            )
        )
        self.db.commit()
