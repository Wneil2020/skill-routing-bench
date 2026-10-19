---
name: related-papers-scout
description: "Use when Discover hot related papers from elite institutions (Google, MIT, Stanford, NVIDIA) or with high Twitter/GitHub traction given an input: covers related, papers, scout, elite, institution"
metadata:
  holon-triggers: |
    find related papers
    similar papers
---

---
name: related-papers-scout
description: >-
  Discover hot related papers from elite institutions (Google, MIT, Stanford,
  NVIDIA) or with high Twitter/GitHub traction given an input paper. Searches
  Semantic Scholar, arXiv, Papers With Code, and Twitter; ranks by institution,
  citations, GitHub stars, and community buzz; posts structured Slack thread.
  Use when the user asks to "find related papers", "similar papers",
  "hot papers", "관련 논문", "유사 논문", "핫한 논문", "논문 추천",
  "scout papers", "related work", "/related-papers-scout".
  Do NOT use for paper review (use paper-review), arXiv-to-slides
  (use nlm-arxiv-slides), or general web search (use parallel-web-search).
metadata:
  author: thaki
  version: 1.0.0
  category: research
---

# Related Papers Scout

Multi-source pipeline that discovers 5 hot related papers from elite
institutions or with high community traction, given an input paper.

## Prerequisites

- `pdfplumber` Python package (`pip install pdfplumber`) for PDF extraction
- `curl` for arXiv PDF download and Defuddle extraction
- Internet access for Semantic Scholar API, WebSearch, and Slack MCP
- `SLACK_BOT_TOKEN` in `.env` for Slack distribution (Phase 6)
- Slack MCP server (`plugin-slack-slack`) connected

## Pipeline Overview

```
Phase 1: Ingest Paper       (extract title, abstract, key terms, arXiv ID)
Phase 2: Multi-Source Search (4 parallel agents across Semantic Scholar, arXiv, PapersWithCode, Twitter/GitHub)
Phase 3: Filter & Rank      (score candidates, select top 5)
Phase 4: Deep Dive          (parallel subagents produce structured summaries per paper)
Phase 5: Report Generation  (consolidated markdown report)
Phase 6: Slack Distribution  (main message + 5 threaded paper summaries)
Phase 7: Archive Registration (register discovered papers in paper-archive index)
```

---

## Phase 1: Paper Ingestion

Determine input type and extract structured metadata for search queries.

### arXiv URL Input

Extract paper ID from the URL (e.g., `2509
