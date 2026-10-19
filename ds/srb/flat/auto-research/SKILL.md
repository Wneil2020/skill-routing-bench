---
name: auto-research
description: "Use when Run the AutoResearchClaw 23-stage autonomous research pipeline that transforms a research topic into a conference-ready: covers auto, research, literature, researchclaw, autoresearchclaw"
metadata:
  holon-triggers: |
    research [topic]
    write a paper about [topic]
---

---
name: auto-research
description: >-
  Run the AutoResearchClaw 23-stage autonomous research pipeline that transforms
  a research topic into a conference-ready paper with real literature, sandbox
  experiments, and LaTeX export. Use when the user asks to "research [topic]",
  "write a paper about [topic]", "autonomous research", "auto-research",
  "자율 연구", "논문 자동 생성", "연구 파이프라인", "ResearchClaw 실행",
  "논문 작성 파이프라인", "연구 자동화", or mentions ResearchClaw.
  Do NOT use for reviewing an existing paper (use paper-review), discovering
  related papers only (use related-papers-scout), or general web research
  without paper output (use parallel-deep-research).
metadata:
  author: thaki
  version: "1.1.0"
  category: research
---

# AutoResearchClaw — Autonomous Research Pipeline

Run the full 23-stage research pipeline: topic scoping, literature discovery,
hypothesis generation, experiment execution, paper writing, peer review, and
conference-ready LaTeX export — all from a single research topic.

## Prerequisites

- **Python 3.11+** installed (via pyenv or Homebrew)
- **AutoResearchClaw** installed at `~/thaki/AutoResearchClaw/`
- **LLM API key** set via `OPENAI_API_KEY` env var (or configured in config)
- Optional: Docker for containerized experiments
- Optional: MetaClaw for cross-run learning

### First-Time Setup

If AutoResearchClaw is not installed, run:

```bash
cd ~/thaki && git clone https://github.com/aiming-lab/AutoResearchClaw.git
cd AutoResearchClaw
/opt/homebrew/bin/python3.11 -m venv .venv && source .venv/bin/activate
pip install -e .
cp config.researchclaw.example.yaml config.arc.yaml
researchclaw --help
```

## Reference Files

Read these for phase-specific details:

- `references/pipeline-stages.md` — All 23 stages with inputs, outputs, and gate logic
- `references/configuration-guide.md` — Config templates for common scenarios
- `references/experiment-modes.md` — Sandbox, Docker, and SSH remote modes
- `references/troubleshooting.md` — Common failures 
