---
name: daily-stock-check
description: "Use when Analyze stocks from Turtle Trading (MA + Donchian) and Bollinger Bands perspectives, then post a buy/sell/neutral summary to Slack. Use when the user asks: covers daily, stock, check, 주식, 체크"
metadata:
  holon-triggers: |
    run a daily stock check
    analyze stock signals
---

---
name: daily-stock-check
description: >-
  Analyze stocks from Turtle Trading (MA + Donchian) and Bollinger Bands
  perspectives, then post a buy/sell/neutral summary to Slack. Use when the user
  asks to run a daily stock check, analyze stock signals, or post trading
  analysis to Slack. Do NOT use for downloading historical stock CSVs or
  refreshing price data (use stock-csv-downloader). Do NOT use for updating
  recent stock prices in the database (use weekly-stock-update). Korean
  triggers: "주식", "체크", "분석", "데이터".
metadata:
  version: "1.0.0"
  category: "generation"
  author: "thaki"
---
# Daily Stock Check

Analyze all stocks in `data/latest/` using Turtle Trading and Bollinger Bands methodologies, then post a formatted summary to `#h-daily-stock-check` on Slack.

## Prerequisites

- Stock CSV files exist in `data/latest/` (download using `stock-csv-downloader` skill if missing)
- Slack MCP server is connected
- Python 3.11+ available

## Quick Start

```bash
cd backend
python -m scripts.daily_stock_check --dir ../data/latest
```

## Analysis Methodology

### Turtle Trading Perspective

Evaluates trend-following signals using:

| Indicator | Period | Signal Logic |
|-----------|--------|-------------|
| SMA | 20, 50 | Price above = bullish, below = bearish |
| EMA | 20 | Trend direction confirmation |
| Donchian Channel | 20 | Price >= 20-high = BUY breakout, <= 20-low = SELL breakdown |
| ATR | 20 | Volatility context |

Scoring: SMA above = +1, SMA below = -1, Donchian breakout = +2, Donchian breakdown = -2.
- Score >= 3: STRONG_BUY
- Score >= 2: BUY
- Score <= -3: STRONG_SELL
- Score <= -2: SELL
- Otherwise: NEUTRAL

### Bollinger Bands Perspective

Evaluates mean-reversion and breakout signals using:

| Indicator | Params | Signal Logic |
|-----------|--------|-------------|
| Bollinger Bands | (20, 2σ) | Upper/Middle/Lower band levels |
| %B | - | Position within bands (0 = lower, 1 = upper) |
| BandWidth | - | Volatility measure |
| Squeeze | 20-ba
