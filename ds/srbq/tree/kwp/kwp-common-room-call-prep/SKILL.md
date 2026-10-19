---
name: kwp-common-room-call-prep
description: "Use when Prepare for a customer or prospect call using Common Room signals. Triggers on 'prep me for my call with [company]', 'prepare for a meeting with: covers kwp, common, room, talking, know"
---

---
name: kwp-common-room-call-prep
description: >-
  Prepare for a customer or prospect call using Common Room signals. Triggers
  on 'prep me for my call with [company]', 'prepare for a meeting with
  [company]', 'what should I know before talking to [company]', or any call
  preparation request. Do NOT use for tasks outside the common-room domain.
metadata:
  author: "anthropic-kwp"
  version: "1.0.0"
  category: "workflow"
---
# Call Prep

Produce a complete, scannable call prep brief by combining account research, contact research, and signal synthesis from Common Room.

## Prep Process

### Step 1: Identify the Account and Attendees

Parse what the user has provided:
- **Company name** — required; look up the account in Common Room
- **Attendee names** — optional; if provided, research each one

**Calendar lookup:** If a `~~calendar` connector is available, search for upcoming meetings with the named company to automatically surface attendee names, meeting time, and any meeting notes or agenda. Use this to fill gaps the user didn't provide.

If neither attendees nor a calendar match can be found, ask: "Who will be on the call from [Company]? I can research each attendee to make your prep more useful."

### Step 2: Run Account Research

Use the account-research skill process to build a full account snapshot. For call prep, prioritize:
- Recent product signals (what are they doing in the product right now?)
- Open opportunities or renewal timeline
- Any risk signals (declining usage, support tickets, churned seats)
- Key recent events (funding, executive change, new hire)

When reviewing activity history, prioritize Gong and call recording activities — these provide direct context about previous conversations. Do not filter out call recordings by activity origin.

### Step 3: Run Contact Research for Each Attendee

For each external attendee, use the contact-research skill process. For call prep, focus on:
- Role and influence in the buying process
- Their perso
