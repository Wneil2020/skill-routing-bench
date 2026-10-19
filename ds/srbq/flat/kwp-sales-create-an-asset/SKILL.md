---
name: kwp-sales-create-an-asset
description: "Use when Generate tailored sales assets (landing pages, decks, one-pagers, workflow demos) from your deal context. Describe your prospect, audience, and goal —: covers kwp, sales, create, 생성, 워크플로우"
---

---
name: kwp-sales-create-an-asset
description: >-
  Generate tailored sales assets (landing pages, decks, one-pagers, workflow
  demos) from your deal context. Describe your prospect, audience, and goal —
  get a polished, branded asset ready to share with customers. Do NOT use for
  tasks outside the sales domain. Korean triggers: "생성", "워크플로우".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Create an Asset

Generate custom sales assets tailored to your prospect, audience, and goals. Supports interactive landing pages, presentation decks, executive one-pagers, and workflow/architecture demos.

---

## Triggers

Invoke this skill when:
- User says `/create-an-asset` or `/create-an-asset [CompanyName]`
- User asks to "create an asset", "build a demo", "make a landing page", "mock up a workflow"
- User needs a customer-facing deliverable for a sales conversation

---

## Overview

This skill creates professional sales assets by gathering context about:
- **(a) The Prospect** — company, contacts, conversations, pain points
- **(b) The Audience** — who's viewing, what they care about
- **(c) The Purpose** — goal of the asset, desired next action
- **(d) The Format** — landing page, deck, one-pager, or workflow demo

The skill then researches, structures, and builds a polished, branded asset ready to share with customers.

---

## Phase 0: Context Detection & Input Collection

### Step 0.1: Detect Seller Context

From the user's email domain, identify what company they work for.

**Actions:**
1. Extract domain from user's email
2. Search: `"[domain]" company products services site:linkedin.com OR site:crunchbase.com`
3. Determine seller context:

| Scenario | Action |
|----------|--------|
| **Single-product company** | Auto-populate seller context |
| **Multi-product company** | Ask: "Which product or solution is this asset for?" |
| **Consultant/agency/generic domain** | Ask: "What company or product are you representing?" |
| **U
