---
name: redteam-maker-checker
description: "Use when 需要红队或质量对抗评审: covers 红队, redteam, maker-checker, 攻击清单"
metadata:
  holon-triggers: |
    给这个草稿做红队评审，攻击清单有哪些维度
    maker-checker 模式怎么防止红队流于形式
    投票共识阈值是多少 should go to /convergence
---

# redteam-maker-checker：质量对抗评审

1. 验证顺序固定：确定性检查（测试、lint、typecheck、schema 校验）→ 程序化 gate → LLM judge 只评残余面；agent 的 APPROVE 永远不替代 CI。
2. 红队按五维攻击清单找茬：正确性、边界（edge case/错误路径/race/覆盖缺口）、安全、事实（无出处断言）、成本（停止规则）。模板见 `references/redteam-maker-checker.md`。
3. 每条 finding 必须带「file + line + 可运行的演示命令及其输出」级别的具体反例，否则该 finding 无效。
4. checker 与被审者上下文隔离：blind comparison、只读权限、最好跨模型/厂商 decorrelate；maker 可用弱模型、checker 用强模型（省 40–60% 成本）。
5. 修复循环硬上限 2 轮（迭代计数 + APPROVED 双条件退出），耗尽升级人审。
6. fan-in 必须做 coverage accounting + 对每个 finding 第二遍 refutation；「干净报告」不等于「全覆盖」。
7. 定期对比 judge verdict 与 CI 结果一致性，分歧即 judge prompt 缺陷。
8. 三种模式（maker-checker / generator-critic / red-blue team）的区别与防流于形式机制详见 `references/redteam-maker-checker.md`。

<!-- sub-skills -->
<!-- /sub-skills -->
