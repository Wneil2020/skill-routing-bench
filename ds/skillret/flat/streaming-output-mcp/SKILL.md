---
name: "streaming-output-mcp"
description: "Use when the task involves implement data: covers streaming, output, mcp, session, multi-format"
---

# streaming-output-mcp

Stream structured content to persistent SQLite storage with automatic session break recovery. Core principle: The content IS the state. Every stream_write is automatically persistent. Supports multi-format export (Markdown, HTML, JSON, YAML, CSV, Text) and 7 document templates. Commands: /stream-ini
