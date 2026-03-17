"""CLI for FestivalApp."""
from __future__ import annotations
import click
from rich.console import Console
from .festivals.calendar import FestivalCalendar
from .festivals.regional import RegionalVariations
from .planner.preparation import PreparationChecklist
from .planner.recipes import FestivalRecipes
from .report import FestivalReport

console = Console()


@click.group()
def cli() -> None:
    """FestivalApp - Hindu Festival Platform."""
    pass


@cli.command()
@click.option("--month", "-m", default=None)
@click.option("--deity", "-d", default=None)
def list_festivals(month: str | None, deity: str | None) -> None:
    """List festivals."""
    cal = FestivalCalendar()
    report = FestivalReport()
    if month:
        fests = cal.get_festivals_by_month(month)
    elif deity:
        fests = cal.get_festivals_by_deity(deity)
    else:
        fests = cal.get_all_festivals()
    report.display_festival_list(fests)


@cli.command()
@click.argument("name")
def show(name: str) -> None:
    """Show festival details."""
    cal = FestivalCalendar()
    report = FestivalReport()
    f = cal.get_festival(name)
    if f:
        report.display_festival(f)
    else:
        console.print(f"[red]Festival not found: {name}[/red]")


@cli.command()
@click.argument("festival")
def regional(festival: str) -> None:
    """Show regional variations."""
    rv = RegionalVariations()
    variations = rv.get_variations(festival)
    for v in variations:
        console.print(f"\n[bold cyan]{v.region}[/bold cyan] - {v.local_name}")
        console.print(f"  Customs: {v.special_customs}")
        console.print(f"  Foods: {', '.join(v.special_foods)}")


@cli.command()
@click.argument("festival")
def recipes(festival: str) -> None:
    """Show recipes for a festival."""
    fr = FestivalRecipes()
    report = FestivalReport()
    report.display_recipes(fr.get_by_festival(festival))


@cli.command()
@click.argument("festival")
def checklist(festival: str) -> None:
    """Show preparation checklist."""
    pc = PreparationChecklist()
    report = FestivalReport()
    report.display_checklist(pc.get_checklist(festival), festival)


if __name__ == "__main__":
    cli()
