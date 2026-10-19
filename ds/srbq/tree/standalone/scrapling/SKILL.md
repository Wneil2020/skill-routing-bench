---
name: scrapling
description: "Use when Write Python web scraping scripts using the Scrapling framework — adaptive parsing, anti-bot bypass (Cloudflare Turnstile), concurrent: covers scrapling, 웹 스크래핑, 크롤링, adaptive, bypass"
metadata:
  holon-triggers: |
    scrape a website
    bypass cloudflare
---

---
name: scrapling
description: >-
  Write Python web scraping scripts using the Scrapling framework — adaptive
  parsing, anti-bot bypass (Cloudflare Turnstile), concurrent spiders, and
  stealth fetching. Use when the user asks to "scrape a website", "bypass
  cloudflare", "crawl pages", "adaptive scraping", "stealth scraping", "anti-bot
  scraping", "web spider", "scrapling", "extract data from website with Python",
  or any Python-based web scraping task that benefits from TLS fingerprint
  impersonation, browser automation, or large-scale crawling. Do NOT use for
  interactive browser automation via CLI (use agent-browser), simple
  URL-to-markdown extraction (use defuddle or WebFetch), or Playwright E2E test
  suites (use e2e-testing). Korean triggers: "웹 스크래핑", "크롤링", "데이터 추출".
metadata:
  author: "thaki"
  version: "1.0.0"
  category: "execution"
---
# Scrapling — Adaptive Web Scraping Framework

Write Python scripts that scrape websites using [Scrapling](https://github.com/D4Vinci/Scrapling) (v0.4.1). Handles anti-bot bypass, adaptive element relocation, and concurrent crawling.

## Prerequisites

```bash
# Parser only (no browser)
pip install scrapling

# With fetchers (HTTP + browser automation)
pip install "scrapling[fetchers]"
scrapling install  # install browser binaries

# With MCP server
pip install "scrapling[ai]"

# Everything
pip install "scrapling[all]"
scrapling install
```

## Fetcher Decision Tree

Pick the right fetcher for the task:

| Need | Fetcher | Why |
|------|---------|-----|
| Fast HTTP, no JS rendering | `Fetcher` | curl_cffi with TLS fingerprint impersonation |
| JS-rendered pages (SPA, dynamic) | `DynamicFetcher` | Playwright Chromium, full DOM |
| Cloudflare / anti-bot protected | `StealthyFetcher` | Fingerprint spoofing + Turnstile solver |
| Multiple requests, keep cookies | `*Session` variant | Persistent cookies and state |
| Large-scale crawl (many pages) | `Spider` | Concurrent requests, pause/resume, export |

## Quick-St
