---
name: today
description: "Use when Run the daily data sync, fundamental collection, hot stock discovery, multi-factor screening, Turtle/Bollinger/Oscillator analysis, and Korean .docx: covers today, adx, crossovers, fcf, macd"
metadata:
  holon-triggers: |
    run a daily pipeline
    sync stock data
---

---
name: today
description: >-
  Run the daily data sync, fundamental collection, hot stock discovery,
  multi-factor screening, Turtle/Bollinger/Oscillator analysis, and Korean .docx
  report pipeline — check DB vs CSV freshness, backfill from Yahoo Finance,
  discover hot stocks from NASDAQ/KOSPI/KOSDAQ 100, screen (P/E, RSI, volume,
  MA crossovers, FCF yield), run SMA 20/55/200 + RSI/MACD/Stochastic/ADX,
  optionally fetch news (alphaear-news) and sentiment (alphaear-sentiment),
  generate buy/sell report via anthropic-docx, post to Slack #h-report,
  optionally run setup-doctor pre-flight and twitter-timeline-to-slack post-pipeline.
  Use when the user asks to run a daily pipeline, sync stock data, discover hot
  stocks, screen stocks, or generate a daily report.
  Do NOT use for weekly price updates only (use weekly-stock-update). Do NOT use
  for stock analysis without data sync (use daily-stock-check). Do NOT use for
  CSV downloads from investing.com (use stock-csv-downloader).
metadata:
  author: thaki
  version: "7.0.0"
  category: execution
---

# Today — Daily Data Sync, Screening, and Report Pipeline

Orchestrates a multi-phase pipeline: optional setup-doctor pre-flight, data freshness check, data sync, fundamental data collection (financial statements from yfinance), hot stock discovery, multi-factor stock screening (P/E, RSI, volume spikes, MA crossovers, earnings proximity, FCF yield, AI sentiment), technical analysis (SMA 20/55/200, Bollinger Bands, RSI/MACD/Stochastic/ADX oscillators), optional market context (alphaear-news + alphaear-sentiment), Korean expert report generation (.docx + optional Slack), and optional twitter-timeline-to-slack post-pipeline. Generates per-stock buy/sell recommendations using 3-way signal combination (Turtle + Bollinger + Oscillator) enhanced with fundamental screening scores and AI sentiment. Reuses `weekly-stock-update`, `daily-stock-check`, `financial-data-collector`, `stock-screener`, `alphaear-reporter`, `anthr
