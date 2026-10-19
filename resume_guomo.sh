#!/bin/bash
# guomohub runs (key injected by host). Low concurrency, long backoff. wang3 token is invalid as of 2026-10-19.
cd /workspace/work/bench
G="export CHAT_URL=https://www.guomohub.me/v1/chat/completions BACKOFF=30"
(eval $G; export MODEL=glm-5.3-flash OUT_SUFFIX=-glm; python3 llm_runner.py srb llm-tree 1 >> log_glm_srb_tree.txt 2>&1; python3 llm_runner.py toolret llm-tree 1 >> log_glm_tr_tree.txt 2>&1) &
(eval $G; export MODEL=glm-5.3-flash OUT_SUFFIX=-glm; python3 llm_runner.py srb llm-rerank 1 >> log_glm_srb_rr.txt 2>&1; python3 llm_runner.py toolret llm-rerank 1 >> log_glm_tr_rr.txt 2>&1) &
(eval $G; export MODEL=deepseek-v4-flash-0731 OUT_SUFFIX=-ds0731; python3 llm_runner.py skillret llm-tree 1 >> log_ds0731_sr_tree.txt 2>&1; python3 llm_runner.py skillret llm-rerank 1 >> log_ds0731_sr_rr.txt 2>&1) &
(export PATH=/workspace/tools/npm/bin:$PATH OPENCODE_CONFIG=/workspace/tools/opencode/opencode.json HOME=/workspace/work/bench/analysis/fakehome; timeout 1500 opencode run -m guomo/glm-5.3-flash "$(cat analysis/PROMPT.md)" > analysis/opencode_log.txt 2>&1) &
wait
