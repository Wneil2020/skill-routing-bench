---
name: mirofish-financial-sim
description: "Use when Run financial market scenario simulations using MiroFish multi-agent engine — predict market reactions to Fed decisions, earnings: covers mirofish, financial, sim, fed, macroeconomic"
metadata:
  holon-triggers: |
    simulate market scenario
    predict Fed impact
---

---
name: mirofish-financial-sim
description: Run financial market scenario simulations using MiroFish multi-agent engine — predict market reactions to Fed decisions, earnings surprises, geopolitical events, and macroeconomic shifts through swarm intelligence. Use when the user asks to "simulate market scenario", "predict Fed impact", "financial simulation", "earnings reaction prediction", "금융 시나리오 시뮬레이션", "시장 반응 예측", "Fed 영향 시뮬레이션", "mirofish-financial", or any request to simulate financial market reactions using AI agents. Do NOT use for static stock analysis without simulation (use daily-stock-check). Do NOT use for real-time market data only (use alphaear-stock). Do NOT use for general MiroFish operations (use mirofish).
---

# MiroFish Financial Scenario Simulation

## Overview

Specialized workflow for running financial market prediction simulations. Feeds market data and economic reports into MiroFish to create a digital financial world populated by investor agents, analyst agents, and institutional agents that react to injected market events.

## Prerequisites

Same as the `mirofish` skill. Verify: `curl -s http://localhost:5001/health`

## Workflow

### Step 1: Prepare Financial Seed Document

Combine relevant financial data into a seed document:

```python
seed_sources = [
    "Fed FOMC minutes or press conference transcript",
    "Company earnings reports (10-K, 10-Q)",
    "Macro indicators (CPI, unemployment, GDP)",
    "Financial news articles from alphaear-news",
    "Analyst reports and consensus estimates"
]
```

**Integration with existing skills:**
- Run `alphaear-news` first to gather current financial news
- Use `trading-market-environment-analysis` for macro context
- Pull `alphaear-sentiment` scores for baseline sentiment

### Step 2: Configure Financial Simulation

```bash
# Create simulation with financial parameters
curl -X POST http://localhost:5001/api/simulation/create \
  -H "Content-Type: application/json" \
  -d '{
    "graph_id": "<g
