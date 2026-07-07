"""History service."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.config import get_settings
from app.db.models.history import ConversionHistory
from app.repositories.history_repository import HistoryRepository


class HistoryService:
    def __init__(self, db: Session) -> None:
        self.repo = HistoryRepository(db)

    def record(
        self,
        *,
        category: str,
        input_value: float,
        from_unit: str,
        to_unit: str,
        result_value: float,
        precision: str,
    ) -> ConversionHistory:
        entry = ConversionHistory(
            category=category,
            input_value=input_value,
            from_unit=from_unit,
            to_unit=to_unit,
            result_value=result_value,
            precision=precision,
        )
        saved = self.repo.add(entry)
        self.repo.trim(get_settings().max_history_items)
        return saved

    def recent(self, limit: int = 50) -> list[ConversionHistory]:
        return self.repo.list_recent(limit)

    def get(self, entry_id: int) -> ConversionHistory | None:
        return self.repo.get(entry_id)

    def delete(self, entry_id: int) -> None:
        self.repo.delete(entry_id)

    def clear(self) -> None:
        self.repo.clear()
