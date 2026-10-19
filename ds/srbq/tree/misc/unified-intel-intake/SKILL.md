---
name: unified-intel-intake
description: "Use when Single entry point for all intelligence sources — news articles, academic papers, tweets, blog posts, and RSS feeds. Auto-classifies content: covers unified, intel, intake, entry, tweets"
metadata:
  holon-triggers: |
    process this link
    classify and route content
---

---
name: unified-intel-intake
description: >-
  Single entry point for all intelligence sources — news articles, academic
  papers, tweets, blog posts, and RSS feeds. Auto-classifies content type
  and topic, routes to the appropriate processing skill, and posts to the
  correct Slack channel. Use when the user asks to "process this link",
  "classify and route content", "unified intel", "인텔 파이프라인",
  "통합 인텔리전스", "unified-intel-intake", or wants a single pipeline for
  all external information sources. Do NOT use for processing a single tweet
  (use x-to-slack), Bespin news only (use bespin-news-digest), or paper
  review (use paper-review directly).
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# Unified Intel Intake

Single pipeline that accepts any URL or content source, classifies it, routes to the appropriate processing skill, and delivers to the right Slack channel.

## When to Use

- As part of the daily Intel track in the SOD-to-EOD pipeline
- When processing a batch of mixed URLs (news, papers, tweets)
- When setting up RSS feed monitoring for automatic intake

## Content Type Detection

| Pattern | Type | Processing Skill |
|---------|------|-----------------|
| `arxiv.org`, `*.pdf` (academic) | Paper | `paper-review` or `alphaxiv-paper-lookup` |
| `x.com`, `twitter.com` | Tweet | `x-to-slack` |
| `huggingface.co/papers` | HF Paper | `hf-trending-intelligence` |
| `github.com` (repo/release) | GitHub | `defuddle` + LLM summary |
| `youtube.com`, `youtu.be` | Video | `defuddle` (transcript extraction) + LLM analysis |
| News domains (techcrunch.com, theverge.com, arstechnica.com, wired.com, reuters.com, bloomberg.com, venturebeat.com, zdnet.com, theregister.com, semafor.com), RSS items from news feeds | News Article | `defuddle` + LLM analysis |
| medium.com, substack.com, dev.to, hashnode.dev, personal domains with blog-like URL paths (`/posts/`, `/blog/`, `/articles/`) | Blog | `defuddle` + LLM analysis |
| Unknown domain — e
