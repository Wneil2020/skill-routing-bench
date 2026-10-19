# 成本与选型：token 倍数、模型搭配、何时不该用多代理

> 面向落地操作的成本决策参考。所有数字均给出出处；标注 [推断] 者为基于出处的工程估算，非原文结论。

## 1. token 消耗倍数实证

- **Anthropic 实测锚点**：agent 交互约消耗普通 chat 的 **4×** token；多代理系统约消耗 **15×** chat（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。[推断] 可把 15× 当作多代理方案的典型成本锚点/上限假设，用于预算估算。
- **性能主要来自 token 投入**：BrowseComp 上 token 用量单独解释 **80%** 的性能方差（其余为 tool call 次数与模型选择）。先扩 token 预算再谈架构（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- **模型代际是更大的效率乘数**：升级到 Claude Sonnet 4 的收益 > 在 Sonnet 3.7 上翻倍 token 预算（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

AdaptOrch 同模型实测（SWE-bench，每实例 token 数；出处：https://arxiv.org/html/2602.16873v1）：

| 方案 | tokens/实例 | 相对单模型 |
|---|---|---|
| Single Best | 12.3K | 1× |
| AdaptOrch（自适应路由） | 41.8K | **3.4×** |
| Static-Sequential | 48.9K | 4.0× |
| Static-Parallel | 52.1K | 4.2× |
| LLM-Blender | 61.7K | 5.0× |
| MoA-3L | 84.6K | 6.9× |

GPQA：4.1K → 15.9K（3.9×）；HotpotQA：6.8K → 22.7K（3.3×）（同上出处）。

- 结论：多代理的**合理下限约为单代理 3–4×**；固定拓扑、不加路由的朴素多代理 4–7×；自适应路由把开销压回下限附近且仍提升精度（出处：https://arxiv.org/html/2602.16873v1）。
- [推断] 估算公式：`总 token ≈ 子代理数 × 平均子任务开销 + 编排/合成开销`。若预算低于 3× 单代理成本，基本无法获得多代理增益。

## 2. AdaptOrch：拓扑错配与自适应路由收益

- **错配反例**：GPQA 上全并行 Static-Parallel 精度 44.1，**低于** Single Best 的 46.2——拓扑错配会主动伤害性能，多代理不是免费午餐（出处：https://arxiv.org/html/2602.16873v1）。
- **编排无收益场景**：原子单步任务（|V|=1）或纯顺序依赖（γ≈1.0）；GPQA 的 single-concept recall 类实例上 AdaptOrch 仅追平 Single Best。编排增益 ∝ 任务可分解性（出处同上）。
- **耦合阈值**：θγ>0.8 会让紧耦合子任务被并行执行导致一致性失败；θγ<0.3 会把可并行任务强行串行。最优 [0.55, 0.65]，鲁棒 [0.5, 0.7]（出处同上）。
- **Topology Routing 规则**（O(|V|+|E|)）：|E|=0 → Parallel；ω=1 → Sequential；γ>θγ 且 |V|>5 → Hierarchical；宽且低耦合 → Parallel；否则 Hybrid。实际分布：Hybrid 49.7%、Hierarchical 19%、Parallel 16.7%、Sequential 14.7%（出处同上）。
- **领域差异**：编码任务并行宽度高（ω≈3.4），62% 路由 Hybrid；推理任务耦合高（γ≈0.55），41% Sequential + 35% Hierarchical；RAG 多跳问答 71% Hybrid（出处同上）。
- 收敛时代（ϵ≈0.03–0.05）**拓扑选择的性能方差超过模型选择方差 ≥20×**（编码任务）——"怎么编排"比"选哪个模型"更影响结果（出处同上）。
- Self-MoA：单一顶级模型多次自查询比多模型混合在 AlpacaEval 2.0 高 6.6%，"模型多样性必然有益"不成立（出处同上）。

## 3. 强模型编排 + 弱模型执行

- Anthropic Research 系统：Opus 4 lead + Sonnet 4 subagent，内部评测比单 agent Opus 4 **高 90.2%**——强模型留在编排/合成位，执行位用便宜模型（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。
- [推断] Anthropic 与 AdaptOrch 均未给出"强编排+弱执行"相对"全强模型"的成本百分比。若执行 token 占总量 70–90%，执行位用 Haiku 级（$0.80/1M in，[推断，2026-10 价格口径]）替代 Opus 级（$15/1M in，[推断，2026-10 价格口径]），总成本可降约 60–85%。落地形态：routing——简单问题到 Haiku 4.5、难题到 Sonnet 4.5（出处：https://www.anthropic.com/engineering/building-effective-agents）。
- AdaptOrch 用五个 ϵ-收敛便宜模型（GPT-4o-mini、Claude 3.5 Haiku、Gemini 2.0 Flash、Llama 3.3 70B、Qwen 2.5 72B）即达 SWE-bench 52.6，超越同预算 Self-MoA 51.5——能力收敛后，弱模型+正确拓扑可逼近强模型（出处：https://arxiv.org/html/2602.16873v1）。
- 但模型质量仍是效率乘数：不能把"弱模型+多代理"当"强模型+单代理"的等价替代（出处：https://www.anthropic.com/engineering/multi-agent-research-system）。

## 4. 「何时不该用多代理」判断清单

逐条打勾，任一命中即退回更简方案：

- [ ] 任务拆不出 |V|≥2 且边不稠密的 DAG（原子单问、单概念回忆）→ 单代理（出处：https://arxiv.org/html/2602.16873v1）
- [ ] 拆分后 ω=1 或 γ≈1（纯链式依赖）→ 顺序 workflow 或单代理即可（出处同上）
- [ ] 没有廉价的确定性验证器（测试/检查器/引用比对）兜底 → 长链路多代理会累积错误且无从收敛（出处：https://www.anthropic.com/engineering/building-effective-agents）
- [ ] 任务价值不足以支付 ~15× chat 的 token 溢价 → 低价值高频任务用 routing 到小模型或单调用解决（出处：https://www.anthropic.com/engineering/multi-agent-research-system）
- [ ] 所有 agent 必须共享同一上下文，或 agent 间依赖很重 → 不适合多代理（编码任务可并行部分少于研究类任务，实时协调委派是 LLM 弱项）（出处同上）
- [ ] 保守基线：先单 prompt + retrieval/in-context examples → 不行再加 workflow → 仅当子任务不可预先确定（如编码改动范围）才上 orchestrator-workers 或全自主 agent（出处：https://www.anthropic.com/engineering/building-effective-agents）
- [ ] 尽早评估：~20 条真实查询的小样本评测即可发现大效应改动，不必等大规模 eval（出处：https://www.anthropic.com/engineering/multi-agent-research-system）

## 5. 成本估算公式与速算表

公式（[推断]，基于 §1 倍数）：

```
多代理总成本 ≈ (子代理数 × 子任务token × 执行模型单价) + (编排token × 强模型单价)
下限校验：总token ≥ 3 × 单代理token，否则预期无增益
```

速算（以单代理 chat = 1 单位成本计；倍数来源见 §1）：

| 方案 | 成本倍数 | 适用 |
|---|---|---|
| 单调用 / routing 小模型 | ~0.05–1× | 原子任务、低价值高频查询 |
| 单 agent（workflow） | ~4× chat | 可验证、中等复杂度 |
| 自适应路由多代理（AdaptOrch 式） | ~3–4× 单代理 | 任务可分解、耦合度可测 |
| 静态拓扑多代理 | 4–7× 单代理 | 仅在无法测任务特征时 |
| 全自主多代理（上限假设） | ~15× chat | 高价值开放任务（Research 类） |

经济性门槛：预期增益 < 成本增幅 → 退回单调用 + routing；复杂度只在实测改善结果时才增加（出处：https://www.anthropic.com/engineering/building-effective-agents）。
