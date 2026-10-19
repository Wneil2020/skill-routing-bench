---
name: nlm-discovery-lab
description: "Use when End-to-end pipeline, run PM product discovery frameworks (OST, assumptions, interview scripts, experiments), user research (personas, journey: covers nlm, discovery, lab, cohort, debate"
metadata:
  holon-triggers: |
    run discovery lab
    product discovery notebook
---

---
name: nlm-discovery-lab
description: >-
  End-to-end pipeline: run PM product discovery frameworks (OST, assumptions,
  interview scripts, experiments), user research (personas, journey maps,
  segmentation), and data frameworks (metrics, cohort, A/B test), compile into
  expert-level EN + KO discovery documents, upload to NotebookLM with competitive
  research, and generate 5 learning assets (quiz, debate podcast, slides, study
  guide, data table).
  Use when the user asks to "run discovery lab", "product discovery notebook",
  "디스커버리 랩", "assumption testing", or run product discovery and produce
  NotebookLM outputs.
  Do NOT use for strategic planning without discovery focus -- use nlm-strategy-hub.
  Do NOT use for GTM launch materials -- use nlm-launch-kit.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use notebooklm-studio.
  Do NOT use for slides-only from local markdown -- use nlm-slides.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# NLM Discovery Lab: Product Discovery Lab Pipeline

End-to-end pipeline that runs a complete product discovery cycle — from opportunity identification through assumption testing to experiment design — then packages everything into a NotebookLM-powered learning environment for the product trio (PM + Designer + Engineer) to align on findings.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- PM skills installed: `pm-product-discovery`, `pm-market-research`, `pm-data-analytics`

## System Prompt

The discovery document rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before the Compile phase. It defines:

- Hypothesis-driven, exploratory tone for each language
- Section structure rules for discovery documents
- White background visual directive
- Quality gates for discovery rigor

## Pipeline

### Phase 1: Gather Input

Collect from the user:
- **Desired outcome** (the product/b
