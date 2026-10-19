---
name: kwp-enterprise-search-search-strategy
description: "Use when Query decomposition and multi-source search orchestration. Breaks natural language questions into targeted searches per source, translates: covers kwp, enterprise, search, 검색, ambiguity"
---

---
name: kwp-enterprise-search-search-strategy
description: >-
  Query decomposition and multi-source search orchestration. Breaks natural
  language questions into targeted searches per source, translates queries into
  source-specific syntax, ranks results by relevance, and handles ambiguity and
  fallback strategies. Do NOT use for tasks outside the enterprise domain.
  Korean triggers: "검색".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Search Strategy


The core intelligence behind enterprise search. Transforms a single natural language question into parallel, source-specific searches and produces ranked, deduplicated results.

## The Goal

Turn this:
```
"What did we decide about the API migration timeline?"
```

Into targeted searches across every connected source:
```
Slack:  "API migration timeline decision" (semantic) + "API migration" in:#engineering after:2025-01-01
Notion: semantic search "API migration timeline decision"
Linear:  text search "API migration" in relevant workspace
```

Then synthesize the results into a single coherent answer.

## Query Decomposition

### Step 1: Identify Query Type

Classify the user's question to determine search strategy:

| Query Type | Example | Strategy |
|-----------|---------|----------|
| **Decision** | "What did we decide about X?" | Prioritize conversations (Slack, email), look for conclusion signals |
| **Status** | "What's the status of Project Y?" | Prioritize recent activity, task trackers, status updates |
| **Document** | "Where's the spec for Z?" | Prioritize Drive, wiki, shared docs |
| **Person** | "Who's working on X?" | Search task assignments, message authors, doc collaborators |
| **Factual** | "What's our policy on X?" | Prioritize wiki, official docs, then confirmatory conversations |
| **Temporal** | "When did X happen?" | Search with broad date range, look for timestamps |
| **Exploratory** | "What do we know about X?" | Broad search across all sources, s
