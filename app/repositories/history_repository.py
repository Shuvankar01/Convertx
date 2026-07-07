"""Data access for conversion history."""
from __future__ import annotations

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from app.db.models.history import ConversionHistory


class HistoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add(self, entry: ConversionHistory) -> ConversionHistory:
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry

    def list_recent(self, limit: int = 50) -> list[ConversionHistory]:
        stmt = (
            select(ConversionHistory)
            .order_by(ConversionHistory.created_at.desc())
            .limit(limit)
        )
        return list(self.db.execute(stmt).scalars())

    def get(self, entry_id: int) -> ConversionHistory | None:
        return self.db.get(ConversionHistory, entry_id)

    def delete(self, entry_id: int) -> None:
        self.db.execute(
            delete(ConversionHistory).where(ConversionHistory.id == entry_id)
        )
        self.db.commit()

    def clear(self) -> None:
        self.db.execute(delete(ConversionHistory))
        self.db.commit()

    def trim(self, keep: int) -> None:
        """Keep at most ``keep`` most recent entries."""
        stmt = select(ConversionHistory.id).order_by(
            ConversionHistory.created_at.desc()
        ).offset(keep)
        stale = [row for row in self.db.execute(stmt).scalars()]
        if stale:
            self.db.execute(delete(ConversionHistory).where(ConversionHistory.id.in_(stale)))
            self.db.commit()
