---
name: tab
description: "Use when the request concerns the tab category of skills: covers tab"
---

Grouping node for the 0 skills of the tab category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **tab-analysis-run** (`tab-analysis-run/`): Use when Run event study analysis (CAR), generate reports, and query patterns. Use when running analysis, '분석 실행', 'tab-analysis-run', 'event study': covers tab, analysis, run, car, screening
- **tab-bollinger-refresh** (`tab-bollinger-refresh/`): Use when Daily refresh of Bollinger Bands signals via POST /bollinger-bands/daily-refresh across 4 methods. Use when refreshing Bollinger, '볼린저 밴드 갱신': covers tab, bollinger, refresh, methods, bands
- **tab-dashboard-summary** (`tab-dashboard-summary/`): Use when Fetch aggregated dashboard data in a single API call via GET /dashboard/agent-summary. Use when fetching dashboard overview, '대시보드 요약': covers tab, dashboard, summary, aggregated, fetching
- **tab-dualma-refresh** (`tab-dualma-refresh/`): Use when Daily refresh of DualMA strategy indicators via daily_stock_check --source db script. Use when refreshing DualMA, '이중이평선 갱신': covers tab, dualma, refresh, refreshing, backtest
- **tab-event-detect** (`tab-event-detect/`): Use when Trigger event detection from RSS feeds via POST /events/detect. Use when detecting events, '이벤트 탐지', 'tab-event-detect', 'RSS event scan'. Do NOT: covers tab, event, detect, detecting, feeds
- **tab-fundamental-sync** (`tab-fundamental-sync/`): Use when Sync quarterly financial statements from Yahoo Finance via POST /financial-statements/sync. Use when syncing fundamentals, '재무제표 동기화': covers tab, fundamental, sync, fundamentals, quarterly
- **tab-genai-features** (`tab-genai-features/`): Use when Generate AI-powered prediction features via POST /genai-features/generate for all tracked stocks. Use when generating GenAI features, 'GenAI 피처: covers tab, genai, features, powered, tracked
- **tab-glossary** (`tab-glossary/`): Use when Manage financial glossary terms via CRUD at /glossary, batch import with POST /glossary/batch, search with GET /glossary/search, and export with: covers tab, glossary, terms, import, export
- **tab-hot-stock-discovery** (`tab-hot-stock-discovery/`): Use when Discover hottest untracked stocks from NASDAQ/KOSPI/KOSDAQ 100 via POST /admin/discover-hot-stocks. Use when discovering hot stocks, '핫 종목 발견': covers tab, hot, stock, hottest, untracked
- **tab-kiwoom** (`tab-kiwoom/`): Use when Interface with Kiwoom Securities brokerage API for real-time Korean stock quotes, order placement, and account management. Use when: covers tab, kiwoom, brokerage, interacting, placement
- **tab-llm-agents** (`tab-llm-agents/`): Use when Run LLM agent pipeline via POST /llm-agents/run and refresh macro data via POST /llm-agents/macro/refresh. Use when running LLM agents, 'LLM 에이전트 실행': covers tab, llm, genai, macro, refresh
- **tab-market-breadth** (`tab-market-breadth/`): Use when Refresh and query market breadth data via POST /market-breadth/refresh and GET /market-breadth/latest, /trend, /composite, /alerts. Use when: covers tab, market, breadth, composite, alerts
- **tab-market-environment** (`tab-market-environment/`): Use when Refresh and query market environment (regime, breadth, news, signals) via POST /market-environment/refresh and GET: covers tab, market, environment, regime, details
- **tab-news-fetch** (`tab-news-fetch/`): Use when Fetch news from all sources via POST /news/fetch, query latest with GET /news/latest, and get aggregated summary via GET /news/summary. Use: covers tab, news, fetch, aggregated, fetching
- **tab-patterns** (`tab-patterns/`): Use when Query event-study pattern groups via GET /patterns, search with GET /patterns/search, get statistics with GET /patterns/stats, and export with: covers tab, patterns, car, groups, statistics
- **tab-report-generate** (`tab-report-generate/`): Use when Generate a daily Korean .docx stock analysis report via POST /reports/generate/daily and list past reports with GET /reports. Use when: covers tab, report, generate, past, generating
- **tab-screening** (`tab-screening/`): Use when Run multi-factor stock screening via POST /admin/screen-stocks combining P/E, RSI, volume, MA signals. Use when screening stocks, '종목 스크리닝': covers tab, screening, admin, rsi, combining
- **tab-stock-sync** (`tab-stock-sync/`): Use when Daily stock price sync from Yahoo Finance to PostgreSQL for all tracked tickers via weekly_stock_update.py script. Use when syncing prices, '주식 데이터: covers tab, stock, sync, prices, tickers
- **tab-strategy-comparison** (`tab-strategy-comparison/`): Use when Run unified cross-strategy backtest comparison via POST /strategy-comparison/run for Turtle, DualMA, and Bollinger strategies. Use when: covers tab, strategy, comparison, dualma, bands
- **tab-technical-analysis** (`tab-technical-analysis/`): Use when Pre-compute technical analysis indicators for all tracked tickers via POST /technical-analysis/batch-compute. Use when computing TA, '기술적: covers tab, technical, analysis, ticker, computing
- **tab-turtle-refresh** (`tab-turtle-refresh/`): Use when Daily refresh of Turtle Trading indicators via POST /turtle/indicators/daily-refresh. Use when refreshing Turtle indicators, '터틀 지표 갱신': covers tab, turtle, refresh, bands, refreshing

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
