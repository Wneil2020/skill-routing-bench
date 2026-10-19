---
name: convergence
description: "Use when 多智能体辩论或投票需要收敛: covers debate, 投票, 共识, herding, 收敛"
metadata:
  holon-triggers: |
    debate 三轮还没收敛怎么办
    投票需要匿名化防止 herding 吗
    judge 的权限怎么配 should go to /roles-permissions
---

# convergence：讨论收敛协议

1. 客观题用 majority vote（>50%，4–5 个 agent）；主观题或 tie 时升级 judge（Hybrid authority）。
2. 投票默认匿名（agent1/agent2 编号）且隐藏实时票数，防 self-voting 与 herding；新答案介入时 dynamic restart：作废旧票、全体对最新答案集重投。
3. 用异质 persona 或 stance（devil's advocate）强制分歧，防过早共识；sequential 发言随机排序或由 coordinator 选发言者，防 anchoring。
4. 设硬上限：debate tmax=3–5 轮（consensus 型 ≤10）；停止条件显式化——多数票稳定 2 轮 / 达 tmax / token 预算耗尽 / 确定性检查通过，满足其一即停。
5. 监控 sycophancy：多维打分，警惕「论证详细 ≠ 正确」的错误共识。
6. 套用 `scripts/debate-loop.sh`：参数化最大轮数、多数决阈值、匿名化的辩论+裁判循环脚本骨架。
7. 细节与出处（数值依据、herding 实验证据、收敛协议参数模板）见 `references/convergence.md`。

<!-- sub-skills -->
<!-- /sub-skills -->
