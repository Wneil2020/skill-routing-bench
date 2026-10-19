---
name: hf-model-trainer
description: "Use when Train or fine-tune language models (FinBERT, sentence-transformers) on HuggingFace Jobs infrastructure using TRL. Covers SFT, DPO, GRPO, reward: covers model, trainer, 모델 훈련, 파인튜닝, dpo"
metadata:
  holon-triggers: |
    fine-tuning financial sentiment models
    training custom embeddings for stock analysis
---

---
name: hf-model-trainer
description: >-
  Train or fine-tune language models (FinBERT, sentence-transformers) on
  HuggingFace Jobs infrastructure using TRL. Covers SFT, DPO, GRPO, reward
  modeling, and GGUF conversion. Use when fine-tuning financial sentiment
  models, training custom embeddings for stock analysis, or running cloud GPU
  training jobs. Do NOT use for daily stock analysis (use daily-stock-check). Do
  NOT use for local model inference (use alphaear-predictor). Do NOT use for
  general HF Hub operations (use hf-cli). Korean triggers: "모델 훈련", "파인튜닝", "TRL".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
license: Complete terms in LICENSE.txt
---
# TRL Training on Hugging Face Jobs

## Overview

Train language models using TRL (Transformer Reinforcement Learning) on fully managed Hugging Face infrastructure. No local GPU setup required—models train on cloud GPUs and results are automatically saved to the Hugging Face Hub.

**TRL provides multiple training methods:**
- **SFT** (Supervised Fine-Tuning) - Standard instruction tuning
- **DPO** (Direct Preference Optimization) - Alignment from preference data
- **GRPO** (Group Relative Policy Optimization) - Online RL training
- **Reward Modeling** - Train reward models for RLHF

**For detailed TRL method documentation:**
```python
hf_doc_search("your query", product="trl")
hf_doc_fetch("https://huggingface.co/docs/trl/sft_trainer")  # SFT
hf_doc_fetch("https://huggingface.co/docs/trl/dpo_trainer")  # DPO
# etc.
```

**See also:** `references/training_methods.md` for method overviews and selection guidance

## When to Use This Skill

Use this skill when users want to:
- Fine-tune language models on cloud GPUs without local infrastructure
- Train with TRL methods (SFT, DPO, GRPO, etc.)
- Run training jobs on Hugging Face Jobs infrastructure
- Convert trained models to GGUF for local deployment (Ollama, LM Studio, llama.cpp)
- Ensure trained models are permanently saved to the Hub
- Use 
