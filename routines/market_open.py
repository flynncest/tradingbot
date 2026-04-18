"""Market-open routine (~8:30/9:30 ET): execute planned trades, set trailing stops."""
import logging
import yaml
from pathlib import Path
from datetime import date
from skills import trading, memory, notification
from routines.base import run_agent

logger = logging.getLogger(__name__)

STRATEGY_PATH = Path(__file__).parent.parent / "strategy.yaml"


def _load_guardrails() -> str:
    with open(STRATEGY_PATH) as f:
        cfg = yaml.safe_load(f)
    g = cfg["guardrails"]
    return f"""GUARDRAILS (must not be violated):
- Max position size: {g['max_position_size_pct']*100:.0f}% of portfolio
- Max daily loss: stop trading if down {g['max_daily_loss_pct']*100:.0f}% today
- Default trailing stop: {g['trailing_stop_pct']}%
- Max open positions: {g['max_positions']}
- Hard cut on loss: close position at -{g['loss_cut_threshold_pct']}% from entry"""


SYSTEM = """You are a disciplined trade execution agent. At market open you:
1. Read the research log to get today's planned trade ideas
2. Check account equity and current positions
3. Execute planned trades that still have valid setups (within guardrails)
4. Immediately set trailing stops on every new position
5. Log every trade to trade_log.md
6. Notify ClickUp only when trades are actually placed

Never exceed guardrails. Prefer not trading to breaking risk rules."""


def run() -> str:
    today = date.today().strftime("%Y-%m-%d")
    guardrails = _load_guardrails()
    logger.info("Starting market-open routine")

    tools = trading.TOOL_DEFINITIONS + memory.TOOL_DEFINITIONS + notification.TOOL_DEFINITIONS
    handlers = {**trading.HANDLERS, **memory.HANDLERS, **notification.HANDLERS}

    prompt = f"""Today is {today}. Run the market-open execution routine.

{guardrails}

Steps:
1. Read memory/research_log.md for today's trade ideas
2. Read memory/trade_log.md to see existing positions
3. Call get_account() to check equity and buying power
4. Call get_positions() to see current exposure
5. For each planned trade that still makes sense:
   a. Verify it fits within guardrails (position size, max positions)
   b. Place a market order via place_market_order()
   c. Immediately set a trailing stop via place_trailing_stop()
6. Update memory/trade_log.md with each new trade entry
7. Send ONE ClickUp notification summarizing all trades placed (only if any were placed)

If account is already at max positions or down too much, skip trading and log the reason."""

    result = run_agent(SYSTEM, prompt, tools, handlers)
    logger.info("Market-open routine complete")
    return result
