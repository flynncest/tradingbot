import os, json, urllib.request, urllib.error
from http.server import BaseHTTPRequestHandler

REPO = "flynncest/tradingbot"

WORKFLOWS = {
    "pre_market":    "pre_market.yml",
    "market_open":   "market_open.yml",
    "midday":        "midday.yml",
    "end_of_day":    "end_of_day.yml",
    "weekly_review": "weekly_review.yml",
}


def _trigger(routine: str) -> dict:
    wf = WORKFLOWS.get(routine)
    if not wf:
        return {"ok": False, "error": "Unknown routine"}

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return {"ok": False, "error": "GITHUB_TOKEN not set"}

    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{wf}/dispatches"
    data = json.dumps({"ref": "main"}).encode()
    req = urllib.request.Request(
        url, data=data, method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
    )
    try:
        urllib.request.urlopen(req, timeout=10)
        return {"ok": True}
    except urllib.error.HTTPError as e:
        return {"ok": False, "error": f"GitHub {e.code}: {e.read().decode()}"}


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        result = _trigger(body.get("routine", ""))
        out = json.dumps(result).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(out)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, *args):
        pass
