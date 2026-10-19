---
name: pm-market-research
description: "Use when Orchestrate market research workflows, user personas, market segmentation, customer journey mapping, competitive analysis, sentiment: covers market, research, 사용자 페르소나, 시장 세분화, journey"
metadata:
  holon-triggers: |
    user persona
    market segmentation
---

---
name: pm-market-research
description: >-
  Orchestrate market research workflows: user personas, market segmentation,
  customer journey mapping, competitive analysis, sentiment analysis, and market
  sizing (TAM/SAM/SOM). Based on phuryn/pm-skills. Use when the user asks for
  "user persona", "market segmentation", "customer journey map", "competitor
  analysis", "sentiment analysis", "market sizing", "TAM SAM SOM", or "user
  segmentation". Do NOT use for product discovery ideation (use
  pm-product-discovery), marketing campaigns (use
  kwp-marketing-campaign-planning), or sales competitive intelligence (use
  kwp-sales-competitive-intelligence). Korean triggers: "사용자 페르소나", "시장 세분화", "고객 여정 지도", "경쟁사 분석", "감성 분석", "시장 규모", "TAM SAM SOM", "사용자 세그먼트", "피드백 분석".
metadata:
  author: "thaki"
  version: "1.0.0"
  upstream: "https://github.com/phuryn/pm-skills"
  category: "product"
---
# PM Market Research

Orchestrates product-market research workflows using seven sub-skills. Routes user requests to the appropriate reference, applies structured analysis steps, and delivers research-backed outputs for personas, segments, journeys, competitors, sentiment, and market sizing.

## Sub-Skill Index

| Sub-Skill | When to Use | Reference |
|-----------|-------------|-----------|
| user-personas | Build personas from survey/interview data; 3 personas with JTBD, pains, gains | [references/user-personas.md](references/user-personas.md) |
| user-segmentation | Segment user base from feedback; 3+ behavioral/needs-based segments | [references/user-segmentation.md](references/user-segmentation.md) |
| market-segments | Identify 3–5 customer segments with demographics, JTBD, product fit | [references/market-segments.md](references/market-segments.md) |
| customer-journey-map | Map awareness→advocacy; touchpoints, emotions, pain points, opportunities | [references/customer-journey-map.md](references/customer-journey-map.md) |
| competitor-analysis | 5 direct competitors; strength
