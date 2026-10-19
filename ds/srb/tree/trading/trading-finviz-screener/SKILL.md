---
name: trading-finviz-screener
description: "Use when Build and open FinViz screener URLs from natural language requests. Use when the user asks to \"screen stocks\", \"find stocks matching criteria\": covers trading, finviz, screener, caps, roe"
metadata:
  holon-triggers: |
    screen stocks
    find stocks matching criteria
---

---
name: trading-finviz-screener
description: >-
  Build and open FinViz screener URLs from natural language requests. Use when the user asks to "screen stocks", "find stocks matching criteria", "FinViz screener", "스크리너", "FinViz로 주식 필터", "高配当で成長している小型株を探したい", "Find oversold large caps with high ROE", or wants to filter by fundamentals or technicals. Supports Japanese and English input. No API key required for public screener. Do NOT use for daily stock signals (use daily-stock-check). Do NOT use for AlphaEar stock search (use alphaear-stock).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: execution
  source: claude-trading-skills
  api_required: none
---

# FinViz Screener

## Overview

Translate natural-language stock screening requests into FinViz screener filter codes, build the URL, and open it in Chrome. No API key required for public screener; FINVIZ Elite is auto-detected from `$FINVIZ_API_KEY` for enhanced functionality.

**Key Features:**
- Natural language → filter code mapping (Japanese + English)
- URL construction with view type and sort order selection
- Elite/Public auto-detection (environment variable or explicit flag)
- Chrome-first browser opening with OS-appropriate fallbacks
- Strict filter validation to prevent URL injection

---

## When to Use This Skill

**Explicit Triggers:**
- "高配当で成長している小型株を探したい"
- "Find oversold large caps near 52-week lows"
- "テクノロジーセクターの割安株をスクリーニングしたい"
- "Screen for stocks with insider buying"
- "FinVizでブレイクアウト候補を表示して"
- "Show me high-growth small caps on FinViz"
- "配当利回り5%以上でROE15%以上の銘柄を探して"

**Implicit Triggers:**
- User describes stock screening criteria using fundamental or technical terms
- User mentions FinViz screener or stock filtering
- User asks to find stocks matching specific financial characteristics

**When NOT to Use:**
- Deep fundamental analysis of a specific stock (use us-stock-analysis)
- Portfolio review with holdings (use portfolio-manager)
- Chart pattern analysis on images (use t
