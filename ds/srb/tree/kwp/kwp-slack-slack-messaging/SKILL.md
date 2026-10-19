---
name: kwp-slack-slack-messaging
description: "Use when Guidance for composing well-formatted, effective Slack messages using mrkdwn syntax. Do NOT use for tasks outside the slack domain.: covers kwp, slack, messaging, composing, mrkdwn"
---

---
name: kwp-slack-slack-messaging
description: >-
  Guidance for composing well-formatted, effective Slack messages using mrkdwn
  syntax. Do NOT use for tasks outside the slack domain.
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Slack Messaging Best Practices

This skill provides guidance for composing well-formatted, effective Slack messages.

## Slack Formatting (mrkdwn)

Slack uses its own markup syntax called **mrkdwn**, which differs from standard Markdown. Always use mrkdwn when composing Slack messages:

| Format | Syntax | Notes |
|--------|--------|-------|
| Bold | `*text*` | Single asterisks, NOT double |
| Italic | `_text_` | Underscores |
| Strikethrough | `~text~` | Tildes |
| Code (inline) | `` `code` `` | Backticks |
| Code block | `` ```code``` `` | Triple backticks |
| Quote | `> text` | Angle bracket |
| Link | `<url\|display text>` | Pipe-separated in angle brackets |
| User mention | `<@U123456>` | User ID in angle brackets |
| Channel mention | `<#C123456>` | Channel ID in angle brackets |
| Bulleted list | `- item` or `• item` | Dash or bullet character |
| Numbered list | `1. item` | Number followed by period |

### Common Mistakes to Avoid

- Do NOT use `**bold**` (double asterisks) — Slack uses `*bold*` (single asterisks)
- Do NOT use `## headers` — Slack does not support Markdown headers. Use `*bold text*` on its own line instead.
- Do NOT use `[text](url)` for links — Slack uses `<url|text>` format
- Do NOT use `---` for horizontal rules — Slack does not render these

## Message Structure Guidelines

- **Lead with the point.** Put the most important information in the first line. Many people read Slack on mobile or in notifications where only the first line shows.
- **Keep it short.** Aim for 1-3 short paragraphs. If the message is long, consider using a Canvas instead.
- **Use line breaks generously.** Walls of text are hard to read. Separate distinct thoughts with blank lines.
- **Use bullet po
