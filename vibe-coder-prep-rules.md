# **Vibe Coder Prep Rules for Dev**

## `vibe-coder-prep-rules.md`

## **1\. Purpose**

`This document exists to enforce UI, UX, and build discipline across all SPA builds.`

`It prevents:`

- `generic UI output`  
- `agent drift`  
- `inconsistent design decisions`  
- `unnecessary rework`

`This is the single source of truth for all frontend styling and interaction behavior.`

## **2\. Default Dev Stack**

`Assume this stack unless explicitly modified by the user:`

- `Astro (SSR mode)`  
- `React (.jsx)`  
- `Tailwind CSS`  
- `Framer Motion`  
- `Vite`  
- `Supabase (initial local/manual testing)`  
- `GitHub (version control)`  
- `Vercel (deployment)`

`Preferred coding environment:`

- `Antigravity (Gemini 3.1 Pro High)`

`Alternatives:`

- `Codex (5.3 or 5.4) if selected`  
- `Devin (cloud agent, PR-first workflow)`

## **3\. Stack Confirmation Protocol**

`Before any build or UI work begins, the agent MUST say:`

`"Default stack detected:`

- `Astro (SSR mode)`  
- `React (.jsx)`  
- `Tailwind CSS`  
- `Framer Motion`  
- `Vite`  
- `Supabase (initial, local testing)`  
- `Vercel deployment (after GitHub) Proceed with this stack? (Yes / Modify)"`

`Rules:`

- `If user says "Yes" → proceed immediately`  
- `If user says "Modify" → ask ONLY what needs to change`  
- `Do NOT restart discovery`  
- `Do NOT ask redundant questions`

## **4\. UI Selection Protocol (MANDATORY)**

`Before applying ANY styling, the agent MUST:`

### **4.1 Color Selection**

`Display this exact numbered list:`

1. `Electric Purple (#9b5cff)`  
2. `Totes Turquoise (#2de2e6)`  
3. `Punk Rock Pink (#ff2f92)`  
4. `Screamer Green (#3cff9e)`  
5. `Highlighter Yellow (#ffe44d)`  
6. `Orange U Bright (#f97316)`

`Ask: "Select your primary, secondary, and optional accent colors by number."`

### **4.2 Font Selection**

`Display this exact numbered list:`

1. `SUSE + SUSE Mono (default)`  
2. `Atkinson Hyperlegible Next + Atkinson Hyperlegible`  
3. `Red Hat Display + Red Hat Mono`  
4. `Reddit Sans + Reddit Mono`  
5. `Google Sans Flex + Google Sans Code`  
6. `Syne + Azeret Mono`  
7. `Noto Sans Display + Noto Sans Mono`  
8. `Urbanist + Kumbh Sans`  
9. `Sora + Inter Tight`

`Ask: "Select a font pairing by number or confirm default."`

### **4.3 Confirmation Gate**

`After selections, confirm:`

`"You selected:`

- `Colors: [insert list]`  
- `Fonts: [insert pair] Proceed with UI styling?"`

`Rules:`

- `Do NOT proceed without confirmation`  
- `Do NOT assume defaults silently`  
- `Pause execution if no response`

### **4.4 Reuse Rule**

`Once selected:`

- `Store selections`  
- `Apply consistently across ALL components`  
- `Do NOT re-ask unless user resets or overrides`

## **5\. Icon System (MANDATORY)**

`Use Lucide icons only.`

`Rules:`

- `Outline style (no fills unless explicitly required)`  
- `Hairline stroke`  
- `Consistent sizing across all components`

`Usage:`

- `toggles`  
- `bullet points`  
- `navigation`  
- `status indicators`  
- `CTA enhancements`

`Do NOT:`

- `use emojis`  
- `mix icon libraries`  
- `randomly size icons`

## **6\. Design System Rules**

### **6.1 Core Color Palette (Strict Adherence)**

`All SPA builds must anchor the base UI on:`

- **`Main Background:`** `#050505 (Deep, almost-pitch black)`  
- **`Primary Text:`** `#F3F4F6 (Off-white for readability)`  
- **`Secondary Text / Subtitles:`** `#5B6B7F (Muted steel blue-gray)`

`Brand gradient behavior:`

- `Linear and/or radial combinations with subtle diffusion glow`  
- `Use only the 2–4 colors chosen by the user from the approved brights palette`  
- `Do not introduce unapproved glow colors`

### **6.2 Color System**

- `Base UI must anchor on #050505, #F3F4F6, and #5B6B7F`  
- `Use ONLY approved palette`  
- `No default Tailwind colors (no blue-500, gray-100, etc.)`  
- `Maintain consistent accent usage`  
- `Brights are for emphasis, glow, borders, and interactive moments — not for replacing the core readability palette`

### **6.3 Typography**

- `Headings: chosen UI font (bold, tight tracking)`  
- `Body: chosen mono or supporting font`  
- `No italics unless explicitly requested`  
- `Use uppercase + tracking for labels and buttons`

#### **6.3.1 Typography Scale (Mandatory)**

- `Micro-labels (status chips, card metadata, footnotes, timestamps): 9px–12px with uppercase + tracking`  
- `Body copy: framework default (typically 14–16px)`  
- `Section labels and CTA button text: framework default + uppercase + tracking`  
- `Headings: chosen UI font, bold, tight tracking — size scales per section hierarchy`

#### **6.3.2 Tertiary Emphasis Rule (Mandatory)**

`For tertiary text — micro-labels, deprioritized metadata, supporting copy inside a card — use the primary text color at opacity-70 rather than introducing a third gray.`

`This preserves the strict core palette (#050505 / #F3F4F6 / #5B6B7F) while still giving visual hierarchy between primary, secondary, and tertiary copy.`

`Examples:`

- `status chips, micro-labels inside a card: text-[#F3F4F6] opacity-70`  
- `timestamps, deprioritized metadata: text-[#F3F4F6] opacity-70`  
- `Do NOT introduce a new hex value for "even lighter gray"`

#### **6.3.3 Failure-State Label Pattern (Mandatory)**

`For failure-bucket, warning, error, or weakness labels (e.g. "BIGGEST GAP", "NEEDS WORK", "MISSING"):`

- `Use the primary-accent color (from the user's selected brights palette) at opacity-70`  
- `Non-italic`  
- `Micro-label scale (9px–12px)`  
- `Uppercase + tracking`  
- `Non-shouting but visually distinct from surrounding card content`

`Reasoning: failure surfaces should read as deliberate visual callouts, not alarms. Dim-but-present beats high-saturation scream.`

### **6.4 Buttons (Critical)**

- `Pill shape ONLY`  
- `Transparent fill (resting state)`  
- `Gradient hairline border (rainbow effect)`  
- `Hover:`  
  - `solid fill (primary accent)`  
  - `dark text for contrast`  
  - `glow effect`

### **6.5 Cards & Containers**

- `Dark backgrounds`  
- `Subtle borders`  
- `Rounded corners`  
- `Glassmorphism for overlays or headers`

### **6.6 Brand Gradient Reference Implementations**

`When a user selects their brights palette (e.g. Punk Rock Pink + Totes Turquoise), use these patterns as implementation defaults:`

#### **Pink-to-Turquoise header accent gradient**

```
background: linear-gradient(90deg, #ff2f92 0%, #2de2e6 100%);
```

`Usage: accent hairline, text gradient on a single heading word, interactive hover glow.`

#### **Radial diffusion glow (single-color accent)**

```
background: radial-gradient(circle at 50% 50%, rgba(255, 47, 146, 0.35) 0%, rgba(255, 47, 146, 0) 70%);
```

`Usage: soft background glow behind hero content, behind a CTA on hover, behind an active tab indicator.`

#### **Gradient hairline border (pill button resting)**

```
border: 1px solid transparent;
background: 
  linear-gradient(#050505, #050505) padding-box,
  linear-gradient(90deg, #ff2f92, #2de2e6) border-box;
```

`Usage: resting-state pill CTA border.`

`Rules:`

- `Substitute the user's actual selected brights palette colors`  
- `Keep glow subtle — opacity 0.25–0.45 for radial diffusions`  
- `Do NOT hard-code a gradient that uses colors outside the user's selected palette`

## **7\. Deck-on-Scroll Presentation Mode**

`Use this layout for SPA pages that behave like landing pages or slide decks.`

### **Behavior**

- `One core idea per screen`  
- `Sections fill approximately one viewport height`  
- `Content vertically centered`  
- `Symmetrical top and bottom padding`

### **Implementation Rules**

- `Main container:`  
  - `vertical scroll snapping enabled`  
- `Sections:`  
  - `snap-aligned`  
  - `structured for clarity, not density`

`Suggested implementation language:`

- `scroll-snap-type: y mandatory`  
- `scroll-snap-align: start OR center (based on content height)`  
- `min-height: 100svh`

### **Motion Behavior**

- `Use subtle entrance animations per section`  
- `Use timed motion ONLY when it enhances clarity`  
- `Avoid over-animation`

`Do NOT:`

- `overload sections with multiple ideas`  
- `break vertical centering`  
- `force scroll snap on long/dense content`

## **7.1 Sticky Headers (Mandatory for SPA builds)**

`All SPA builds use a sticky header.`

### **Alignment Rules**

- `Left outside edge of the app icon (next to App Name) aligns with the left outside edge of the app's outermost viewing container below it`  
- `Right outside edge of the chosen right-margin element aligns with the right outside edge of the app's outermost viewing container below it:`  
  - `rightmost nav icon (for app-experience SPAs)`  
  - `pulsating text string (for one-page scrolling website experience)`

### **Spacing Rules**

- `Symmetrical top and bottom padding inside the header — negative space above and below header elements should visually match`  
- `Appropriate negative space at the top of the vertical viewing area for the preferred viewing device (no content shoved against the viewport edge)`

### **Tailwind Implementation Defaults**

`Reference implementation (adjust per build, but keep the shape):`

```jsx
<header className="sticky top-0 z-50 w-full bg-[#050505]/80 backdrop-blur-md">
  <div className="max-w-[container-width] mx-auto flex items-center justify-between px-[container-pad] py-3">
    <div className="flex items-center gap-3">
      <AppIcon />
      <span className="font-[ui-font] text-[#F3F4F6]">App Name</span>
    </div>
    <nav className="flex items-center gap-4">
      {/* right-margin element (nav icons or pulsating text string) */}
    </nav>
  </div>
</header>
```

### **Scroll Behavior**

- `Header remains fully visible while scrolling`  
- `Background blur / dim on scroll only if it aids readability of the content below`  
- `z-index must be high enough to stay above deck-on-scroll sections`  
- `Header height must not change on scroll (no shrink-on-scroll unless explicitly requested)`

### **Canonical Reference**

`Reference implementation: gig-spottr-bot sticky header (see PR #1 diff). All future SPAs should match this shape unless the user explicitly overrides.`

## **8\. Motion & Interaction Rules**

- `All interactive elements:`  
  - `transition-all`  
  - `duration-300`  
  - `hover elevation`  
- `Use:`  
  - `subtle glow backgrounds`  
  - `gradient text sparingly`  
  - `micro-interactions for feedback`  
- `Avoid:`  
  - `static UI`  
  - `excessive animation`  
  - `distracting motion`

## **9\. Layout Rules**

- `Mobile-first design`  
- `Left alignment preferred`  
- `Maintain symmetry across sections`  
- `High negative space`  
- `Clear section separation`

## **10\. Build Discipline**

- `Build module by module`  
- `Validate before expanding`  
- `Keep components modular`  
- `Avoid unnecessary dependencies`

## **11\. Agent Behavior Rules**

- `Do NOT assume beyond documented defaults`  
- `Do NOT override confirmed stack`  
- `Do NOT skip UI selection protocol`  
- `Do NOT overengineer MVP`  
- `Do NOT add unapproved features`  
- `Ask minimum necessary questions only`

## **12\. Documentation Discipline**

`All required docs must be generated before major build output:`

- `/misc-docs/prd.md`  
- `/misc-docs/mvp-spec.md`  
- `/misc-docs/future-spec.md`  
- `/misc-docs/tech-spec.md`  
- `/misc-docs/build-instructions.md`  
- `/misc-docs/vibe-coder-prep.md`  
- `/misc-docs/file-tree.txt`

## **13\. Do Not Do List**

- `Don't freestyle the stack`  
- `Don't skip confirmation gates`  
- `Don't use generic UI defaults`  
- `Don't mix design systems`  
- `Don't collapse MVP and future scope`  
- `Don't ask user to repeat known defaults`  
- `Don't introduce fonts outside the approved 9-pair list without explicit approval`  
- `Don't introduce a third gray — use primary text color at opacity-70 for tertiary emphasis`
