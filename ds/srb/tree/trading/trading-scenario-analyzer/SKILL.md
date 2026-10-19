---
name: trading-scenario-analyzer
description: "Use when Analyze news headlines for 18-month investment scenarios. Orchestrates scenario-analyst (main analysis) and strategy-reviewer (second: covers trading, scenario, analyzer, headlines, impacts"
---

---
name: trading-scenario-analyzer
description: >-
  Analyze news headlines for 18-month investment scenarios. Orchestrates scenario-analyst (main analysis)
  and strategy-reviewer (second opinion) agents to produce comprehensive reports with 1st/2nd/3rd-order
  impacts, recommended stocks, and review feedback in Japanese.
  Use for "scenario analysis", "headline scenario", "18-month outlook", "シナ리오 분석", "뉴스 시나리오", "18개월 전망".
  Do NOT use for daily stock signals (use daily-stock-check).
  Do NOT use for AlphaEar analysis (use alphaear-deepear-lite).
  Do NOT use for weekly price updates (use weekly-stock-update).
metadata:
  author: tradermonty
  version: "1.0.0"
  category: analysis
  source: claude-trading-skills
  api_required: none
---

# Headline Scenario Analyzer

## Overview

このスキルは、ニュースヘッドラインを起点として中長期（18ヶ月）の投資シナリオを分析します。
2つの専門エージェント（`scenario-analyst`と`strategy-reviewer`）を順次呼び出し、
多角的な分析と批判的レビューを統合した包括的なレポートを生成します。

## When to Use This Skill

以下の場合にこのスキルを使用してください：

- ニュースヘッドラインから中長期の投資影響を分析したい
- 18ヶ月後のシナリオを複数構築したい
- セクター・銘柄への影響を1次/2次/3次で整理したい
- セカンドオピニオンを含む包括的な分析が必要
- 日本語でのレポート出力が必要

**使用例:**
```
/headline-scenario-analyzer "Fed raises interest rates by 50bp, signals more hikes ahead"
/headline-scenario-analyzer "China announces new tariffs on US semiconductors"
/headline-scenario-analyzer "OPEC+ agrees to cut oil production by 2 million barrels per day"
```

## Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Skill（オーケストレーター）                        │
│                                                                      │
│  Phase 1: 準備                                                       │
│  ├─ ヘッドライン解析                                                  │
│  ├─ イベントタイプ分類                                                │
│  └─ リファレンス読み込み                                              │
│                                                                      │
│  Phase 2: エージェント呼び出し（Cursor Task subagen
