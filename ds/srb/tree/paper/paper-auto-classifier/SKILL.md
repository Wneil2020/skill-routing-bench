---
name: paper-auto-classifier
description: "Use when Automatically discover, classify, and route academic papers from arXiv RSS feeds and HuggingFace daily papers. Scores relevance to tracked: covers paper, auto, classifier, queues, feeds"
metadata:
  holon-triggers: |
    monitor papers
    auto-classify papers
---

---
name: paper-auto-classifier
description: >-
  Automatically discover, classify, and route academic papers from arXiv RSS
  feeds and HuggingFace daily papers. Scores relevance to tracked research
  topics, routes high-relevance papers to Slack with summaries, and queues
  top papers for full review. Use when the user asks to "monitor papers",
  "auto-classify papers", "paper radar", "논문 자동 분류", "논문 레이더",
  "paper-auto-classifier", or wants automated paper discovery and routing.
  Do NOT use for reviewing a specific paper (use paper-review), looking up
  a known paper (use alphaxiv-paper-lookup), or general web research (use
  parallel-web-search).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Paper Auto-Classifier

Automated paper discovery pipeline: poll sources, classify by relevance, summarize, and route to appropriate channels.

## When to Use

- As part of the daily Intel track (runs automatically)
- When setting up monitoring for a new research area
- To discover papers from overnight arXiv submissions

## Tracked Research Topics

Configurable topic registry with relevance keywords:

| Topic | Keywords | Weight |
|-------|----------|--------|
| LLM Infrastructure | inference, serving, vLLM, SGLang, TensorRT | 1.0 |
| GPU/Accelerator | CUDA, H100, B200, GPU cluster, NVLink | 0.9 |
| Kubernetes/Cloud | K8s, orchestration, scheduling, Kueue | 0.8 |
| Fine-tuning | LoRA, QLoRA, RLHF, DPO, SFT, distillation | 0.8 |
| AI Agents | agentic, tool use, MCP, agent framework | 0.9 |
| MLOps | model serving, monitoring, A/B testing | 0.7 |
| Security/Safety | alignment, guardrails, red-teaming, jailbreak | 0.7 |

## Workflow

### Step 1: Poll Sources

**arXiv RSS Feeds** (configurable categories):
- `cs.CL` — Computation and Language
- `cs.AI` — Artificial Intelligence
- `cs.DC` — Distributed Computing
- `cs.CR` — Cryptography and Security

**HuggingFace Daily Papers**:
```
hf papers list --date today
```

**Semantic Scholar Alerts** (if 
