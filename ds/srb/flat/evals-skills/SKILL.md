---
name: evals-skills
description: "Use when Orchestrate LLM eval pipeline tasks, audit existing evals, analyze errors in traces, generate synthetic test data, write LLM judge: covers evals, skills, LLM 평가, eval 파이프라인, annotation"
metadata:
  holon-triggers: |
    eval audit
    error analysis
---

---
name: evals-skills
description: >-
  Orchestrate LLM eval pipeline tasks: audit existing evals, analyze errors in
  traces, generate synthetic test data, write LLM judge prompts, validate
  evaluators against human labels, evaluate RAG pipelines, and build annotation
  interfaces. Based on hamelsmu/evals-skills (50+ company patterns). Use when
  the user asks for "eval audit", "error analysis", "judge prompt", "validate
  evaluator", "synthetic data", "evaluate RAG", "annotation interface", "review
  traces", "evals", or "LLM evaluation". Do NOT use for general code review (use
  backend-expert or frontend-expert), ML model training, unit testing (use
  qa-test-expert), or non-LLM evaluation tasks. Korean triggers: "LLM 평가", "eval 파이프라인".
metadata:
  author: "thaki"
  version: "1.0.0"
  upstream: "https://github.com/hamelsmu/evals-skills"
  category: "execution"
---
# Evals Skills — LLM Evaluation Pipeline Toolkit

Orchestrate LLM product evaluation tasks using 7 specialized sub-skills from [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills).

## Sub-Skill Index

| Sub-Skill | When to Use | Reference |
|-----------|-------------|-----------|
| eval-audit | Starting point: audit an eval pipeline or bootstrap from scratch | [references/eval-audit.md](references/eval-audit.md) |
| error-analysis | Read traces systematically and categorize failure modes | [references/error-analysis.md](references/error-analysis.md) |
| generate-synthetic-data | Bootstrap eval datasets when real traces are sparse | [references/generate-synthetic-data.md](references/generate-synthetic-data.md) |
| write-judge-prompt | Design binary pass/fail LLM-as-Judge for subjective criteria | [references/write-judge-prompt.md](references/write-judge-prompt.md) |
| validate-evaluator | Calibrate LLM judges against human labels (TPR/TNR) | [references/validate-evaluator.md](references/validate-evaluator.md) |
| evaluate-rag | Evaluate retrieval and generation quality in RAG pipelines |
