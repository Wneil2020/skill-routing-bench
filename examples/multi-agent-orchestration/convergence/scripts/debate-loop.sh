#!/usr/bin/env bash
# ============================================================================
# debate-loop.sh（D12）— 辩论 + 裁判循环参考模板
# ----------------------------------------------------------------------------
# 用途：multi-agent debate 的编排骨架。支持 --dry-run 模式：不调用任何
#       agent API，用确定性桩数据完整跑通主循环（收敛路径与 judge 路径），
#       用于验证编排逻辑。接入真实 agent 时把 run_agent / collect_stances /
#       tally_votes 替换为项目内实际调用（如 `opencode run --agent <name> "..."`）。
#
# 设计依据（出处见 ../references/convergence.md）：
#   - 最大轮数默认 3（通用 debate 3–5 轮，轮数翻倍收益递减）；
#   - 多数决阈值：4–5 个 agent 时简单多数（>50%）；tie 或未到阈值时升级 judge（Hybrid）；
#   - 投票默认 Anonymous Voting + Hidden Tally（答案只挂匿名 ID agent1/agent2，
#     投票前不可见他人票数），防 self-voting 与 herding；
#   - sequential 发言随机排序，防 anchoring（先发言者锚定后续推理）；
#   - judge tie-breaker 全程最多调用 1 次，避免 judge 独裁；
#   - 停止条件（满足任一即停）：①某答案获多数且连续 2 轮无新答案/改票；
#     ②达到 MAX_ROUNDS；③token/时间预算耗尽；④确定性检查通过。
#
# 用法：
#   ./debate-loop.sh [--dry-run] "争议议题" [MAX_ROUNDS] [MAJORITY_THRESHOLD]
#   --dry-run：不调 agent，桩函数输出确定性数据；DRY_SCENARIO=majority（默认，
#              验证多数票收敛路径）| tie（验证 judge tie-breaker 路径）
# ============================================================================
set -euo pipefail

DRY_RUN=0
if [[ "${1:-}" == "--dry-run" ]]; then DRY_RUN=1; shift; fi
DRY_SCENARIO="${DRY_SCENARIO:-majority}"

TOPIC="${1:?用法: debate-loop.sh [--dry-run] <topic> [max_rounds] [majority_threshold]}"
MAX_ROUNDS="${2:-3}"                    # 最大轮数（默认 3；consensus 型可上调至 ≤10）
MAJORITY_THRESHOLD="${3:-0.5}"          # 多数决阈值（默认 >50%）

# 参数校验：MAX_ROUNDS 必须为 ≥1 的整数，否则零轮静默成功或 set -u 下不优雅报错
if ! [[ "$MAX_ROUNDS" =~ ^[0-9]+$ ]] || (( MAX_ROUNDS < 1 )); then
  echo "错误: MAX_ROUNDS 须为正整数（收到: '$MAX_ROUNDS'）" >&2
  exit 2
fi
BLACKBOARD="blackboard"                 # 黑板目录：产物与轮次状态落盘处
JUDGE_USED=0                            # judge tie-breaker 全局最多 1 次
STABLE_ROUNDS=0                         # 「同一答案连续获多数」轮数计数器
PREV_WINNER=""                          # 上一轮多数答案（用于判定「同一答案连续 2 轮」）

# ---------------------------------------------------------------------------
# 匿名化提示词：stance 仅挂匿名 ID，隐藏计票，随机发言顺序
# ---------------------------------------------------------------------------
ANONYMITY_PREAMBLE="
【匿名辩论规则】
- 你的身份是匿名 ID（agent1/agent2/...），发言中不得透露或猜测自己/他人的真实身份。
- 本题为对抗性立场题：你将收到分配给你的 stance（立场），必须为其辩护并攻击对立立场。
- 每轮陈述时你**看不到**其他 agent 的投票结果（Hidden Tally），只可见匿名化后的论点原文。
- 发言顺序每轮随机打乱，请勿依赖「上一轮谁先发言」做判断。
- 投票时禁止投给自己的答案（防 self-voting）。
"

# ---------------------------------------------------------------------------
# 待替换的桩函数：接入项目实际的 agent 调用
# ---------------------------------------------------------------------------
run_agent() {
  # $1=agent 名  $2=prompt  $3=输出文件（可选）
  # 落地示例：
  #   opencode run --agent "$1" --format json "$2" >> "${3:-/dev/null}"
  if (( DRY_RUN )); then
    printf '[DRY-RUN] %s 产物（议题：%s）\n' "$1" "$TOPIC" > "${3:-/dev/null}"
  fi
  echo "[STUB] run_agent $1" >&2
}

collect_stances() {   # 并行/串行收集各 debate agent 的本轮立场
  if (( DRY_RUN )); then
    printf 'agent1: stance A 论据\nagent2: stance B 论据\n'
    return
  fi
  echo "[STUB] collect_stances" >&2   # 应输出匿名化后的 stance 列表
}

tally_votes() {       # 隐藏计票：只返回票数分布，不向 agent 披露
  if (( DRY_RUN )); then
    if [[ "$DRY_SCENARIO" == "tie" ]]; then printf 'A:1\nB:1\n'; else printf 'A:2\nB:1\n'; fi
    return
  fi
  echo "[STUB] tally_votes" >&2       # 应输出 "answer_id:count" 列表
}

# ---------------------------------------------------------------------------
# 主循环：每轮 = debate agent 轮流陈述 → 匿名投票 → 收敛判定 → 必要时 judge 裁决
# ---------------------------------------------------------------------------
mkdir -p "$BLACKBOARD"

for (( round=1; round<=MAX_ROUNDS; round++ )); do
  echo "===== Round $round / $MAX_ROUNDS ====="

  # 1) debate：每个 agent 带匿名化提示 + 分配 stance，轮流陈述
  #    （顺序随机：shuf 索引数组；simultaneous 变体可改为并行生成再广播）
  run_agent "debate-a" "$ANONYMITY_PREAMBLE
议题：$TOPIC
stance：支持。请给出最强论据并反驳对方预期论点。
（第 $round 轮）" "$BLACKBOARD/debate-r${round}-a.md"
  run_agent "debate-b" "$ANONYMITY_PREAMBLE
议题：$TOPIC
stance：反对。请给出最强论据并反驳对方预期论点。
（第 $round 轮）" "$BLACKBOARD/debate-r${round}-b.md"
  # 可扩展 debate-c / debate-d ...（4–5 个 agent 时多数决最有效）

  # 2) 收集立场 + 匿名投票（Hidden Tally：agent 看不到票数）
  stances="$(collect_stances)"
  votes="$(tally_votes <<<"$stances")"

  # 3) 收敛判定
  winner="$(awk -F: -v t="$MAJORITY_THRESHOLD" '{c[$1]=$2; total+=$2} END {for (a in c) if (total > 0 && c[a]/total > t) {print a; exit}}' <<<"$votes")"

  # 仅当本轮 winner 与上一轮为同一答案才累计；winner 轮换或空缺即清零
  if [[ -n "$winner" && "$winner" == "$PREV_WINNER" ]]; then
    STABLE_ROUNDS=$((STABLE_ROUNDS + 1))
  elif [[ -n "$winner" ]]; then
    STABLE_ROUNDS=1
  else
    STABLE_ROUNDS=0
  fi
  PREV_WINNER="$winner"

  # 停止条件 ①：同一答案连续 2 轮获多数（且无新答案/改票）
  if (( STABLE_ROUNDS >= 2 )); then
    echo "收敛：答案 $winner 连续 2 轮获多数"
    break
  fi

  # 停止条件 ②：最后一轮直接收尾（报告最终多数答案，若有）
  if (( round == MAX_ROUNDS )); then
    echo "达到最大轮数 $MAX_ROUNDS；最终多数答案：${winner:-无（未收敛，升级人工或 judge）}"
  fi

  # 4) tie / 未到阈值 → Hybrid：升级 judge 裁决（全程最多 1 次）
  if [[ -z "$winner" && "$JUDGE_USED" -eq 0 ]]; then
    JUDGE_USED=1
    # judge 只做 argument evaluation（定性综合），不重新投票
    run_agent "judge" "你是裁判。以下是匿名化辩论记录（含隐藏计票的票数分布）：
$stances
票数分布：$votes
请对各方论证做定性综合，输出 verdict：采纳哪一方 + 理由 + 证据。" \
      "$BLACKBOARD/judge-r${round}.md"
    # 注：judge verdict 落盘 blackboard/judge-r<N>.md，由编排者读取并作为本轮结论；
    #     如需「新答案触发 dynamic restart（作废旧票、全体重新评估）」在此插入。
    break   # judge tie-breaker 后不再进入下一轮（避免 judge 独裁）
  fi
done

echo "辩论结束。产物见 $BLACKBOARD/debate-r*.md 与 judge-r*.md"
