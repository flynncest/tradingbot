# Lessons Database

This file grows automatically. Every closed trade adds a lesson. Weekly review synthesizes patterns into strategy rule updates.

## Pattern Library — What Works
(Populated automatically by EOD routine)

## Mistake Log — What to Avoid
(Populated automatically by EOD routine)

## Strategy Rule Updates
(Populated automatically by weekly review)

## Win/Loss Stats by Pattern
(Populated automatically by weekly review)

---

## 2026-04-20 (Mon) — EOD Post-Mortem

### Trade-level post-mortems
**None.** Zero trades opened, zero trades closed. Broker API (`get_account`, `get_positions`, `get_open_orders`) returned `unauthorized` at open, midday, and EOD. The open routine correctly stood down rather than trade blind.

### Meta-level post-mortem (the real lesson of the day)

**[OPERATIONS] NO-TRADE DAY — Forced stand-down from broker auth failure**
- **Entry thesis:** N/A — routine called for NVDA >$202.25 breakout + IGV $85.15 reclaim + IWM >$276.50.
- **What happened:** Alpaca returned `unauthorized` on every account/position/order call across three routines. Setups could not be sized, placed, or monitored. SPY closed -0.31% — a mild risk-off day that was arguably a decent tactical environment but we had no way to verify guardrails (exposure, daily loss cap, position count), so standing down was the only defensible decision.
- **Root cause of outcome:** Not a trading error. An **operational/infrastructure failure** — almost certainly expired or revoked API credentials, or an account-level permission change. This has now cost a full trading day.
- **Lesson:** **When broker auth fails on the open routine, immediately escalate to a credentials check — do NOT just "retry at midday."** Three identical failures in one day is a process bug. Treat auth errors as a P0 incident, not a transient glitch.
- **Strategy impact:** Add an explicit Operational Guardrails section to strategy.md covering (a) what to do on auth failure, (b) required pre-market health check, and (c) the "stand-down is correct" rule so it isn't second-guessed later.

### Pattern Library — What Works
- Confirmed: **Standing down when guardrails cannot be verified is the correct default.** Trading blind is worse than missing a setup. A missed breakout costs opportunity; an unbounded position can cost the account.

### Mistake Log — What to Avoid
- **Retry loops without escalation.** Running the same failing API call at open → midday → EOD without attempting to fix the underlying credentials is wasted observation. The second failure, not the third, should have triggered an "ops incident" flag in the log.
- **Incomplete state going into next session.** Because we can't read positions, we literally do not know what we own heading into Tuesday. This is the worst possible starting state and must be resolved *before* Tuesday's open routine runs.
