---
name: weekly-stock-update
description: "Use when Fetch the last week of stock prices from Yahoo Finance and upsert into PostgreSQL for all tracked tickers. Optionally sync quarterly financial: covers weekly, stock, update, 주식, 테스트"
metadata:
  holon-triggers: |
    update recent stock data
    refresh weekly prices
---

---
name: weekly-stock-update
description: >-
  Fetch the last week of stock prices from Yahoo Finance and upsert into
  PostgreSQL for all tracked tickers. Optionally sync quarterly financial
  statements (--fundamentals). Use when the user asks to update recent stock
  data, refresh weekly prices, sync latest prices to DB, sync financial
  statements, or run a quick stock update. Do NOT use for historical backfill or
  gap-fill from investing.com (use stock-csv-downloader). Do NOT use for stock
  analysis, trading signals, or Slack posting (use daily-stock-check). Korean
  triggers: "주식", "테스트", "체크", "동기화".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Weekly Stock Update

Fetch recent stock prices from Yahoo Finance (yfinance) and batch upsert them into PostgreSQL. Covers all configured tickers with a single lightweight script — no browser automation required. With `--fundamentals`, also syncs quarterly financial statements (income, balance sheet, cash flow) and computed metrics (P/E, ROE, FCF yield, etc.).

## Prerequisites

- Python dependencies installed (`yfinance`, `sqlalchemy`, `asyncpg`)
- PostgreSQL running and migrated (`alembic upgrade head`)

## Quick Start

```bash
cd backend
python scripts/weekly_stock_update.py                    # All tickers, last 10 days
python scripts/weekly_stock_update.py --fundamentals     # Prices + financial statements
python scripts/weekly_stock_update.py --status           # Show DB coverage
python scripts/weekly_stock_update.py --dry-run          # Preview without DB write
```

## Workflow

### Step 1: Check Current Coverage

```bash
cd backend
python scripts/weekly_stock_update.py --status
```

Shows record count, first date, and last date for each of the 21 tickers.

### Step 2: Run Update

```bash
cd backend
python scripts/weekly_stock_update.py
```

For specific tickers only:

```bash
python scripts/weekly_stock_update.py --ticker NVDA AAPL 005930
```

For a custom lookback window (e.g
