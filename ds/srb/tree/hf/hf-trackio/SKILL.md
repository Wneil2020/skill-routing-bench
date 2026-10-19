---
name: hf-trackio
description: "Use when Track and visualize ML training experiments with Trackio — log metrics via Python API, fire alerts for diagnostics, and retrieve metrics: covers trackio, 실험 추적, 학습 모니터링, diagnostics, fire"
metadata:
  holon-triggers: |
    monitoring financial model training runs
    comparing experiment results
---

---
name: hf-trackio
description: >-
  Track and visualize ML training experiments with Trackio — log metrics via
  Python API, fire alerts for diagnostics, and retrieve metrics via CLI. Use
  when monitoring financial model training runs, comparing experiment results,
  or setting up real-time dashboards on HF Spaces. Do NOT use for model training
  itself (use hf-model-trainer). Do NOT use for stock price tracking (use
  weekly-stock-update). Do NOT use for AI report quality metrics (use
  ai-quality-evaluator). Korean triggers: "실험 추적", "학습 모니터링".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Trackio - Experiment Tracking for ML Training

Trackio is an experiment tracking library for logging and visualizing ML training metrics. It syncs to Hugging Face Spaces for real-time monitoring dashboards.

## Three Interfaces

| Task | Interface | Reference |
|------|-----------|-----------|
| **Logging metrics** during training | Python API | [references/logging_metrics.md](references/logging_metrics.md) |
| **Firing alerts** for training diagnostics | Python API | [references/alerts.md](references/alerts.md) |
| **Retrieving metrics & alerts** after/during training | CLI | [references/retrieving_metrics.md](references/retrieving_metrics.md) |

## When to Use Each

### Python API → Logging

Use `import trackio` in your training scripts to log metrics:

- Initialize tracking with `trackio.init()`
- Log metrics with `trackio.log()` or use TRL's `report_to="trackio"`
- Finalize with `trackio.finish()`

**Key concept**: For remote/cloud training, pass `space_id` — metrics sync to a Space dashboard so they persist after the instance terminates.

→ See [references/logging_metrics.md](references/logging_metrics.md) for setup, TRL integration, and configuration options.

### Python API → Alerts

Insert `trackio.alert()` calls in training code to flag important events — like inserting print statements for debugging, but structured and queryable:

- `trackio
