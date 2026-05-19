# Devin Gaps — DevOps Pack

**Purpose:** extend Patty's Agent Army system to cover Devin-specific workflows. Your local Antigravity / Codex rules (`system-rules.md`, `handoff-rules.md`, `vibe-coder-prep-rules.md`, `step-1-prompt.md`, `step-2-prompt.md`, `vc-agent-opening-prompt.md`) stay as the primary system. This doc adapts them to Devin's cloud-VM environment.

**When to use:** any session where Devin is a primary contributor (even alongside Antigravity / Codex).

---

## 1. Path Translation

| Antigravity / Codex | Devin |
|---|---|
| `/Volumes/Sandbox/agents/resources/` | **Not reachable.** Load rules via Devin Knowledge (user-level) or commit rule docs to `.agents/rules/` inside the repo. |
| `/Volumes/Sandbox/agents/[app-name-here]/` | `/home/ubuntu/repos/<repo-name>/` (cloned per session, ephemeral). |
| `/Volumes/Sandbox/agents/[app-name-here]/misc-docs/` | `/home/ubuntu/repos/<repo-name>/misc-docs/` — **committed to the repo** (overrides default `gitignore /misc-docs/` rule). |
| Local attachments | `/home/ubuntu/attachments/` (ephemeral per session). |

**Rule:** You cannot point Devin at `/Volumes/Sandbox/`. The rule docs must be either:
- Loaded as a Devin Knowledge note at session start (recommended for cross-repo rules), OR
- Committed into the repo under `.agents/rules/` (recommended for repo-specific rules or skills)

---

## 2. Devin-Specific Workflow Tools (Not In Current Agent Army Docs)

These are Devin features your current system doesn't leverage:

- **PR-first workflow.** Devin creates PRs for all code changes rather than committing to main. Enforced per session; not optional.
- **Preview URLs.** Vercel (or equivalent) generates a preview per PR. Devin validates against that URL, not `localhost`. The user also tests from the preview URL.
- **CI pass gate.** Devin waits for CI (lint, build, any automated checks) before declaring a change done. Uses `git(action="pr_checks", wait_mode="all")`.
- **Devin Review.** Second-pass bot reviews every PR and posts findings. Devin addresses findings in-session rather than asking the user to click autofix. The user should expect Devin to push fixes directly and report "now clean to merge."
- **Skills (`.agents/skills/<name>/SKILL.md`).** Reusable, repo-specific procedures that auto-load when Devin works in that repo. Examples: "how to run tests here", "how to log in to the staging app", "deploy checklist".
- **Knowledge notes.** User-level context that auto-loads into every Devin session across all of that user's repos. Example: the consolidated Agent Army rules live here.
- **Playbooks.** Saved reusable session templates. Example: "new SPA build — runs Step 1 per Patty's system, generates the 7 docs, commits them, pauses at Gate 1." Bootstrap a new session with all the right prompts.
- **Schedules.** Recurring Devin sessions ("every Monday, audit repo X for issues").
- **Child sessions.** Spin up parallel Devin instances to work on independent tasks.
- **Environment config (`devin.yaml` / org-level).** Setup script that runs before every Devin session touches the repo (installs deps, runs migrations, starts services).
- **Integrations / MCP.** Devin can talk to external services directly (Notion, Linear, Slack, Google Drive, Figma) with the right auth configured.
- **Test mode + screen recording.** Devin can record itself testing the app end-to-end and attach a video to the PR as visual proof.

---

## 3. What Devin *Can't* Do From The Current Agent Army System

- Can't read `/Volumes/Sandbox/` — rule docs unreachable unless committed or loaded via Knowledge.
- Can't execute Antigravity or Codex prompts literally (they reference local paths + local editors).
- Can't enforce "approval gates via file-path handoffs" — its gates happen in chat via `message_user` with `block_on_user=true`.
- Can't expose `localhost` to the user — Devin points the user to preview URLs instead.

---

## 4. What Devin *Can* Do That The Current System Doesn't Leverage

- Parallel and stacked PRs (e.g. gig-spottr-bot PR #5 stacked on PR #3 — merged cleanly after rebase).
- Automated PR template enforcement via `git_pr(action="fetch_template")` — prevents Devin from writing a PR body that diverges from repo conventions.
- Devin Review feedback loop, self-healed in-session (fix pushed within seconds of finding).
- Child sessions for parallelization of independent V2 / V3 work streams.

---

## 5. Devin Adapter Rules (authoritative when Devin is the active agent)

### 5.1 Repo Hygiene Override

- Commit `/misc-docs/` to the repo (overrides `system-rules.md` §12 Antigravity default).
- Still gitignore `/resources/`, `.env`, `.env.local`, `node_modules/`.
- Never commit secrets.

### 5.2 Handoff Translation

- "Handoff" between Step 1 and Step 2 is not a file-path load. In Devin it means:
  - Step 1 docs committed to `/misc-docs/` in the repo OR pasted inline in the chat
  - Explicit chat-based approval gate using `message_user(block_on_user=true)`
  - Step 2 begins only after user posts approval in chat

### 5.3 Approval Gate Translation

| Agent Army gate | Devin equivalent |
|---|---|
| Gate 1 (after docs generated) | `message_user` with attached docs and `content_type="user_question"`, block until user approves |
| Gate 2 (after file tree + architecture approved) | Same pattern, block until approved |
| Gate 3 (after UI selections confirmed) | Same pattern — MUST include colors + fonts numbered list, block until selection confirmed |

### 5.4 Branch Naming

- Format: `devin/<unix-timestamp>-<short-kebab-description>`
- Example: `devin/1776535922-lever-resolver`
- Never force-push to main. `--force-with-lease` permitted on feature branches only (e.g. after rebase).

### 5.5 PR Requirements

- Always run `git_pr(action="fetch_template")` before writing a PR body — use the repo's actual template.
- Always attach the preview URL in the final message to the user.
- Always use `git(action="pr_checks", wait_mode="all")` to confirm CI green before reporting done.

### 5.6 Devin Review Findings

- Devin handles findings directly, in-session, without waiting on the user to click autofix.
- Push the fix, reply in-PR-thread with the fix commit SHA, and notify the user "now clean to merge."
- Do not block the user on Review findings unless the finding requires a product decision.

### 5.7 Blocker Rule (Devin flavor)

Same as `system-rules.md` §14:

- Stop
- State the blocker plainly
- Propose the smallest next action

Additionally for Devin: use `message_user(block_on_user=true)` with `user_action_required` set so the UI surfaces the block clearly. Do not invent workarounds without user approval.

### 5.8 Priority When Rules Conflict

1. User's explicit current instruction
2. Approved project-specific docs in `/misc-docs/` (committed to repo)
3. This `devin-gaps-devops-pack.md` (loaded via Knowledge note or committed to repo)
4. `system-rules.md` (Antigravity system, still applies where not overridden)
5. Default templates in `/resources/`
6. Agent preference

Devin does not improvise around documented rules.

---

## 6. Communication Tone (Patty-Specific)

- Neurodivergent solo entrepreneur / Operations Strategist
- Avoid developer jargon → plain-English explanations of features
- Don't over-explain SPA basics (she knows the stack structure)
- Minimize walls of text: concise numbered lists, IFTTT logic, minimum detail for action
- Ask the fewest questions necessary
- Bias toward linking evidence (PR URLs, preview URLs, file references) over long descriptions
- When reporting completion: lead with the link, then one-sentence summary, then "ready when you are"

---

## Version

v1 — 2026-04-18. Derived from Patty's Phase 1 Agent Army docs + observations from `gig-spottr-bot` Devin session. Update this pack as Devin-workflow patterns stabilize.
