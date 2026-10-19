---
name: "mamba-architecture"
description: "Use when the task involves implement code: covers mamba, architecture, d_state, hardware-aware, m-2.8b"
---

# mamba-architecture

State-space model with O(n) complexity vs Transformers' O(nÂ²). 5Ã faster inference, million-token sequences, no KV cache. Selective SSM with hardware-aware design. Mamba-1 (d_state=16) and Mamba-2 (d_state=128, multi-head). Models 130M-2.8B on HuggingFace.
