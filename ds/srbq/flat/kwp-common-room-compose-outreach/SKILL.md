---
name: kwp-common-room-compose-outreach
description: "Use when Generate personalized outreach messages using Common Room signals. Triggers on 'draft outreach to [person]', 'write an email to [name]', 'compose a message: covers kwp, common, room, 생성, 이메일"
---

---
name: kwp-common-room-compose-outreach
description: >-
  Generate personalized outreach messages using Common Room signals. Triggers
  on 'draft outreach to [person]', 'write an email to [name]', 'compose a
  message for [contact]', or any outreach drafting request. Do NOT use for tasks
  outside the common-room domain. Korean triggers: "생성", "이메일".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Compose Outreach

Generate three personalized outreach formats — email, call script, and LinkedIn message — grounded in Common Room signals for a specific company or contact.

## Outreach Process

### Step 1: Look Up the Target

Use Common Room MCP tools to find and retrieve data for the target (company and/or specific contact). Pull:
- Recent product activity and engagement signals
- Community activity (posts, questions, reactions)
- 3rd-party intent signals (job postings, news, funding)
- Relationship history (prior contact, meetings, email opens)

If the user specified a person, run contact-level research. If only a company was given, identify the best contact to target based on title, engagement, and role.

### Step 2: Web Search for External Hooks (If CR Signals Are Thin)

If CR returned strong signals (recent activity, engagement, product usage), those should drive personalization — skip web search. If CR signals are thin or the prospect has little CR activity, run a web search for external hooks:

**What to search:**
- `"[company name]" funding OR acquisition OR launch OR announcement` — last 30 days
- `"[contact full name]" "[company name]"` — look for recent articles, interviews, LinkedIn posts, or conference talks

**Prioritize external hooks that are:**
- Very recent (< 2 weeks) — the prospect is likely still thinking about it
- Publicly visible — they know you could have seen it
- Change-signaling — growth, new role, new product, new market

If the user explicitly asks for web search or external hooks, run it regardless of
