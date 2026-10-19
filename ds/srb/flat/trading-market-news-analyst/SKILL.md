---
name: trading-market-news-analyst
description: "Use when Analyze recent market-moving news events and their impact on equity markets and commodities. Use when the user asks to \"analyze market news\", \"FOMC: covers trading, market, news, cap, fomc"
metadata:
  holon-triggers: |
    analyze market news
    FOMC impact
---

---
name: trading-market-news-analyst
description: >-
  Analyze recent market-moving news events and their impact on equity markets and commodities.
  Use when the user asks to "analyze market news", "FOMC impact", "geopolitical commodity correlations",
  "mega-cap earnings review", "시장 뉴스 분석", "FOMC 영향", "지정학적 상품 상관관계", or needs impact-ranked analysis of major financial news from the past 10 days.
  Do NOT use for AlphaEar news aggregation (use alphaear-news). Do NOT use for AlphaEar sentiment analysis (use alphaear-sentiment). Do NOT use for general web search (use WebSearch directly).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: research
  source: claude-trading-skills
  api_required: none
---

# Market News Analyst

## Overview

Comprehensive analysis of market-moving news from the past 10 days. WebSearch/WebFetch for collection; evaluate impact magnitude; analyze market reactions; produce structured English reports ranked by impact. US equities and commodities focus.

## When to Use

- Recent major market news analysis (past 10 days)
- Event-specific impact (FOMC, earnings, geopolitical)
- Market news summary with impact assessment
- News-commodity correlations
- Central bank policy effects on markets

## Analysis Workflow

### Step 1: News Collection

**Search categories:** Monetary policy (FOMC, ECB, BOJ), Inflation/Economic (CPI, NFP, GDP), Mega-cap earnings (AAPL, MSFT, NVDA, etc.), Geopolitical, Commodities, Corporate.

**Sources:** Official (FederalReserve.gov, SEC, Treasury, BLS), Tier 1 (Bloomberg, Reuters, WSJ, FT), Specialized (CNBC, MarketWatch, S&P Platts). See [references/trusted_news_sources.md](references/trusted_news_sources.md).

**Filter:** Tier 1 market-moving events per [references/market_event_patterns.md](references/market_event_patterns.md). Exclude minor stock news.

### Step 2: Load Knowledge Base

**Always:** `market_event_patterns.md`, `trusted_news_sources.md`
**If monetary policy:** Central Bank section of market_e
