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


---

## 2026-04-21 (Tue) — EOD Post-Mortem

### Trade-level post-mortems
**None.** Zero trades closed today (and zero opened). Auth-failure incident continues — Day 2 of forced stand-down.

### Meta-level post-mortem (Day 2 of ops incident)

**[OPERATIONS] AUTH FAULT ISOLATED — Public data works, authenticated endpoints do not**
- **Entry thesis:** N/A — routines called for reconciling positions and re-evaluating NVDA/IWM/IGV setups.
- **What happened:** `get_account` and `get_positions` returned `unauthorized` on every attempt across open, midday, and EOD on Tuesday. However, `get_market_snapshot("SPY")` succeeded cleanly. This definitively isolates the fault to **authentication/permissions on the account-level API**, not a general outage or network issue. SPY closed -0.75% — a real trend day we had no ability to act on.
- **Root cause of outcome:** Credentials are broken (expired, revoked, or account permission changed). The Monday "escalate after second failure" rule was followed at Tuesday open, but we still burned two more API cycles (midday + EOD) that we already knew would fail. Observing the same failure three more times added zero information after the auth fault was confirmed.
- **Lesson:** **Once a failure mode is diagnostically confirmed (e.g., auth fails while public market data succeeds), STOP re-running the failing call. Switch the day's routine from "trade" to "incident mode": log the diagnosis, halt further API probing, and explicitly defer all setup evaluation until auth is restored.** Repeated identical probes do not constitute escalation.
- **Strategy impact:** Refine the Operational Guardrails in strategy.md — specifically the "auth-failure escalation rule" — to add a diagnostic step (test a public endpoint to isolate the fault) and an "incident mode" state that suppresses further redundant API retries within the same incident window.

### Pattern Library — What Works
- Re-confirmed (Day 2): **Standing down is still the correct default.** Had we guessed at positions and traded, today's -0.75% SPY move would have hit unknown exposure in unknown direction. The cost of missing NVDA/IWM setups is bounded; the cost of an unbounded position is not.
- New: **Public-endpoint probe as a diagnostic.** `get_market_snapshot` succeeded while `get_account` failed — that single data point isolates the fault to credentials. This should be a standard first-response diagnostic, not a Day-2 realization.

### Mistake Log — What to Avoid
- **Redundant probing within a confirmed incident.** After the open-routine auth failure was confirmed a credentials issue, running the same `get_account` / `get_positions` at midday and again at EOD produced no new information. Process bug: the "escalation rule" added yesterday addressed *detection* but not *suppression* of further identical probes once the incident is active.
- **Two-day forfeit without a path to resolution.** The escalation rule tells us to flag P0; it does not define what happens when flagging it doesn't fix it. We need a defined out-of-loop action (credential rotation, support ticket) — not just more logging.
