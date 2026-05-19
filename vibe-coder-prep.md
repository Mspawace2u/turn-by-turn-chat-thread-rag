# **Vibe Coder Prep for \[Project Name\]**

## `vibe-coder-prep.md`

## **1\. Purpose**

`This document is the active project-specific UI source of truth for the current build.`

`It defines:`

- `approved colors`  
- `approved typography`  
- `icon rules`  
- `interaction rules`  
- `CTA behavior`  
- `layout discipline`  
- `deck-on-scroll usage rules`  
- `frontend guardrails for MVP implementation`

## **2\. Confirmed Stack Context**

`Use this stack unless the user explicitly changes it:`

- `Astro (SSR mode)`  
- `React (.jsx)`  
- `Tailwind CSS`  
- `Framer Motion`  
- `Vite`  
- `Supabase (initial local/manual testing)`  
- `GitHub`  
- `Vercel`

`Preferred coding environment:`

- `Antigravity (Gemini 3.1 Pro High)`

`Alternative:`

- `Codex (5.3 or 5.4) if needed`

## **3\. Confirmed UI Selections**

### **3.1 Core Color Palette (Strict Adherence)**

- **`Main Background:`** `#050505 (Deep, almost-pitch black)`  
- **`Primary Text:`** `#F3F4F6 (Off-white for readability)`  
- **`Secondary Text / Subtitles:`** `#5B6B7F (Muted steel blue-gray)`  
- **`Brand Gradients (The "Vibe" Glow):`**  
  - `Linear and/or radial combinations with subtle diffusion glow`  
  - `Use only the 2–4 colors chosen by the user from the approved brights palette`  
  - `Do not introduce unapproved glow colors`

### **3.2 Approved Brights Palette**

`Use ONLY these approved bright colors:`

- **`Electric Purple`** `#9b5cff`  
- **`Totes Turquoise`** `#2de2e6`  
- **`Punk Rock Pink`** `#ff2f92`  
- **`Screamer Green`** `#3cff9e`  
- **`Highlighter Yellow`** `#ffe44d`  
- **`Orange U Bright`** `#f97316`

### **3.3 Locked Project Colors**

- **`Primary:`** `[insert selected color + hex]`  
- **`Secondary:`** `[insert selected color + hex]`  
- **`Accent 1:`** `[insert selected color + hex]`  
- **`Accent 2:`** `[insert selected color + hex if used]`

### **3.4 Confirmed Font Pairing**

- **`Heading / UI font:`** `[insert font]`  
- **`Supporting / body font:`** `[insert font]`

`Do not re-ask for colors or fonts unless the user explicitly resets or overrides them.`

## **4\. Typography Rules**

- `Headings use the chosen UI font`  
- `Body copy uses the chosen supporting/body font`  
- `No italics unless explicitly requested`  
- `Labels and buttons should use uppercase with clean tracking where appropriate`  
- `Keep typography crisp, readable, and premium without crowding the screen`

## **5\. Icon Rules**

- `Use Lucide only`  
- `Outline style only`  
- `Hairline stroke`  
- `Consistent sizing across components`  
- `No mixed icon libraries`

`Proper usage includes:`

- `toggles`  
- `bullet points`  
- `navigation`  
- `status indicators`  
- `CTA enhancements`

`Do NOT:`

- `use emojis unless directed otherwise`  
- `mix icon libraries`  
- `randomly size icons`

## **6\. Design System Rules**

### **6.1 Color system**

- `Base UI must anchor on #050505, #F3F4F6, and #5B6B7F`  
- `Use ONLY the approved palette`  
- `No generic Tailwind defaults like blue-500, gray-100, etc.`  
- `Maintain consistent accent usage`  
- `Brights are for emphasis, glow, borders, and interactive moments — not for replacing the core readability palette`  
- `Dark backgrounds should support glow, contrast, and readability`

### **6.2 Buttons**

`Critical rules:`

- `Pill shape ONLY`  
- `Transparent fill in resting state`  
- `Gradient hairline border`  
- `Hover state:`  
  - `solid fill using approved primary color logic`  
  - `brand white text for contrast`  
  - `glow effect`  
- `Keep labels short bold in all caps body copy font`

### **6.3 Cards and containers**

- `Dark backgrounds`  
- `Subtle hairline borders`  
- `Rounded corners`  
- `Glassmorphism for overlays, headers, or layered interface moments where it enhances clarity`  
- `Avoid heavy lines or visual clutter`

## **7\. Motion and Interaction Rules**

- `All interactive elements use:`  
  - `transition-all`  
  - `duration-300`  
  - `hover elevation where appropriate`  
- `Use subtle glow backgrounds`  
- `Use gradient text sparingly to highlight a word or two in section headlines when requested`  
- `Use micro-interactions for feedback`  
- `Avoid static-feeling UI`  
- `Avoid excessive animation or distracting motion`

## **8\. Layout Rules**

- `Mobile-first design`  
- `Left alignment inside containers preferred`  
- `Maintain symmetry across sections`  
- `High negative space`  
- `Clear section separation`

### **8.1 Sticky Headers**

`All headers are sticky. Be sure to:`  
 

- `Leave appropriate negative space at the top of the vertical viewing area for the preferred viewing device`  
- `Add bottom padding below elements in the header so there’s symmetry in the negative space above and below the header elements`  

`Wrap header so that:`  
 

- `Left outside edge of app icon next to App Name aligns with the left outside edge of the app’s outermost viewing container below it`      
- `Right outside edge of chosen right margin element aligns with the right outside edge of the app’s outermost viewing container below it:`   
  - `the right most Nav Icon (for app experience)`   
  - `the pulsating text string message (for one-page scrolling website experience)`

### **8.2 Nav Bars**

`Mobile first app experience with 3 functional UX flow pages default to Lucide icons in the sticky header.`

`More complex apps or multi-feature websites meant for Desktop may have:`

- `a right-aligned hamburger menu`  
- `a left-aligned multi-tab experience`  
- `a footer-based icon with text string`   

### **8.3 App Icons & Favicons**

`Glassmorphic style PNG will be added by user in the public folder file for use in the following three ways:`

- `on the left side of the sticky header, scaled to the appropriate size`  
- `as the favicon for the browser tab`  
- `as the iOS icon for users who use the Add to Home Screen share option when viewing as a web page`

**`IMPORTANT DEV NOTE`**`: you must code functionality into the SPA to perform like a native iOS app when accessed from the pinned Home Screen favicon on user’s iPhone.`   

## **9\. Deck-on-Scroll Rules**

`Use deck-on-scroll only if a page is behaving like a landing-page or slide-deck experience.`

`If used:`

- `one core idea per screen`  
- `vertically centered content`  
- `symmetrical top and bottom spacing`  
- `avoid overloading each screen`

**`Do NOT`**`:`

- `overload sections with multiple ideas`  
- `break vertical centering or left alignment in containers`  
- `force scroll snap on long/dense content`

### **9.1 Implementation**

`Main container:`

- `vertical scroll snapping enabled`

`Sections:`

- `snap-aligned`  
- `structured for clarity, not density`

`Suggested implementation language:`

- `scroll-snap-type: y mandatory`  
- `scroll-snap-align: start OR center (based on content height)`

`min-height: 100svh`  

### **9.2 Motion Behavior**

`Reference special time-delayed motion effects asked for by user on live websites or via access to deployed app repos for clarification when needed`

`Otherwise:`

- `Use subtle entrance animations per section`  
- `Use timed motion ONLY when it enhances clarity`  
- `Avoid over-animation`

## **10\. App-Specific UX Notes**

- `[insert app-specific UX notes]`  
- `Keep friction low`  
- `Preserve the emotional payoff of the primary interaction flow`

## **11\. Locked Copy / Interaction Labels**

`Use exact approved labels unless the user approves changes:`

- `[insert locked labels]`

## **12\. Documentation Discipline**

`If not already completed, you must generate and file all required docs in the proper pathway before major build output:`

- `/misc-docs/prd.md`  
- `/misc-docs/mvp-spec.md`  
- `/misc-docs/future-spec.md`  
- `/misc-docs/tech-spec.md`  
- `/misc-docs/build-instructions.md`  
- `/misc-docs/vibe-coder-prep.md`  
- `/misc-docs/file-tree.txt`

## **13\. Build Discipline**

- `Build module by module`  
- `Validate before expanding`  
- `Keep components modular`  
- `Avoid unnecessary dependencies`  
- `Do not override confirmed UI choices mid-build`  
- `Do not add unapproved features`  
- `Ask minimum necessary questions only`

## **14\. Do Not Do List**

`You must honor this exclusion list as the coding agent:`

- `DO NOT freestyle or override confirmed stack`  
- `Do NOT skip UI selection protocol`  
- `DO NOT skip confirmation gates`  
- `Don’t use generic UI defaults`  
- `Don’t mix design systems`  
- `Do NOT add unapproved features`  
- `Don’t collapse MVP and future scope`  
- `Don’t re-ask for already approved colors or fonts`  
- `Do NOT assume beyond documented defaults`
