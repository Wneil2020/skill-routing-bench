---
name: hf-evaluation
description: "Use when Evaluate ML model quality and manage evaluation results in HuggingFace model cards. Supports running benchmarks with: covers evaluation, 모델 평가, 벤치마크, artificial, benchmarks"
metadata:
  holon-triggers: |
    evaluating fine-tuned financial sentiment models
    benchmarking prediction accuracy
---

---
name: hf-evaluation
description: >-
  Evaluate ML model quality and manage evaluation results in HuggingFace model
  cards. Supports running benchmarks with lighteval/inspect-ai, extracting eval
  tables, and importing scores from Artificial Analysis API. Use when evaluating
  fine-tuned financial sentiment models, benchmarking prediction accuracy, or
  adding evaluation metrics to model cards. Do NOT use for model training (use
  hf-model-trainer). Do NOT use for AI report quality scoring (use
  ai-quality-evaluator). Do NOT use for stock signal analysis (use
  daily-stock-check). Korean triggers: "모델 평가", "벤치마크".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "ml"
---
# Overview
This skill provides tools to add structured evaluation results to Hugging Face model cards. It supports multiple methods for adding evaluation data:
- Extracting existing evaluation tables from README content
- Importing benchmark scores from Artificial Analysis
- Running custom model evaluations with vLLM or accelerate backends (lighteval/inspect-ai)

## Integration with HF Ecosystem
- **Model Cards**: Updates model-index metadata for leaderboard integration
- **Artificial Analysis**: Direct API integration for benchmark imports
- **Papers with Code**: Compatible with their model-index specification
- **Jobs**: Run evaluations directly on Hugging Face Jobs with `uv` integration
- **vLLM**: Efficient GPU inference for custom model evaluation
- **lighteval**: HuggingFace's evaluation library with vLLM/accelerate backends
- **inspect-ai**: UK AI Safety Institute's evaluation framework

# Version
1.3.0

# Dependencies

## Core Dependencies
- huggingface_hub>=0.26.0
- markdown-it-py>=3.0.0
- python-dotenv>=1.2.1
- pyyaml>=6.0.3
- requests>=2.32.5
- re (built-in)

## Inference Provider Evaluation
- inspect-ai>=0.3.0
- inspect-evals
- openai

## vLLM Custom Model Evaluation (GPU required)
- lighteval[accelerate,vllm]>=0.6.0
- vllm>=0.4.0
- torch>=2.0.0
- transformers>=4.40.0
- ac
