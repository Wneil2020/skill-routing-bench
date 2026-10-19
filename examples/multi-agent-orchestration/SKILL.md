---
name: multi-agent-orchestration
description: "Use when \u7f16\u6392\u591a\u4e2a\u5b50\u4ee3\u7406\u5b8c\u6210\u590d\u6742\u4efb\u52a1: covers \u7f16\u6392, \u591a\u4ee3\u7406, subagent, \u62d3\u6251, orchestration"
metadata:
  holon-archive-count: "1"
  holon-triggers: |
    比较多代理方案的成本并选择合适的拓扑
    规划一个带红队评审的多代理工作流
    debate 投票几轮收敛 should go to /convergence
---

# multi-agent-orchestration

A skill folder may contain sub-skill folders. Any subfolder with a `SKILL.md` is a sub-skill. A parent `SKILL.md` lists its sub-skills between `<!-- sub-skills -->` markers; that list is the routing table, and a tool writes it.

When a loaded `SKILL.md` contains such a list:

1. **Go down only when a line matches.** Compare the task with each sub-skill's description and with the words its line says it also takes through its sub-skills. When one matches, read the `SKILL.md` in that subfolder before acting.
2. **Repeat at each level.** If that sub-skill lists further sub-skills, compare again and go down again.
3. **Read only what is on the path.** Never load every sub-skill in advance.
4. **If nothing matches, stay here.** Act on the current `SKILL.md`. Do not force a descent.
5. **Come back up when done.** When a sub-skill finishes, return to the parent and continue its remaining steps. The child's output is the parent's input.
6. **Report misses.** If no sub-skill matches, or the one reached does not handle the task, append one line to `_feedback.md` at the tree root: `task sentence | path taken | outcome`. Then carry on. The next absorption reads that line.

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **convergence** (`convergence/`): Use when 多智能体辩论或投票需要收敛: covers debate, 投票, 共识, herding, 收敛
- **cost-selection** (`cost-selection/`): Use when 评估多代理成本或判断是否该用多代理: covers 成本, token, 选型, 单代理
- **failure-modes** (`failure-modes/`): Use when 多代理系统出问题需要排障: covers 失败模式, 排障, 死循环, 上下文膨胀, 开销失控
- **opencode-setup** (`opencode-setup/`): Use when 在 OpenCode 中配置子代理编排: covers opencode, permission, 黑板, 断点续跑
- **planning** (`planning/`): Use when 拆解复杂任务为计划并验证重规划: covers 规划, DAG, 重规划, 验收标准
- **redteam-maker-checker** (`redteam-maker-checker/`): Use when 需要红队或质量对抗评审: covers 红队, redteam, maker-checker, 攻击清单
- **roles-permissions** (`roles-permissions/`): Use when 分配子代理角色与权限: covers 角色, 权限, planner, worker, judge
- **scenario-decision** (`scenario-decision/`): Use when 按任务类型选择编排方案: covers 决策表, 深度调研, 代码改造, 写作, 问答
- **topologies** (`topologies/`): Use when 选择多代理拓扑结构: covers 拓扑, orchestrator-worker, pipeline, blackboard, hierarchical

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->

## Routing lessons from the benchmark (2026-10)

Measured on three public skill libraries (SkillRetBench, ToolRet, SkillRet): strict "exactly one sibling matches literally" routing reached 0.6-4.5% Hit@1, while a model reading these same descriptions level by level reached 50-66%. So:

7. **Choose by meaning, not by string.** Read every sibling line and pick the closest one even when no cover word appears verbatim in the task. Cover words are hints, not gates.
8. **When two lines both fit, keep both.** Read both sub-skills' SKILL.md (at most three) and pick after reading, instead of stopping at the parent.
9. **Siblings must not share cover words.** When editing a sub-skill line, give each sibling at least one word no other sibling has. Generic words (skills, docs, automation, 多代理) never go in covers.

## 编排决策流程（本节点的自身步骤）

跨多个子主题的编排任务按以下顺序判断，任一步不满足即停在当前层级：

1. **单代理基线**：单 prompt + 检索/工具能解决就停；只有上下文溢出、需要并行/隔离、或错误代价高于多倍 token 时才升级。
2. **可分解性**：能拆成 |V|≥2 且边不稠密的 DAG 才继续；否则单代理 + routing。
3. **耦合与并行宽度**：|E|=0 → Parallel；ω=1 → Sequential；γ>0.6 且 |V|>5 → Hierarchical；其余 Hybrid。先判耦合再选并行。
4. **验证信号形态**：有确定性 ground truth → orchestrator-workers + 反馈环；无 ground truth → debate + judge。
5. **子任务可预知性**：可预知且线性 → pipeline；不可预知 → orchestrator-workers；规划本身不可预知 → adaptive planning。
6. **价值密度**：多代理约 15× chat token；覆盖不了就退回单调用 + 小模型 routing。
7. **尽早评估**：~20 条真实样本的小评测即可发现大效应问题。

按任务类型直接查表见 `scenario-decision/`；各步骤深入知识在对应子节点的 `references/`。
