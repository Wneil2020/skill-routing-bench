# 红蓝队 / maker-checker：对抗式评审的可操作指南

## 1. 三种模式的区别

| 模式 | 角色关系 | 本质 |
| --- | --- | --- |
| maker-checker | maker 生成，checker 校验，循环直到通过 | 角色固定的非对称验证循环 |
| generator-critic | critic 用不同 system prompt / 不同优先级评审 generator 输出 | 与 maker-checker 同构（金融业控制术语 vs ML 社区术语）[推断] |
| red-blue team | 红队主动攻击、蓝队防御建设 | 对抗强度升级：不只是「校验」而是「主动攻击」，攻击清单需显式枚举 [推断] |

要点：

- maker-checker 是 multi-agent debate 模式的实用变体（角色固定、非对称）；debate 本身是对称 peer-to-peer 立场对抗 + judge 裁决。beam.ai 将 maker-checker 列为 debate 的子变体（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- 成本变体：maker 用便宜快速的模型、checker 用强模型，可降本 40–60% 且保留质量收益（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- Anthropic 官方命名为 evaluator-optimizer：一个 LLM call 生成、另一个评估反馈构成循环；适用于评估标准明确、迭代精修有可测收益的场景（出处：https://www.anthropic.com/engineering/building-effective-agents）
- 与 self-critique 的区别：同上下文自我批评带着产生 bug 的相同盲区；独立 reviewer 带 fresh context、只读工具、固定报告格式，能抓到不同类型的错误，换不同模型/厂商差异更大（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- 防 sycophancy：agent 倾向附和多数立场即使它是错的，产生 confidently incorrect 的假共识；评审者与被审者共享上下文会加剧此问题（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- 冲突观点并列 [说明]：beam.ai 认为 debate 类（含 maker-checker）能降低幻觉、质量收益明确；而 llm-stack-book 的定量模型显示同模型采样受 1−ρ 系统性失败上限约束、相关采样收益远低于独立假设预测——不矛盾：前者是定性生产经验，后者提醒必须用 decorrelation 手段才能兑现收益（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）

## 2. 五维攻击清单模板

以下 checklist 可直接复制给红队 reviewer。每维至少产出：finding 编号、file + line、一条可运行的演示命令及其输出；style 偏好永远不构成阻断（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

```markdown
## 红队攻击清单

### ① 正确性
- [ ] 需求/规格逐条核对：实现是否满足验收标准？遗漏了哪条？
- [ ] 主路径行为与 spec 的每个输入输出对是否一致？
- [ ] 是否存在「改测试以弱化断言」的 oracle 篡改行为？

### ② 边界 / edge case
- [ ] 空输入、超大输入、异常字符集、并发调用是否被处理？
- [ ] 错误路径是否吞掉失败（try/except 后静默返回）？
- [ ] race condition：共享状态、非原子操作、时序假设？
- [ ] 测试覆盖缺口：哪些行为没有被任何测试覆盖？列出未完成项
      （coverage accounting；「60% 文件无发现」≠「无发现」）

### ③ 安全
- [ ] 注入面（prompt injection、SQL、命令、路径穿越）？
- [ ] 权限越界：越权读写、密钥/token 泄漏？
- [ ] 内容审查是否需要 sectioning guardrails（一个实例处理查询、
      另一个并行筛查，比同一 call 兼顾两者效果更好）？
- [ ] 多 prompt 并行审查 + 问题即标记（voting 变体）是否已跑过？

### ④ 事实
- [ ] 每条结论是否有出处？找出 gaps 与 unsupported claims
- [ ] 第二遍 refutation：由不同 agent 尝试反驳每个 finding，
      只保留存活者
- [ ] 「干净报告」≠「全覆盖」：worker 中断后的空结果被静默丢弃？

### ⑤ 成本 / 收敛
- [ ] 修复循环是否有停止规则（stop rule）？
- [ ] writer 最多两轮修复，之后未决 finding 升级人审
- [ ] 成本是否随 agent 数增长而非结果大小？预算是否封顶？
```

出处支撑：代码维度清单、oracle 篡改与 coverage accounting（https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）；安全 voting / sectioning guardrails（https://www.anthropic.com/engineering/building-effective-agents）；事实维度 gaps/refute（https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）；成本维度（预算上限 + 定时取消 + 修复轮数上限，https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。五维综合 [推断]。

## 3. 确定性检查优先原则

固定验证顺序：**确定性检查（测试 / lint / typecheck / schema）→ 程序化 gate（脚本、路径检查）→ LLM judge（只评确定性检查覆盖不到的残余面）**；agent 的 APPROVE 永远不替代 CI（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

理由：

- 只读代码的 judge 只是「第二意见」；先跑确定性检查再评审缺失部分的 judge 才是「闸门/gate」（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- 验证链：lane gate（脚本做路径检查 + acceptance 命令）→ judge 重跑决定性检查 → integration gate 合并后全量跑 → CI 在干净机器重跑相同 gate（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- pipeline 中 stage 1 的幻觉被 stage 2 当作 ground truth 继承，无验证步骤时错误跨 stage 复合；阶段交接必须交付「可校验形状的工件」（plan.json 对 schema、分支对 acceptance 命令），交付散文的 stage 会累积彼此错误（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://www.anthropic.com/engineering/building-effective-agents）
- MAST taxonomy（1600+ 执行轨迹标注）：多代理失败最大家族之一是 task verification——「没人检查输出，或 checker 太浅」；且失败多是组织性的而非能力性的，工程投入应放在交接验证与真正的验证阶段，而不是再加一个 agent（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- 代码领域尤其适合确定性验证：解可通过自动测试验证、agent 可用测试结果迭代反馈、质量可客观度量（出处：https://www.anthropic.com/engineering/building-effective-agents）
- LLM 评审的正当领域仅剩「需求符合性、可读性、无测试覆盖的逻辑正确性」等无法程序化判定的残余面 [推断]

## 4. 防止红队流于形式的具体机制

### 4.1 强制具体证据
reviewer 只报告「带 file + line + 一条能演示问题的命令」的 finding，并要求实际运行该命令、附输出；具体反例要求天然过滤空洞批评（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

### 4.2 上下文隔离与 blind comparison
- judge 不得知道自己评审的候选是哪个 agent/模型写的（blind comparison），并在多次运行间变换顺序（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- writer/reviewer 分离 + 只读工具 + 不同模型/厂商；reviewer 声明「这不是我写的代码，不许改它」，输出 APPROVE / REQUEST_CHANGES（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）

### 4.3 Decorrelation（防共谋、防同源盲区）
- judge 不得编辑它评审的代码（不能让自己的 verdict 成真）（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- 多 agent 同源采样共享系统性盲区，必须主动 decorrelate：不同基座模型、不同 persona/分解、不同工具权限、更高 temperature；否则 10 个同 agent 副本在 temperature 0 下什么都减不掉（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/；https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html）
- 「judge approves everything」的根因：judge 只读不跑检查、与 writer 共享上下文、或能编辑代码；修法是移除 Edit/Write 权限、要求每行 verdict 携带 command + exit code（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）

### 4.4 量化门槛与硬上限
- writer 最多两轮修复，之后未决 finding 升级给人（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）
- group chat 限 3 个 agent 以内（出处：https://beam.ai/agentic-insights/multi-agent-orchestration-patterns-production）
- APPROVED 需匹配硬迭代上限（`"APPROVED" in critique or iteration >= 3`）；用最大迭代数等停止条件维持控制（出处：https://prakashkagitha.github.io/llm-stack-book/08-agents-harness/07-multi-agent-systems.html；https://www.anthropic.com/engineering/building-effective-agents）

### 4.5 Verdict–CI 一致性审计
定期对比最近 5 次 judge verdict 与 CI 结果：不一致即说明 judge prompt 本身是 bug，需修 prompt 而非信任 verdict（出处：https://developertoolkit.ai/en/workflows/automate/orchestration-patterns/）。

## 5. 落地检查单（最小可行红队）

- [ ] maker 弱模型 + checker 强模型（降本 40–60%）
- [ ] checker 只读权限、fresh context、不共享 writer 上下文
- [ ] 阶段交接工件可对 schema/acceptance 命令校验
- [ ] 五维攻击清单逐项过，finding 必附 file+line+演示命令+输出
- [ ] 确定性检查全绿后才进入 LLM judge，judge 只评残余面
- [ ] 修复循环硬上限 2–3 轮，超限升级人审
- [ ] 定期审计 judge verdict vs CI 一致性
