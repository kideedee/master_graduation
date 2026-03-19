---
name: plan
description: >
  Quick shortcut to invoke the thesis-planner agent.
  Use when user says "/plan" followed by a chapter/section description.
  Example: "/plan c3 phương pháp đề xuất"
---

# /plan — Invoke Thesis Planner

Delegate directly to the `thesis-planner` agent.

## Usage

```
/plan <chapter> <section description>
```

## Behavior

1. Pass the user's arguments to the `thesis-planner` agent:
   > "Use the thesis-planner agent to create a plan for [user's arguments]"

2. The agent will:
   - Read existing content, references, and terminology
   - Create a plan file in `plans/`
   - Present the plan for user confirmation

3. After the plan is confirmed, suggest: "Run `/implement` to write content from this plan."

## If No Arguments Provided

Ask the user which chapter and section they want to plan. Example:
> "Which chapter/section do you want to plan? E.g., `/plan c3 phương pháp đề xuất`"