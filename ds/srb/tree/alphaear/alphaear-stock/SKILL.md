---
name: alphaear-stock
description: "Use when Search A-Share/HK/US stock tickers and retrieve OHLCV price history. Use when the user asks about stock codes, recent price changes, specific company: covers alphaear, stock, 주식, 체크, codes"
metadata:
  holon-triggers: |
    recent price changes
    specific company stock info
---

---
name: alphaear-stock
description: >-
  Search A-Share/HK/US stock tickers and retrieve OHLCV price history. Use when
  the user asks about stock codes, recent price changes, specific company stock
  info, or ad-hoc historical price queries. Do NOT use for routine weekly price
  updates (use weekly-stock-update). Do NOT use for CSV downloads from
  investing.com (use stock-csv-downloader). Do NOT use for technical indicator
  analysis (use daily-stock-check). Korean triggers: "주식", "체크", "검색".
metadata:
  version: "1.0.0"
  category: "data-collection"
  author: "alphaear"
---
# AlphaEar Stock

## Overview

Search A-Share, HK, and US stock tickers by code or name, and retrieve historical OHLCV price data. Optimized for ad-hoc lookups and historical queries. The project also tracks 21 tickers in `data/latest/` and PostgreSQL — for routine updates, use `weekly-stock-update`; for CSV imports from investing.com, use `stock-csv-downloader`.

## Prerequisites

- Python 3.10+
- `pandas`, `requests`, `akshare`, `yfinance`
- `scripts/database_manager.py` (PostgreSQL or SQLite for local cache)
- Network access for akshare/yfinance

## Workflow

1. **Initialize**: Create `DatabaseManager`, then `StockTools(db)`.
2. **Search ticker**: Call `StockTools.search_ticker(query)` — fuzzy search by code (e.g. "600519") or name (e.g. "Moutai", "宁德时代").
3. **Get price**: Call `StockTools.get_stock_price(ticker, start_date, end_date)` with dates in `YYYY-MM-DD` format.
4. **Routine updates**: For the 21 tracked tickers, prefer `weekly-stock-update` skill instead of this skill.
5. **CSV downloads**: For investing.com historical CSVs and gap-fill, use `stock-csv-downloader` skill.

## Examples

| Trigger | Action | Result |
|--------|--------|--------|
| "Search for Moutai" | `search_ticker("Moutai")` | `[{code: "600519", name: "贵州茅台"}]` |
| "Price history of 600519" | `get_stock_price("600519", "2025-01-01", "2025-02-28")` | DataFrame with date, open, close, high, low, volume, change_pct
