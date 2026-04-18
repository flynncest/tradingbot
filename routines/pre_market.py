"""Pre-market routine (~6:00 ET): review memory, draft trade ideas, update research log."""
import logging
from datetime import date
from skills import research, memory, notification
from routines.base import run_agent

logger = logging.getLogger(__name__)

SYSTEM = """You are a pre-market trading analyst. Your job each morning is to:
1. Read memory files to understand current positions, watchlist, and strategy
2. Based on what you know, draft 3-5 actionable trade ideas with rationale, entry levels, and risk
3. Update research_log.md with today's watchlist and plan
4. Only log a notification if something is URGENT (position at risk, critical event noted in logs)

Be concise and actionable. Focus on high-probability setups based on prior research in memory."""


def run() -> str:
    today = date.today().strftime("%Y-%m-%d %A")
    logger.info("Starting pre-market routine")

    tools = research.TOOL_DEFINITIONS + memory.TOOL_DEFINITIONS + notification.TOOL_DEFINITIONS
    handlers = {**research.HANDLERS, **memory.HANDLERS, **notification.HANDLERS}

    prompt = f"""Today is {today}. Run the pre-market routine:

1. Read memory/strategy.md, memory/trade_log.md, memory/research_log.md, and memory/lessons.md
2. Get market snapshots: SPY, QQQ, IWM, VIX to read the regime
3. Get news for SPY and 2-3 stocks from the current watchlist
4. Draft 3-5 trade ideas for today with symbol, catalyst, entry, stop, target
5. Update memory/research_log.md with:
   - Market regime (SPY vs moving averages, VIX level)
   - Today's watchlist with entry levels and catalysts
   - Key risks or events to watch
6. Only log a notification if there is an urgent situation

Focus on finding the best 1-2 high-conviction setups."""

    result = run_agent(SYSTEM, prompt, tools, handlers)
    logger.info("Pre-market routine complete")
    return result
