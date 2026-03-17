"""Tests for FestivalApp."""
import pytest
from festivalapp.festivals.calendar import FestivalCalendar
from festivalapp.festivals.details import FestivalDatabase
from festivalapp.festivals.regional import RegionalVariations
from festivalapp.planner.preparation import PreparationChecklist
from festivalapp.planner.recipes import FestivalRecipes


class TestFestivalCalendar:
    def test_30_plus_festivals(self):
        cal = FestivalCalendar()
        assert len(cal.get_all_festivals()) >= 30

    def test_get_festival(self):
        cal = FestivalCalendar()
        d = cal.get_festival("Diwali")
        assert d is not None
        assert d.duration_days == 5

    def test_festivals_by_month(self):
        cal = FestivalCalendar()
        jan = cal.get_festivals_by_month("January")
        assert len(jan) >= 2

    def test_festivals_by_deity(self):
        cal = FestivalCalendar()
        krishna = cal.get_festivals_by_deity("Krishna")
        assert len(krishna) >= 2

    def test_festivals_by_region(self):
        cal = FestivalCalendar()
        kerala = cal.get_festivals_by_region("Kerala")
        assert len(kerala) >= 1


class TestFestivalDatabase:
    def test_get_details(self):
        db = FestivalDatabase()
        d = db.get_festival_details("Diwali")
        assert d is not None

    def test_fasting_festivals(self):
        db = FestivalDatabase()
        fasting = db.get_festivals_with_fasting()
        assert len(fasting) >= 3

    def test_multi_day(self):
        db = FestivalDatabase()
        multi = db.get_multi_day_festivals()
        assert len(multi) >= 5


class TestRegionalVariations:
    def test_diwali_variations(self):
        rv = RegionalVariations()
        variations = rv.get_variations("Diwali")
        assert len(variations) >= 3

    def test_by_region(self):
        rv = RegionalVariations()
        bengal = rv.get_by_region("Bengal")
        assert len(bengal) >= 1


class TestFestivalRecipes:
    def test_50_plus_recipes(self):
        fr = FestivalRecipes()
        assert len(fr.get_all_recipes()) >= 50

    def test_diwali_recipes(self):
        fr = FestivalRecipes()
        diwali = fr.get_by_festival("Diwali")
        assert len(diwali) >= 3

    def test_search_recipes(self):
        fr = FestivalRecipes()
        results = fr.search_recipes("coconut")
        assert len(results) >= 1

    def test_all_vegetarian(self):
        fr = FestivalRecipes()
        assert all(r.is_vegetarian for r in fr.get_all_recipes())


class TestPreparationChecklist:
    def test_diwali_checklist(self):
        pc = PreparationChecklist()
        items = pc.get_checklist("Diwali")
        assert len(items) >= 10

    def test_high_priority(self):
        pc = PreparationChecklist()
        high = pc.get_high_priority("Diwali")
        assert all(i.priority == "high" for i in high)
