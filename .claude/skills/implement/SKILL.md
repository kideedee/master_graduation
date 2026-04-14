---
name: implement
description: >
  Quick shortcut to invoke the thesis-writer agent.
  Use when user says "/implement" to write LaTeX from a confirmed plan.
  Example: "/implement plans/c3_method_plan.md"
---

# /implement — Invoke Thesis Writer

Delegate directly to the `thesis-writer` agent.

## Usage

```
/implement [plan file path]
```

## Behavior

1. If a plan file path is provided, pass it to the `thesis-writer` agent:
   > "Use the thesis-writer agent to write content from the plan [path]"

2. If no path is provided, look for the most recent plan in `plans/` and confirm with the user.

3. The agent will:
   - Read the plan, terminology, and existing chapter content
   - Write LaTeX directly into the target chapter file
   - Verify citations inline

4. After writing is complete, suggest: "Run `/verify` to check the new content."

## Prerequisites

A confirmed plan must exist in `plans/`. If not, suggest: "Run `/plan` first to create a writing plan."