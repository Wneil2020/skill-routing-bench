---
name: hf-model-arena
description: "Use when Competitive model evaluation arena that discovers competing models for a given task, runs head-to-head evaluations on a standardized: covers model, arena, competing, deploys, dimensional"
metadata:
  holon-triggers: |
    compare models
    model arena
---

---
name: hf-model-arena
description: >-
  Competitive model evaluation arena that discovers competing models for a
  given task, runs head-to-head evaluations on a standardized dataset,
  generates a multi-dimensional leaderboard, deploys the winner as an
  inference endpoint, and archives all artifacts. Use when the user asks to
  "compare models", "model arena", "model shootout", "find best model for
  task", "head-to-head evaluation", "leaderboard", "모델 비교", "모델 아레나",
  "모델 대결", "최적 모델 선정", "리더보드 생성", or wants a systematic
  comparison of competing models with deployment of the winner.
  Do NOT use for training models (use hf-model-trainer).
  Do NOT use for daily stock analysis (use today).
  Do NOT use for single model evaluation only (use hf-evaluation).
  Do NOT use for model search without evaluation (use hf-models).
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "research"
---

# Model Arena — Competitive Model Evaluation

End-to-end pipeline: discover competing models → evaluate head-to-head →
generate leaderboard → deploy winner → archive artifacts.

## Prerequisites

- `hf` CLI installed and authenticated (see `hf-hub` skill)
- HF Pro/Team plan for Jobs infrastructure (evaluation) and Inference Endpoints (deployment)
- `jq` for JSON processing

## Required Skills

- `hf-models` — candidate discovery and metadata collection
- `hf-evaluation` — benchmark execution
- `hf-endpoints` — winner deployment
- `hf-buckets` — artifact archival
- `hf-collections` — curated winner collection
- `hf-jobs` — compute infrastructure for evaluation
- `hf-dataset-viewer` — evaluation dataset validation
- `anthropic-docx` — evaluation report generation
- `visual-explainer` — interactive leaderboard HTML

## Reference Files

- `references/evaluation-dimensions.md` — scoring dimensions and benchmark selection
- `references/leaderboard-template.md` — leaderboard report structure
- `references/deployment-guide.md` — hardware selection for winner deployment

## Input
