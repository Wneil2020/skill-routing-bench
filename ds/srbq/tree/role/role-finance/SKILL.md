---
name: role-finance
description: "Use when Analyze a given topic from the Finance perspective — financial impact, budget variance, ROI analysis, cash flow implications, and: covers role, finance, 재무 관점, 재무 분석, reconciliation"
metadata:
  holon-triggers: |
    finance perspective
    재무 관점
---

---
name: role-finance
description: >
  Analyze a given topic from the Finance perspective — financial impact, budget variance,
  ROI analysis, cash flow implications, and audit/compliance requirements.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes kwp-finance-variance-analysis, kwp-finance-financial-statements,
  agency-finance-tracker, kwp-finance-audit-support, workflow-miner,
  semantic-guard, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "finance perspective", "재무 관점", "재무 분석", "financial impact analysis".
  Do NOT use for financial statement generation (use kwp-finance-financial-statements),
  month-end close management (use kwp-finance-close-management), or
  reconciliation (use kwp-finance-reconciliation).
  Korean triggers: "재무 관점", "재무 분석", "재무 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# Finance Perspective Analyzer

Analyzes any business topic from the Finance team's viewpoint, covering financial impact,
budget implications, ROI projection, cash flow effects, and audit compliance.

## Relevance Criteria

Score the topic 1-10 based on overlap with finance concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Revenue & cost | High | revenue, cost, margin, pricing, unit economics |
| Budget & forecast | High | budget, forecast, variance, capex, opex |
| Investment & ROI | High | ROI, payback, NPV, IRR, investment, funding |
| Cash flow | High | cash flow, runway, burn rate, working capital |
| Audit & compliance | Medium | audit, SOX, tax, regulatory, disclosure |
| Vendor & procurement | Medium | vendor, contract, SLA, procurement, licensing |
| Risk management | Medium | financial risk, hedging, insurance, contingency |
| Financial reporting | Medium | P&L, balance sheet, KPI, dashboard |
| Technical implementation | Low | code, API, database, deploy
