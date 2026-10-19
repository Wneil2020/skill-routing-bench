---
name: twitter-timeline-to-slack
description: "Use when Fetch the latest tweets from a Twitter/X user's profile, store locally with deduplication, classify each tweet by topic, and post to the: covers twitter, timeline, slack, 타임라인, 트위터 타임라인"
metadata:
  holon-triggers: |
    fetch tweets from timeline
    post timeline to slack
---

---
name: twitter-timeline-to-slack
description: >-
  Fetch the latest tweets from a Twitter/X user's profile, store locally with
  deduplication, classify each tweet by topic, and post to the appropriate Slack
  channel using the x-to-slack pipeline with rate limiting. Supports batch
  processing and resumable posting. Use when the user asks to "fetch tweets
  from timeline", "post timeline to slack", "twitter timeline", "scrape tweets",
  "twitter-timeline-to-slack", or wants to batch-process a user's tweets to
  Slack. Do NOT use for posting a single tweet URL (use x-to-slack). Do NOT use
  for general Slack messaging (use kwp-slack-slack-messaging). Do NOT use for
  Twitter scraping without Slack posting (use scrapling or agent-browser).
  Korean triggers: "타임라인", "트위터 타임라인", "트윗 일괄", "트윗 스크래핑".
metadata:
  author: "thaki"
  version: "2.1.0"
  category: "execution"
---
# Twitter Timeline to Slack Pipeline

Fetch a user's latest tweets, classify by topic, and post each to the appropriate Slack channel via the x-to-slack skill.

## Input

The user provides:
1. **Twitter screen name** (optional, default: `hjguyhan`) -- e.g. `someuser` or `@someuser`
2. **Options** (optional):
   - `--limit N` -- max tweets to post (default: all unposted)
   - `--dry-run` -- classify without posting
   - `--fetch-only` -- fetch and store only, no posting

When invoked without a screen name (e.g. `/twitter-timeline-to-slack` or "트위터 타임라인 슬랙에 올려줘"), default to `hjguyhan`.

## Prerequisites

- `TWITTER_COOKIE` must be set in `.env` (Twitter session cookie for Syndication API)
- Channel DB must exist at `outputs/twitter/slack-channels.json`

## Workflow

### Phase 0: Cookie Validation

Before fetching tweets, verify that `TWITTER_COOKIE` is set and functional.

#### Step 0a: Check .env

Read the project `.env` file and check if `TWITTER_COOKIE` is present and non-empty.

- If **missing or empty** → jump to Step 0c (Cookie Registration).
- If **present** → proceed to Step 0b.

#### Step 
