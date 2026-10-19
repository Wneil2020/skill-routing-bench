---
name: kwp-common-room-prospect
description: "Use when Build targeted account or contact lists using Common Room's Prospector. Triggers on 'find companies that match [criteria]', 'build a prospect: covers kwp, common, room, 빌드, alphabetically"
metadata:
  holon-triggers: |
    Show companies hiring AI engineers this month
    Are you looking for net-new companies not yet in Common Room, or filtering accounts already in your workspace?
---

---
name: kwp-common-room-prospect
description: >-
  Build targeted account or contact lists using Common Room's Prospector.
  Triggers on 'find companies that match [criteria]', 'build a prospect list',
  'find contacts at [type of company]', 'show me companies hiring [role]', or
  any list-building request. Do NOT use for tasks outside the common-room
  domain. Korean triggers: "빌드".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Prospecting

Build targeted account and contact lists using Common Room's Prospector. Supports iterative refinement through natural conversation, intent-based discovery, and both net-new prospecting and signal-based queries against existing accounts.

## Critical Distinction: Two Object Types

Common Room's Prospector operates against two fundamentally different object types. Always clarify which one is in play before running a query:

**`ProspectorOrganization`** — Companies **not yet in Common Room**
- Net-new companies that match specified criteria
- Available fields are firmographic only: name, domain, size, industry, capital raised, annual revenue, location
- Fewer filter options — no signal-based filters, no scores, no activity history
- Use when: building a brand-new target list, territory planning, top-of-funnel expansion

**`Organization`** (in Common Room) — Companies **already in your CR workspace**
- Full signal data available: product usage, community activity, CRM fields, scores, custom fields
- Much richer filter set — includes signal-based, score-based, segment-based, and firmographic filters
- Use when: finding warm accounts to prioritize, identifying expansion candidates, surfacing intent signals within existing pipeline

When a user's request could apply to both (e.g., "Show companies hiring AI engineers this month"), clarify:
> "Are you looking for net-new companies not yet in Common Room, or filtering accounts already in your workspace?"

The catalog should make this distinction ex
