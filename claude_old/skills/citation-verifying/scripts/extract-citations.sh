#!/bin/bash
# Extract all citation keys from .tex files and check against references.bib
# Usage: bash extract-citations.sh <tex_file_or_directory> [references.bib]
#
# Examples:
#   bash extract-citations.sh chapters/c3/chapter_3.tex
#   bash extract-citations.sh chapters/c3/
#   bash extract-citations.sh chapters/ references.bib

TARGET="${1:-.}"
BIB="${2:-references.bib}"

if [ ! -f "$BIB" ]; then
  echo "ERROR: $BIB not found"
  exit 1
fi

# Find .tex files
if [ -d "$TARGET" ]; then
  FILES=$(find "$TARGET" -name "*.tex" -type f)
elif [ -f "$TARGET" ]; then
  FILES="$TARGET"
else
  echo "ERROR: $TARGET not found"
  exit 1
fi

echo "=== Citation Key Report ==="
echo "Bib file: $BIB"
echo "Target: $TARGET"
echo ""

# Extract all keys
ALL_KEYS=$(echo "$FILES" | xargs grep -ohP '\\cite[tp]?\{[^}]+\}' 2>/dev/null \
  | grep -oP '\{[^}]+\}' \
  | tr ',' '\n' \
  | sed 's/[{}]//g; s/^ *//; s/ *$//' \
  | sort -u)

TOTAL=$(echo "$ALL_KEYS" | grep -c .)
FOUND=0
MISSING=0
MISSING_LIST=""

while IFS= read -r key; do
  [ -z "$key" ] && continue
  if grep -q "{${key}," "$BIB" 2>/dev/null; then
    FOUND=$((FOUND + 1))
  else
    MISSING=$((MISSING + 1))
    # Find which file uses this key
    SOURCE=$(echo "$FILES" | xargs grep -l "$key" 2>/dev/null | head -1)
    MISSING_LIST="${MISSING_LIST}  ✗ ${key} (used in: $(basename ${SOURCE:-unknown}))\n"
  fi
done <<< "$ALL_KEYS"

echo "Total unique keys: $TOTAL"
echo "Found in bib:      $FOUND ✓"
echo "Missing from bib:  $MISSING ✗"
echo ""

if [ $MISSING -gt 0 ]; then
  echo "MISSING KEYS:"
  echo -e "$MISSING_LIST"
fi

# Show keys per file
echo ""
echo "=== Keys per file ==="
for f in $FILES; do
  COUNT=$(grep -coP '\\cite[tp]?\{' "$f" 2>/dev/null || echo 0)
  if [ "$COUNT" -gt 0 ]; then
    echo "  $(basename $f): $COUNT citations"
  fi
done
