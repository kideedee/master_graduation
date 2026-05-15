---
name: spx-verify
description: Verify implementation matches change artifacts. Use when the user wants to validate that implementation is complete, correct, and coherent before archiving.
---

You are using the spx-verify skill, which is described as follows:

Verify that an implementation matches the change artifacts (specs, tasks, design).

> **CLI NOTE**: Run all `openspec` and `bash` commands directly from the workspace root. Do NOT `cd` into any directory before running them. The `openspec` CLI is designed to work from the project root.

> **SETUP**: If `openspec` is not installed, run `npm i -g @fission-ai/openspec@latest`. If you need to run `openspec init`, always use `openspec init --tools none`.

**🚫 SUBAGENT BLACKLIST:** NEVER use the `explore` or `plan` subagents. These are generic subagents from other kits and are NOT part of this workflow. Only use verifier subagents listed in this command.

**Why subagent?** Verification runs in clean context, avoiding bias from implementation conversation. This ensures independent, unbiased assessment.

**Input**: Optionally specify a change name. If omitted, check if it can be inferred from conversation context. If vague or ambiguous you MUST prompt for available changes.

**Steps**

1. **If no change name provided, prompt for selection**

   Run `openspec list --json` to get available changes. Use the **AskUserQuestion tool** to let the user select.

   Show changes that have implementation tasks (tasks artifact exists).
   Include the schema used for each change if available.
   Mark changes with incomplete tasks as "(In Progress)".

   **IMPORTANT**: Do NOT guess or auto-select a change. Always let the user choose.

2. **Check status to understand the schema**
   ```bash
   openspec status --change "<name>" --json
   ```
   Parse the JSON to understand:
   - `schemaName`: The workflow being used (e.g., "spec-driven")
   - Which artifacts exist for this change

3. **Get the change directory and load artifacts**

   ```bash
   openspec instructions apply --change "<name>" --json
   ```

   This returns the change directory and context files. Read all available artifacts from `contextFiles`.

   Also check if `openspec/changes/<name>/verify-fixes.md` exists. If it does, read it — this contains previously fixed issues that verifiers should skip.

4. **Detect change type and run verifiers in parallel**

   Determine which verifiers to spawn based on actual implementation — check the files that were modified, not just artifact keywords:
   - **Has architectural changes**: new files/modules created, dependency changes, new patterns introduced, structural refactors (check git diff or task descriptions for new file creation, package.json changes, new directories)
   - **Has UI files**: modified files include UI components — check actual file extensions/content (`.tsx`, `.vue`, `.svelte`, `.css`, `.scss`, component directories, style files), not just artifact keywords
   - **Has testable code**: project has test framework (jest.config.*, vitest.config.*, pytest.ini, *.test.*, *.spec.*) AND change touches code that should have tests
   - **Has backend API files**: modified files include API layer code — check for `.java` files with `@RestController` or `@Controller` (Spring), `@Path` resource classes (Quarkus/JAX-RS), Python files with FastAPI (`from fastapi import`) or DRF (`from rest_framework.views`), API route handlers, controller classes, DTO/request-response model files. Also check for OpenAPI spec files (`openapi.yaml`, `openapi.json`, `swagger.yaml`). Quarkus signals: `Uni<T>`/`Multi<T>` return types, `RestResponse<T>`, `@ServerExceptionMapper`, MicroProfile OpenAPI annotations.
   - **Has reliability/performance patterns**: modified files include caching config (`@Cacheable`, `Caffeine`, `@CacheResult`, `cachetools`, `lru_cache`), retry/circuit breaker (`Resilience4j`, `@Retry`, `@CircuitBreaker`, `@Timeout`, `@Bulkhead`, `@Fallback`, `@RateLimit`, `tenacity`, `pybreaker`), HTTP client calls (`WebClient`, `RestTemplate`, `@RegisterRestClient`, `requests`, `httpx`), connection pool config (`HikariCP`, `Agroal`, `quarkus.datasource.jdbc.*`, `SQLAlchemy` pool), or observability (`Micrometer`, `@Timed`, `quarkus-smallrye-health`, `@Liveness`, `@Readiness`, `structlog`, health endpoints).
   - **Has security-sensitive code**: modified files include auth/authZ logic (`Spring Security`, `SecurityFilterChain`, `@PreAuthorize`, `@RolesAllowed`, `@Authenticated`, `SecurityIdentity`, `Depends(verify_token)`, permission classes), JWT handling (`quarkus-oidc`, `quarkus-smallrye-jwt`, `mp.jwt.verify.*`), password hashing, SQL/NoSQL query construction (including Panache `find()` with string concatenation), file upload handling, secrets/config files, or CORS/CSRF configuration (`quarkus.http.cors.*`).
   - **Has database changes**: modified files include migration scripts (Flyway `V*__*.sql`, Liquibase changelogs, Alembic versions, Mongock `@ChangeUnit`), ORM entity/model changes (`@Entity`, `@Document`, `PanacheEntity`, `PanacheMongoEntity`, `models.Model`, SQLAlchemy models), repository/DAO files, or raw SQL/MongoDB query construction.

   Run selected verifiers **in parallel**:

   | Verifier | Condition |
   |----------|-----------|
   | `spx-verifier` | Always — artifact completeness check |
   | `spx-arch-verifier` | Change introduced new files/patterns/dependencies or structural changes. Skip for routine implementation within existing patterns. |
   | `spx-uiux-verifier` | Modified files include UI components (by actual file content/extension) |
   | `spx-test-verifier` | Project has test framework AND change touched testable code |
   | `spx-api-verifier` | Modified files include backend API layer code (Java Spring controllers, Python FastAPI/DRF routes, API handlers, DTOs, OpenAPI specs) |
   | `spx-perf-verifier` | Modified files include caching, retry/circuit breaker, timeout, connection pool, or observability patterns |
   | `spx-security-verifier` | Modified files include auth/authZ, JWT, query construction, file upload, secrets, or security config |
   | `spx-db-verifier` | Modified files include migration scripts, ORM entity/model changes, or database query construction |

   Instruction template for ALL verifiers:
   ```
   Verify implementation for change: <name>

   **Artifact paths:**
   - Tasks: openspec/changes/<name>/tasks.md
   - Proposal: openspec/changes/<name>/proposal.md
   - Design: openspec/changes/<name>/design.md (if exists)
   - Specs: openspec/changes/<name>/specs/*.md (if exist)

   **Files modified:** [list from implementation]

   **Previously fixed issues (from verify-fixes.md):**
   [content of verify-fixes.md, or "None" if file doesn't exist]
   ```

   Add verifier-specific context:
   - `spx-verifier`: include verify focus points from task annotations
   - `spx-uiux-verifier`: include which files contain UI components
   - `spx-test-verifier`: include test framework name and test command
   - `spx-arch-verifier`: include project language/framework
   - `spx-api-verifier`: include which files contain API endpoints (controllers, routers), detected API stack (Spring MVC, FastAPI, DRF), and path to OpenAPI spec file if present
   - `spx-perf-verifier`: include which files contain caching/retry/circuit breaker/timeout/pool config, detected libraries (Resilience4j, Caffeine, tenacity, HikariCP)
   - `spx-security-verifier`: include which files contain auth logic, security config, query construction, detected security stack (Spring Security, FastAPI auth, Django auth)
   - `spx-db-verifier`: include which files contain migrations, entity/model changes, query patterns, detected DB stack (PostgreSQL/MongoDB, Flyway/Alembic/Mongock)

   **Severity classification guidance** (include in ALL verifier instructions):
   - CRITICAL: Broken functionality, missing core requirements, security holes, data loss risks. These block archiving.
   - WARNING: Improvement opportunities, minor inconsistencies, non-blocking concerns. User decides whether to fix.
   - SUGGESTION: Nice-to-have, style preferences, optional enhancements.
   Be conservative with CRITICAL — only use it for things that are genuinely broken or missing. When in doubt, use WARNING.

5. **Merge and present verification reports**

   Combine reports from all verifiers into a single unified report. Do NOT fix any issues — this command is report-only.

   ```
   ## Verification Report: <change-name>

   **Verifiers run:** spx-verifier [, spx-arch-verifier] [, spx-uiux-verifier] [, spx-test-verifier] [, spx-api-verifier]

   ### Summary
   | Dimension | Source | Status |
   |-----------|--------|--------|
   | Completeness | spx-verifier | ... |
   | Correctness | spx-verifier | ... |
   | Coherence | spx-verifier | ... |
   | Architecture | spx-arch-verifier | ... (or "skipped — no structural changes") |
   | UI/UX | spx-uiux-verifier | ... (or "skipped — no UI files") |
   | Test Coverage | spx-test-verifier | ... (or "skipped — no test framework") |
   | API Contract | spx-api-verifier | ... (or "skipped — no backend API files") |
   | Performance & Reliability | spx-perf-verifier | ... (or "skipped — no perf/reliability patterns") |
   | Security | spx-security-verifier | ... (or "skipped — no security-sensitive code") |
   | Database | spx-db-verifier | ... (or "skipped — no database changes") |

   ### All Issues (merged, sorted by priority)
   **CRITICAL**: [all critical from all verifiers]
   **WARNING**: [all warnings from all verifiers]
   **SUGGESTION**: [all suggestions from all verifiers]
   ```

   Deduplicate overlapping issues (e.g., if both spx-verifier and spx-arch-verifier flag the same file). Keep the more specific one.

6. **Suggest next actions based on report**

   **If CRITICAL issues exist:**
   ```
   X critical issue(s) found. Fix before archiving.

   → Use `/spx-apply <name>` to continue implementation and fix issues
   → Or fix manually and run `/spx-verify` again
   ```

   **If only warnings/suggestions:**
   ```
   No critical issues. Y warning(s) found — review and decide. These do not block archiving.

   → Ready for archive: `/spx-archive <name>`
   → Or fix warnings first with `/spx-apply <name>`
   ```

   **If all clear:**
   ```
   All checks passed. Ready for archive.

   → `/spx-archive <name>`
   ```

**Subagent Reference**

| Subagent | Purpose | Condition |
|----------|---------|-----------|
| `spx-verifier` | Completeness, correctness, coherence against artifacts | Always |
| `spx-arch-verifier` | Architecture, design patterns, SOLID, library replacement | New files/patterns/dependencies or structural changes |
| `spx-uiux-verifier` | Accessibility, design tokens, responsive, component states, UI flows | Modified files include UI components |
| `spx-test-verifier` | Test existence, coverage, quality, edge cases | Project has test framework AND testable code touched |
| `spx-api-verifier` | API contract: REST conventions, validation, error handling, versioning, OpenAPI sync | Modified files include backend API layer code (controllers, routers, DTOs, OpenAPI specs) |
| `spx-perf-verifier` | Performance & reliability: caching, retry/circuit breaker, timeout, connection pool, observability | Modified files include caching, retry, circuit breaker, timeout, pool config, or observability patterns |
| `spx-security-verifier` | Security: auth/authZ, injection prevention, secrets, input sanitization, infrastructure security | Modified files include auth logic, security config, query construction, file upload, or secrets |
| `spx-db-verifier` | Database: migration safety, query patterns, schema design, backward compatibility | Modified files include migration scripts, entity/model changes, or database query construction |

**Subagent Briefing Protocol (mandatory before every spawn):**

Before launching ANY verifier subagent, output a brief to the user in the user's language:

```
📋 **[subagent-name]**
- Why: [why this verifier is needed — 1 line]
- Expect: [what you expect to receive back]
- Handle output:
  - If CRITICAL issues → report, suggest /spx-apply to fix
  - If only WARNING/SUGGESTION → report, user decides
  - If clean → this dimension passed
```

The template above is in English for prompt readability. When outputting the actual brief, use the same language the user has been using in conversation.

When spawning multiple verifiers in parallel, brief ALL of them in a single block before launching. This gives the user full visibility into what's about to happen and why.

**No background mode — ever.** NEVER use `run_in_background` for any subagent. All subagents must run in parallel foreground so their execution is visible and controllable by the user. Background execution is uncontrollable behavior.

**Delegation rules:**
- **Select verifiers smartly** — do NOT blindly spawn all five. Only spawn verifiers relevant to what was actually modified.
- Run selected verifiers **in parallel** — they are independent
- **NEVER use `run_in_background`** — covered by briefing protocol above
- Provide ALL artifact paths from contextFiles to each verifier
- Each subagent has no conversation history — be explicit about what to verify
- All subagents return reports only — this command does NOT fix issues
- Merge reports into single unified output, deduplicate overlapping issues

**Output**

This command outputs a verification report only. It does NOT:
- Fix code
- Update tasks
- Modify any files

To fix issues found in the report, use `/spx-apply <name>` which will auto-verify and auto-fix.

The following is the user's request: