"""Report generation for FestivalApp."""
from __future__ import annotations
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from .models import FestivalDetail, Recipe, RegionalVariation, ChecklistItem


class FestivalReport:
    def __init__(self) -> None:
        self.console = Console()

    def display_festival(self, festival: FestivalDetail) -> None:
        rituals = "\n".join(f"  - {r}" for r in festival.rituals)
        foods = ", ".join(festival.foods)
        self.console.print(Panel(
            f"[bold magenta]{festival.name}[/bold magenta]\n"
            f"Month: {festival.month} | Duration: {festival.duration_days} day(s)\n"
            f"Deity: {festival.deity} | Tithi: {festival.tithi}\n\n"
            f"[bold]Significance:[/bold] {festival.significance}\n\n"
            f"[bold]Rituals:[/bold]\n{rituals}\n\n"
            f"[bold]Foods:[/bold] {foods}",
            title="Festival Details"))

    def display_festival_list(self, festivals: list[FestivalDetail]) -> None:
        table = Table(title="Hindu Festivals")
        table.add_column("Festival", style="bold magenta")
        table.add_column("Month", style="cyan")
        table.add_column("Days")
        table.add_column("Deity", style="yellow")
        table.add_column("Significance", width=40)
        for f in festivals:
            table.add_row(f.name, f.month, str(f.duration_days), f.deity, f.significance[:50])
        self.console.print(table)

    def display_recipes(self, recipes: list[Recipe]) -> None:
        for r in recipes:
            self.console.print(Panel(
                f"[bold]{r.name}[/bold] ({r.category})\n"
                f"Festival: {r.festival} | Region: {r.region}\n"
                f"Prep time: {r.prep_time_minutes} min\n\n"
                f"[bold]Ingredients:[/bold] {', '.join(r.ingredients[:5])}...\n"
                f"[bold]Steps:[/bold] {len(r.instructions)} steps",
                title="Recipe"))

    def display_checklist(self, items: list[ChecklistItem], festival: str) -> None:
        table = Table(title=f"Preparation Checklist: {festival}")
        table.add_column("Item", style="cyan")
        table.add_column("Category", style="yellow")
        table.add_column("Priority", style="bold")
        table.add_column("Notes")
        for i in items:
            table.add_row(i.item, i.category, i.priority, i.notes)
        self.console.print(table)
