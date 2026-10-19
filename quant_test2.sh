#!/bin/bash
# Same 40 SRB qids: hub v4.1 rerank vs wang3 v4.1 rerank (llm-rerank-deepseek). Separate dir ds/srbq, never merged.
cd /workspace/work/bench
export CHAT_URL=https://hub.oaifree.com/v1/chat/completions MODEL=deepseek-v4.1-flash OUT_SUFFIX=-dsv41hub_r2 BACKOFF=20 RPM5=20
python3 llm_runner.py srbq llm-rerank 2 > log_quant2.txt 2>&1
