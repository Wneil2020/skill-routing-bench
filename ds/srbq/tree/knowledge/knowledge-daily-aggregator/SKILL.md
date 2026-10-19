---
name: knowledge-daily-aggregator
description: "Use when End-of-day pipeline that collects all daily outputs (email summaries, sprint digests, news analyses, meeting notes, code reviews: covers knowledge, daily, aggregator, collects, consolidate"
metadata:
  holon-triggers: |
    aggregate today's knowledge
    daily knowledge sync
---

---
name: knowledge-daily-aggregator
description: >-
  End-of-day pipeline that collects all daily outputs (email summaries, sprint
  digests, news analyses, meeting notes, code reviews, strategy briefings),
  ingests them into the Cognee knowledge graph, extracts new entities and
  relationships, and updates MEMORY.md. Use when the user asks to "aggregate
  today's knowledge", "daily knowledge sync", "지식 그래프 갱신",
  "일일 지식 종합", "knowledge-daily-aggregator", or wants to consolidate
  the day's learning into persistent memory. Do NOT use for Cognee operations
  directly (use cognee), context recall (use recall), or MEMORY.md manual
  updates (update directly).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Knowledge Daily Aggregator

End-of-day pipeline that consolidates all daily outputs into the Cognee knowledge graph, building persistent organizational memory.

## When to Use

- As the final step in the EOD pipeline (after `eod-ship`, before daily-strategy-post)
- As part of the Execute → Learn → Evolve flywheel (Learn phase)
- When the user wants to consolidate a day's worth of work into searchable knowledge

## Data Sources

| Source | Skill That Generates It | Content Type |
|--------|------------------------|--------------|
| Email summaries | `gmail-daily-triage` | People, decisions, action items |
| Sprint digests | `github-sprint-digest` | Issues, PRs, contributors, progress |
| News analyses | `unified-intel-intake` | Companies, technologies, trends |
| Meeting notes | `meeting-digest` | Decisions, attendees, action items |
| Code reviews | `deep-review`, `ship` | Architecture patterns, tech debt |
| Strategy briefings | `daily-strategy-post` | Strategic insights, market signals |
| Paper reviews | `paper-review` | Research concepts, methods, findings |
| Trading analysis | `daily-stock-check` | Market signals, positions, theses |

## Workflow

### Step 1: Collect Daily Outputs

Scan for today's generated artifacts:

```bash
fi
