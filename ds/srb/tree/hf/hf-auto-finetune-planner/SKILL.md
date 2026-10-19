---
name: hf-auto-finetune-planner
description: "Use when End-to-end autonomous fine-tuning planner that takes a natural language task description, discovers the optimal base model + training: covers auto, finetune, planner, combination, estimates"
metadata:
  holon-triggers: |
    plan fine-tuning
    find best model for task
---

---
name: hf-auto-finetune-planner
description: >-
  End-to-end autonomous fine-tuning planner that takes a natural language task
  description, discovers the optimal base model + training dataset combination
  on HF Hub, validates dataset quality via SQL, estimates GPU cost, generates a
  training config, and optionally launches the job. Use when the user asks to
  "plan fine-tuning", "find best model for task", "auto fine-tune", "training
  planner", "파인튜닝 계획", "자동 파인튜닝", "모델 + 데이터셋 매칭", "학습 계획",
  "fine-tune planner", or wants to go from a task description to a training-ready
  configuration. Do NOT use for running the existing daily pipeline (use today).
  Do NOT use for direct model training without planning (use hf-model-trainer).
  Do NOT use for dataset exploration only (use hf-dataset-viewer).
  Do NOT use for model search only (use hf-models).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "research"
---

# Auto Fine-Tune Planner

End-to-end pipeline that transforms a natural language task description into a
training-ready configuration. Autonomously discovers models, matches datasets,
validates quality, estimates costs, and generates configs.

## Prerequisites

- `hf` CLI installed and authenticated (see `hf-hub` skill)
- HF Pro/Team plan for Jobs cost estimation and execution
- `jq` for JSON processing

## Required Skills

- `hf-models` — model discovery and info
- `hf-datasets` (existing) — dataset CRUD and SQL queries
- `hf-dataset-viewer` — dataset exploration via REST API
- `hf-evaluation` — existing benchmark lookup
- `hf-jobs` — hardware listing and cost estimation
- `hf-model-trainer` — training execution (Phase 6)
- `hf-trackio` — experiment monitoring (Phase 6)
- `hf-collections` — save curated model+dataset pairs

## Reference Files

Read these as needed during execution:

- `references/task-taxonomy.md` — maps task descriptions to HF model tags and dataset filters
- `references/cost-estimation.md` — hardware FLOPS tables and traini
