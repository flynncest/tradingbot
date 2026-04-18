import os
import json
from decimal import Decimal

TOOL_DEFINITIONS = [
    {
        "name": "get_account",
        "description": "Get Alpaca account info: equity, cash, buying power, day P&L.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "get_positions",
        "description": "Get all open positions with current P&L.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "place_market_order",
        "description": "Place a market buy or sell order.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "qty": {"type": "number", "description": "Number of shares"},
                "side": {"type": "string", "enum": ["buy", "sell"]},
            },
            "required": ["symbol", "qty", "side"],
        },
    },
    {
        "name": "place_trailing_stop",
        "description": "Place a trailing stop sell order to protect a long position.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"},
                "qty": {"type": "number"},
                "trail_percent": {"type": "number", "description": "Trail % (e.g. 5.0 for 5%)"},
            },
            "required": ["symbol", "qty", "trail_percent"],
        },
    },
    {
        "name": "close_position",
        "description": "Close an entire position in a symbol.",
        "input_schema": {
            "type": "object",
            "properties": {"symbol": {"type": "string"}},
            "required": ["symbol"],
        },
    },
    {
        "name": "cancel_all_orders",
        "description": "Cancel all open orders.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "get_open_orders",
        "description": "List all open/pending orders.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
]


def _get_client():
    from alpaca.trading.client import TradingClient
    return TradingClient(
        api_key=os.getenv("ALPACA_API_KEY"),
        secret_key=os.getenv("ALPACA_SECRET_KEY"),
        paper=os.getenv("ALPACA_PAPER", "true").lower() == "true",
    )


def get_account() -> str:
    try:
        client = _get_client()
        acct = client.get_account()
        return json.dumps({
            "equity": str(acct.equity),
            "cash": str(acct.cash),
            "buying_power": str(acct.buying_power),
            "portfolio_value": str(acct.portfolio_value),
            "daytrade_count": acct.daytrade_count,
            "pattern_day_trader": acct.pattern_day_trader,
        }, indent=2)
    except Exception as e:
        return f"Error getting account: {e}"


def get_positions() -> str:
    try:
        client = _get_client()
        positions = client.get_all_positions()
        if not positions:
            return "No open positions."
        result = []
        for p in positions:
            result.append({
                "symbol": p.symbol,
                "qty": str(p.qty),
                "avg_entry_price": str(p.avg_entry_price),
                "current_price": str(p.current_price),
                "market_value": str(p.market_value),
                "unrealized_pl": str(p.unrealized_pl),
                "unrealized_plpc": f"{float(p.unrealized_plpc)*100:.2f}%",
            })
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error getting positions: {e}"


def place_market_order(symbol: str, qty: float, side: str) -> str:
    try:
        from alpaca.trading.requests import MarketOrderRequest
        from alpaca.trading.enums import OrderSide, TimeInForce
        client = _get_client()
        req = MarketOrderRequest(
            symbol=symbol.upper(),
            qty=qty,
            side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
            time_in_force=TimeInForce.DAY,
        )
        order = client.submit_order(req)
        return json.dumps({
            "order_id": str(order.id),
            "symbol": order.symbol,
            "qty": str(order.qty),
            "side": str(order.side),
            "status": str(order.status),
        }, indent=2)
    except Exception as e:
        return f"Error placing order: {e}"


def place_trailing_stop(symbol: str, qty: float, trail_percent: float) -> str:
    try:
        from alpaca.trading.requests import TrailingStopOrderRequest
        from alpaca.trading.enums import OrderSide, TimeInForce
        client = _get_client()
        req = TrailingStopOrderRequest(
            symbol=symbol.upper(),
            qty=qty,
            side=OrderSide.SELL,
            time_in_force=TimeInForce.GTC,
            trail_percent=trail_percent,
        )
        order = client.submit_order(req)
        return json.dumps({
            "order_id": str(order.id),
            "symbol": order.symbol,
            "qty": str(order.qty),
            "trail_percent": trail_percent,
            "status": str(order.status),
        }, indent=2)
    except Exception as e:
        return f"Error placing trailing stop: {e}"


def close_position(symbol: str) -> str:
    try:
        client = _get_client()
        result = client.close_position(symbol.upper())
        return f"Closed position in {symbol}: order {result.id}"
    except Exception as e:
        return f"Error closing position {symbol}: {e}"


def cancel_all_orders() -> str:
    try:
        client = _get_client()
        cancelled = client.cancel_orders()
        return f"Cancelled {len(cancelled)} orders."
    except Exception as e:
        return f"Error cancelling orders: {e}"


def get_open_orders() -> str:
    try:
        from alpaca.trading.requests import GetOrdersRequest
        from alpaca.trading.enums import QueryOrderStatus
        client = _get_client()
        orders = client.get_orders(GetOrdersRequest(status=QueryOrderStatus.OPEN))
        if not orders:
            return "No open orders."
        result = []
        for o in orders:
            result.append({
                "id": str(o.id),
                "symbol": o.symbol,
                "qty": str(o.qty),
                "side": str(o.side),
                "type": str(o.order_type),
                "status": str(o.status),
            })
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error getting orders: {e}"


HANDLERS = {
    "get_account": get_account,
    "get_positions": get_positions,
    "place_market_order": place_market_order,
    "place_trailing_stop": place_trailing_stop,
    "close_position": close_position,
    "cancel_all_orders": cancel_all_orders,
    "get_open_orders": get_open_orders,
}
