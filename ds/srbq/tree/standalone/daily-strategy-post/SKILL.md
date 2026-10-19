---
name: daily-strategy-post
description: "Use when Run multi-role strategic analysis on the day's aggregated intelligence and post company/team/product strategy documents to Slack: covers daily, strategy, post, distributed, synthesizes"
metadata:
  holon-triggers: |
    post daily strategy
    전략 브리핑 올려줘
---

---
name: daily-strategy-post
description: >-
  Run multi-role strategic analysis on the day's aggregated intelligence and post
  company/team/product strategy documents to Slack. Synthesizes all daily inputs
  (emails, news, sprint data, research) into actionable strategy briefings. Use
  when the user asks to "post daily strategy", "전략 브리핑 올려줘", "daily
  strategy", "오늘의 전략 분석", "daily-strategy-post", or wants end-of-day
  strategic analysis distributed to the team. Do NOT use for single-role analysis
  (use the specific role-* skill), morning briefings (use morning-ship), or
  investor presentations (use presentation-strategist).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "strategy"
---
# daily-strategy-post

Run multi-role strategic analysis on the day's aggregated intelligence and distribute to Slack.

## Workflow

1. **Aggregate intelligence** — Collect day's outputs: email research findings, Twitter/news intelligence, GitHub sprint digest, knowledge graph updates
2. **Role dispatch** — Run `role-dispatcher` with the aggregated intelligence as input topic, activating CEO, CTO, PM, CSO perspectives at minimum
3. **Executive synthesis** — Invoke `executive-briefing` to produce cross-role consensus, conflicts, and prioritized action items
4. **Strategy documents** — Generate three focused strategy documents in Korean:
   - Company-level: market positioning, competitive response, partnership opportunities
   - Team-level: resource allocation, sprint priority adjustments, hiring signals
   - Product-level: feature prioritization changes, technical debt priorities, customer-driven adjustments
5. **Distribute** — Post each document to Slack `#strategy` channel as threaded messages; optionally upload to Google Drive

## Composed Skills

- `role-dispatcher` — 12-role parallel analysis
- `executive-briefing` — Cross-role synthesis
- Slack MCP — Strategy channel posting
- `gws-drive` — Document archival (optional)

## Error Handling

| Error | Action |
|--
