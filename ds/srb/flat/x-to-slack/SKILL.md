---
name: x-to-slack
description: "Use when Fetches tweet content from X/Twitter via FxTwitter API, performs web research, and posts structured intelligence to Slack in a 3-message thread. Use: covers slack, 분석, 검색, fxtwitter, fetches"
metadata:
  holon-triggers: |
    tweet to slack
    share this tweet
---

---
name: x-to-slack
description: >-
  Fetches tweet content from X/Twitter via FxTwitter API, performs web
  research, and posts structured intelligence to Slack in a 3-message thread.
  Use when user shares an X/Twitter link (x.com or twitter.com URL) and wants to
  analyze it for Slack posting, or says "tweet to slack", "share this tweet",
  "x-to-slack". Do NOT use for general Slack messaging, channel management, or
  non-Twitter content sharing. Korean triggers: "분석", "검색", "리서치", "API".
metadata:
  author: "thaki"
  version: "1.1.0"
  category: "execution"
---
# X-to-Slack: Tweet Intelligence Pipeline

> **Note**: This is the project-level Twitter-only handler (v1.1.0). The canonical universal handler supporting Twitter, GitHub, YouTube (with Defuddle transcript), and articles is at `~/.cursor/skills/x-to-slack/SKILL.md` (v2.2.0). Use the user-level version for non-Twitter URLs.

Process an X (Twitter) URL, gather context through web research, and post a structured 3-message thread to a specified Slack channel.

## Input

The user provides:
1. **X URL** -- e.g. `https://x.com/user/status/1234567890`
2. **Slack channel name** -- e.g. `#general` or `general`

## Workflow

### Step 1: Fetch Tweet via FxTwitter API

Convert the URL by replacing `x.com` or `twitter.com` with `api.fxtwitter.com`. Use `WebFetch` to retrieve the JSON.

For response schema, field extraction details, and error codes, see [references/fxtwitter-api.md](references/fxtwitter-api.md).

Extract: `tweet.text`, `tweet.author.name`, `tweet.author.screen_name`, `tweet.likes`, `tweet.retweets`, `tweet.views`, `tweet.url`, `tweet.quote`, `tweet.media`.

If `code` is not `200`, inform the user of the error and do not proceed.

### Step 2: Additional Web Research

Based on the tweet content:
1. Identify 2-3 key topics, technologies, or entities mentioned.
2. Run `WebSearch` for each to gather background, recent developments, and implications.
3. Collect relevant findings for the summary.

### Step 3:
