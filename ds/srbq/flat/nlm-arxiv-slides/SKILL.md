---
name: nlm-arxiv-slides
description: "Use when End-to-end pipeline that takes an arXiv paper URL, downloads the PDF, extracts and rewrites content into expert-level English and Korean, uploads: covers nlm, arxiv, slides, rewrites, takes"
metadata:
  holon-triggers: |
    arxiv to slides
    paper to slides
---

---
name: nlm-arxiv-slides
description: >-
  End-to-end pipeline that takes an arXiv paper URL, downloads the PDF,
  extracts and rewrites content into expert-level English and Korean,
  uploads to NotebookLM with optional web research enrichment, queries
  for key analysis, generates slide deck PDFs, and downloads them.
  Orchestrates 6 skills: defuddle, anthropic-pdf, nlm-slides, notebooklm,
  notebooklm-research, notebooklm-studio.
  Use when the user asks to "arxiv to slides", "paper to slides",
  "arxiv slides", "analyze arxiv paper", "arXiv 분석", "논문 슬라이드",
  "논문 분석 슬라이드", "arXiv 논문 슬라이드", "arXiv paper slides",
  "nlm-arxiv-slides", "/nlm-arxiv-slides",
  or any request to convert an arXiv paper into NotebookLM slide decks.
  Do NOT use for ad-hoc studio_create on existing notebooks -- use
  notebooklm-studio. Do NOT use for local markdown to slides -- use
  nlm-slides. Do NOT use for general paper reading without slides -- use
  anthropic-pdf. Do NOT use for non-arXiv URLs -- use nlm-slides with
  defuddle.
metadata:
  author: thaki
  version: 1.0.0
  category: generation
---

# NLM arXiv Slides: arXiv Paper to Expert Slide Deck Pipeline

End-to-end pipeline that transforms an arXiv paper into professional NotebookLM slide decks in both English and Korean, combining PDF analysis, expert rewriting, web research enrichment, and automated slide generation.

## Prerequisites

- `notebooklm-mcp` MCP server registered and authenticated (see `notebooklm` skill)
- `curl` available for PDF download and Defuddle abstract extraction
- `pdfplumber` Python package installed (`pip install pdfplumber`)
- Authentication often expires between sessions; if `notebook_create` fails with "Authentication expired", run `nlm login` in terminal, then call `refresh_auth` MCP tool before retrying

## Reference Files

Read these before executing the pipeline:

- `references/system-prompt.md` — Expert rewrite prompt adapted for academic papers (section-aware, visual hints for figures/equa
