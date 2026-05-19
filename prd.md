# **Product Requirements Document (PRD)**

## **1\. Project Title**

`[Project Name]`

## **2\. Problem Statement**

`This product solves: [Describe the operational, user, or workflow problem]`

## **3\. Target User**

`Primary user: [Describe user type]`

`Secondary user (if any): [Describe secondary user type]`

## **4\. Core Use Case**

`The main thing this app must help the user do is: [Describe the primary outcome]`

## **5\. Default Build Context**

`Unless otherwise specified, this project should assume the following default dev stack and workflow:`

- `Build and test locally in the user's MacOS LDE on an external hard drive`  
- `Coding environment: Antigravity with Gemini 3.1 Pro High preferred unless user selects Codex 5.3 or 5.4`  
- `App type: Serverless full-stack app`  
- `Framework: Astro (SSR mode)`  
- `Frontend: React (.jsx)`  
- `Styling: Tailwind CSS`  
- `Motion layer: Framer Motion`  
- `Build tool: Vite`  
- `Initial data layer: Supabase, set up manually for testing before deploy`  
- `Deployment path: local testing → GitHub repo → Vercel deployment`  
- `Future migration path may include Cloudflare Workers, KV, and Durable Objects`  
- `Agent must present this default stack and confirm: "Default stack detected. Proceed with this stack? (Yes / Modify)"`

## **6\. Success Criteria**

`This project is successful when:`

- `[Success metric 1]`  
- `[Success metric 2]`  
- `[Success metric 3]`

## **7\. Key Features**

- `[Core feature 1]`  
- `[Core feature 2]`  
- `[Core feature 3]`

## **8\. Out of Scope**

`This project does NOT include in the current phase:`

- `[Excluded item 1]`  
- `[Excluded item 2]`  
- `[Excluded item 3]`

## **9\. Constraints**

- `Must avoid unnecessary tool sprawl`  
- `Must prioritize low-cost, reliable tooling`  
- `Must translate dev logic into plain English for the HITL`  
- `Must avoid assumptions and confirm defaults before proceeding`  
- `Must keep build scope aligned to MVP first`

## **10\. Approval Gate**

`Do not proceed into architecture, file tree, or code generation until the user approves this PRD.`  
