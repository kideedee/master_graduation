#!/bin/bash
# PostToolUse hook: Check citation keys after .tex file edits
# Exit 1 = warning (non-blocking), stderr shown to Claude
# Exit 0 = all good

# Check if FILE_PATH is set and is a .tex file
if [ -z "$FILE_PATH" ]; then
  exit 0
fi

if [[ "$FILE_PATH" != *.tex ]]; then
  exit 0
fi

# Check if the file exists
if [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# Find references.bib relative to project dir
BIB_FILE="${CLAUDE_PROJECT_DIR:-$(pwd)}/references.bib"
if [ ! -f "$BIB_FILE" ]; then
  exit 0
fi

# Extract citation keys from the edited file
CITE_KEYS=$(grep -oP '\\cite[tp]?\{[^}]+\}' "$FILE_PATH" 2>/dev/null | grep -oP '\{[^}]+\}' | tr ',' '\n' | sed 's/[{}]//g;s/^ *//;s/ *$//' | sort -u)

if [ -z "$CITE_KEYS" ]; then
  exit 0
fi

MISSING=""
while IFS= read -r key; do
  if [ -n "$key" ] && ! grep -q "$key" "$BIB_FILE" 2>/dev/null; then
    MISSING="${MISSING}  - ${key}\n"
  fi
done <<< "$CITE_KEYS"

if [ -n "$MISSING" ]; then
  echo "WARNING: Missing citation keys in references.bib:" >&2
  echo -e "$MISSING" >&2
  echo "Run: grep -c \"KEY\" references.bib to verify" >&2
  exit 1
fi

exit 0