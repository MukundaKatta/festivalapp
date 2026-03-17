"""Pydantic models for FestivalApp."""
from __future__ import annotations
from pydantic import BaseModel, Field


class FestivalDetail(BaseModel):
    name: str
    month: str
    duration_days: int = 1
    significance: str
    mythology: str = ""
    rituals: list[str] = Field(default_factory=list)
    foods: list[str] = Field(default_factory=list)
    mantras: list[str] = Field(default_factory=list)
    greetings: list[str] = Field(default_factory=list)
    regions: list[str] = Field(default_factory=list)
    tithi: str = ""
    deity: str = ""


class RegionalVariation(BaseModel):
    festival_name: str
    region: str
    local_name: str
    special_customs: str
    special_foods: list[str] = Field(default_factory=list)


class Recipe(BaseModel):
    name: str
    festival: str
    region: str = ""
    category: str = ""  # sweet, savory, main, snack, drink
    ingredients: list[str] = Field(default_factory=list)
    instructions: list[str] = Field(default_factory=list)
    prep_time_minutes: int = 30
    is_vegetarian: bool = True


class ChecklistItem(BaseModel):
    item: str
    category: str  # shopping, decoration, food, ritual, clothing
    priority: str = "medium"
    notes: str = ""
