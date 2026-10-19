---
name: paper-review
description: "Use when End-to-end academic paper review pipeline that ingests a paper (arXiv URL, PDF, or markdown), produces a structured Korean review: covers paper, review, ingests, threaded, distributes"
metadata:
  holon-triggers: |
    review a paper
    paper review
---

---
name: paper-review
description: >-
  End-to-end academic paper review pipeline that ingests a paper (arXiv URL, PDF,
  or markdown), produces a structured Korean review markdown, runs multi-perspective
  PM/research analysis using 7 PM skills, generates a consolidated Word document,
  a PowerPoint presentation, NotebookLM slide decks, creates structured Notion
  pages, and distributes everything to Slack with threaded summaries, Notion links,
  and file uploads.
  Use when the user asks to "review a paper", "paper review", "논문 리뷰",
  "논문 분석", "analyze this paper", "academic paper review", "연구 논문 리뷰",
  "paper review pipeline", "/paper-review", "논문 요약 분석", "논문 정리",
  or any request to systematically review and analyze an academic paper from
  multiple business/research perspectives.
  Do NOT use for arXiv-to-slides without review (use nlm-arxiv-slides).
  Do NOT use for general PDF reading (use anthropic-pdf).
  Do NOT use for market research without a paper (use pm-market-research).
  Do NOT use for ad-hoc Notion page creation (use Notion MCP directly).
metadata:
  author: thaki
  version: 2.0.0
  category: research
---

# Paper Review Pipeline

End-to-end pipeline that transforms an academic paper into a structured Korean
review, multi-perspective PM/research analysis documents, a consolidated Word
report, a PowerPoint presentation, NotebookLM slide decks, distributes
structured pages to Notion, and posts threaded summaries with file uploads
and Notion links to Slack.

## Prerequisites

- `pdfplumber` Python package (`pip install pdfplumber`)
- `curl` for arXiv PDF download and Defuddle extraction
- `docx` npm package (`npm install -g docx`) for Word generation
- `pptxgenjs` npm package (`npm install -g pptxgenjs`) for PowerPoint generation
- `defusedxml` and `lxml` for DOCX validation (`pip install defusedxml lxml`)
- `notebooklm-mcp` MCP server authenticated (run `nlm login` if needed)
- `plugin-notion-workspace-notion` MCP server connected for Notion page cr
