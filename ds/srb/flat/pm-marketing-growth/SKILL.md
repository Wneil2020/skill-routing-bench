---
name: pm-marketing-growth
description: "Use when Orchestrate product marketing and growth workflows, marketing ideas, positioning, value proposition statements, North Star metrics, and: covers marketing, growth, 마케팅 아이디어, 포지셔닝, north"
metadata:
  holon-triggers: |
    marketing ideas
    positioning
---

---
name: pm-marketing-growth
description: >-
  Orchestrate product marketing and growth workflows: marketing ideas,
  positioning, value proposition statements, North Star metrics, and product
  naming. Based on phuryn/pm-skills. Use when the user asks for "marketing
  ideas", "positioning", "value proposition statements", "North Star metric",
  "product name ideas", or "growth metrics". Do NOT use for marketing campaign
  planning (use kwp-marketing-campaign-planning), brand voice (use
  kwp-marketing-brand-voice), or GTM strategy (use pm-go-to-market). Korean triggers: "마케팅 아이디어", "포지셔닝", "가치 제안 문구",
  "North Star 메트릭", "제품 이름", "노스스타", "마케팅 캠페인", "브랜딩", "네이밍".
metadata:
  author: "thaki"
  version: "1.0.0"
  upstream: "https://github.com/phuryn/pm-skills"
  category: "product"
---
# PM Marketing and Growth

Orchestrate product marketing and growth workflows using phuryn/pm-skills — marketing ideas, positioning, value proposition statements, North Star metrics, and product naming.

## Sub-Skill Index

| Sub-Skill | When to Use | Reference |
|-----------|--------------|-----------|
| marketing-ideas | Marketing campaigns, product promotion, creative tactics | [references/marketing-ideas.md](references/marketing-ideas.md) |
| north-star-metric | North Star Metric, metrics framework, OMTM, key metric | [references/north-star-metric.md](references/north-star-metric.md) |
| positioning-ideas | Product positioning, differentiation, brand positioning | [references/positioning-ideas.md](references/positioning-ideas.md) |
| product-name | Product naming, rebranding, name ideas | [references/product-name.md](references/product-name.md) |
| value-prop-statements | Marketing copy, sales messaging, onboarding copy | [references/value-prop-statements.md](references/value-prop-statements.md) |

## Workflow

1. **Identify sub-skill**: From the user's request and trigger words, pick the matching sub-skill from the index.
2. **Read reference**: Load the corresponding `references/<
