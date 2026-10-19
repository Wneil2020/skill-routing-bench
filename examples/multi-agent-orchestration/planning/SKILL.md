---
name: planning
description: "Use when 拆解复杂任务为计划并验证重规划: covers 规划, DAG, 重规划, 验收标准"
metadata:
  holon-triggers: |
    把这个复杂任务拆成 DAG 并给出每单元的验收标准
    验证失败时什么时候触发重规划
    worker 的权限怎么最小化 should go to /roles-permissions
---

# planning：Plan→Execute→Verify→Replan

1. Plan：把任务拆成 DAG，每单元带 VMAO 七字段——id、question、agent_type、dependencies、priority、context_from_deps、verification_criteria；产出契约（落盘 schema）并入 verification_criteria 表达；拆解三原则 RAG First、Maximize Parallelism、Minimize Dependencies。
2. 单元粒度以「单次调用可完成 + 验收可判定」为准。
3. Execute：上游产物落盘为带 schema 的契约文件，下游按 id/路径引用；依赖结果显式声明才注入。
4. Verify：验收标准五维——completeness、evidence quality、metadata（URL/日期）、specificity、contradictions；确定性检查优先于 LLM 评审，judge 用与执行器不同且更强的模型。
5. Replan：触发条件为验证失败（incomplete 全部进 retry）、新信息、预算耗尽；动作优先 retry、其次新增子问题；默认最大重规划 3 次，配 token 预算与 diminishing returns（<5%）双保险，耗尽即带 gaps 收尾。
6. 窄任务退化为单 agent 或静态 pipeline——验证驱动重规划只对开放式多维任务划算。
7. plan.md 模板、VMAO 默认参数（k=3、timeout 600s、阈值 0.8/0.75）与出处见 `references/planning.md`。

<!-- sub-skills -->
<!-- /sub-skills -->
