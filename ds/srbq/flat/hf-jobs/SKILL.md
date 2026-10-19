---
name: hf-jobs
description: "Use when Run compute workloads on HuggingFace Jobs infrastructure — UV scripts, Docker jobs, batch inference, data processing, and scheduled tasks. Use: covers jobs, HF Jobs, GPU 작업, workloads, trl"
metadata:
  holon-triggers: |
    running GPU workloads for financial model inference
    batch processing stock data
---

---
name: hf-jobs
description: >-
  Run compute workloads on HuggingFace Jobs infrastructure — UV scripts, Docker
  jobs, batch inference, data processing, and scheduled tasks. Use when running
  GPU workloads for financial model inference, batch processing stock data, or
  scheduling recurring compute jobs on HF infra. Do NOT use for TRL model
  training (use hf-model-trainer). Do NOT use for local script execution. Do NOT
  use for stock analysis (use daily-stock-check). Korean triggers: "HF Jobs", "GPU 작업".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
license: Complete terms in LICENSE.txt
---
# Running Workloads on Hugging Face Jobs

## Overview

Run any workload on fully managed Hugging Face infrastructure. No local setup required—jobs run on cloud CPUs, GPUs, or TPUs and can persist results to the Hugging Face Hub.

**Common use cases:**
- **Data Processing** - Transform, filter, or analyze large datasets
- **Batch Inference** - Run inference on thousands of samples
- **Experiments & Benchmarks** - Reproducible ML experiments
- **Model Training** - Fine-tune models (see `model-trainer` skill for TRL-specific training)
- **Synthetic Data Generation** - Generate datasets using LLMs
- **Development & Testing** - Test code without local GPU setup
- **Scheduled Jobs** - Automate recurring tasks

**For model training specifically:** See the `model-trainer` skill for TRL-based training workflows.

## When to Use This Skill

Use this skill when users want to:
- Run Python workloads on cloud infrastructure
- Execute jobs without local GPU/TPU setup
- Process data at scale
- Run batch inference or experiments
- Schedule recurring tasks
- Use GPUs/TPUs for any workload
- Persist results to the Hugging Face Hub

## Key Directives

When assisting with jobs:

1. **ALWAYS use `hf_jobs()` MCP tool** - Submit jobs using `hf_jobs("uv", {...})` or `hf_jobs("run", {...})`. The `script` parameter accepts Python code directly. Do NOT save to local files unless th
