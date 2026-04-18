#!/usr/bin/env python3
"""Entry point: run a specific routine manually or start the scheduler."""
import sys
import os
from dotenv import load_dotenv

load_dotenv()


def usage():
    print("Usage:")
    print("  python main.py scheduler          # Start the cron scheduler")
    print("  python main.py pre_market         # Run pre-market routine now")
    print("  python main.py market_open        # Run market-open routine now")
    print("  python main.py midday             # Run midday routine now")
    print("  python main.py end_of_day         # Run end-of-day routine now")
    print("  python main.py weekly_review      # Run weekly review now")


def main():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "scheduler":
        from scheduler import main as run_scheduler
        run_scheduler()

    elif cmd == "pre_market":
        from routines.pre_market import run
        print(run())

    elif cmd == "market_open":
        from routines.market_open import run
        print(run())

    elif cmd == "midday":
        from routines.midday import run
        print(run())

    elif cmd == "end_of_day":
        from routines.end_of_day import run
        print(run())

    elif cmd == "weekly_review":
        from routines.weekly_review import run
        print(run())

    else:
        print(f"Unknown command: {cmd}")
        usage()
        sys.exit(1)


if __name__ == "__main__":
    main()
