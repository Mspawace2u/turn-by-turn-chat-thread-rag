# VC opening prompt — addendum to load new template files

**How to use:** paste the block below into your VC agent opening prompt wherever it currently lists the files to load from your DevOps pack (`/Volumes/Sandbox/agents/resources/...`). If you already have a loop like "read every file in `/resources/templates/`", you don't need to do anything — just drop the two new template files in that folder and they'll auto-load.

---

## Two new template files to add to your DevOps pack

Save to `/Volumes/Sandbox/agents/resources/templates/`:

1. `skill-overview-template.md` — boilerplate for the repo-level `.agents/skills/overview/SKILL.md` that Devin auto-loads on every session. Generated during Step 1 and committed alongside `/misc-docs/`.
2. `devin-yaml-template.yaml` — boilerplate for `/devin.yaml` at repo root. Bootstraps new Devin sessions with install + build. Generated during Step 1 and committed to repo root.

---

## Addendum block for your VC opening prompt

Paste this under whatever section of your VC opening prompt currently lists the resources pack contents (or under a "Step 1 outputs" list if you have one):

```
During Step 1 doc-pack generation, in addition to the 7 required /misc-docs/ files (prd.md, tech-spec.md, mvp-spec.md, future-spec.md, vibe-coder-prep.md, file-tree.txt, build-instructions.md), also generate:

1. .agents/skills/overview/SKILL.md
   - Use /Volumes/Sandbox/agents/resources/templates/skill-overview-template.md as the boilerplate
   - Fill from decisions made during Step 1: stack fingerprint, approved-brights picked, approved font pair picked, known integrations, run-locally commands, env-var names
   - Commit alongside /misc-docs/ in the repo so it auto-loads every Devin session

2. devin.yaml (repo root)
   - Use /Volumes/Sandbox/agents/resources/templates/devin-yaml-template.yaml as the boilerplate
   - Replace [REPO-NAME] with the actual repo name
   - Adjust install / maintenance commands to match the package manager decided during Step 1
   - List env-var names in the header comment (reference only — never commit actual secret values)
   - Commit at repo root

Both files are part of the same initial Step 1 commit as /misc-docs/. No extra approval gate needed — they're generated from decisions already approved in Gates 1-3.

If Step 2 (UI build) discovers new integrations or env-vars not listed in SKILL.md, update SKILL.md in the same PR as the Step 2 work.
```

---

## Why this change

- **No extra prompt from you** — still one agent prompt, still two-step workflow, still three approval gates.
- **Per-repo context ships with the repo** — any future Devin session on the same repo loads SKILL.md + devin.yaml automatically. No re-derivation from code.
- **Faster session bootstrap** — first shell on a new session comes with deps installed + build warmed, because `devin.yaml` runs during session start.
- **Cross-repo rules stay in Knowledge note** (loads on every session, any repo); per-repo specifics stay in `.agents/skills/overview/SKILL.md` (loads only on that repo). No duplication.

---

## Conflict-priority update (if you want to mirror this in system-rules.md)

Current priority order from Knowledge note:
1. User's explicit current instruction
2. Approved project-specific docs committed to the repo (`/misc-docs/`)
3. Knowledge note
4. `system-rules.md` + `devin-gaps-devops-pack.md` (if committed in repo)
5. Default templates
6. Agent preference

Where `.agents/skills/overview/SKILL.md` slots in: **between 2 and 3** — it's more specific than the Knowledge note but less authoritative than `/misc-docs/`. If SKILL.md contradicts `/misc-docs/`, `/misc-docs/` wins. Rule of thumb: SKILL.md captures observed state + drift from the doc-pack intent; `/misc-docs/` captures the canonical intent.

No code change required for this priority shuffle unless you want to document it explicitly in your system-rules.md.
