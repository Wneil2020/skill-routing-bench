---
name: gws
description: "Use when the request concerns the gws category of skills: covers gws"
---

Grouping node for the 0 skills of the gws category. 

<!-- sub-skills -->
## Sub-skills (auto-generated, do not edit by hand)

- **gws-calendar** (`gws-calendar/`): Use when Manage Google Calendar via the gws CLI -- view agenda, create events, check availability, and manage invitations. Use when the user asks to check: covers gws, calendar, 캘린더, 일정, automatic
- **gws-chat** (`gws-chat/`): Use when Manage Google Chat via the gws CLI -- send messages, list spaces, and manage chat conversations. Use when the user asks to send a Google Chat message: covers gws, chat, 구글 챗, 챗 메시지, sms
- **gws-docs** (`gws-docs/`): Use when Manage Google Docs via the gws CLI -- create documents, append text, and read content. Use when the user asks to create a Google Doc, write to a: covers gws, docs, 구글 문서, 문서 작성, append
- **gws-drive** (`gws-drive/`): Use when Manage Google Drive via the gws CLI -- upload, download, search, and share files and folders. Use when the user asks to upload files, list Drive: covers gws, drive, 구글 드라이브, 파일 업로드, folders
- **gws-email-reply** (`gws-email-reply/`): Use when Compose and send email replies via Google Workspace CLI with AI-drafted responses, knowledge-based context retrieval, brand voice enforcement: covers gws, email, reply, continuation, han
- **gws-gmail** (`gws-gmail/`): Use when Manage Gmail via the gws CLI -- send emails, triage inbox, watch for new messages, manage labels and filters. Use when the user asks to send email: covers gws, gmail, 이메일, 메일 보내기, invites
- **gws-recipe-audit-sharing** (`gws-recipe-audit-sharing/`): Use when Find and review Google Drive files shared outside the organization, with option to revoke external access. Use when the user asks to audit external: covers gws, recipe, audit, 외부 공유, 권한 감사
- **gws-recipe-doc-from-template** (`gws-recipe-doc-from-template/`): Use when Copy a Google Docs template, fill in content, and share with collaborators. Use when the user asks to create a document from a template, duplicate a: covers gws, recipe, doc, 템플릿 문서, 문서 복사
- **gws-recipe-events-from-sheet** (`gws-recipe-events-from-sheet/`): Use when Read event data from a Google Sheets spreadsheet and create Google Calendar entries for each row. Use when the user asks to bulk-create: covers gws, recipe, events, 일정 일괄 생성, 시트에서 일정
- **gws-recipe-personalized-emails** (`gws-recipe-personalized-emails/`): Use when Read recipient data from Google Sheets and send personalized Gmail messages to each row. Use when the user asks to send bulk personalized: covers gws, recipe, personalized, 일괄 이메일, 메일 머지
- **gws-recipe-save-email-to-doc** (`gws-recipe-save-email-to-doc/`): Use when Save a Gmail message body into a Google Doc for archival or reference. Use when the user asks to archive an email to Docs, save email content as a: covers gws, recipe, save, 이메일 보관, 메일 문서화
- **gws-sheets** (`gws-sheets/`): Use when Manage Google Sheets via the gws CLI -- read cell ranges, append rows, and create spreadsheets. Use when the user asks to read spreadsheet data: covers gws, sheets, 구글 시트, 스프레드시트, disk
- **gws-workflows** (`gws-workflows/`): Use when Cross-service Google Workspace productivity workflows via the gws CLI -- daily standup reports, meeting preparation, weekly digests: covers gws, 데일리 스탠드업, 주간 요약, announce, announcements
- **gws-workspace** (`gws-workspace/`): Use when Install, authenticate, and configure the Google Workspace CLI (gws) for controlling Gmail, Drive, Calendar, Sheets, Docs, and Chat from: covers gws, workspace, 구글 워크스페이스, gws 설정, controlling

Routing rule: when the task matches one of the sub-skills above, read the SKILL.md in that subdirectory for detailed instructions before acting;
if that sub-skill lists deeper sub-skills, repeat the descent. Load only the documents on the matching path.
<!-- /sub-skills -->
