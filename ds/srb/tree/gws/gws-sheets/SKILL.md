---
name: gws-sheets
description: "Use when Manage Google Sheets via the gws CLI -- read cell ranges, append rows, and create spreadsheets. Use when the user asks to read spreadsheet data: covers gws, sheets, 구글 시트, 스프레드시트, disk"
metadata:
  holon-triggers: |
    read spreadsheet data
    write to sheets
---

---
name: gws-sheets
description: >-
  Manage Google Sheets via the gws CLI -- read cell ranges, append rows, and
  create spreadsheets. Use when the user asks to read spreadsheet data, write to
  sheets, append rows, or create new spreadsheets. Do NOT use for Google Docs
  (use gws-docs), Drive file management (use gws-drive), or CSV files on disk
  (handle locally). Korean triggers: "구글 시트", "스프레드시트".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Google Sheets

> **Prerequisites**: `gws` must be installed and authenticated. See `gws-workspace` skill.

```bash
gws sheets <resource> <method> [flags]
```

## Quick Commands

### Read Values

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--spreadsheet` | Yes | Spreadsheet ID |
| `--range` | Yes | Range (e.g. `'Sheet1!A1:D10'`) |

Read-only -- never modifies the spreadsheet.

### Append Rows

```bash
gws sheets +append --spreadsheet <ID> --values 'Alice,100,true'
gws sheets +append --spreadsheet <ID> --json-values '[["a","b"],["c","d"]]'
```

| Flag | Required | Description |
|------|----------|-------------|
| `--spreadsheet` | Yes | Spreadsheet ID |
| `--values` | One of | Comma-separated values (single row) |
| `--json-values` | One of | JSON array of rows (bulk insert) |

> **Write command** -- confirm with the user before executing.

## Shell Escaping

Sheets ranges use `!` which bash interprets as history expansion. Always wrap in **single quotes**:

```bash
gws sheets spreadsheets values get \
  --params '{"spreadsheetId": "ID", "range": "Sheet1!A1:C10"}'
```

## Raw API Resources

### spreadsheets

- `batchUpdate`, `create`, `get`, `getByDataFilter`
- `developerMetadata` -- get, search
- `sheets` -- copyTo
- `values` -- append, batchClear, batchGet, batchGetByDataFilter, batchUpdate, batchUpdateByDataFilter, clear, get, update

## Discovering Commands

```bash
gws she
