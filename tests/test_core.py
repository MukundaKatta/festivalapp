"""Tests for Festivalapp."""
from src.core import Festivalapp
def test_init(): assert Festivalapp().get_stats()["ops"] == 0
def test_op(): c = Festivalapp(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Festivalapp(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Festivalapp(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Festivalapp(); r = c.process(); assert r["service"] == "festivalapp"
