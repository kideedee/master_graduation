# Review: Claude Code Configuration cho LaTeX Thesis Project

## Tổng quan đánh giá

Vũ, project của bạn thuộc top thiết lập tốt trong số các Claude Code project tôi thấy — bạn đã áp dụng đúng nhiều best practice: skills với progressive disclosure, agents cho context isolation, rules tách biệt, CLAUDE.md ngắn gọn. Tuy nhiên, có một số vấn đề cần chỉnh để phối hợp tốt hơn và theo kịp cập nhật mới nhất (commands đã merge vào skills từ v2.1.3).

---

## 1. Vấn đề quan trọng nhất: Commands đã merge vào Skills

### Thực tế hiện tại

Từ Claude Code v2.1.3 (khoảng tháng 1/2026), **commands và skills đã được hợp nhất**. `.claude/commands/` vẫn hoạt động (backward compatible) nhưng `.claude/skills/` là canonical path. Nếu cùng tên, skill ưu tiên hơn command.

### Khuyến nghị cho `/plan`, `/implement`, `/verify`

Bạn muốn đưa 3 shortcut này vào `.claude/commands/` — **KHÔNG nên**. Thay vào đó, hãy giữ chúng trong `.claude/skills/` như hiện tại nhưng cải thiện cấu trúc. Lý do:

1. **Skills là hướng đi chính thức** — Anthropic khuyến nghị dùng skills cho mọi thứ mới
2. **Skills hỗ trợ thêm**: supporting files, auto-invocation, subagent execution, frontmatter control
3. **Commands trong `.claude/commands/` là legacy** — vẫn hoạt động nhưng không được khuyến nghị cho project mới

Tuy nhiên, nếu bạn thực sự muốn cả hai path (ví dụ để đảm bảo `/plan` luôn xuất hiện trong `/` menu dù skill auto-trigger có lúc không hoạt động), bạn có thể tạo thin wrapper commands:

```
.claude/commands/plan.md      → chỉ gọi skill plan
.claude/commands/implement.md → chỉ gọi skill implement  
.claude/commands/verify.md    → chỉ gọi skill verify
```

Nhưng theo best practice mới nhất, điều này **không cần thiết** vì skills đã có `user_invocable: true` mặc định.

---

## 2. Đánh giá CLAUDE.md

### ✅ Đã tốt
- Dưới 200 dòng (best practice khuyến nghị < 200)
- Có Gotchas section — đây là phần có **highest signal** theo nhiều nguồn
- Project map rõ ràng
- Critical rules ngắn gọn, actionable
- Skills index giúp Claude biết có gì available

### ⚠️ Cần cải thiện

| Vấn đề | Chi tiết | Đề xuất |
|---------|----------|---------|
| **Agents section quá chi tiết** | Mô tả agent + skill + shortcut lặp lại 3 lần (Skills section, Agent shortcuts, Agents section) | Gom lại thành 1 bảng duy nhất |
| **Rules section dài** | Liệt kê 7 rule files + mô tả — Claude sẽ tự đọc `.claude/rules/` khi cần | Chỉ cần liệt kê tên file, bỏ mô tả chi tiết |
| **Thiếu `@` imports** | Có thể dùng `@document/phabert_cnn.tex` thay vì mô tả dài | Dùng `@` syntax cho reference files |
| **"NEVER run any git commands" nên dùng hook** | Instruction trong CLAUDE.md chỉ ~70% effective. Hook block 100% | Tạo hook chặn git commands |

### Đề xuất CLAUDE.md tối ưu (~80 dòng)

```markdown
# CLAUDE.md

Vietnamese master's thesis: PhaBERT-CNN (DNABERT-2 + CNN) for phage lifestyle prediction.
Author: Vũ Quang Sơn · VNU-UET · Supervisor: Dr. Diep Thi Hoang · 2025

## Commands
pdflatex thesis.tex && bibtex thesis && pdflatex thesis.tex && pdflatex thesis.tex  # Full compile
pdflatex thesis.tex  # Quick compile

## Project Map  
thesis.tex → Entry point | references.bib → Bibliography (single source of truth)
chapters/c1/→c5/ → Chapters | document/phabert_cnn.tex → Ground truth for OUR numbers
plans/ → Writing plans | imgs/ → Figures | snipet/ → Code examples

## IMPORTANT: Critical Rules
1. Vietnamese-first. English ONLY for model names, untranslatable terms. Check .claude/rules/vietnamese-terms.md
2. Every number needs a source. Our results → document/phabert_cnn.tex. Others → verify via WebFetch
3. Every \cite{key} must exist: `grep -c "KEY" references.bib` BEFORE using
4. Every figure/table/equation needs \label{} and \ref{}
5. Full compile after bib changes (4-command sequence above)

## Gotchas — ALWAYS READ BEFORE WRITING
- **Citation key hallucination**: Claude invents keys not in references.bib. ALWAYS grep first.
- **Vietnamese term drift**: Different VN translations across sessions. ALWAYS read vietnamese-terms.md
- **Inaccurate paper claims**: Wrong numbers or wrong attribution. ALWAYS verify against source
- **LaTeX special chars**: Use \_ in text mode. Use \% outside math mode

## LaTeX Config
report, A4, 13pt · L=3cm R=2cm T=2.5cm B=3cm · Line spacing 1.3
Vietnamese: \usepackage[utf8]{vietnam} · Bibliography: natbib, unsrt, numbers, sort&compress

## Skills & Agents (type / to invoke)
| Skill | Trigger | Agent used |
|-------|---------|------------|
| /thesis-writing | Write new content | planner → writer → verifier |
| /plan <ch> <sec> | Create writing plan | thesis-planner |
| /implement <plan> | Write from plan | thesis-writer |
| /verify <file> | Check citations | citation-verifier |
| /latex-compiling | Compile + debug | — |
| /citation-verifying | Full citation check | citation-verifier |
| /thesis-reviewing | Review chapter | — |
| /paper-converting | Paper → thesis | planner → writer → verifier |
| /terminology-managing | Term management | — |
| /plagiarism-checking | Self-plagiarism check | — |

## Rules (.claude/rules/) — auto-loaded when relevant
vietnamese-terms.md · bibliography.md · bioinformatics-content.md
figures-tables.md · latex-commands.md · python-code.md · troubleshooting.md
```

---

## 3. Đánh giá Skills

### ✅ Skills đã tốt

| Skill | Đánh giá |
|-------|----------|
| `thesis-writing` | Orchestrator tốt — Plan→Write→Verify workflow rõ ràng |
| `citation-verifying` | Giải quyết pain point lớn nhất. Script `extract-citations.sh` là progressive disclosure đúng kiểu |
| `latex-compiling` | Đơn giản, đủ dùng |
| `terminology-managing` | Cụ thể, có 3 sub-tasks rõ ràng |

### ⚠️ Skills cần cải thiện

**a) `/plan`, `/implement`, `/verify` — quá mỏng, nên merge hoặc bổ sung**

Ba skill này hiện tại chỉ là thin wrapper (~10 dòng) nói "delegate to agent X". Vấn đề:
- Claude đôi khi không trigger đúng agent vì instruction quá ngắn
- Thiếu `context: fork` — nên chạy planner/verifier trong isolated subagent để không ô nhiễm main context

**Đề xuất:** Bổ sung frontmatter đúng chuẩn và thêm `context: fork` cho plan/verify:

```yaml
# .claude/skills/plan/SKILL.md
---
name: plan
description: >
  Create a writing plan for thesis chapter sections. Use when user says 
  "/plan", "plan section", "lập kế hoạch viết", or before writing new content.
  Example: /plan c3 phương pháp đề xuất
context: fork
agent: thesis-planner
allowed-tools: Read, Grep, Glob, Bash, Write
---
```

```yaml
# .claude/skills/verify/SKILL.md  
---
name: verify
description: >
  Verify citation keys and claims in thesis files. Use when user says
  "/verify", "check citations", "kiểm tra trích dẫn".
  Example: /verify chapters/c3/chapter_3.tex
context: fork
agent: citation-verifier
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch
---
```

```yaml
# .claude/skills/implement/SKILL.md
---
name: implement
description: >
  Write LaTeX thesis content from a confirmed plan. Use when user says
  "/implement", "write from plan", "viết theo kế hoạch".
  Example: /implement plans/c3_method_plan.md
allowed-tools: Read, Grep, Glob, Edit, Write, Bash
agent: thesis-writer
---
```

**Lưu ý quan trọng**: `context: fork` cho plan và verify giúp giữ main context sạch. Implement KHÔNG nên fork vì cần Edit/Write vào chapter files.

**b) `thesis-reviewing` — thiếu Gotchas section**

Skill review 5 dimensions nhưng không có "common mistakes" list. Theo best practice, mọi skill nên có Gotchas section ghi lại các lỗi Claude hay mắc khi dùng skill đó.

**c) `paper-converting` — overlap với `thesis-writing`**

Cả hai đều dùng Plan→Write→Verify workflow. `paper-converting` chỉ thêm "expansion guidelines" table. Đề xuất: merge thành 1 tham số của `thesis-writing`:

```
/thesis-writing c3 method --from-paper
```

Hoặc giữ riêng nhưng thêm `context: fork` cho step Plan.

**d) `plagiarism-checking` — thiếu script thực tế**

Hiện tại skill mô tả quy trình nhưng không có script. Nên thêm script Python/bash đơn giản tính word overlap:

```
.claude/skills/plagiarism-checking/
├── SKILL.md
└── scripts/
    └── check-similarity.py  # So sánh sentence-level overlap
```

---

## 4. Đánh giá Agents

### ✅ Đã tốt
- 3 agent có phân vai rõ: planner (read-only), writer (edit), verifier (web access)
- Model đúng: dùng `sonnet` cho agent — tiết kiệm token
- Memory: `project` — phù hợp cho thesis project

### ⚠️ Cần cải thiện

| Vấn đề | Chi tiết | Đề xuất |
|---------|----------|---------|
| **thesis-planner có Write tool** | Planner nên read-only, chỉ viết vào `plans/`. Hiện có Bash + Write → rủi ro edit chapter files | Loại Bash, chỉ giữ Read, Grep, Glob, Write (và document rằng Write chỉ cho `plans/` folder) |
| **thesis-writer quá nhiều tools** | Có Read, Grep, Glob, Edit, Write, Bash — Bash không cần thiết cho writing | Loại Bash hoặc giới hạn `Bash(grep *)` |
| **Agent descriptions quá dài** | Mỗi agent ~30-40 dòng instruction. LLMs follow ~150-200 instructions total. Agent description nên < 20 dòng core instructions | Tách detail vào supporting files trong agent folder |
| **Thiếu `maxTurns` hợp lý** | thesis-writer có maxTurns=30 — quá nhiều, dễ loop. citation-verifier maxTurns=15 OK | Giảm thesis-writer xuống 20, thesis-planner xuống 15 |

### Đề xuất cấu trúc agent tối ưu

```
.claude/agents/
├── thesis-planner.md     # maxTurns: 15, tools: Read, Grep, Glob, Write
├── thesis-writer.md      # maxTurns: 20, tools: Read, Grep, Glob, Edit, Write
└── citation-verifier.md  # maxTurns: 15, tools: Read, Grep, Glob, WebFetch, WebSearch
```

---

## 5. Thiếu sót quan trọng

### a) KHÔNG có Hooks

Bạn mention hooks trong `readme.md` (migration guide) nhưng thực tế **không có hooks nào** trong `.claude/settings.json` (file rỗng `{}`). Hooks là **deterministic** — chạy 100% mọi lần, không phụ thuộc Claude "nhớ" hay không.

**Đề xuất tạo 2 hooks quan trọng nhất:**

**Hook 1: Chặn git commands** (thay cho rule trong CLAUDE.md)
```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hook": "bash .claude/hooks/block-git.sh"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hook": "bash .claude/hooks/check-citations.sh"
      }
    ]
  }
}
```

**Hook 2: Auto-check citations sau edit .tex files**

Bạn đã có script `extract-citations.sh` — wire nó vào PostToolUse hook. Khi Claude edit bất kỳ file `.tex` nào, hook tự động chạy kiểm tra citation keys.

### b) Thiếu `!` dynamic context injection trong skills

Best practice mới: dùng `!`command`` syntax trong SKILL.md để inject dynamic data. Ví dụ:

```markdown
# In citation-verifying/SKILL.md
## Current citation keys in project
!`grep -rohP '\\cite[tp]?\{[^}]+\}' chapters/*/chapter_*.tex | sort -u | head -50`

## Bibliography keys available  
!`grep -oP '@\w+\{([^,]+)' references.bib | sed 's/@\w\+{//' | sort | head -50`
```

Claude sẽ thấy data thực tế thay vì phải tự chạy grep.

### c) Thiếu validation loop trong thesis-writing skill

Best practice từ Anthropic: skill nên có validation loop. Hiện tại `/thesis-writing` chỉ nói "Fix ALL reported issues" nhưng không có cơ chế cụ thể. Đề xuất thêm:

```markdown
## Validation Loop
After writing, ALWAYS run:
1. `grep -oP '\\cite[tp]?\{[^}]+\}' <file> | sort -u` → check all keys exist
2. `pdflatex thesis.tex` → verify compilable  
3. If errors: fix and re-validate. Do NOT proceed until both pass.
```

---

## 6. Phối hợp giữa Skills và Agents

### Hiện tại: Tốt nhưng có overlap

```
thesis-writing (skill) → orchestrates → thesis-planner (agent)
                                       → thesis-writer (agent)  
                                       → citation-verifier (agent)

plan (skill)       → delegates to → thesis-planner (agent)
implement (skill)  → delegates to → thesis-writer (agent)
verify (skill)     → delegates to → citation-verifier (agent)
```

**Vấn đề**: Có 2 path để gọi cùng 1 agent:
- Path 1: `/thesis-writing` → tự gọi 3 agents tuần tự
- Path 2: `/plan` → `/implement` → `/verify` riêng lẻ

Điều này OK (flexible), nhưng cần đảm bảo CLAUDE.md ghi rõ khi nào dùng path nào.

### Đề xuất

Thêm vào CLAUDE.md:
```markdown
## When to use which workflow
- **Full flow** (`/thesis-writing`): Viết section mới từ đầu — tự chạy Plan→Write→Verify
- **Step-by-step** (`/plan` → `/implement` → `/verify`): Khi muốn review/confirm plan trước khi viết
- **Quick fix** (direct edit): Sửa nhỏ — không cần workflow, chỉ cần grep check citations sau
```

---

## 7. Đề xuất cấu trúc cuối cùng

```
.claude/
├── agents/
│   ├── thesis-planner.md      # Read-only explorer + plan creator
│   ├── thesis-writer.md       # LaTeX writer from plans
│   └── citation-verifier.md   # WebFetch verifier
├── skills/
│   ├── thesis-writing/
│   │   └── SKILL.md           # Orchestrator: Plan→Write→Verify
│   ├── plan/
│   │   └── SKILL.md           # context: fork, agent: thesis-planner
│   ├── implement/
│   │   └── SKILL.md           # agent: thesis-writer
│   ├── verify/
│   │   └── SKILL.md           # context: fork, agent: citation-verifier
│   ├── citation-verifying/
│   │   ├── SKILL.md
│   │   └── scripts/
│   │       └── extract-citations.sh
│   ├── latex-compiling/
│   │   └── SKILL.md
│   ├── thesis-reviewing/
│   │   └── SKILL.md
│   ├── paper-converting/       # Xem xét merge vào thesis-writing
│   │   └── SKILL.md
│   ├── terminology-managing/
│   │   └── SKILL.md
│   └── plagiarism-checking/
│       ├── SKILL.md
│       └── scripts/
│           └── check-similarity.py
├── hooks/
│   ├── block-git.sh           # MỚI: chặn git commands 100%
│   └── check-citations.sh     # MỚI: auto-check sau edit .tex
├── rules/                     # Giữ nguyên 7 files
│   └── (unchanged)
├── settings.json              # CẬP NHẬT: thêm hooks config
└── settings.local.json        # Giữ nguyên permissions
```

**Không cần `.claude/commands/`** — skills đã thay thế hoàn toàn.

---

## 8. Priority Action Items

| # | Hành động | Effort | Impact |
|---|-----------|--------|--------|
| 1 | **Tạo hooks** (block-git + check-citations) | 30 min | 🔴 Critical — deterministic > advisory |
| 2 | **Cập nhật plan/implement/verify skills** với frontmatter đúng chuẩn (context: fork, agent, allowed-tools) | 20 min | 🔴 High — cải thiện context management |
| 3 | **Rút gọn CLAUDE.md** bỏ duplicate sections | 15 min | 🟡 Medium — giảm instruction count |
| 4 | **Thêm `!` dynamic injection** cho citation-verifying | 10 min | 🟡 Medium — agent thấy data thực ngay |
| 5 | **Thêm validation loop** cho thesis-writing | 10 min | 🟡 Medium — catch errors sớm |
| 6 | **Giảm maxTurns** cho thesis-writer (30→20) | 5 min | 🟢 Low — tránh agent loop |
| 7 | **Merge paper-converting vào thesis-writing** | 30 min | 🟢 Optional — giảm skill count |

---

## Tham khảo Best Practices đã áp dụng

Các nguồn đã tổng hợp:

- [Anthropic Official: Best Practices](https://code.claude.com/docs/en/best-practices) — CLAUDE.md ngắn, skills progressive disclosure, hooks deterministic
- [Anthropic Official: Skill Authoring](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — validation loops, concise SKILL.md
- [Anthropic Official: Skills Docs](https://code.claude.com/docs/en/skills) — commands merged into skills, frontmatter options
- [HumanLayer Blog](https://www.humanlayer.dev/blog/writing-a-good-claude-md) — ~150-200 instruction limit, CLAUDE.md < 200 lines
- [Shrivu Shankar](https://blog.sshh.io/p/how-i-use-every-claude-code-feature) — Master-Clone architecture, avoid custom subagent anti-pattern
- [Daniel Miessler](https://danielmiessler.com/blog/when-to-use-skills-vs-commands-vs-agents) — Skills = domain, Workflows = tasks, Agents = parallel workers
- [Builder.io](https://www.builder.io/blog/agent-skills-rules-commands) — Description is for routing, body is procedure
- [GenAI Unplugged](https://genaiunplugged.substack.com/p/claude-code-skills-commands-hooks-agents) — Hooks > CLAUDE.md for safety rules
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) — Gotchas in every skill, `context: fork` for isolation