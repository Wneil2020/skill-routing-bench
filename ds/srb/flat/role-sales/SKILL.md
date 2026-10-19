---
name: role-sales
description: "Use when Analyze a given topic from the Sales perspective — sales enablement impact, competitive battlecard needs, customer outreach implications, pipeline: covers role, sales, 영업 관점, 영업 분석, effects"
metadata:
  holon-triggers: |
    sales perspective
    영업 관점
---

---
name: role-sales
description: >
  Analyze a given topic from the Sales perspective — sales enablement impact, competitive
  battlecard needs, customer outreach implications, pipeline effects, and demo/asset requirements.
  Scores topic relevance (1-10) and produces a structured Korean analysis document when relevant (>= 5).
  Composes kwp-sales-account-research, kwp-sales-competitive-intelligence,
  kwp-sales-create-an-asset, demo-forge, workflow-miner, and intent-alignment-tracker.
  Use when the role-dispatcher invokes this skill with a topic, or when the user asks for
  "sales perspective", "영업 관점", "영업 분석", "sales enablement impact".
  Do NOT use for drafting outreach emails (use kwp-sales-draft-outreach), call preparation
  (use kwp-sales-call-prep), or lead prospecting (use kwp-apollo-prospect).
  Korean triggers: "영업 관점", "영업 분석", "세일즈 영향".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "role-analysis"
---

# Sales Perspective Analyzer

Analyzes any business topic from the Sales team's viewpoint, covering sales enablement,
competitive positioning, customer impact, pipeline effects, and demo/asset requirements.

## Relevance Criteria

Score the topic 1-10 based on overlap with sales concerns:

| Domain | Weight | Keywords |
|--------|--------|----------|
| Customer impact | High | customer, enterprise, deal, contract, renewal, churn |
| Competitive positioning | High | competitor, differentiation, win/loss, battlecard |
| Sales enablement | High | pitch, demo, deck, one-pager, case study, ROI |
| Pipeline & revenue | High | pipeline, ARR, deal size, conversion, quota |
| Product launch | Medium | launch, new feature, GA, beta, pricing change |
| Market & ICP | Medium | market, segment, ICP, vertical, territory |
| Partner & channel | Medium | partner, reseller, channel, referral |
| Technical details | Low | API, code, architecture, deployment |
| HR & operations | Low | hiring, process, compliance, finance |

Score >= 5 → produce full analysis
