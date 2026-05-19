# **System Rules**

## **1\. Purpose**

`This document defines cross-document guardrails, execution logic, and anti-drift rules for all app builds using the Agent Army two-step workflow.`

`It exists to keep the system:`

- `simple`  
- `repeatable`  
- `executable`  
- `consistent across builds`

## **2\. Core Workflow Model**

`This is a two-step execution system:`

- `STEP 1 = backend, logic, discovery, and documentation`  
- `STEP 2 = frontend, UI selection, and implementation`

`The system must follow:`  
`Document → Confirm → Build → Enforce`

`Do NOT follow:`  
`Guess → Build → Fix later`

## **3\. Default Local Path Rule**

`Unless explicitly modified, new app builds should use:`

`/Volumes/Sandbox/agents/[app-name-here]`

`This is the standard working project directory.`

## **4\. Resources vs App Separation Rule**

`Use this separation at all times:`

- `/Volumes/Sandbox/agents/resources/ = reference library only`  
- `app folder = actual project build target`  
- `/misc-docs/ = generated per-project docs for the current build`

`The agent may read from /Volumes/Sandbox/agents/resources/, but must not treat it as app source code.`

`Do NOT include /resources/ contents in the app repo.`

## **5\. Required Doc Creation Order**

`Generate the project docs in exactly this order:`

1. `prd.md`  
2. `mvp-spec.md`  
3. `future-spec.md`  
4. `tech-spec.md`  
5. `build-instructions.md`  
6. `vibe-coder-prep.md`  
7. `file-tree.txt`

`Do not change the order unless the user explicitly approves a change.`

## **6\. Required Doc Output Location**

`Project-specific generated docs must be saved into:`

`/Volumes/Sandbox/agents/[app-name-here]/misc-docs/`

`Required files:`

- `/misc-docs/prd.md`  
- `/misc-docs/mvp-spec.md`  
- `/misc-docs/future-spec.md`  
- `/misc-docs/tech-spec.md`  
- `/misc-docs/build-instructions.md`  
- `/misc-docs/vibe-coder-prep.md`  
- `/misc-docs/file-tree.txt`

## **7\. Naming Convention Rule**

`Use these defaults`

### **Folders**

- `kebab-case`

### **Misc docs**

`Use these exact locked names:`

- `prd.md`  
- `mvp-spec.md`  
- `future-spec.md`  
- `tech-spec.md`  
- `build-instructions.md`  
- `vibe-coder-prep.md`  
- `system-rules.md`  
- `file-tree.txt`

### **Resource prompt / rule files**

`Use these exact names:`

- `step-1-prompt.md`  
- `handoff-rule.md`  
- `step-2-prompt.md`  
- `vibe-coder-prep-rules.md`

### **Routes and paths**

- `lowercase or kebab-case as appropriate to framework`

### **React component files**

- `PascalCase`

`Do NOT rename standard files unless the user explicitly approves it.`

## **8\. Approval Gates**

`The system uses exactly 3 approval gates:`

### **Gate 1**

`After all required docs are generated`

### **Gate 2**

`After file tree and architecture are generated`

### **Gate 3**

`After UI selections are confirmed:`

- `colors`  
- `fonts`

`Do not skip approval gates.`

## **9\. MVP Anti-Bloat Rule**

`If a feature is not required for the app’s minimum useful function, move it to:`

`future-spec.md`

`Do not silently expand MVP scope.`

`Do not add “nice to have” features into current build logic unless explicitly approved.`

## **10\. UI Governance Rule**

`Master UI and design rules are governed by:`

`/Volumes/Sandbox/agents/resources/prompts/vibe-coder-prep-rules.md`

`Project-specific applied UI rules must be generated into:`

`/Volumes/Sandbox/agents/[app-name-here]/misc-docs/vibe-coder-prep.md`

`Do NOT:`

- `redefine UI rules in other docs`  
- `override design system logic elsewhere`  
- `apply generic defaults outside the rules file`  
- `skip generation of the project-specific vibe doc`

`tech-spec.md controls structure and logic only.`  
`mvp-spec.md controls MVP scope only.`  
`future-spec.md controls future scope only.`

## **11\. File Tree Rule**

`file-tree.txt must:`

- `be generated after architecture is approved`  
- `use tree style formatting`  
- `reflect actual build structure exactly`  
- `contain no comments or explanations inside the tree`

`Use:`

- `├──`  
- `└──`

`Do not mix file tree styles.`

## **12\. Repo Hygiene Rule**

`Before first commit, create or verify .gitignore.`

`Must exclude:`

- `/misc-docs/`  
- `/resources/`  
- `.env`  
- `.env.local`  
- `node_modules/`  
- `local-only planning/reference files`  
- `system junk files`

`Do not commit:`

- `secrets`  
- `template resources`  
- `local-only docs`  
- `generated misc docs`

`Unless the user explicitly overrides this rule.`

## **13\. Build Order Rule**

`Do not generate architecture, file tree, Step 2 output, or code until:`

- `stack is confirmed`  
- `environment is confirmed`  
- `UX flow is clear`  
- `required docs are generated`  
- `Gate 1 approval is received`

`Do not begin Step 2 until:`

- `file tree and architecture are approved`  
- `Gate 2 approval is received`  
- `/Volumes/Sandbox/agents/resources/prompts/vibe-coder-prep-rules.md is loaded`  
- `/Volumes/Sandbox/agents/[app-name-here]/misc-docs/vibe-coder-prep.md is generated`  
- `UI Selection Protocol is executed`  
- `Gate 3 approval is received`

## **14\. Blocker Rule**

`If blocked:`

- `stop`  
- `state the blocker plainly`  
- `propose the smallest next action`

`Do NOT:`

- `invent workarounds without approval`  
- `fake progress`  
- `skip required steps`

## **15\. Done Definition**

`A build is not considered ready until:`

- `required docs exist`  
- `architecture is approved`  
- `file tree is approved`  
- `app runs locally`  
- `UI works in local browser`  
- `approved repo structure is in place`  
- `.gitignore is correct`  
- `GitHub repo is created from the app folder`  
- `deploy path is ready or completed`  
- `no critical blocker remains undocumented`

## **16\. Final Enforcement Rule**

`When rules conflict, apply this priority order:`

1. `User’s explicit current instruction`  
2. `Approved project-specific docs in /misc-docs/`  
3. `system-rules.md`  
4. `default templates and rules in /Volumes/Sandbox/agents/resources/`  
5. `agent preference`

`The agent does not get to improvise around documented system rules.`  