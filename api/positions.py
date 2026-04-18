import os, json
from http.server import BaseHTTPRequestHandler


def _get_data():
    from alpaca.trading.client import TradingClient
    client = TradingClient(
        api_key=os.environ["ALPACA_API_KEY"],
        secret_key=os.environ["ALPACA_SECRET_KEY"],
        paper=os.environ.get("ALPACA_PAPER", "true").lower() == "true",
    )
    positions = client.get_all_positions()
    return {
        "ok": True,
        "positions": [
            {
                "symbol": p.symbol,
                "qty": str(p.qty),
                "avg_entry_price": str(p.avg_entry_price),
                "current_price": str(p.current_price),
                "market_value": str(p.market_value),
                "unrealized_pl": str(p.unrealized_pl),
                "unrealized_plpc": f"{float(p.unrealized_plpc)*100:.2f}%",
            }
            for p in positions
        ],
    }


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            body = json.dumps(_get_data()).encode()
        except Exception as e:
            body = json.dumps({"ok": False, "positions": [], "error": str(e)}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):
        pass
