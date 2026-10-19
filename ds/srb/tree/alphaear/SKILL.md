---
name: alphaear
description: "Use when the request concerns the alphaear category of skills: covers alphaear"
---

Grouping node for the 0 skills of the alphaear category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **alphaear-deepear-lite** (`alphaear-deepear-lite/`): Use when Lightweight orchestration of AlphaEar skills for comprehensive financial analysis. Use when the user asks broad questions like "Analyze how X affects: covers alphaear, deepear, lite, 분석, 체크
- **alphaear-logic-visualizer** (`alphaear-logic-visualizer/`): Use when Creates Draw.io XML diagrams to visualize financial logic chains and transmission flows. Use when explaining investment theses, signal: covers alphaear, logic, visualizer, 생성, 설계
- **alphaear-news** (`alphaear-news/`): Use when Fetch real-time financial news from 10+ sources (Weibo, Zhihu, WallstreetCN, Hacker News, etc.) and Polymarket prediction market data. Use when: covers alphaear, news, 뉴스, 리포트, polymarket
- **alphaear-predictor** (`alphaear-predictor/`): Use when Market prediction using Kronos time-series model with news-aware adjustments. Use when user needs finance market time-series forecasting: covers alphaear, predictor, 테스트, 체크, adjustments
- **alphaear-reporter** (`alphaear-reporter/`): Use when Plan, write, and edit professional financial reports, generate finance chart configurations. Use when condensing finance analysis into a: covers alphaear, reporter, 생성, 체크, assembling
- **alphaear-search** (`alphaear-search/`): Use when Perform finance-specific web searches (Jina/DDG/Baidu) and local RAG search. Use when the user needs finance info from the web, local document store: covers alphaear, search, 검색, 주식, baidu
- **alphaear-sentiment** (`alphaear-sentiment/`): Use when Analyze financial text sentiment using LLM (default) or FinBERT (optional). Use when the user needs to determine sentiment: covers alphaear, sentiment, 감성, 분석, negative
- **alphaear-signal-tracker** (`alphaear-signal-tracker/`): Use when Tracks finance investment signal evolution — determines if signals are Strengthened, Weakened, or Falsified based on new market info. Use when: covers alphaear, signal, tracker, 체크, 리포트
- **alphaear-stock** (`alphaear-stock/`): Use when Search A-Share/HK/US stock tickers and retrieve OHLCV price history. Use when the user asks about stock codes, recent price changes, specific company: covers alphaear, stock, 주식, 체크, codes

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
