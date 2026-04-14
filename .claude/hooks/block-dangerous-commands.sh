#!/bin/bash
# PreToolUse hook: Block dangerous Bash commands
# Exit 2 = block action, stderr shown to Claude

INPUT=$(cat)
CMD=$(echo "$INPUT" | python -c "import sys,json; data=json.load(sys.stdin); print(data.get('tool_input',{}).get('command',''))" 2>/dev/null)

if [ -z "$CMD" ]; then
  exit 0
fi

# Block git push --force
if echo "$CMD" | grep -qE 'git\s+push\s+(-f|--force)'; then
  echo "BLOCKED: git push --force is not allowed" >&2
  exit 2
fi

# Block git reset --hard
if echo "$CMD" | grep -qE 'git\s+reset\s+--hard'; then
  echo "BLOCKED: git reset --hard is not allowed" >&2
  exit 2
fi

# Block rm -rf /
if echo "$CMD" | grep -qE 'rm\s+-rf\s+/'; then
  echo "BLOCKED: rm -rf / is not allowed" >&2
  exit 2
fi

# Block DROP TABLE
if echo "$CMD" | grep -qiE 'DROP\s+TABLE'; then
  echo "BLOCKED: DROP TABLE is not allowed" >&2
  exit 2
fi

exit 0