---
name: kwp-sales-account-research
description: "Use when Research a company or person and get actionable sales intel. Works standalone with web search, supercharged when you connect enrichment tools or your: covers kwp, sales, account, 리서치, 검색"
---

---
name: kwp-sales-account-research
description: >-
  Research a company or person and get actionable sales intel. Works standalone
  with web search, supercharged when you connect enrichment tools or your CRM.
  Trigger with "research [company]", "look up [person]", "intel on [prospect]",
  "who is [name] at [company]", or "tell me about [company]". Do NOT use for
  tasks outside the sales domain. Korean triggers: "리서치", "검색".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Account Research

Get a complete picture of any company or person before outreach. This skill always works with web search, and gets significantly better with enrichment and CRM data.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                     ACCOUNT RESEARCH                             │
├─────────────────────────────────────────────────────────────────┤
│  ALWAYS (works standalone via web search)                        │
│  ✓ Company overview: what they do, size, industry               │
│  ✓ Recent news: funding, leadership changes, announcements      │
│  ✓ Hiring signals: open roles, growth indicators                │
│  ✓ Key people: leadership team from LinkedIn                    │
│  ✓ Product/service: what they sell, who they serve              │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Enrichment: verified emails, phone, tech stack, org chart    │
│  + CRM: prior relationship, past opportunities, contacts        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Getting Started

Just tell me who to research:

- "Research Stripe"
- "Look up the CTO at Notion"
- "Intel on acme.com"
- "Who is Sarah Chen at TechCorp?"
- "Tell me about [company] before my call"

I'll run web searches immediately. If you have enrichment or CRM connected, I'll pull that data too.

---

## 
