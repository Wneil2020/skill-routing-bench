---
name: failure-modes
description: "Use when 多代理系统出问题需要排障: covers 失败模式, 排障, 死循环, 上下文膨胀, 开销失控"
metadata:
  holon-triggers: |
    多代理系统死循环了怎么排障
    上下文膨胀这类失败模式怎么排查
    怎么选多代理拓扑 should go to /topologies
---

# failure-modes：失败模式与排障

1. 出问题先查组织与流程（角色规范 > 交接校验 > 真实验证环节），而非先换更强模型。
2. 按症状定位到 7 大失败模式之一，每种的症状/根因/排查步骤/预防见 `references/failure-modes.md`：
   - 上下文膨胀 → 产物落盘只回传引用
   - 错误级联 → inter-agent 边界结构化校验，畸形输出 fail loudly
   - herding/过早共识 → 匿名化 + 隐藏票数（见 /convergence）
   - 死循环/goal drift → 一切循环硬上限 + stopping conditions
   - 文件冲突/race condition → 一个 path 只归一个 unit，共享文件串行先落
   - 成本失控 → scaling rules + 预算上限（见 /cost-selection）
   - judge 被 maker 污染 → 只读、blind、verdict 必带命令与 exit code（见 /redteam-maker-checker）
3. 所有循环设硬上限（max_turns / 修复 2 轮后升人工 / 重规划 ≤3 次）。
4. 用 `references/failure-modes.md` 末尾的 12 项 troubleshooting checklist 逐条打勾排查。
5. 预防优于排障：每个 inter-agent 边界做 schema/验收命令校验；fan-in 做覆盖率对账；合并后跑全量集成检查。

<!-- sub-skills -->
<!-- /sub-skills -->
