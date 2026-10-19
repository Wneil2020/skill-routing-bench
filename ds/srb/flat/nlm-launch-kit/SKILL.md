---
name: nlm-launch-kit
description: "Use when End-to-end pipeline, run PM go-to-market frameworks (GTM strategy, ICP, battlecards, beachhead), execution docs (PRD, release notes: covers nlm, launch, kit, beachhead, enablement"
metadata:
  holon-triggers: |
    create launch kit
    build launch package
---

---
name: nlm-launch-kit
description: >-
  End-to-end pipeline: run PM go-to-market frameworks (GTM strategy, ICP,
  battlecards, beachhead), execution docs (PRD, release notes, stakeholder map),
  and marketing assets (positioning, value props, naming), compile into expert-level
  EN + KO launch documents, upload to NotebookLM with competitive research, and
  generate 5 artifact types (slides, video, infographic, flashcards, quiz).
  Use when the user asks to "create launch kit", "build launch package",
  "GTM launch materials", "런치 키트 생성", "출시 자료", "NLM 런치킷",
  "launch kit from product brief", "go-to-market launch bundle",
  "sales enablement kit", "product launch deck and video",
  or any request to generate a complete product launch package via NotebookLM.
  Do NOT use for strategic analysis without launch focus -- use nlm-strategy-hub.
  Do NOT use for product discovery and assumptions -- use nlm-discovery-lab.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use notebooklm-studio.
  Do NOT use for slides-only from local markdown -- use nlm-slides.
metadata:
  author: thaki
  version: 1.0.0
  category: orchestration
---

# NLM Launch Kit: Go-to-Market Launch Kit Generator Pipeline

End-to-end pipeline that generates a complete product launch package — GTM strategy, sales enablement materials, customer-facing content, and internal alignment resources — all from a single product brief, packaged as a NotebookLM knowledge base with 5 output formats.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- PM skills installed: `pm-go-to-market`, `pm-execution`, `pm-marketing-growth`

## System Prompt

The launch document rewrite system prompt is stored at `references/system-prompt.md` (relative to this skill). Read it before the Compile phase. It defines:

- Persuasive, action-oriented launch tone for each language
- Section structure rules for launch kit documents
- White background visual directive
- Qu
