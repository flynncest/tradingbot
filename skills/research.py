import json
from datetime import datetime

TOOL_DEFINITIONS = [
    {
        "name": "get_stock_news",
        "description": "Get recent news headlines for a stock ticker or index (e.g. SPY, AAPL, NVDA).",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string", "description": "Ticker symbol"},
                "limit": {"type": "integer", "default": 8},
            },
            "required": ["symbol"],
        },
    },
    {
        "name": "get_market_snapshot",
        "description": "Get current price, day change, and volume for a ticker.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbol": {"type": "string"}
            },
            "required": ["symbol"],
        },
    },
    {
        "name": "get_multiple_snapshots",
        "description": "Get price snapshots for a list of tickers at once.",
        "input_schema": {
            "type": "object",
            "properties": {
                "symbols": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of ticker symbols, e.g. ['SPY','QQQ','NVDA']"
                }
            },
            "required": ["symbols"],
        },
    },
]


def get_stock_news(symbol: str, limit: int = 8) -> str:
    try:
        import yfinance as yf
        ticker = yf.Ticker(symbol.upper())
        news = ticker.news or []
        if not news:
            return f"No news found for {symbol}"
        results = []
        for n in news[:limit]:
            content = n.get("content", {})
            title = content.get("title") or n.get("title", "")
            summary = content.get("summary") or n.get("summary", "")
            provider = content.get("provider", {}).get("displayName", "") if isinstance(content.get("provider"), dict) else ""
            pub_date = content.get("pubDate") or ""
            results.append(f"**{title}**\n{provider} {pub_date}\n{summary[:200]}")
        return "\n\n".join(results)
    except Exception as e:
        return f"Error fetching news for {symbol}: {e}"


def get_market_snapshot(symbol: str) -> str:
    try:
        import yfinance as yf
        t = yf.Ticker(symbol.upper())
        info = t.fast_info
        price = info.last_price
        prev  = info.previous_close
        chg   = price - prev
        pct   = (chg / prev) * 100 if prev else 0
        vol   = getattr(info, 'three_month_average_volume', None)
        return json.dumps({
            "symbol": symbol.upper(),
            "price": round(price, 2),
            "change": round(chg, 2),
            "change_pct": f"{pct:+.2f}%",
            "prev_close": round(prev, 2),
            "avg_volume": vol,
        })
    except Exception as e:
        return f"Error fetching snapshot for {symbol}: {e}"


def get_multiple_snapshots(symbols: list[str]) -> str:
    results = []
    for s in symbols:
        results.append(get_market_snapshot(s))
    return "\n".join(results)


HANDLERS = {
    "get_stock_news": get_stock_news,
    "get_market_snapshot": get_market_snapshot,
    "get_multiple_snapshots": get_multiple_snapshots,
}
