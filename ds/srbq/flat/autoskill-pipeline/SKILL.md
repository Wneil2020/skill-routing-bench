---
name: autoskill-pipeline
description: "Use when Orchestrates the full AutoSkill adaptation, research analysis, multi-role strategy, skill creation, infrastructure, QA. Use when the: covers autoskill, pipeline, adaptation, adapt, evolution"
metadata:
  holon-triggers: |
    run autoskill pipeline
    autoskill adaptation
---

---
name: autoskill-pipeline
description: >-
  Orchestrates the full AutoSkill adaptation: research analysis, multi-role
  strategy, skill creation, infrastructure, QA. Use when the user asks to
  "run autoskill pipeline", "autoskill adaptation", "adapt a learning
  framework", "AutoSkill 파이프라인", "학습 프레임워크 적용", "연구 논문 기반
  스킬 생성". Do NOT use for evolution loop only (use autoskill-evolve),
  single-transcript extraction (use autoskill-extract), evolution status
  (use autoskill-status), or paper review without implementation
  (use paper-review).
metadata:
  author: thaki
  version: "0.2.0"
  category: self-improvement
---

# AutoSkill Pipeline

End-to-end meta-skill that orchestrates the complete AutoSkill adaptation process: research paper analysis, multi-role strategy assessment, skill creation, infrastructure integration, and quality assurance. Encapsulates the full workflow from analyzing an experience-driven lifelong learning methodology to implementing it as Cursor skills, rules, and commands.

## Instructions

### Pipeline Phases

The pipeline has 4 phases, each runnable independently or as a full sequence.

#### Phase 1: Research Analysis (`--phase analyze`)

1. **Paper Ingestion**: Download the research paper (PDF/arXiv URL), extract content using `anthropic-pdf` skill, and get structured overview via `alphaxiv-paper-lookup`
2. **Repository Analysis**: Use GitHub MCP or `defuddle` to analyze the paper's implementation repository — extract key modules, prompts, data models, and configuration
3. **Paper Review**: Run `paper-review` pipeline (Ingest → Review → PM Analysis → DOCX) to produce a structured Korean review with multi-perspective PM analysis
4. **Technical Documentation**: Create `docs/research/<topic>-analysis.md` with architecture diagrams (mermaid), module breakdown, key prompts, and gap analysis vs current infrastructure

**Skills used**: `anthropic-pdf`, `alphaxiv-paper-lookup`, `defuddle`, `paper-review`, `visual-explainer`

#### Phase 2: Strat
