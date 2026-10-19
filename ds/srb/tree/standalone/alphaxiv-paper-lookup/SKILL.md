---
name: alphaxiv-paper-lookup
description: "Use when Look up any arXiv paper on alphaxiv.org to get a structured AI-generated overview (machine-readable report) without reading raw PDFs: covers alphaxiv, paper, lookup, 논문 조회, arXiv 요약"
metadata:
  holon-triggers: |
    explain this paper
    summarize arxiv paper
---

---
name: alphaxiv-paper-lookup
description: >-
  Look up any arXiv paper on alphaxiv.org to get a structured AI-generated overview
  (machine-readable report) without reading raw PDFs. Extracts paper ID from arXiv or
  AlphaXiv URLs, fetches the structured report, and optionally retrieves the full paper
  text as a fallback. Use when the user shares an arXiv link, paper ID, or asks to
  "explain this paper", "summarize arxiv paper", "look up paper", "alphaxiv", "논문 조회",
  "arXiv 논문 요약", "논문 설명", "paper overview", or references an arXiv paper ID like
  "2401.12345". Do NOT use for full academic paper review with PM analysis and PPTX
  (use paper-review), arXiv-to-NotebookLM slide pipeline (use nlm-arxiv-slides), or
  general web page extraction (use defuddle).
  Korean triggers: "논문 조회", "arXiv 요약", "논문 설명", "논문 개요".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "research"
---

# AlphaXiv Paper Lookup

Fetch a structured AI-generated overview of any arXiv paper from alphaxiv.org. Faster and
more reliable than reading raw PDFs — one `curl` call returns a comprehensive markdown report.

## Input

The user provides one of:
- An arXiv URL (e.g., `https://arxiv.org/abs/2401.12345`)
- An AlphaXiv URL (e.g., `https://alphaxiv.org/overview/2401.12345`)
- A bare paper ID (e.g., `2401.12345` or `2401.12345v2`)

## Workflow

### Step 1: Extract Paper ID

Parse the paper ID from the user's input:

| Input Format | Extracted ID |
|-------------|-------------|
| `https://arxiv.org/abs/2401.12345` | `2401.12345` |
| `https://arxiv.org/pdf/2401.12345` | `2401.12345` |
| `https://alphaxiv.org/overview/2401.12345` | `2401.12345` |
| `2401.12345v2` | `2401.12345v2` |
| `2401.12345` | `2401.12345` |

### Step 2: Fetch Machine-Readable Report

```bash
curl -sL --max-time 30 "https://alphaxiv.org/overview/{PAPER_ID}.md"
```

**CRITICAL**: The `-L` flag is required to follow 301 redirects from the AlphaXiv server.

This returns a structured, detailed analysis optimized for LL
