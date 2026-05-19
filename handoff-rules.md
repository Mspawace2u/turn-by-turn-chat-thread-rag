# **Handoff Rules**

## `handoff-rules.md`

`Once all Step 1 confirmations are complete, the agent must generate ALL required documentation BEFORE any architecture, file tree, or code output.`

---

## **Required Document Generation**

`Generate the following documents in order:`

1. `PRD (Product Requirements Document)`  
2. `MVP Specification (Phase 1)`  
3. `Future Specification (Phase 2+)`  
4. `Technical Specification`  
5. `Build Instructions`  
6. `Vibe Coder Prep`  
7. `File Tree`

---

## **Output Location**

`All documents must be:`

- `Output as clean .md or .txt files`  
- `Structured and copy-ready`  
- `Saved to:`

`/misc-docs/`

`Required file paths:`

`/misc-docs/prd.md`  
`/misc-docs/mvp-spec.md`  
`/misc-docs/future-spec.md`  
`/misc-docs/tech-spec.md`  
`/misc-docs/build-instructions.md`  
`/misc-docs/vibe-coder-prep.md`  
`/misc-docs/file-tree.txt`

---

## **Document Alignment Rule**

`All documents must:`

- `Use the confirmed default stack unless modified`  
- `Remain consistent with each other (no contradictions)`  
- `Respect MVP vs Future scope separation`  
- `Reflect the confirmed use case and UX flow`

---

## **Vibe Doc Priority Rule**

`The file: /misc-docs/vibe-coder-prep.md is the single source of truth for:`

- `UI rules`  
- `design system`  
- `interaction behavior`  
- `layout patterns`  
- `icon usage (Lucide)`  
- `scroll behavior (deck-on-scroll)`  
- `UI selection protocol (fonts + colors)`

`All UI implementation MUST reference this file.`

---

## **Approval Gate (Mandatory)**

`After generating all documents:`

`STOP.`

`Present a summary of what was created and ask:`

`"All documentation has been generated and saved to /misc-docs/.`

`Review and approve before proceeding to architecture and build.`

`Proceed?"`

`Do NOT:`

- `generate file tree`  
- `generate architecture`  
- `generate UI`  
- `generate code`

`Until explicit user approval is received.`

---

## **Post-Approval Execution**

`Once approved, proceed in this order:`

1. `Generate file tree`  
2. `Generate architecture plan`  
3. `Generate component structure`  
4. `Generate data structure`  
5. `Begin Step 2 (Frontend Dev Prompt)`

---

## **STEP 2 Handoff Requirement**

`Before any UI work begins the agent MUST:`

1. `Load: /misc-docs/vibe-coder-prep.md`  
2. `Execute:`  
- `UI Selection Protocol (colors + fonts)`  
- `Confirmation gate`  
3. `Only after confirmation:`  
- `begin UI implementation`

---

## **Failure Prevention Rules**

`Do NOT:`

- `skip documentation generation`  
- `collapse all docs into one file`  
- `begin build early`  
- `ignore vibe-coder-prep.md`  
- `assume UI decisions`  
- `proceed without confirmation gates`

---

## **Final Directive**

`Think first. Document second. Build last.`

`Precision > speed`  
`Clarity > assumptions`  
`System > improvisation`

## 

## 

## 

## 

