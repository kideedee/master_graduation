---
name: plan
description: >
  Create a writing plan for thesis chapter sections. Use when user says 
  "/plan", "plan section", "lập kế hoạch viết", or before writing new content.
  Example: "/plan c3 phương pháp đề xuất"
argument-hint: "<chapter> <section>"
context: fork
agent: thesis-planner
allowed-tools: Read, Grep, Glob, Write
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