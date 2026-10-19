---
name: kwp-enterprise-search-knowledge-synthesis
description: "Use when Combines search results from multiple sources into coherent, deduplicated answers with source attribution. Handles confidence scoring based: covers kwp, enterprise, search, 검색, attribution"
---

---
name: kwp-enterprise-search-knowledge-synthesis
description: >-
  Combines search results from multiple sources into coherent, deduplicated
  answers with source attribution. Handles confidence scoring based on freshness
  and authority, and summarizes large result sets effectively. Do NOT use for
  tasks outside the enterprise domain. Korean triggers: "검색".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Knowledge Synthesis

The last mile of enterprise search. Takes raw results from multiple sources and produces a coherent, trustworthy answer.

## The Goal

Transform this:
```
Slack result: "Sarah said in #eng: 'let's go with REST, GraphQL is overkill for our use case'"
Gmail result: "Subject: API Decision — Sarah's email confirming REST approach with rationale"
Google Drive result: "API Design Doc v3 — updated section 2 to reflect REST decision"
Linear result: "Task: Finalize API approach — marked complete by Sarah"
```

Into this:
```
The team decided to go with REST over GraphQL for the API redesign. Sarah made the
call, noting that GraphQL was overkill for the current use case. This was discussed
in #engineering on Tuesday, confirmed via email Wednesday, and the design doc has
been updated to reflect the decision. The related Linear task is marked complete.

Sources:
- Slack: #engineering thread (Jan 14)
- Gmail: "API Decision" from Sarah (Jan 15)
- Google Drive: "API Design Doc v3" (updated Jan 15)
- Linear: "Finalize API approach" (completed Jan 15)
```

## Deduplication

### Cross-Source Deduplication

The same information often appears in multiple places. Identify and merge duplicates:

**Signals that results are about the same thing:**
- Same or very similar text content
- Same author/sender
- Timestamps within a short window (same day or adjacent days)
- References to the same entity (project name, document, decision)
- One source references another ("as discussed in Slack", "per the email", "see the doc")

**How to
