"""APScheduler-based scheduler for all five trading routines (times in US/Eastern)."""
import logging
import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

ET = pytz.timezone("US/Eastern")


def _run(routine_name: str, fn):
    def wrapper():
        logger.info(f"=== Starting {routine_name} ===")
        try:
            result = fn()
            logger.info(f"=== {routine_name} complete ===\n{result[:500] if result else ''}")
        except Exception as e:
            logger.exception(f"=== {routine_name} FAILED: {e} ===")
    return wrapper


def main():
    from routines import pre_market, market_open, midday, end_of_day, weekly_review

    scheduler = BlockingScheduler(timezone=ET)

    # Pre-market: Mon-Fri 6:00 ET
    scheduler.add_job(
        _run("pre_market", pre_market.run),
        CronTrigger(day_of_week="mon-fri", hour=6, minute=0, timezone=ET),
        id="pre_market",
    )

    # Market open: Mon-Fri 8:30 ET
    scheduler.add_job(
        _run("market_open", market_open.run),
        CronTrigger(day_of_week="mon-fri", hour=8, minute=30, timezone=ET),
        id="market_open",
    )

    # Midday: Mon-Fri 12:00 ET
    scheduler.add_job(
        _run("midday", midday.run),
        CronTrigger(day_of_week="mon-fri", hour=12, minute=0, timezone=ET),
        id="midday",
    )

    # End of day: Mon-Fri 15:00 ET
    scheduler.add_job(
        _run("end_of_day", end_of_day.run),
        CronTrigger(day_of_week="mon-fri", hour=15, minute=0, timezone=ET),
        id="end_of_day",
    )

    # Weekly review: Friday 16:00 ET
    scheduler.add_job(
        _run("weekly_review", weekly_review.run),
        CronTrigger(day_of_week="fri", hour=16, minute=0, timezone=ET),
        id="weekly_review",
    )

    logger.info("Scheduler started. Routines:")
    logger.info("  Pre-market:    Mon-Fri 06:00 ET")
    logger.info("  Market open:   Mon-Fri 08:30 ET")
    logger.info("  Midday:        Mon-Fri 12:00 ET")
    logger.info("  End of day:    Mon-Fri 15:00 ET")
    logger.info("  Weekly review: Friday  16:00 ET")

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Scheduler stopped.")


if __name__ == "__main__":
    main()
