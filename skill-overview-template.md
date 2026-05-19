# [REPO-NAME] — repo fingerprint & guardrails

**Trigger:** When working in the `[REPO-NAME]` repo.

<!--
TEMPLATE INSTRUCTIONS (delete this block before committing):

- Fill every [PLACEHOLDER] below based on the decisions made in Step 1 (Agent Army two-step workflow) + actual repo state.
- Anything you don't know yet → leave the placeholder so the next Devin session knows to fill it in.
- Commit path: `.agents/skills/overview/SKILL.md` (auto-loads every Devin session on this repo).
- Keep under ~120 lines. More detail → spin up additional skill files under `.agents/skills/<topic>/SKILL.md`.
- When fixing a known issue, promote that section from "Known issues" → "Resolved" with PR reference. Don't just delete.
-->

## Purpose of app
[ONE PARAGRAPH — what the app does, who the user is, primary problem it solves. Pulled from PRD §1 or vibe-coder-prep §1.]

## Stack fingerprint
- Node [X.X] (`engines.node` pinned in package.json)
- [Framework: Astro X / Vite+React / etc.]
- [React X] if applicable
- Tailwind CSS [X]
- [Key libs: framer-motion, lucide-react, etc.]
- Data: [scraping libs, parsing libs, HTTP client]
- Backend: [Supabase / Neon / Notion / custom API / none]
- Deploy target: [Vercel / Fly / other]
- Test runner: [node --test / vitest / none]

## Observed design system (strict — follow, don't silently "fix")
- **Base:** `#050505` bg, `#F3F4F6` text, `#5B6B7F` muted
- **Brights in use (user-picked 2-4 from approved 6):** [#HEX1] [Name], [#HEX2] [Name], [#HEX3] [Name]
- **Font pair (user-picked from approved 9):** [Heading Font] + [Supporting Font]. Loaded via [@fontsource / @import url(...) / <link>].
- **Tertiary emphasis rule:** primary text color at `opacity-70` for micro-labels, weakness chips, card metadata. NOT a new gray.
- **Sticky header:** canonical implementation — PR #[X]. App icon left-edge aligns with container left-edge; right element aligns with right-edge. Uses shared `--shell-max-w: [XX]px` and `--shell-pad-x: [X]rem`.
- **Build mode:** [Standard SPA / Mode A vertical slide-deck / Mode B horizontal deck]. If slide-deck → see `misc-docs/slide-deck-rules.md`.

## Run locally (if needed)
```bash
npm install
npm run dev       # [framework-specific dev command]
```

Required env vars (not in repo — source from Devin secrets or `.env`):
- `[ENV_VAR_1]` — [purpose]
- `[ENV_VAR_2]` — [purpose]

## Testing tips
- [App-specific quirks: LLM temperature ±variance, known flaky paths, regression URLs to validate against]
- [Where to put breakpoints for common debugging]
- [Specific CLI commands or scripts for common test scenarios]

## Integration rules (defensive writes)
- **Schema-drift retry** (if writing to Notion/Supabase/Neon): catch "unknown property" / "column does not exist" errors, log, retry with problematic field omitted. Never fail whole write on single drifted field.
- **Fail-closed on empty extraction** (if running LLM scoring / matching): empty input → explicit `UNREADABLE` flag, manual-fallback UI. Do NOT default score to 100%.
- **[Add repo-specific defensive rules here]**

## V2 / V3 backlog (do not auto-implement — ask first)
- **V2:** [feature improvements the user has noted but not yet requested]
- **V3:** [larger architectural changes or new integrations]

## Known issues (track, don't treat as rules)
- **[Issue name]:** [description]. [Fix suggestion / status / PR reference when resolved].

## Agent Army alignment
This repo follows Patty's Agent Army design system (see user Knowledge note v2.2+). Defaults: dark mode, approved-6-brights palette, approved-9-font-pairs list. Commit `/misc-docs/` by default. PR-first workflow. No direct commits to main.

---
**Last updated:** [YYYY-MM-DD] by [session-id or agent name]
