---
name: roles-permissions
description: "Use when 分配子代理角色与权限: covers 角色, 权限, planner, worker, judge"
metadata:
  holon-triggers: |
    planner worker judge 的角色边界怎么划
    子代理的权限如何按角色最小化
    多代理成本是单代理的几倍 should go to /cost-selection
---

# roles-permissions：角色与权限

1. 划清职责边界：planner 只产计划不写实现；worker 只做分配单元、不碰单元外文件、不改评判自己的测试；redteam 只报告不修改；judge 只读裁决。边界表见 `references/roles-permissions.md`。
2. 上下文隔离：worker 只接收「任务描述 + 输出契约 + 最小必要上下文」，不透传全部历史；产出写文件系统、只回传引用，避免「传话游戏」与 token 重复计费。
3. 文件所有权：每个产出单元有唯一所有者；共享文件仅编排者可写；黑板 key 命名空间化 + append-only。
4. 权限按角色最小化：judge/critic/redteam 只读（edit/bash deny）；worker 写权限限定目录；只读探索 agent 不透出 shell。
5. 给 subagent 的任务描述必须含目标、输出格式、工具/来源指导、任务边界，否则必然重复劳动或留空档。
6. critic gate（失败检测 + 重试同一 worker）是性价比最高的质量投资，应作为默认闭环。
7. 角色→工具权限映射表与出处见 `references/roles-permissions.md`；OpenCode 具体配置语法见 /opencode-setup。

<!-- sub-skills -->
<!-- /sub-skills -->
