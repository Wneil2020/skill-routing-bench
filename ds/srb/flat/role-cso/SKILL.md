---
name: role-cso
description: "Use when Analyze a given topic from the CSO (Chief Strategy Officer) perspective — market sizing, competitive positioning, GTM strategy, business model: covers role, cso, CSO 관점, 전략 분석, officer"
metadata:
  holon-triggers: |
    CSO perspective
    CSO 관점
---

---
name: role-cso
description: >
  Analyze a given topic from the CSO (Chief Strategy Officer) perspective — market sizing,
  competitive positioning, GTM strategy, business model impact, and scenario planning.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes pm-market-research, pm-go-to-market, pm-product-strategy,
  kwp-marketing-competitive-analysis, workflow-miner, skill-composer,
  and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "CSO perspective", "CSO 관점", "전략 분석", "market strategy impact".
  Do NOT use for full GTM execution (use pm-go-to-market), Lean Canvas only
  (use pm-product-strategy), or competitive battlecard creation (use kwp-sales-competitive-intelligence).
  Korean triggers: "CSO 관점", "전략 분석", "시장 전략 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# CSO Perspective Analyzer

Analyzes any business topic from the CSO's strategic viewpoint, covering market opportunity,
competitive landscape, go-to-market implications, business model changes, and scenario planning.

## Relevance Criteria

Score the topic 1-10 based on overlap with CSO concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Market opportunity | High | TAM, SAM, SOM, market size, growth, expansion |
| Competitive landscape | High | competitor, differentiation, positioning, battlecard |
| GTM strategy | High | go-to-market, launch, channel, ICP, beachhead |
| Business model | High | pricing, monetization, revenue model, unit economics |
| Product strategy | High | vision, roadmap, pivot, value proposition |
| Growth & acquisition | Medium | growth loop, viral, PLG, funnel, conversion |
| Partnerships | Medium | partner, ecosystem, integration, alliance |
| Trends & research | Medium | trend, industry, regulation, disruption |
| Technical implementation | Low | code, API, database, CI/CD |
| HR
