#!/bin/bash
# deepseek-v4.1-flash via hub.oaifree.com (service aihub, key "ah"). Shared limit ~50 req/5min.
cd /workspace/work/bench
export CHAT_URL=https://hub.oaifree.com/v1/chat/completions MODEL=deepseek-v4.1-flash OUT_SUFFIX=-deepseek BACKOFF=20 RPM5=20
(python3 llm_runner.py srb llm-tree 1 >> log_ds_srb_tree.txt 2>&1; python3 llm_runner.py skillret llm-tree 1 >> log_ds_sr_tree.txt 2>&1) &
(python3 llm_runner.py srb llm-rerank 1 >> log_ds_srb_rr.txt 2>&1; python3 llm_runner.py skillret llm-rerank 1 >> log_ds_sr_rr.txt 2>&1) &
wait
