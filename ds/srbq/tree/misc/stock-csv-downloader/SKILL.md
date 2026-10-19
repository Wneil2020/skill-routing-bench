---
name: stock-csv-downloader
description: "Use when Download historical stock price CSVs from investing.com and import into the database. Use when the user asks to download stock data, fetch stock CSVs: covers stock, csv, downloader, 주식, 체크"
metadata:
  holon-triggers: |
    download stock data
    fetch stock CSVs
---

---
name: stock-csv-downloader
description: >-
  Download historical stock price CSVs from investing.com and import into the
  database. Use when the user asks to download stock data, fetch stock CSVs,
  update stock prices from investing.com, or refresh historical price data. Do
  NOT use for quick weekly price updates from Yahoo Finance (use
  weekly-stock-update). Do NOT use for stock analysis, trading signals, or Slack
  posting (use daily-stock-check). Korean triggers: "주식", "체크", "데이터", "데이터베이스".
metadata:
  version: "1.0"
  category: "generation"
  author: "thaki"
---
# Stock CSV Downloader

Download per-ticker historical CSVs from investing.com via Playwright and import them into PostgreSQL using the existing CSV import pipeline.

## Prerequisites

- Python Playwright installed: `pip install playwright && playwright install chromium`
- Backend dependencies installed
- Database running and migrated (`alembic upgrade head`)

## Quick Start

```bash
cd backend
python scripts/download_stock_csv.py --ticker NVDA --import   # Single ticker
python scripts/download_stock_csv.py --gap-fill --import       # Fill all gaps
python scripts/download_stock_csv.py --list                    # List tickers
python scripts/download_stock_csv.py --status                  # DB coverage
```

## How It Works

The script uses Playwright to open investing.com in a headless browser, extracts the `instrument_id` from the page's `__NEXT_DATA__`, then calls the `api.investing.com` historical data API directly from the browser context. The JSON response is converted to the standard investing.com CSV format.

## Workflow

### Step 1: Check Coverage

See what data is already in the database and which tickers have gaps:

```bash
python scripts/download_stock_csv.py --status
```

Output shows first/last date, record count, missing weekdays, and coverage percentage for each ticker since 2021-01-01.

### Step 2–4: Download and Import

**Gap-fill (recommended):** `--gap-fill --import` fills missi
