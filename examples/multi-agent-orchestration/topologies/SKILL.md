---
name: topologies
description: "Use when 选择多代理拓扑结构: covers 拓扑, orchestrator-worker, pipeline, blackboard, hierarchical"
metadata:
  holon-triggers: |
    pipeline 和 blackboard 拓扑各自适合什么场景
    hierarchical 拓扑什么时候用
    辩论投票几轮能收敛 should go to /convergence
---

# topologies：选择多代理拓扑

1. 先跑单代理基线；只有上下文溢出、需要并行/隔离、或错误代价高于多倍 token 时才升级多代理。
2. 按「工作形状」而非 agent 数量选拓扑：
   - 已知分解、需并行执行 → orchestrator-worker
   - 固定线性步骤 → pipeline
   - 需要质量对抗与裁决 → debate+judge（配合 /convergence 与 /redteam-maker-checker）
   - ≥4 个独立并行项、orchestrator 上下文吃紧 → blackboard（状态外置到文件）
   - 路由不可预知 → hierarchical
   - 开放式问题 → hybrid（动态规划）
3. pipeline 阶段间只交接可校验的 artifact（对照 schema 的 JSON、带验收命令的分支），禁止交接散文。
4. 并行 fan-out 三件套：lane 化（每 worker 声明 owned_paths）、覆盖率对账、合并后跑一次全量集成检查。
5. worker ≥4 时把计划与产物写文件系统、只回传引用，orchestrator 上下文是稀缺资源。
6. 对照 `references/topologies.md`：6 种拓扑各自的定义、适用条件、失败模式、最小实现要点与选择速查表（含出处 URL）。

<!-- sub-skills -->
<!-- /sub-skills -->
