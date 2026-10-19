---
name: role-ceo
description: "Use when Analyze a given topic from the CEO/executive perspective — strategic impact, market positioning, stakeholder communication, and investment: covers role, ceo, CEO 관점, 경영진 분석, comms"
metadata:
  holon-triggers: |
    CEO perspective
    CEO 관점
---

---
name: role-ceo
description: >
  Analyze a given topic from the CEO/executive perspective — strategic impact, market positioning,
  stakeholder communication, and investment implications. Scores topic relevance (1-10) and produces
  a structured Korean analysis document when relevant (>= 5).   Composes pm-product-strategy, presentation-strategist, agency-executive-summary-generator,
  pm-market-research, workflow-miner, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "CEO perspective", "CEO 관점", "경영진 분석", "strategic impact analysis".
  Do NOT use for daily morning briefings (use morning-ship), investor deck creation only
  (use presentation-strategist), or routine stakeholder updates (use kwp-product-management-stakeholder-comms).
  Korean triggers: "CEO 관점", "경영진 분석", "전략 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# CEO Perspective Analyzer

Analyzes any business topic from the CEO's strategic viewpoint, covering market positioning,
financial implications, stakeholder communication needs, and decision-making priorities.

## Relevance Criteria

Score the topic 1-10 based on overlap with CEO concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Strategic direction | High | vision, strategy, roadmap, pivot, expansion, market entry |
| Financial impact | High | revenue, cost, ROI, investment, funding, runway, valuation |
| Market & competitive | High | market share, competition, TAM, positioning, differentiation |
| Stakeholder relations | Medium | investors, board, partners, customers, reputation |
| Organization & culture | Medium | hiring, team structure, leadership, culture, growth |
| Product decisions | Medium | product launch, feature priority, pricing, go-to-market |
| Operations & risk | Low | compliance, security incident, process change |
| Technical implementation | Low | code, API, database, CI/CD, testing |

Score >= 
