# **Technical Specification**

## **1\. Project Title**

`[Project Name]`

## **2\. Default Technical Stack**

`Use this stack by default unless user modifies it:`

- `Runtime / app framework: Astro (SSR mode)`  
- `Frontend UI layer: React (.jsx)`  
- `Styling system: Tailwind CSS`  
- `Motion / micro-interactions: Framer Motion`  
- `Build tool: Vite`  
- `Initial backend / data layer: Supabase`  
- `Local dev environment: MacOS LDE on external hard drive`  
- `Preferred coding environment: Antigravity with Gemini 3.1 Pro High`  
- `Alternative coding environment: Codex 5.3 or 5.4`  
- `Version control: GitHub`  
- `Deployment target: Vercel`  
- `Possible future migration path: Cloudflare Workers + KV + Durable Objects`

## **3\. Confirmation Rule**

`Before architecture or code generation begins, the agent must confirm:`

`"Default stack detected:`

- `Astro (SSR mode)`  
- `React (.jsx)`  
- `Tailwind CSS`  
- `Framer Motion`  
- `Vite`  
- `Supabase (initial, local testing)`  
- `Vercel deployment (after GitHub)`

`Proceed with this stack? (Yes / Modify)"`

## **4\. Architecture Overview**

`Describe the app’s high-level structure:`

- `frontend rendering approach`  
- `route/page logic`  
- `data flow`  
- `state flow`  
- `backend responsibilities`  
- `deployment path`

## **5\. UI Governance Rule**

`All UI and design decisions are governed exclusively by: /misc-docs/vibe-coder-prep.md`

`Do NOT:`

- `redefine UI rules in this document`  
- `override design system constraints`  
- `introduce new styling logic outside the vibe doc`

`This document controls structure and logic only.`

## **6\. File Structure**

`Document the intended file tree, including:`

- `/src or /app`  
- `/components`  
- `/lib`  
- `/styles`  
- `/public`  
- `/misc-docs`

## **7\. Data Structure**

`Document key data models, JSON structures, and local or remote storage assumptions.`

## **8\. State Management**

`Document:`

- `local component state`  
- `shared state`  
- `persistence logic`  
- `any progression or session storage rules`

## **9\. Logic Flows**

`Document the major system flows:`

- `user entry`  
- `user action`  
- `response generation`  
- `data save/update`  
- `completion logic`

## **10\. Integrations**

`Document any required integrations for MVP and any deferred integrations for later phases.`

## **11\. Risks / Edge Cases**

`Document likely failure points, weird cases, and assumptions that need validation.`

## **12\. Approval Gate**

`Do not generate code until this technical spec is reviewed and approved by the user.`  
