---
name: kwp-common-room-weekly-prep-brief
description: "Use when Generate a comprehensive weekly briefing for all external calls in the next 7 days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I: covers kwp, common, room, 생성, 계획"
---

---
name: kwp-common-room-weekly-prep-brief
description: >-
  Generate a comprehensive weekly briefing for all external calls in the next 7
  days. Triggers on 'weekly prep brief', 'prepare my week', 'what calls do I
  have this week', 'Monday prep', or any weekly planning request. Do NOT use for
  tasks outside the common-room domain. Korean triggers: "생성", "계획".
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Weekly Prep Brief

Generate a single comprehensive weekly briefing that covers every external customer or prospect call in the next 7 days, with per-meeting account and contact research from Common Room.

## Briefing Process

### Step 1: Get the Week's External Meetings

**Option A — Calendar connected:**
Use the `~~calendar` connector to fetch all meetings scheduled in the next 7 days (or a user-specified range). Filter to keep only external meetings — those with attendees from outside your organization. Discard internal-only meetings, one-on-ones with colleagues, and recurring internal syncs.

Identify for each external meeting:
- Company name
- Meeting date and time
- External attendee names and email addresses

**Option B — No calendar connected:**
Ask the user: "To build your weekly prep brief, I'll need your upcoming external calls. Please list them: company name, date/time, and attendee names."

Accept freeform input and parse it into a structured list before proceeding.

### Step 2: Confirm the Meeting List

Present the identified meetings to the user for confirmation before beginning research:

> "Here are the external calls I found for this week. Let me know if anything's missing or should be excluded:
> - [Company] — [Day], [Time] — [Attendees]
> - ..."

This prevents wasted research on cancelled or incorrect meetings.

### Step 3: Research Each Meeting

For each confirmed external meeting, run in parallel where possible:
1. **Account research** — full account snapshot using the account-research skill
2. **Contac
