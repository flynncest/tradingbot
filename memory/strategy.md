# Trading Strategy

## Style
Momentum / swing trading with defined risk. Hold 1-5 days. Cut losers fast, let winners run.

## Entry Criteria
- Strong relative strength vs SPY
- Catalyst (earnings beat, upgrade, sector rotation, macro event)
- Volume surge (2x+ average)
- Clear technical setup (breakout, pullback to moving average)

## Position Sizing
- Standard: 5% of portfolio
- High conviction: up to 10% (guardrail max)
- Scale in: start at 50%, add on confirmation

## Exit Rules
- Trailing stop: 5% from high (set at entry)
- Tighten to 3% once position is up 5%+
- Hard cut at -8% from entry (no averaging down)
- Take partial profits (+10%) to reduce risk

## Operational Guardrails
# Added 2026-04-20 Monday: Lost a full trading day to Alpaca `unauthorized` errors across three routines. Standing down was correct; the process failure was not escalating auth problems until EOD.

- **Pre-market health check (MANDATORY before open routine):** call `get_account()` as the very first action. If it returns any auth error, STOP — do not proceed to market data or order logic. Log the incident and flag for credential rotation.
- **Auth-failure escalation rule:** A **second** consecutive `unauthorized` response in the same session is a P0 incident. Do not run a third identical retry hours later — that is wasted observation. Mark the day as an ops incident day in trade_log.md and notify immediately.
- **Stand-down is correct (do not second-guess later):** When equity, positions, or open orders cannot be verified, guardrails (10% max size, max 5 positions, -2% daily loss halt) are not enforceable. Trading blind is strictly worse than missing a setup — a missed breakout costs opportunity; an unbounded position can cost the account. No trades under unverified state.
- **Unknown-position recovery:** If a session ends without being able to read positions, the FIRST action next session is to reconcile holdings before any new entries or exits. Never layer new trades on top of an unknown book.

## Watchlist Notes
(Updated by routines — see research_log.md for current ideas)
