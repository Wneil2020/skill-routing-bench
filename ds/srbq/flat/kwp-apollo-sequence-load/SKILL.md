---
name: kwp-apollo-sequence-load
description: "Use when Find leads matching criteria and bulk-add them to an Apollo outreach sequence. Handles enrichment, contact creation, deduplication, and: covers kwp, apollo, sequence, enrollment, bulk"
---

---
name: kwp-apollo-sequence-load
description: >-
  Find leads matching criteria and bulk-add them to an Apollo outreach
  sequence. Handles enrichment, contact creation, deduplication, and enrollment
  in one flow. Do NOT use for tasks outside the apollo domain.
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Sequence Load

Find, enrich, and load contacts into an outreach sequence — end to end. The user provides targeting criteria and a sequence name via "$ARGUMENTS".

## Examples

- `/apollo:sequence-load add 20 VP Sales at SaaS companies to my "Q1 Outbound" sequence`
- `/apollo:sequence-load SDR managers at fintech startups → Cold Outreach v2`
- `/apollo:sequence-load list sequences` (shows all available sequences)
- `/apollo:sequence-load directors of engineering, 500+ employees, US → Demo Follow-up`
- `/apollo:sequence-load reload 15 more leads into "Enterprise Pipeline"`

## Step 1 — Parse Input

From "$ARGUMENTS", extract:

**Targeting criteria:**
- Job titles → `person_titles`
- Seniority levels → `person_seniorities`
- Industry keywords → `q_organization_keyword_tags`
- Company size → `organization_num_employees_ranges`
- Locations → `person_locations` or `organization_locations`

**Sequence info:**
- Sequence name (text after "to", "into", or "→")
- Volume — how many contacts to add (default: 10 if not specified)

If the user just says "list sequences", skip to Step 2 and show all available sequences.

## Step 2 — Find the Sequence

Use `mcp__claude_ai_Apollo_MCP__apollo_emailer_campaigns_search` to find the target sequence:
- Set `q_name` to the sequence name from input

If no match or multiple matches:
- Show all available sequences in a table: | Name | ID | Status |
- Ask the user to pick one

## Step 3 — Get Email Account

Use `mcp__claude_ai_Apollo_MCP__apollo_email_accounts_index` to list linked email accounts.

- If one account → use automatically
- If multiple → show them and ask which to send from

## Step 4 — 
