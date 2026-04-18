"""FastAPI dashboard — runs the scheduler in a background thread."""
import json
import logging
import threading
import importlib
from collections import deque
from datetime import datetime
from pathlib import Path

import pytz
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

load_dotenv()

ET = pytz.timezone("US/Eastern")
log_entries: deque[dict] = deque(maxlen=300)
running_routines: set[str] = set()

# ── logging ──────────────────────────────────────────────────────────────────

class _BufferHandler(logging.Handler):
    def emit(self, record):
        log_entries.append({
            "t": datetime.now(ET).strftime("%H:%M:%S"),
            "lvl": record.levelname,
            "name": record.name.split(".")[-1],
            "msg": record.getMessage(),
        })

_handler = _BufferHandler()
_handler.setFormatter(logging.Formatter("%(message)s"))
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s")
logging.getLogger().addHandler(_handler)

# ── app ───────────────────────────────────────────────────────────────────────

app = FastAPI()
_HTML = (Path(__file__).parent / "templates" / "index.html").read_text()

ROUTINE_MODULES = {
    "pre_market":    "routines.pre_market",
    "market_open":   "routines.market_open",
    "midday":        "routines.midday",
    "end_of_day":    "routines.end_of_day",
    "weekly_review": "routines.weekly_review",
}

SCHEDULE_LABELS = {
    "pre_market":    "Mon–Fri 06:00 ET",
    "market_open":   "Mon–Fri 08:30 ET",
    "midday":        "Mon–Fri 12:00 ET",
    "end_of_day":    "Mon–Fri 15:00 ET",
    "weekly_review": "Friday  16:00 ET",
}


# ── routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(_HTML)


@app.get("/api/account")
async def api_account():
    try:
        from skills.trading import get_account
        return JSONResponse({"ok": True, "data": json.loads(get_account())})
    except Exception as e:
        return JSONResponse({"ok": False, "error": str(e)})


@app.get("/api/positions")
async def api_positions():
    try:
        from skills.trading import get_positions
        raw = get_positions()
        data = json.loads(raw) if raw.startswith("[") else []
        return JSONResponse({"ok": True, "data": data})
    except Exception as e:
        return JSONResponse({"ok": False, "error": str(e), "data": []})


@app.get("/api/memory/{filename:path}")
async def api_memory(filename: str):
    try:
        from skills.memory import read_memory_file
        return JSONResponse({"ok": True, "content": read_memory_file(filename)})
    except Exception as e:
        return JSONResponse({"ok": False, "content": f"Error: {e}"})


@app.get("/api/logs")
async def api_logs():
    return JSONResponse({"logs": list(log_entries)})


@app.get("/api/schedule")
async def api_schedule():
    return JSONResponse({
        "routines": [
            {"id": k, "label": SCHEDULE_LABELS[k], "running": k in running_routines}
            for k in ROUTINE_MODULES
        ]
    })


@app.post("/api/run/{routine}")
async def api_run(routine: str):
    if routine not in ROUTINE_MODULES:
        return JSONResponse({"ok": False, "error": "Unknown routine"}, status_code=400)
    if routine in running_routines:
        return JSONResponse({"ok": False, "error": "Already running"})

    def _run():
        running_routines.add(routine)
        try:
            mod = importlib.import_module(ROUTINE_MODULES[routine])
            mod.run()
        except Exception as e:
            logging.getLogger("dashboard").error(f"{routine} failed: {e}")
        finally:
            running_routines.discard(routine)

    threading.Thread(target=_run, daemon=True).start()
    return JSONResponse({"ok": True})


# ── scheduler thread ──────────────────────────────────────────────────────────

def _start_scheduler():
    from apscheduler.schedulers.blocking import BlockingScheduler
    from apscheduler.triggers.cron import CronTrigger
    from routines import pre_market, market_open, midday, end_of_day, weekly_review

    def _wrap(name, fn):
        def wrapper():
            running_routines.add(name)
            try:
                fn()
            finally:
                running_routines.discard(name)
        return wrapper

    sched = BlockingScheduler(timezone=ET)
    sched.add_job(_wrap("pre_market",    pre_market.run),    CronTrigger(day_of_week="mon-fri", hour=6,  minute=0,  timezone=ET))
    sched.add_job(_wrap("market_open",   market_open.run),   CronTrigger(day_of_week="mon-fri", hour=8,  minute=30, timezone=ET))
    sched.add_job(_wrap("midday",        midday.run),        CronTrigger(day_of_week="mon-fri", hour=12, minute=0,  timezone=ET))
    sched.add_job(_wrap("end_of_day",    end_of_day.run),    CronTrigger(day_of_week="mon-fri", hour=15, minute=0,  timezone=ET))
    sched.add_job(_wrap("weekly_review", weekly_review.run), CronTrigger(day_of_week="fri",     hour=16, minute=0,  timezone=ET))
    logging.getLogger("scheduler").info("Scheduler running inside dashboard")
    sched.start()


threading.Thread(target=_start_scheduler, daemon=True).start()

if __name__ == "__main__":
    uvicorn.run("dashboard:app", host="0.0.0.0", port=8000, reload=False)
