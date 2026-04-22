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
# Updated 2026-04-21 Tuesday: Day 2 of the same incident. Monday's rule flagged the issue correctly at open but we still ran redundant midday and EOD probes. Adding (a) diagnostic isolation step, (b) incident-mode suppression of further probes, (c) defined out-of-loop resolution path.
# Updated 2026-04-22 Wednesday: Day 3 of the same incident. The escalation rule exists but the operator hasn't acted — because our notifications look like routine status updates, not escalations. Adding (d) a Day-2+ single-purpose urgent notification rule, and (e) a reduced-EOD rule so we stop producing process theater during an active outage.

- **Pre-market health check (MANDATORY before open routine):** call `get_account()` as the very first action. If it returns any auth error, STOP — do not proceed to market data or order logic. Log the incident and flag for credential rotation.

- **Auth-failure diagnostic (NEW 2026-04-21):** On any `unauthorized` from an authenticated endpoint, immediately call one *public* endpoint (e.g., `get_market_snapshot("SPY")`) as a diagnostic. If the public call succeeds, the fault is isolated to **credentials/permissions** — not network, not outage. Record this diagnosis in the trade log and do not repeat the diagnostic later in the same incident.

- **Auth-failure escalation rule:** A **second** consecutive `unauthorized` response in the same session is a P0 incident. Do not run a third identical retry hours later — that is wasted observation. Mark the day as an ops incident day in trade_log.md and notify immediately.

- **Incident mode (NEW 2026-04-21):** Once an auth incident is confirmed (failure + public-endpoint diagnostic), the day switches to **incident mode**: suppress all further `get_account` / `get_positions` / `get_open_orders` / order-placement calls for the remainder of the session. Subsequent routines (midday, EOD) should log "incident still active — no new probes" rather than re-running the same failing calls. Only attempt to re-auth at the *next session's* pre-market health check, or after an explicit credential rotation.

- **Resolution path (NEW 2026-04-21):** Flagging a P0 is not a fix. If auth remains broken at the end of a session, the next-session pre-market routine must assume credentials require **out-of-loop action** (rotate API keys, open broker support ticket, verify account status in broker UI) before any retry. More than 1 consecutive blocked trading day = mandatory credential rotation before continuing.

- **Day-2+ urgent escalation notification (NEW 2026-04-22):** On Day 2 or later of an active auth outage, the open routine and the EOD routine must each emit exactly ONE `send_notification(urgent=true)` whose message content is *only* the required out-of-loop action — e.g., "ROTATE ALPACA API KEYS — Day N of outage, all trading halted." No market commentary, no P&L summary, no watchlist. A single-purpose alert is not ignorable; a status report is. The goal is to force operator action, not to document that action is needed.

- **Reduced-EOD during active incident (NEW 2026-04-22):** On Day 2+ of a confirmed outage with zero trades possible, the EOD routine is collapsed to: (1) one auth retry, (2) one-line log entry in trade_log.md (incident still active, days blocked = N, SPY close for reference), (3) the Day-2+ urgent notification above. **Skip** full performance-summary regeneration, skip benchmark-vs-portfolio math (portfolio return is `UNKNOWN` — there is nothing to compare), skip generating new post-mortems that just rephrase yesterday's. The trade_log and lessons.md entries for Day 3+ of the same incident should each fit in a few lines, not a page. Producing more text while producing zero trades is process theater and dilutes the escalation signal.

- **Stand-down is correct (do not second-guess later):** When equity, positions, or open orders cannot be verified, guardrails (10% max size, max 5 positions, -2% daily loss halt) are not enforceable. Trading blind is strictly worse than missing a setup — a missed breakout costs opportunity; an unbounded position can cost the account. No trades under unverified state.

- **Unknown-position recovery:** If a session ends without being able to read positions, the FIRST action next session is to reconcile holdings before any new entries or exits. Never layer new trades on top of an unknown book.

## Watchlist Notes
(Updated by routines — see research_log.md for current ideas)
