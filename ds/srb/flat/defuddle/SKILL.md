---
name: defuddle
description: "Use when Extract clean markdown content from any web page URL or YouTube video transcript using the Defuddle API. For web pages, strips ads, sidebars: covers defuddle, 검색, 데이터, ads, chapter"
metadata:
  holon-triggers: |
    read this page
    extract content from URL
---

---
name: defuddle
description: >-
  Extract clean markdown content from any web page URL or YouTube video
  transcript using the Defuddle API. For web pages: strips ads, sidebars,
  navigation, and UI noise, returning markdown with YAML frontmatter. For
  YouTube URLs: returns full transcripts with timestamps, chapter markers,
  and speaker diarization. Use when the user asks to "read this page",
  "extract content from URL", "get markdown from website", "clean up this
  webpage", "get YouTube transcript", "extract video transcript", "defuddle",
  or when feeding web/video content to an LLM with minimal noise. Do NOT use
  for general web search (use WebSearch), API endpoint calls, browser
  automation (use agent-browser), or fetching structured JSON data from APIs.
  Do NOT use for local audio/video files or Instagram/TikTok transcription
  (use transcribee). Korean triggers: "검색", "데이터", "API", "자동화",
  "트랜스크립트", "유튜브 자막".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# Defuddle — Web Page & YouTube Transcript to Clean Markdown

Extract the main content from any web page or YouTube video as clean markdown via the Defuddle API. For web pages, strips ads, sidebars, headers, footers, and navigation clutter. For YouTube videos, returns full transcripts with timestamps, chapters, and speaker diarization.

## Input

The user provides one or more URLs to extract content from.

## Workflow

### Step 1: Extract Content

Run via Shell:

```bash
curl -s "https://defuddle.md/{url_without_protocol}"
```

**CRITICAL**: The URL must omit the protocol prefix (`https://` or `http://`). Examples:

```bash
# Correct
curl -s "https://defuddle.md/example.com/article"

# Incorrect — do not include protocol
curl -s "https://defuddle.md/https://example.com/article"
```

The response is markdown with YAML frontmatter:

```markdown
---
title: "Article Title"
author: "Author Name"
published: 2025-10-20T00:00:00+00:00
source: "https://example.com/article"
domain
