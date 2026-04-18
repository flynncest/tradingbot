"""End-of-day: summarize, learn from closed trades, update strategy."""
import logging
from datetime import date
from skills import research, trading, memory, notification
from routines.base import run_agent

logger = logging.getLogger(__name__)

SYSTEM = """You are a trading performance analyst AND a learning system. Each day you do two jobs:

JOB 1 — PERFORMANCE REVIEW
Pull account data, record results, update trade log.

JOB 2 — LEARN FROM TODAY (most important)
For every trade that closed today — win OR loss — do a post-mortem:
- What was the entry thesis?
- What actually happened and why?
- What specifically caused the win or loss?
- What is the ONE concrete lesson (specific enough to act on next time)?

Then update memory/lessons.md with each lesson.
Then ask: does this lesson confirm or contradict anything in strategy.md?
If a clear pattern is emerging (even from just one strong example), update strategy.md with a precise new rule or refinement.

Be brutally honest. Losing trades teach more than winning ones.
Never write vague lessons like "be more careful." Write specific rules like:
"Do not buy breakouts in the first 30 minutes — wait for 10:30 AM confirmation."

The goal: the strategy file should be measurably smarter after every single trading day."""


def run() -> str:
    today = date.today().strftime("%Y-%m-%d %A")
    logger.info("Starting end-of-day routine")

    tools = (research.TOOL_DEFINITIONS + trading.TOOL_DEFINITIONS
             + memory.TOOL_DEFINITIONS + notification.TOOL_DEFINITIONS)
    handlers = {**research.HANDLERS, **trading.HANDLERS,
                **memory.HANDLERS, **notification.HANDLERS}

    prompt = f"""Today is {today}. Run end-of-day review and learning.

=== PART 1: PERFORMANCE ===
1. get_account() — final equity and P&L
2. get_positions() — what's still open
3. get_market_snapshot("SPY") — today's benchmark
4. read_memory_file("trade_log.md") — today's trades

Calculate: portfolio return % vs SPY return % today.
Update trade_log.md — add closed trades, update Performance Summary.

=== PART 2: LEARN (do this for every trade closed today) ===
For each closed trade, write a structured post-mortem:

**[SYMBOL] [WIN/LOSS] [P&L%]**
- Entry thesis: (why did we buy?)
- What happened: (price action, news, market context)
- Root cause of outcome: (what made it win/lose?)
- Lesson: (one specific, actionable rule)
- Strategy impact: (does this change a rule in strategy.md?)

Append all post-mortems to memory/lessons.md under today's date.

=== PART 3: STRATEGY UPDATE ===
5. read_memory_file("strategy.md")
6. read_memory_file("lessons.md")

If today's lesson clearly refines or contradicts a strategy rule → update strategy.md now.
Be surgical: change the specific rule, don't rewrite everything.
Add a comment: # Updated {today}: [reason]

=== PART 4: NOTIFY ===
Log notification "EOD {today}" with:
- Portfolio vs SPY today
- Trades closed (symbol, P&L%)
- Open positions going into tomorrow
- Today's key lesson in one sentence"""

    result = run_agent(SYSTEM, prompt, tools, handlers)
    logger.info("End-of-day routine complete")
    return result
