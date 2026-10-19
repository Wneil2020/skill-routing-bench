---
name: mirofish-opinion-sim
description: "Use when Run public opinion and social media reaction simulations using MiroFish multi-agent engine — predict how communities, media, regulators, and: covers mirofish, opinion, sim, consumers, crises"
metadata:
  holon-triggers: |
    simulate public reaction
    opinion simulation
---

---
name: mirofish-opinion-sim
description: Run public opinion and social media reaction simulations using MiroFish multi-agent engine — predict how communities, media, regulators, and consumers respond to events, crises, or announcements through swarm intelligence on simulated Twitter/Reddit platforms. Use when the user asks to "simulate public reaction", "opinion simulation", "crisis simulation", "PR impact prediction", "social media prediction", "여론 시뮬레이션", "위기 시뮬레이션", "PR 영향 예측", "mirofish-opinion", or any request to simulate public opinion dynamics. Do NOT use for financial market simulations (use mirofish-financial-sim). Do NOT use for general MiroFish operations (use mirofish). Do NOT use for actual Twitter scraping (use twitter-timeline-to-slack).
---

# MiroFish Public Opinion Simulation

## Overview

Specialized workflow for simulating public opinion dynamics on dual social media platforms (Twitter + Reddit). Creates digital communities of diverse stakeholders who react to news events, product launches, policy announcements, and crises.

## Prerequisites

Same as the `mirofish` skill. Verify: `curl -s http://localhost:5001/health`

## Workflow

### Step 1: Prepare Opinion Seed Document

Compile background context:
- Company/organization profile and history
- Product/service documentation
- Past public incidents or controversies
- Key stakeholder positions and influence networks
- Relevant social media history and sentiment baselines

### Step 2: Configure Opinion Simulation

```bash
curl -X POST http://localhost:5001/api/simulation/create \
  -H "Content-Type: application/json" \
  -d '{
    "graph_id": "<graph_id>",
    "prediction_requirement": "Simulate public reaction across Twitter and Reddit if a safety incident with our autonomous vehicle goes viral. Track sentiment trajectory over 7 days. Include consumer advocates, regulators, industry analysts, competing brands, general public, and media. Predict boycott probability and regulatory response likeli
