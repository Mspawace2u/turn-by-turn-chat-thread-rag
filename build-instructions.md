# **Agent Army | Wavemaker LLC Brand Dev Guidelines (Revised Core)**

## **System Overview**

`This is a TWO-STEP execution system:`

- `STEP 1 = Backend + Logic + Documentation`  
- `STEP 2 = Frontend + UI Implementation`

`All reusable rules, constraints, and UI systems live in: /misc-docs/`

---

## **STEP 1 — Backend Dev (Revised Behavior)**

### **Core Rules**

- `Do NOT assume stack or tools`  
- `Present default stack and confirm`  
- `Ask minimum required questions only`  
- `Generate ALL required docs before build`  
- `STOP for approval before proceeding`

---

### **Default Stack (Confirmation Required)**

`Agent must say:`

`"Default stack detected:`

- `Astro (SSR mode)`  
- `React (.jsx)`  
- `Tailwind CSS`  
- `Framer Motion`  
- `Vite`  
- `Supabase (initial, local testing)`  
- `Vercel deployment (after GitHub)`

`Proceed with this stack? (Yes / Modify)"`

`Rules:`

- `If Yes → proceed`  
- `If Modify → ask ONLY what changes`  
- `Do NOT restart discovery loop`

---

### **Required Step 1 Flow**

1. `Confirm:`  
   - `Use case (SPA / site / other)`  
   - `Purpose (internal / product / etc.)`  
   - `Syntax preference`  
   - `Build environment (Antigravity or Codex)`

   

2. `Confirm stack (default or modified)`  
3. `Confirm UX basics:`  
   - `Minimum goal`  
   - `User interaction`  
   - `Trigger flow`

---

### **Handoff To Documentation**

`Once confirmed:`

`👉 Execute HANDOFF RULE`  
`(Defined in separate handoff-rule.md)`

---

## **STEP 2 — Frontend Dev (Revised Behavior)**

### **Core Rules**

- `Do NOT design freely`  
- `Do NOT assume UI choices`  
- `MUST read: /misc-docs/vibe-coder-prep.md`

---

### **Required Step 2 Flow**

1. `Load: /misc-docs/vibe-coder-prep.md`  
2. `Execute:`  
- `UI Selection Protocol (colors + fonts)`  
- `Confirmation Gate`  
3. `After approval:`  
- `Begin UI implementation`  
- `Follow all design + layout rules strictly`

---

### **UI Enforcement**

`All UI decisions must follow: /misc-docs/vibe-coder-prep.md`

`Includes:`

- `color system`  
- `typography`  
- `Lucide icons`  
- `scroll behavior (deck-on-scroll)`  
- `CTA styles`  
- `layout rules`

`Before UI implementation:`  
`- Review /misc-docs/vibe-coder-prep.md`  
`- Confirm font + color selections with user`  
`- Do not proceed with styling until confirmed`

---

## **Document System (Source Of Truth)**

`All builds must generate and use:`

`/misc-docs/prd.md`  
`/misc-docs/mvp-spec.md`  
`/misc-docs/future-spec.md`  
`/misc-docs/tech-spec.md`  
`/misc-docs/build-instructions.md`  
`/misc-docs/vibe-coder-prep.md`

---

## **System Rules**

- `Do NOT duplicate logic across docs`  
- `Do NOT override confirmed defaults`  
- `Do NOT skip approval gates`  
- `Do NOT build before documentation is complete`  
- `Do NOT implement UI without selection protocol`

---

## **Final Directive**

`This system enforces:`  
`Document → Confirm → Build → Enforce`

`NOT:`  
`Guess → Build → Fix later`
