---
name: mirofish
description: "Use when Orchestrate MiroFish multi-agent swarm intelligence simulations — auto-generate seed documents from daily stock analysis, build GraphRAG: covers mirofish, eye, god, digital, graphrag"
metadata:
  holon-triggers: |
    run MiroFish simulation
    predict scenario
---

---
name: mirofish
description: Orchestrate MiroFish multi-agent swarm intelligence simulations — auto-generate seed documents from daily stock analysis, build GraphRAG knowledge graphs, run simulations with 26 AI agent personas, produce prediction reports, and interact with simulated agents. Supports a **Daily Stock Mode** for repeatable analysis from `today` pipeline outputs. Use when the user asks to "run MiroFish simulation", "predict scenario", "swarm simulation", "multi-agent prediction", "시뮬레이션 실행", "시나리오 예측", "MiroFish", "미로피쉬", "God's Eye injection", "digital sandbox", "/mirofish", or any request to simulate future scenarios using autonomous AI agents. Do NOT use for daily stock checks without simulation (use daily-stock-check). Do NOT use for simple financial news aggregation (use alphaear-news). Do NOT use for static technical analysis (use trading-technical-analyst).
---

# MiroFish Orchestrator

## Overview

MiroFish is a multi-agent swarm intelligence prediction engine. It constructs high-fidelity parallel digital worlds from seed documents using GraphRAG + autonomous agents with long-term memory (Zep Cloud), enabling "God's Eye View" variable injection for future scenario prediction.

**Repository:** `~/thaki/MiroFish/`
**Backend API:** `http://localhost:5001`
**Frontend UI:** `http://localhost:3000`

## Prerequisites

- MiroFish cloned to `~/thaki/MiroFish/`
- Dependencies installed: `npm run setup:all`
- `.env` configured with `LLM_API_KEY`, `LLM_BASE_URL`, `LLM_MODEL_NAME`, `ZEP_API_KEY`
- Services running: `cd ~/thaki/MiroFish && npm run dev` (or `npm run backend` for API only)

Verify with: `curl -s http://localhost:5001/health`

> **IMPORTANT:** After updating `.env`, you MUST restart the backend. It caches env vars at startup.
> ```bash
> lsof -ti :5001 | xargs kill -9 && cd ~/thaki/MiroFish && npm run backend
> ```

---

## Daily Stock Mode (Primary Workflow)

The standard daily workflow auto-generates a seed document from `today` pipeline out
