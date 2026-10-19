---
name: kwp-sales-draft-outreach
description: "Use when Research a prospect then draft personalized outreach. Uses web research by default, supercharged with enrichment and CRM. Trigger with \"draft outreach to: covers kwp, sales, draft, 검색, 이메일"
---

---
name: kwp-sales-draft-outreach
description: >-
  Research a prospect then draft personalized outreach. Uses web research by
  default, supercharged with enrichment and CRM. Trigger with "draft outreach to
  [person/company]", "write cold email to [prospect]", "reach out to [name]". Do
  NOT use for tasks outside the sales domain. Korean triggers: "검색", "이메일",
  "리서치".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Draft Outreach

Research first, then draft. This skill never sends generic outreach - it always researches the prospect first to personalize the message. Works standalone with web search, supercharged when you connect your tools.

## Before You Start

Before drafting outreach, ask the user to clarify (use AskQuestion):

1. **Prospect** — Who are you reaching out to? (name, company, title, or LinkedIn URL)
2. **Channel** — Email, LinkedIn message, or cold call script?
3. **Goal** — What do you want the prospect to do? (book a meeting, reply, try the product)
4. **Context** — Any prior relationship, mutual connections, or trigger event?

If the user provides a name or company inline, begin research immediately and skip redundant questions.

## Connectors (Optional)

| Connector | What It Adds |
|-----------|--------------|
| **Enrichment** | Verified email, phone, background details |
| **CRM** | Prior relationship context, existing contacts |
| **Email** | Create draft directly in your inbox |

> **No connectors?** Web research works great. I'll output the email text for you to copy.

---

## How It Works

```
+------------------------------------------------------------------+
|                      DRAFT OUTREACH                               |
|                                                                   |
|  Step 1: RESEARCH (always happens first)                         |
|  - Web search (default)                                           |
|  - + Enrichment (if enrichment tools connected)                 
