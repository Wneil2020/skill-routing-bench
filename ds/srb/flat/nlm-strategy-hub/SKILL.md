---
name: nlm-strategy-hub
description: "Use when End-to-end pipeline, run PM strategy frameworks (Lean Canvas, SWOT, Porter's Five Forces, market sizing, competitor analysis, personas), compile: covers nlm, strategy, hub, forces, porter"
metadata:
  holon-triggers: |
    create strategy hub
    build strategy notebook
---

---
name: nlm-strategy-hub
description: >-
  End-to-end pipeline: run PM strategy frameworks (Lean Canvas, SWOT, Porter's
  Five Forces, market sizing, competitor analysis, personas), compile results
  into expert-level EN + KO documents, upload to NotebookLM with web research
  enrichment, and generate multi-format strategy outputs (slide deck, audio
  podcast, mind map, executive report).
  Use when the user asks to "create strategy hub", "build strategy notebook",
  "product strategy research", "전략 허브 생성", "전략 리서치", "NLM 전략",
  "strategy research hub", "strategy to slides and podcast",
  "comprehensive strategy analysis", "investor deck from strategy",
  or any request to run PM strategy analysis and produce NotebookLM outputs.
  Do NOT use for GTM launch materials -- use nlm-launch-kit.
  Do NOT use for product discovery and assumption testing -- use nlm-discovery-lab.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use notebooklm-studio.
  Do NOT use for slides-only from local markdown -- use nlm-slides.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# NLM Strategy Hub: Product Strategy Research Hub Pipeline

End-to-end pipeline that transforms a product/company description into a comprehensive strategy knowledge base in NotebookLM — enriched with web research and delivered as multiple output formats for different audiences (board, team, investors).

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- PM skills installed: `pm-product-strategy`, `pm-market-research`, `pm-marketing-growth`

## System Prompt

The strategy document rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before the Compile phase. It defines:

- Authoritative, data-backed strategy tone for each language
- Section structure rules for strategy documents
- White background visual directive
- Quality gates for strategic content

## Pipeline

### Phase 1
