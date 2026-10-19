---
name: auto-research-distribute
description: "Use when Distribute AutoResearchClaw pipeline outputs (paper, LaTeX, experiments) to Notion, Slack, NotebookLM, PPTX, and paper-archive: covers auto, research, distribute, autoresearchclaw, latex"
metadata:
  holon-triggers: |
    distribute research results
    post research to Slack
---

---
name: auto-research-distribute
description: >-
  Distribute AutoResearchClaw pipeline outputs (paper, LaTeX, experiments) to
  Notion, Slack, NotebookLM, PPTX, and paper-archive. Use when the user asks to
  "distribute research results", "post research to Slack", "upload paper to Notion",
  "auto-research-distribute", "연구 결과 배포", "논문 배포", "연구 Notion 업로드",
  "연구 결과 공유", "논문 슬랙 공유", or after completing an auto-research pipeline
  run. Do NOT use for running the research pipeline itself (use auto-research),
  reviewing existing papers (use paper-review), or publishing arbitrary markdown
  to Notion (use md-to-notion).
metadata:
  author: thaki
  version: "1.1.0"
  category: research
---

# AutoResearchClaw — Post-Pipeline Distribution

Take deliverables from a completed AutoResearchClaw pipeline run and distribute
them across the project ecosystem: paper-archive, Notion, Slack, NotebookLM,
and PPTX.

## Prerequisites

- A completed AutoResearchClaw pipeline run with deliverables directory
- Slack MCP configured (for `#deep-research` channel posting)
- Notion MCP configured (for research page creation)
- NotebookLM MCP configured (optional, for study artifacts)

## Reference Files

- `references/distribution-channels.md` — Channel configs and templates

## Pipeline Overview

```
Phase 1: Locate Deliverables    → Find and validate artifact files
Phase 2: Paper Archive           → Register in paper-archive index
Phase 3: Notion Upload           → Create structured Notion sub-pages
Phase 4: PPTX Generation        → Generate executive summary slides
Phase 5: NotebookLM Upload      → Create notebook with study artifacts
Phase 6: Slack Notification      → Post summary thread to #deep-research
```

## Execution

### Phase 1: Locate Deliverables

1. Find the deliverables directory. It is either:
   - Provided by user: `--artifacts-dir <path>`
   - Auto-detected: `~/thaki/AutoResearchClaw/artifacts/rc-*/deliverables/`

2. Verify required files exist:

```bash
ls <artifacts-d
