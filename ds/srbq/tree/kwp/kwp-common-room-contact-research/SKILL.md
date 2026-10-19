---
name: kwp-common-room-contact-research
description: "Use when Research a specific person using Common Room data. Triggers on 'who is [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or any: covers kwp, common, room, 리서치, 검색"
---

---
name: kwp-common-room-contact-research
description: >-
  Research a specific person using Common Room data. Triggers on 'who is
  [name]', 'look up [email]', 'research [contact]', 'is [name] a warm lead', or
  any contact-level question. Do NOT use for tasks outside the common-room
  domain. Korean triggers: "리서치", "검색", "이메일", "데이터".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Contact Research

Retrieve a comprehensive contact profile from Common Room. Supports lookup by email, social handle, or name + company. Returns enriched data including activity history, Spark, scores, website visits, and CRM fields.

## Step 1: Locate the Contact

Common Room supports multiple lookup methods — use whichever the user has provided:

| What the user gives | Lookup method |
|---------------------|--------------|
| Email address | Look up by email (most reliable) |
| LinkedIn, Twitter/X, or GitHub handle | Look up by social handle — specify handle type explicitly |
| Name + company | Identity resolution by name + org domain; present matches if ambiguous |
| Name only | Search by name; if multiple matches, show a brief list and ask the user to confirm |

If no match is found, respond: "Common Room doesn't have a record for this person." Do not speculate or fabricate profile data.

## Step 2: Fetch Contact Fields

Use the Common Room object catalog to see available field groups and their contents. For full profiles, request all groups. For targeted questions, request only what's relevant.

**Key field groups to know about:**
- **Scores** — always return as raw values or percentiles, never labels
- **Recent activity** — use `Contact Initiated` filter (last 60 days) for their actions, not your team's
- **Website visits** — total count + specific pages (last 12 weeks)
- **Spark** — retrieve all Sparks when tracking engagement evolution over time

## Step 3: Run Spark Enrichment (If Available)

If Spark is available, use it. Spark provides:
-
