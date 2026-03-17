"""FestivalDatabase with significance/rituals/foods/mantras per festival."""
from __future__ import annotations
from .calendar import FestivalCalendar
from ..models import FestivalDetail


class FestivalDatabase:
    """Extended festival information database."""

    def __init__(self) -> None:
        self._calendar = FestivalCalendar()

    def get_festival_details(self, name: str) -> FestivalDetail | None:
        return self._calendar.get_festival(name)

    def get_festivals_with_fasting(self) -> list[FestivalDetail]:
        return [f for f in self._calendar.get_all_festivals()
                if any("fast" in r.lower() for r in f.rituals)]

    def get_multi_day_festivals(self) -> list[FestivalDetail]:
        return [f for f in self._calendar.get_all_festivals() if f.duration_days > 1]

    def get_festivals_for_planning(self, month: str) -> list[FestivalDetail]:
        """Get festivals that need advance planning for a given month."""
        return self._calendar.get_festivals_by_month(month)

    def get_all(self) -> list[FestivalDetail]:
        return self._calendar.get_all_festivals()
