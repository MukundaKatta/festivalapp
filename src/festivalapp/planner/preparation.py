"""PreparationChecklist with shopping/decoration/food lists."""
from __future__ import annotations
from ..models import ChecklistItem, FestivalDetail


class PreparationChecklist:
    """Generate preparation checklists for festivals."""

    def __init__(self) -> None:
        self._common_puja_items: list[ChecklistItem] = [
            ChecklistItem(item="Agarbatti (incense)", category="shopping", priority="high"),
            ChecklistItem(item="Camphor (kapoor)", category="shopping", priority="high"),
            ChecklistItem(item="Ghee diyas and wicks", category="shopping", priority="high"),
            ChecklistItem(item="Flowers (fresh)", category="shopping", priority="high", notes="Buy day before or morning of"),
            ChecklistItem(item="Fruits for offering", category="shopping", priority="medium"),
            ChecklistItem(item="Kumkum and haldi", category="shopping", priority="medium"),
            ChecklistItem(item="Coconut", category="shopping", priority="medium"),
            ChecklistItem(item="Puja thali", category="shopping", priority="low"),
        ]
        self._festival_checklists: dict[str, list[ChecklistItem]] = self._load_checklists()

    def _load_checklists(self) -> dict[str, list[ChecklistItem]]:
        return {
            "Diwali": [
                ChecklistItem(item="Clean and declutter entire house", category="decoration", priority="high", notes="Start 1 week before"),
                ChecklistItem(item="Diyas (50+)", category="shopping", priority="high"),
                ChecklistItem(item="Rangoli colors and stencils", category="decoration", priority="high"),
                ChecklistItem(item="String lights and lamps", category="decoration", priority="high"),
                ChecklistItem(item="Marigold and mango leaf torans", category="decoration", priority="high"),
                ChecklistItem(item="New clothes for family", category="clothing", priority="high"),
                ChecklistItem(item="Lakshmi-Ganesh idol or image", category="shopping", priority="high"),
                ChecklistItem(item="Sweets for distribution", category="food", priority="high"),
                ChecklistItem(item="Gift boxes for friends/family", category="shopping", priority="medium"),
                ChecklistItem(item="Firecrackers (eco-friendly)", category="shopping", priority="low"),
                ChecklistItem(item="Account books for Chopda Pujan", category="ritual", priority="medium"),
                ChecklistItem(item="Silver/gold coins", category="shopping", priority="medium"),
            ],
            "Ganesh Chaturthi": [
                ChecklistItem(item="Ganesh idol (eco-friendly clay)", category="shopping", priority="high", notes="Order 2 weeks before"),
                ChecklistItem(item="Modak ingredients", category="food", priority="high"),
                ChecklistItem(item="Durva grass", category="shopping", priority="high"),
                ChecklistItem(item="Decoration for mandal", category="decoration", priority="high"),
                ChecklistItem(item="Red flowers", category="shopping", priority="high"),
                ChecklistItem(item="Visarjan arrangements", category="ritual", priority="high"),
            ],
            "Navratri": [
                ChecklistItem(item="Ghatasthapana kalash and barley seeds", category="ritual", priority="high"),
                ChecklistItem(item="Nine color outfits (one per day)", category="clothing", priority="medium"),
                ChecklistItem(item="Garba/Dandiya sticks", category="shopping", priority="medium"),
                ChecklistItem(item="Fasting ingredients (sabudana, rajgira, singhara)", category="food", priority="high"),
                ChecklistItem(item="Kanya Pujan gifts (day 8/9)", category="shopping", priority="high"),
                ChecklistItem(item="Akhand diya and oil supply", category="ritual", priority="high"),
            ],
            "Holi": [
                ChecklistItem(item="Organic/natural colors (gulal)", category="shopping", priority="high"),
                ChecklistItem(item="Water balloons/pichkari", category="shopping", priority="medium"),
                ChecklistItem(item="Gujiya ingredients", category="food", priority="high"),
                ChecklistItem(item="Thandai ingredients", category="food", priority="high"),
                ChecklistItem(item="Old white clothes for playing", category="clothing", priority="medium"),
                ChecklistItem(item="Holika Dahan firewood", category="ritual", priority="high"),
                ChecklistItem(item="Coconut oil for skin protection", category="shopping", priority="medium"),
            ],
        }

    def get_checklist(self, festival_name: str) -> list[ChecklistItem]:
        """Get preparation checklist for a festival."""
        specific = self._festival_checklists.get(festival_name, [])
        return self._common_puja_items + specific

    def get_by_category(self, festival_name: str, category: str) -> list[ChecklistItem]:
        """Get checklist items filtered by category."""
        return [i for i in self.get_checklist(festival_name) if i.category == category]

    def get_high_priority(self, festival_name: str) -> list[ChecklistItem]:
        """Get high priority items only."""
        return [i for i in self.get_checklist(festival_name) if i.priority == "high"]
