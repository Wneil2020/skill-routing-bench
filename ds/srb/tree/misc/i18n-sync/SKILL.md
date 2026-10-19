---
name: i18n-sync
description: "Use when Synchronize translation keys across all locale files (en, ko, ja, zh-CN), detect missing or extra keys, generate translation drafts via LLM, and: covers i18n, sync, 동기화, 감사, locale"
metadata:
  holon-triggers: |
    check translations
    sync i18n keys
---

---
name: i18n-sync
description: >-
  Synchronize translation keys across all locale files (en, ko, ja, zh-CN),
  detect missing or extra keys, generate translation drafts via LLM, and
  sort/deduplicate keys. Use when the user asks to check translations, sync i18n
  keys, add new translated strings, or audit locale files. Do NOT use for
  frontend component review (use frontend-expert) or general documentation
  writing (use technical-writer). Korean triggers: "동기화", "감사", "리뷰", "생성".
metadata:
  version: "1.0.0"
  category: "execution"
  author: "thaki"
---
# i18n Sync Manager

Manages translation synchronization across 4 locales in `frontend/src/i18n/locales/`.

## When to Use

- After adding new UI strings to the frontend
- Before releases to ensure all locales are complete
- When the user asks to "add translations" or "check i18n"
- As part of the `/i18n-check` workflow (called by mission-control)

## Locale Files

| Locale | File | Role |
|--------|------|------|
| English | `frontend/src/i18n/locales/en.json` | **Source of truth** |
| Korean | `frontend/src/i18n/locales/ko.json` | Translation |
| Japanese | `frontend/src/i18n/locales/ja.json` | Translation |
| Chinese (Simplified) | `frontend/src/i18n/locales/zh-CN.json` | Translation |

English (`en.json`) is the canonical reference. All other locales must have the same key structure.

## Execution Steps

### Step 1: Load and Parse All Locale Files

Read all 4 JSON files. Parse into nested key maps.

Flatten nested keys using dot notation for comparison:

```
{ "nav": { "dashboard": "Dashboard" } }
→ "nav.dashboard" = "Dashboard"
```

### Step 2: Detect Key Mismatches

Compare each locale against `en.json`:

1. **Missing keys**: Keys in `en.json` but not in target locale
2. **Extra keys**: Keys in target locale but not in `en.json` (possibly deprecated)
3. **Empty values**: Keys present but with empty string `""`
4. **Untranslated values**: Values identical to English (possible copy-paste)

### Step 3: Gener
