---
name: cost-selection
description: "Use when 评估多代理成本或判断是否该用多代理: covers 成本, token, 选型, 单代理"
metadata:
  holon-triggers: |
    多代理 token 成本是单代理的几倍
    这个任务该用单代理还是多代理，选型怎么定
    怎么选拓扑结构 should go to /topologies
---

# cost-selection：成本与选型

1. 记住成本锚点：agent ≈ 4× chat token，多代理 ≈ 15× chat；任务价值必须覆盖该溢价，否则退回单调用 + 按难度 routing 到小模型。
2. token 用量解释约 80% 的评测方差——先扩 token 预算再谈架构；升级模型代际优于加倍 token 预算。
3. 强模型放编排/judge 位，弱模型放执行/maker 位（Opus lead + Sonnet subagents 实测超单 Opus 90.2%；maker-checker 弱 maker 可省 40–60%）。
4. 「何时不该用多代理」清单：原子任务；γ≈1 全序紧耦合任务（全并行在 GPQA 上比单代理还差 44.1 vs 46.2）；无确定性验证且价值密度低；编排增益与可分解性成正比。完整清单见 `references/cost-selection.md`。
5. DAG 三特征路由：|E|=0 → Parallel；ω=1 → Sequential；γ>0.6 且 |V|>5 → Hierarchical；其余 Hybrid。
6. 复杂度只在实测改善结果时才增加；从单 prompt 起步逐级加，~20 条真实样本的小评测即可发现大效应。
7. 成本速算表与 AdaptOrch 详细结论见 `references/cost-selection.md`。

<!-- sub-skills -->
<!-- /sub-skills -->
