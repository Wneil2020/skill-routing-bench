---
name: scenario-decision
description: "Use when 按任务类型选择编排方案: covers 决策表, 深度调研, 代码改造, 写作, 问答"
metadata:
  holon-triggers: |
    深度调研任务该用哪种编排方案
    写作报告类任务在决策表里推荐什么
    OpenCode 里怎么配置 subagent should go to /opencode-setup
---

# scenario-decision：按任务类型选编排方案

1. 打开 `references/scenario-decision-table.md` 的决策总表，定位任务类型行：深度调研 / 大型代码改造 / 写作报告 / 决策评估 / 开放式探索 / 事实准确问答。
2. 按该行取推荐拓扑、是否需要 debate/judge、并行度、成本提示与退化单代理条件；行内结论均带出处 URL，口径分歧处并列注明。
3. 速记：
   - 深度调研 → orchestrator-worker，lead + 3–5 并行 subagent；简单查证退化单代理
   - 大型代码改造 → orchestrator-workers + 测试反馈环（确定性 ground truth，不用 debate）
   - 写作/报告 → prompt chaining + evaluator-optimizer（不用 debate）
   - 决策评估 → ≤3 agent 串行/层级 debate 或 maker-checker，防 sycophancy
   - 开放式探索 → adaptive planning + 环境 ground truth + 硬停止条件；时间敏感不做
   - 事实问答 → 默认单代理 + 检索 + citation 检查（多代理最多持平）
4. 拿不准时走表末的 7 步决策流程（单代理基线 → 可分解性 → 耦合宽度 → 验证信号 → 可预知性 → 价值密度 → 尽早评估）。
5. 端到端落地样例（DAG、角色、模型、停止条件、token 估算）见 `references/examples.md`：深度调研 / 大型代码改造 / 长文写作三个完整示例。
6. 选定拓扑后到 /topologies 看实现要点；成本核对到 /cost-selection；OpenCode 配置到 /opencode-setup。

<!-- sub-skills -->
<!-- /sub-skills -->
