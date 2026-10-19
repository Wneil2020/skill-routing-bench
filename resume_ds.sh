#!/bin/bash
# Resume DeepSeek (wang3) runs + holon failure analysis via opencode. No keys here; injected by host.
cd /workspace/work/bench
export CHAT_URL=https://router.wang3.top/v1/chat/completions MODEL=deepseek/deepseek-v4.1-flash-fast OUT_SUFFIX=-deepseek BACKOFF=20
(python3 llm_runner.py srb llm-tree 1 >> log_ds_srb_tree.txt 2>&1; python3 llm_runner.py skillret llm-tree 2 >> log_ds_sr_tree.txt 2>&1) &
(python3 llm_runner.py srb llm-rerank 1 >> log_ds_srb_rr.txt 2>&1; python3 llm_runner.py skillret llm-rerank 2 >> log_ds_sr_rr.txt 2>&1) &
(export PATH=/workspace/tools/npm/bin:$PATH OPENCODE_CONFIG=/workspace/tools/opencode/opencode.json HOME=/workspace/work/bench/analysis/fakehome; timeout 1100 opencode run -m wang3/deepseek/deepseek-v4.1-flash-fast "$(cat analysis/PROMPT.md)" > analysis/opencode_log.txt 2>&1) &
(export MODEL=MiniMax-M3 OUT_SUFFIX=-minimax BACKOFF=30 CHAT_URL=https://hub.oaifree.com/v1/chat/completions; python3 llm_runner.py toolret llm-tree 1 >> log_mm_tr_tree.txt 2>&1; python3 llm_runner.py srb llm-tree 1 >> log_mm_srb_tree.txt 2>&1) &
(export MODEL=MiniMax-M3 OUT_SUFFIX=-minimax BACKOFF=30 CHAT_URL=https://hub.oaifree.com/v1/chat/completions; python3 llm_runner.py srb llm-rerank 1 >> log_mm_srb_rr.txt 2>&1) &
wait
