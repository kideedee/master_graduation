# Migration Guide: Restructuring Claude Code cho LaTeX Thesis

## Tổng quan thay đổi

### Trước (cấu trúc cũ)
```
CLAUDE.md                    ← ~250 dòng, chứa mọi thứ
.claude/
├── commands/                ← 6 command files (compile, review, paper2thesis, plagiarism, write-content, terminology)
│   ├── compile.md
│   ├── paper2thesis.md
│   ├── plagiarism.md
│   ├── review.md
│   ├── terminology.md
│   └── write-content.md
└── rules/                   ← 7 rule files (giữ nguyên)
    ├── vietnamese-terms.md
    ├── bibliography.md
    ├── bioinformatics-content.md
    ├── figures-tables.md
    ├── latex-commands.md
    ├── python-code.md
    └── troubleshooting.md
```

### Sau (cấu trúc mới)
```
CLAUDE.md                    ← ~100 dòng, chỉ universal instructions
.claude/
├── skills/                  ← 7 skills (thay thế commands, có thêm progressive disclosure)
│   ├── thesis-writing/
│   │   └── SKILL.md
│   ├── latex-compiling/
│   │   └── SKILL.md
│   ├── citation-verifying/  ← MỚI: skill riêng cho verify citations
│   │   └── SKILL.md
│   ├── thesis-reviewing/
│   │   └── SKILL.md
│   ├── paper-converting/
│   │   └── SKILL.md
│   ├── terminology-managing/
│   │   └── SKILL.md
│   └── plagiarism-checking/
│       └── SKILL.md
├── hooks/                   ← MỚI: auto-check sau mỗi lần edit
│   ├── check-citations.sh
│   └── check-terminology.sh
├── rules/                   ← Giữ nguyên 7 rule files
│   └── (unchanged)
└── settings.json            ← MỚI: hooks + permissions config
```

## Thay đổi chính

### 1. CLAUDE.md giảm từ ~250 → ~100 dòng
**Tại sao:** Theo best practice, CLAUDE.md quá dài khiến Claude bỏ qua instructions.
LLM chỉ follow ~150-200 instructions tốt. Claude Code system prompt đã chiếm ~50.
File dài = mọi instruction đều bị ignore đồng đều.

**Đã di chuyển ra skills:**
- "Mandatory Writing Workflow" (Plan→Write→Verify) → `/thesis-writing`
- "Paper to Thesis Notes" → `/paper-converting`
- Chi tiết chapter content → không cần trong CLAUDE.md

**Đã thêm:**
- Gotchas section (highest-signal content theo best practice)
- Skills index (để Claude biết skill nào available)

### 2. Commands → Skills
**Tại sao:** Skills có progressive disclosure (chỉ load khi cần),
có thể auto-trigger, và hỗ trợ bundled resources (scripts, references).

| Cũ (command) | Mới (skill) |
|---|---|
| `/compile` | `/latex-compiling` |
| `/review` | `/thesis-reviewing` |
| `/paper2thesis` | `/paper-converting` |
| `/plagiarism` | `/plagiarism-checking` |
| `/write-content` | `/thesis-writing` |
| `/terminology` | `/terminology-managing` |
| (không có) | `/citation-verifying` ← MỚI |

### 3. Hooks mới (PostToolUse)
**Tại sao:** Hooks chạy deterministic sau mỗi edit, không phụ thuộc vào
Claude "nhớ" check. Giải quyết 2 lỗi hay gặp nhất.

Hooks được wire vào event `PostToolUse` với matcher `Edit|MultiEdit|Write`.
Khi Claude edit file .tex trong `chapters/`, hooks tự động:
- `check-citations.sh`: grep tất cả `\cite{key}` → báo nếu key không có trong references.bib
- `check-terminology.sh`: phát hiện Vietnamese term drift (8 pattern phổ biến)

**Lưu ý:** Hooks hiện exit 0 (warning only, không block edit). Nếu muốn
block edit khi có lỗi citation, đổi `exit 0` thành `exit 2` trong hook script.

### 4. Citation verification tách thành skill riêng
**Tại sao:** Đây là pain point lớn nhất (sai citation key + sai số liệu).
Skill riêng cho phép gọi độc lập và có workflow chi tiết hơn.

## Cách apply

### Bước 1: Backup
```bash
cp -r .claude .claude.backup
cp CLAUDE.md CLAUDE.md.backup
```

### Bước 2: Thay thế CLAUDE.md
```bash
cp output/CLAUDE.md ./CLAUDE.md
```

### Bước 3: Tạo thư mục skills
```bash
mkdir -p .claude/skills
cp -r output/.claude/skills/* .claude/skills/
```

### Bước 4: Tạo hooks
```bash
mkdir -p .claude/hooks
cp output/.claude/hooks/* .claude/hooks/
chmod +x .claude/hooks/*.sh
```

### Bước 5: Cập nhật settings
```bash
cp output/.claude/settings.json .claude/settings.json
```

### Bước 6: Xóa commands cũ (optional, skills sẽ override)
```bash
# Giữ lại nếu muốn, nhưng skills sẽ được ưu tiên
rm -rf .claude/commands/
```

### Bước 7: Tạo thư mục plans (nếu chưa có)
```bash
mkdir -p plans
```

### Bước 8: Test
```bash
# Mở Claude Code, thử:
# - /thesis-writing c2 background "CNN fundamentals"
# - /citation-verifying chapters/c3/chapter_3.tex
# - /terminology-managing verify
```

## Lưu ý quan trọng

1. **Rules files KHÔNG thay đổi** — chúng đã tốt, giữ nguyên.
2. **Hooks cần chmod +x** — nếu không chạy được, kiểm tra quyền execute.
3. **settings.json** — nếu bạn đã có settings.json riêng, merge thủ công phần hooks.
4. **Gotchas section** — cập nhật thường xuyên khi phát hiện lỗi mới. Đây là phần quan trọng nhất.
5. **Skill descriptions** — nếu skill không auto-trigger đúng, chỉnh description cho "pushy" hơn.

