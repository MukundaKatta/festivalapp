"""CLI for festivalapp."""
import sys, json, argparse
from .core import Festivalapp

def main():
    parser = argparse.ArgumentParser(description="FestivalApp — Hindu Festival Platform. Festival calendar, rituals, recipes, and community events.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Festivalapp()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"festivalapp v0.1.0 — FestivalApp — Hindu Festival Platform. Festival calendar, rituals, recipes, and community events.")

if __name__ == "__main__":
    main()
