"""Midday routine (~12:00 ET): review positions, cut losers, tighten stops on winners."""
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
    return f"""GUARDRAILS:
- Cut any position down more than {g['loss_cut_threshold_pct']}% from entry immediately
- Tighten trailing stop to 3% on any position up {g['tighten_stop_at_profit_pct']}%+
- If account is down {g['max_daily_loss_pct']*100:.0f}% today, close ALL positions and halt"""


SYSTEM = """You are a disciplined midday position manager. Your job is to:
1. Review all open positions and their current P&L
2. Cut losers that have hit the loss threshold (no averaging down)
3. Tighten trailing stops on winners to protect profits
4. Update trade log and memory with current state
5. No new trades — only risk management

Be ruthless about cutting losers. Let winners run with tighter stops."""


def run() -> str:
    today = date.today().strftime("%Y-%m-%d")
    guardrails = _load_guardrails()
    logger.info("Starting midday routine")

    tools = trading.TOOL_DEFINITIONS + memory.TOOL_DEFINITIONS + notification.TOOL_DEFINITIONS
    handlers = {**trading.HANDLERS, **memory.HANDLERS, **notification.HANDLERS}

    prompt = f"""Today is {today}. Run the midday position review routine.

{guardrails}

Steps:
1. Call get_account() — check if daily loss limit is hit
2. Call get_positions() — review all open positions
3. For each position:
   a. If P&L is worse than the loss cut threshold → close_position() immediately
   b. If P&L is +5% or better → cancel existing trailing stop and place_trailing_stop() at 3%
   c. Otherwise → leave it alone
4. Call get_open_orders() to verify trailing stops are in place
5. Update memory/trade_log.md with midday status and any actions taken
6. Update memory/research_log.md with current market regime observation

Only send a notification if you had to cut positions or if the daily loss limit was hit."""

    result = run_agent(SYSTEM, prompt, tools, handlers)
    logger.info("Midday routine complete")
    return result
