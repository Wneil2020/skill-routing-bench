---
name: gws-drive
description: "Use when Manage Google Drive via the gws CLI -- upload, download, search, and share files and folders. Use when the user asks to upload files, list Drive: covers gws, drive, 구글 드라이브, 파일 업로드, folders"
metadata:
  holon-triggers: |
    upload files
    list Drive contents
---

---
name: gws-drive
description: >-
  Manage Google Drive via the gws CLI -- upload, download, search, and share
  files and folders. Use when the user asks to upload files, list Drive
  contents, manage permissions, search Drive, or organize folders. Do NOT use
  for Sheets data (use gws-sheets), Docs content (use gws-docs), or email
  attachments (use gws-gmail). Korean triggers: "구글 드라이브", "파일 업로드", "파일 공유".
metadata:
  author: "googleworkspace/cli (adapted)"
  version: "1.0.0"
  category: "integration"
---
# Google Drive

> **Prerequisites**: `gws` must be installed and authenticated. See `gws-workspace` skill.

```bash
gws drive <resource> <method> [flags]
```

## Quick Commands

### Upload a File

```bash
gws drive +upload <file>
gws drive +upload ./report.pdf --parent FOLDER_ID
gws drive +upload ./data.csv --name 'Sales Data.csv'
```

| Flag | Required | Description |
|------|----------|-------------|
| `<file>` | Yes | Path to file |
| `--parent` | No | Parent folder ID |
| `--name` | No | Target filename (defaults to source name) |

MIME type is detected automatically.

> **Write command** -- confirm with the user before executing.

## Raw API Resources

### files

- `copy`, `create`, `delete`, `emptyTrash`, `export`, `generateIds`, `get`, `list`, `update`
- `download` -- download file content (use `-o` flag)

### permissions

- `create`, `delete`, `get`, `list`, `update`

### comments / replies

- CRUD on file comments and replies

### changes / channels

- `list` changes, `watch` for changes, `stop` watch channels

### drives (shared drives)

- `create`, `delete`, `get`, `hide`, `list`, `unhide`, `update`

### revisions

- `delete`, `get`, `list`, `update`

## Discovering Commands

```bash
gws drive --help
gws schema drive.files.list
gws schema drive.files.create
```

## Common Patterns

**Note**: `--fields` is NOT a standalone flag. Pass `fields` inside `--params` JSON.

```bash
# List files (use fields inside params to protect context window)
gws drive 
