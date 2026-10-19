# 实战示例：三个端到端编排方案

> 每个示例含：任务设定 → DAG → 角色分配 → 模型选择 → 停止条件 → 预估 token。
> token 估算基于 cost-selection.md 的实测倍数（AdaptOrch 同模型口径：单代理 12.3K/实例、自适应多代理 41.8K/实例；Anthropic 口径：多代理 ≈15× chat）；均为 [推断] 级估算，用前应实测校准。

## 示例 1：深度调研（"2026 年多代理编排生产实践综述"）

**任务设定**：广度优先开放问题，需跨 10+ 独立来源，超出单上下文窗口。选 orchestrator-workers（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

**DAG**：

```
P0 planner 拆解（8–12 子问题，VMAO 七字段）
 ├─ R1 拓扑模式调研 ─┐
 ├─ R2 成本实证调研 ─┤
 ├─ R3 失败模式调研 ─┼─→ S1 分组综合（>10 条触发 hierarchical synthesis）
 ├─ R4 收敛机制调研 ─┤      ↓
 ├─ R5 落地工具调研 ─┘   C1 CitationAgent 引用定位 → J1 judge 终审
```

**角色分配**：orchestrator（primary，dispatch + 合成）；planner×1；worker-research×5（并行，各写 blackboard/notes/r<N>.md）；CitationAgent×1；judge×1。

**模型选择**：orchestrator/judge/synthesis 用强模型（Opus 级）；5 个 research worker 用便宜模型（Sonnet/Haiku 级）——强编排+弱执行，执行 token 占 70–90% 时总成本可降 60–85%（见 cost-selection.md §3）。

**停止条件**：①每个 worker 回传轻量引用且 verification_criteria 通过（VMAO Verify：completeness ≥0.8，缺项触发 ≤3 次 replan）；②CitationAgent 完成全部 claim→source 对齐；③judge 单次评分 ≥0.8 或修复 2 轮后升人；④硬上限：replan ≤3、token 预算 ≥ 预估上限（本例设 45× chat 等价，见下方预估）——注意 15× chat 是「是否值得上多代理」的门槛参照（cost-selection.md §1），不是执行预算。

**预估 token**：chat 基线 ≈4K/轮；5 worker × ~30K（含检索工具调用）+ 编排/合成/judge ~20K ≈ **170K（≈40× chat，高价值研究类任务的上限区）**；若任务收窄为 3 子问题则 ≈90K。对照：单代理顺序做同任务会撞 200K 截断且丢失并行压缩收益（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

## 示例 2：大型代码改造（"把 30 个调用点从 v1 API 迁移到 v2 并修复回归"）

**任务设定**：改动范围无法预先确定（orchestrator-workers 典型场景）；SWE-bench 类任务 ω≈3.4、γ≤0.4，62% 实例路由 Hybrid（出处：https://arxiv.org/html/2602.16873v1）。有测试套件作确定性 ground truth——**不需要 debate**。

**DAG**：

```
P0 planner：静态分析调用点 → 按模块切 6 个迁移单元（deps ⊆ completed 判定就绪）
 ├─ W1 模块 A 迁移 → 跑 pytest（模块 A）
 ├─ W2 模块 B 迁移 → 跑 pytest（模块 B）   （W1–W3 相互独立，并行）
 ├─ W3 模块 C 迁移 → 跑 pytest（模块 C）
 ├─ W4 模块 D 迁移（依赖 W1 的公共类型变更）─ 串行
 ├─ W5 模块 E 迁移（依赖 W2）
 └─ W6 模块 F 迁移（依赖 W3）
 → I1 全量集成测试（orchestrator 触发，非 agent）
 → RT redteam 五维攻击（边界/回归/权限越界）
 → J judge 终审（先跑 CI 确定性检查，再评残余面）
```

**角色分配**：orchestrator×1；planner×1；worker-code×6（各自 owned_paths 隔离，edit 白名单限定 src/**、tests/**）；redteam×1（只读产物，bash ask）；judge×1（只读，bash ask 重跑测试）。

**模型选择**：planner/judge 强模型；worker-code 可用 ϵ-收敛便宜模型（AdaptOrch：五个便宜模型 + 正确拓扑达 SWE-bench 52.6，超同预算 Self-MoA 51.5）。

**停止条件**：①6 单元 pytest 全绿；②集成测试通过；③redteam APPROVE 或 REQUEST_CHANGES 修复 ≤2 轮后升人；④judge verdict 每条带 command + exit code 且与 CI 对账一致；⑤硬上限：worker steps ≤40、修复 ≤2 轮。

**预估 token**：按 AdaptOrch SWE-bench 实测，自适应路由 ≈**41.8K/实例（单代理 12.3K 的 3.4×）**；6 单元静态并行无路由则 ~4–5×。若预算 < 3× 单代理，退回单代理 + 测试循环。

## 示例 3：长文写作（"40 页技术白皮书：大纲已定，分章撰写 + 一致性打磨"）

**任务设定**：清晰线性依赖（大纲→分章→打磨），选 prompt chaining + evaluator-optimizer；**不要用 debate 替代 evaluator-optimizer**（评估标准单一明确时一个评估器循环更便宜可控，见 scenario-decision-table.md 写作行）。

**DAG**：

```
G0 outline（人审 gate：对照 checklist 程序化校验章节覆盖）
 ├─ W1 第 1–2 章 ─┐
 ├─ W2 第 3–4 章 ─┤  （分章可并行，唯并行环节）
 ├─ W3 第 5–6 章 ─┤
 └─ W4 第 7–8 章 ─┘
 → A1 主代理按 outline 组装成文
 → E1 evaluator 评审（结构/术语一致性/证据密度 rubric）
 → R1 修订（evaluator-optimizer 循环，≤3 轮）
 → E2 终审 → 人审发布
```

**角色分配**：orchestrator（兼 assembler）×1；writer worker×4（各领 2 章，交接物 = 对照 outline checklist 的章节草稿文件，非散文摘要）；evaluator×1（与 writer 不同模型或不同 system prompt，防自评偏差）。

**模型选择**：writer 用中档模型（长文生成是 token 大头）；evaluator 用强模型（反馈必须 demonstrably 改进输出，否则裁剪该环节，出处：https://www.anthropic.com/engineering/building-effective-agents）。

**停止条件**：①outline gate 通过才进入分章写作；②evaluator rubric 各项达标或 3 轮循环上限（收益递减即停）；③长上下文接力：临近 200K 时 spawn 干净 context 新 writer + 结构化交接简报；④总轮数（写作+修订）≤8。

**预估 token**：40 页 ≈ 60K 正文 token；写作 4×~25K + 评估/修订 3 轮 ×~30K ≈ **190K**。对照 Beam 口径：3-agent pipeline 约 29K vs 单 agent 10K——若章节间不需要真正专业化，合并环节，不为同一结果付 3 倍价钱（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）。
