---
name: kwp-common-room-account-research
description: "Use when Research a company using Common Room data. Triggers on 'research [company]', 'tell me about [domain]', 'pull up signals for [account]', 'what's going on: covers kwp, common, room, 리서치, 검색"
---

---
name: kwp-common-room-account-research
description: >-
  Research a company using Common Room data. Triggers on 'research [company]',
  'tell me about [domain]', 'pull up signals for [account]', 'what's going on
  with [company]', or any account-level question. Do NOT use for tasks outside
  the common-room domain. Korean triggers: "리서치", "검색", "데이터".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Account Research

Retrieve and synthesize account information from Common Room. Handles four interaction patterns: full overviews, targeted field questions, sparse data situations, and combined MCP data + LLM reasoning.

## Step 0: Load User Context (Me)

Before researching any account, fetch the `Me` object from Common Room. This provides:
- The user's profile, title, role, and Persona in CR
- The user's segments ("My Segments")

Default all queries to the user's own segments unless the user explicitly asks for a broader view. This keeps results scoped to their territory.

## Step 1: Identify the Interaction Pattern

Determine what the user actually needs before deciding how much data to fetch:

**Pattern 1 — Full Overview:** "Tell me about Datadog" / "Summarize cloudflare.com"
→ Fetch the full field set and produce a structured briefing.

**Pattern 2 — Targeted Question:** "Who owns the Snowflake account?" / "Is acme.io showing buying signals?" / "What's the employee count for notion.so?"
→ Fetch only the relevant field(s). Return a direct, concise answer — do not produce a full brief for a simple question.

**Pattern 3 — Sparse Data:** "Tell me about tiny-startup.io"
→ If Common Room has limited data for an account, say so honestly: "There is limited information available for this account." Never speculate or fill gaps with generic statements.

**Pattern 4 — Combined Reasoning:** Fetch structured MCP data, then layer in LLM analysis — e.g., "Stripe has 8,000 employees and is hiring heavily for AI roles. Based on your ICP of 1k–10
