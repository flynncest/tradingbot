import os, json
from http.server import BaseHTTPRequestHandler


def _get_data():
    from alpaca.trading.client import TradingClient
    client = TradingClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
        paper=os.environ.get("ALPACA_PAPER", "true").lower() == "true",
    )
    a = client.get_account()
    return {
        "ok": True,
        "equity": str(a.equity),
        "cash": str(a.cash),
        "buying_power": str(a.buying_power),
        "portfolio_value": str(a.portfolio_value),
        "daytrade_count": a.daytrade_count,
    }


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            body = json.dumps(_get_data()).encode()
        except Exception as e:
            body = json.dumps({"ok": False, "error": str(e)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass
