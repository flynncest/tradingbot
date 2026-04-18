"""Weekly review: post-mortem, pattern synthesis, strategy evolution."""
import logging
from datetime import date
from pathlib import Path
from skills import research, trading, memory, notification
from routines.base import run_agent

logger = logging.getLogger(__name__)

REVIEWS_DIR = Path(__file__).parent.parent / "memory" / "weekly_reviews"

SYSTEM = """You are a trading coach and strategy evolution engine. Every Friday you run the deepest analysis of the week.

Your most important job is PATTERN SYNTHESIS:
- Read every lesson logged this week in lessons.md
- Find patterns ACROSS multiple trades (not just one)
- Identify which strategy rules are working and which are failing
- Make data-driven updates to strategy.md

The strategy.md is a living document. It should be meaningfully different — and better — after every weekly review.

Grading criteria:
- Discipline: Did we follow our own rules? (A = always, F = repeatedly broke rules)
- Edge: Are our entry criteria actually predicting winners? (track win rate by setup type)
- Risk management: Did stops protect us? Did we cut fast enough?

Be ruthless. A good week where we got lucky is worse than a bad week where we learned something real.

The goal over months: a strategy file so refined by real trades that it becomes a genuine edge."""


def run() -> str:
    today = date.today()
    week_str = today.strftime("%Y-W%V")
    today_str = today.strftime("%Y-%m-%d")
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    review_file = f"weekly_reviews/week_{week_str}.md"
    logger.info("Starting weekly review")

    tools = (research.TOOL_DEFINITIONS + trading.TOOL_DEFINITIONS
             + memory.TOOL_DEFINITIONS + notification.TOOL_DEFINITIONS)
    handlers = {**research.HANDLERS, **trading.HANDLERS,
                **memory.HANDLERS, **notification.HANDLERS}

    prompt = f"""Today is {today_str} (Friday). Run the weekly review for {week_str}.

=== STEP 1: GATHER DATA ===
1. get_account() — current portfolio value
2. get_market_snapshot("SPY") — weekly SPY performance
3. read_memory_file("trade_log.md") — all trades this week
4. read_memory_file("lessons.md") — all lessons logged this week
5. read_memory_file("strategy.md") — current rules

=== STEP 2: PATTERN SYNTHESIS ===
Group this week's trades by setup type. For each setup type:
- How many trades? Win rate? Avg win vs avg loss?
- Is this setup generating real edge or just noise?

Look for cross-trade patterns:
- Did losses cluster around a specific market condition (e.g. high VIX, afternoon, sector weakness)?
- Did wins share a specific trait (e.g. gap + volume, earnings catalyst, sector leader)?
- Are there any rules we consistently broke? Why?

=== STEP 3: WRITE WEEKLY REVIEW ===
Write to {review_file}:

## Week {week_str} — Trading Review

### Performance
- Portfolio: $X (+/-Y%)
- SPY this week: +/-Z%
- Alpha generated: +/-W%
- Trades: N total, X wins (Y% win rate)

### Trade Analysis
[Table: Symbol | Setup | Entry | Exit | P&L% | What worked/failed]

### Pattern Findings
[What patterns emerged across trades this week]

### Discipline Grade: [A-F]
[Specific examples of rule adherence or violations]

### Edge Assessment: [A-F]
[Are our entry criteria actually working?]

### Strategy Updates This Week
[List every rule change made during EOD reviews this week]

### Compounding Lessons
[Lessons from this week that BUILD on previous weeks' lessons]

### Next Week Focus
[2-3 specific things to watch based on what we learned]

=== STEP 4: EVOLVE THE STRATEGY ===
6. read_memory_file("strategy.md")

Now make the most important weekly strategy update:
- Promote patterns that worked into explicit rules
- Demote or remove rules that generated losses
- Add specific conditions that improve entry timing
- Update position sizing if the data suggests a better approach

Update strategy.md. Every rule change must cite evidence:
# Updated {today_str}: [specific trade or pattern that motivated this change]

This is the most important step. The strategy must be measurably better than last Friday.

=== STEP 5: NOTIFY ===
Log notification "Weekly Review {week_str}" with:
- Portfolio vs SPY for the week
- Discipline grade + edge grade
- The single most important lesson of the week
- Top strategy change made
- 2-3 themes to watch next week"""

    result = run_agent(SYSTEM, prompt, tools, handlers)
    logger.info("Weekly review complete")
    return result
