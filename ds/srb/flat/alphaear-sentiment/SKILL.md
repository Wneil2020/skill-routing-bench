---
name: alphaear-sentiment
description: "Use when Analyze financial text sentiment using LLM (default) or FinBERT (optional). Use when the user needs to determine sentiment: covers alphaear, sentiment, 감성, 분석, negative"
---

---
name: alphaear-sentiment
description: >-
  Analyze financial text sentiment using LLM (default) or FinBERT (optional).
  Use when the user needs to determine sentiment (positive/negative/neutral) and
  score of financial text. Do NOT use for news aggregation (use alphaear-news).
  Do NOT use for trading signal generation (use daily-stock-check). Do NOT use
  for market prediction (use alphaear-predictor). Korean triggers: "감성", "분석",
  "체크", "주식".
metadata:
  version: "1.0.0"
  category: "analysis"
  author: "alphaear"
---
# AlphaEar Sentiment

## Overview

Analyze financial text sentiment with a score from -1.0 (negative) to 1.0 (positive). Default mode is LLM-only — no torch/transformers required. Optional FinBERT mode provides fast local batch analysis when `torch` and `transformers` are installed. Results are persisted to PostgreSQL via `scripts/database_manager.py`.

## Prerequisites

- **Minimal (LLM-only)**: `loguru`, `scripts/database_manager.py`, LLM API credentials.
- **Full (FinBERT)**: `torch`, `transformers`, plus minimal deps.
- PostgreSQL configured for `daily_news` table (or compatible backend).

## Workflow

1. **Initialize**: Create `DatabaseManager`, then `SentimentTools(db, mode="llm")` — use `"llm"` for default (no torch).
2. **Single analysis (LLM)**: Run the prompt below with your LLM; parse JSON; optionally call `update_single_news_sentiment(id, score, reason)` to save.
3. **Single analysis (FinBERT)**: If `mode="bert"` or `mode="auto"` with BERT available, call `analyze_sentiment(text)` — returns `{score, label, reason}`.
4. **Batch update**: Call `batch_update_news_sentiment(source, limit)` — uses FinBERT when available; otherwise no-op (use Agent + `update_single_news_sentiment` for LLM batch).
5. **Persistence**: `update_single_news_sentiment(news_id, score, reason)` writes to `daily_news.sentiment_score` and `meta_data.sentiment_reason`.

## LLM Prompt (Default Mode)

Use this prompt for sentiment analysis when FinBERT is not used:


