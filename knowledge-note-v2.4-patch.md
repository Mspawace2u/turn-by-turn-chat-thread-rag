# Knowledge Note v2.4 — Patch

**Goal:** close the resource-doc gap surfaced by the `watchr` session. Future Devin sessions on any of Patty's repos auto-load these rulesets without needing the `vibe-coder-prep-rules.md` / `gig-spottr-header-spec.md` / `slide-deck-rules.md` resource files re-attached each time.

**How to apply:** paste the *patched sections* below into your Devin Knowledge note titled "Wavemaker / Agent Army — SPA Build System v2.3 (Devin edition)". Bump the header to **v2.4** and append the v2.3 → v2.4 changelog line at the bottom.

Four inline additions + one revision. Nothing is removed.

---

## [INSERT into "Design system (strict)" → "Colors" subsection, replacing the single `Approved brights` bullet]

### Colors
- **Base:** `#050505` bg, `#F3F4F6` primary text, `#5B6B7F` secondary text
- **Approved brights (user picks 2–4 from these 6):**
  1. Electric Purple `#9b5cff`
  2. Totes Turquoise `#2de2e6`
  3. Punk Rock Pink `#ff2f92`
  4. Screamer Green `#3cff9e`
  5. Highlighter Yellow `#ffe44d`
  6. Orange U Bright `#f97316`
- **Tertiary emphasis:** primary-text color at `opacity-70` (NOT a new gray). Applies to micro-labels, weakness chips, card metadata.
- **No generic Tailwind colors** (no `blue-500`, `gray-100`, etc.)
- Brights are for emphasis, glow, borders, and interactive moments — not for replacing the core readability palette.

---

## [INSERT into "Design system (strict)" → "Typography" subsection, replacing the single `approved 9-pairing list` bullet]

### Typography
- Heading + supporting font pair selected from the **approved 9 pairings** (canonical list — do not invent new pairs):
  1. **SUSE + SUSE Mono** (default if user doesn't choose)
  2. Atkinson Hyperlegible Next + Atkinson Hyperlegible
  3. Red Hat Display + Red Hat Mono
  4. Reddit Sans + Reddit Mono
  5. Google Sans Flex + Google Sans Code
  6. Syne + Azeret Mono
  7. Noto Sans Display + Noto Sans Mono
  8. **Urbanist + Kumbh Sans** (used in `watchr`)
  9. Sora + Inter Tight
- **Micro-labels (9–12 px, uppercase, tracked):** for status chips, card metadata, footnotes.
- No italics unless explicitly requested.
- Headings use the UI font (bold, tight tracking); body uses the supporting / mono font.

---

## [REVISE existing "Components" subsection to clarify the Lucide-only rule + reveal-card exception]

### Components
- **CTA buttons:** pill shape only, transparent fill rest, gradient hairline border, solid accent fill + glow on hover.
- **Cards:** dark bg, subtle hairline border, rounded corners, glassmorphism for overlays.
- **Icons:** **Lucide only, outline, hairline stroke, consistent sizing.** No mixing icon libraries, no random sizing.
  - **Exception — reveal / rating cards:** in-card message content inside a reveal or rating card may use Apple-style emoji (e.g. 🎁 as the "open reveal" CTA, 🌮 in a 1–5 rating-scale legend). The Lucide-only rule still applies to chrome, nav, status chips, and prompts outside the card surface. The exception covers *content*, not *UI affordances*.
  - Everywhere else: no emojis.

---

## [INSERT as a new subsection under "Design system (strict)" → "Layout", right after the sticky-header bullets]

### Sticky header — canonical tokens (reference apps)
For any SPA build, the sticky header + main viewing area share a **single column** defined by two tokens. Declare them once on `:root`:

```css
:root {
  --shell-max-w: 480px;    /* phone column, centered on desktop */
  --shell-pad-x: 24px;     /* horizontal gutter */
}
```

- **Both header and `<main>`** set `max-width: var(--shell-max-w)` and `padding-inline: var(--shell-pad-x)`. This is what makes the brand mark in the header align pixel-exact with the first card below.
- **Viewport meta** must include `viewport-fit=cover` so `env(safe-area-inset-*)` returns real values on iOS notched devices.
- **Header:** `padding-top: env(safe-area-inset-top)`. **Main:** `padding-bottom: calc(2rem + env(safe-area-inset-bottom))`.
- **Frosted-glass recipe (three independent dials):**
  - Background opacity: `bg-brand-bg/60` (range: `/40`–`/60` on dark apps; `/80+` reads as an opaque bar, not glass).
  - Blur: `backdrop-blur-xl` (`blur(24px)`). `blur-lg` also fine; `blur-md` is too crisp; `blur-3xl` smears content into a blob.
  - Saturation: `backdrop-saturate-150`. Skip only for intentionally muted brands. Always include `-webkit-backdrop-filter` prefix.
- **Bottom border:** always 1 px at 5 % white alpha — the visual cue that something is scrolling underneath. Never remove.
- **Never** wrap the sticky header in a parent that uses `overflow: hidden / auto`, `transform`, `filter`, or `perspective` — any of these silently break `position: sticky`.
- `z-index: 50` on the header. Modals / toasts layer above at 60+.

Reference implementations: `gig-spottr-bot`, `cu-bettr`, `ss-reader`, `watchr` (all use the same two tokens + recipe).

---

## [INSERT as a new subsection under "Design system (strict)" → "Layout", right after the slide-deck-rules pointer bullet]

### Slide-deck mode — quick reference (full spec in `misc-docs/slide-deck-rules.md`)
Any slide-deck / one-pager / sales-page build picks **one** of two modes; mixing is forbidden.

**Mode A — Vertical Scroll Lander (default)**
- Standard page scroll; sections stack top-to-bottom.
- Each section `min-height: 100svh`, vertically centered content.
- Use for: marketing landers, long-form sales pages, launch announcements.
- Canonical section inventory (long-form V1): hero → social proof → problem → solution → features → testimonials → pricing → FAQ → final CTA.
- MVP short-form (V2): hero → problem → solution → one testimonial → single CTA.

**Mode B — Horizontal Deck-on-Scroll (pitch mode)**
- Horizontal scroll, one slide per viewport width.
- `scroll-snap-type: x mandatory` on the container; `scroll-snap-align: center` on each slide.
- Use for: pitch decks, investor one-pagers, sales decks meant to feel like Keynote/PowerPoint.
- Extras specified but not always shipped: fullscreen toggle, print-to-PDF, present mode, top-right button cluster (see `slide-deck-rules.md` §11.6–§11.9).

**Shared rules (both modes):**
- Use a `PAGE_DATA` config object, not hard-coded copy in components, so the same template can be reused across offers.
- Mode A and Mode B headers both use the canonical `--shell-max-w` / `--shell-pad-x` tokens above.
- Mode B slides do not scroll internally — if content doesn't fit at mobile width, split across slides.

---

## [APPEND to bottom of note — add v2.4 changelog entry under "Version"]

**v2.3 → v2.4 changes (watchr session, Apr 2026):**
- Inlined the **approved 6 brights palette** as a numbered list (was a single bullet).
- Inlined the **approved 9 font pairings** as a numbered list (was a single bullet). Added reminder that pair #8 = Urbanist + Kumbh Sans is used in `watchr`.
- Added **reveal / rating card emoji exception** under Components → Icons. Covers in-card *content* only (🎁 open-reveal, 🌮 rating legend). Lucide-only rule still holds everywhere else.
- Added **Sticky header — canonical tokens** subsection. Declares `--shell-max-w: 480px` and `--shell-pad-x: 24px` as shared tokens between header and `<main>`; documents the iOS `viewport-fit=cover` + `env(safe-area-inset-*)` pattern; documents the three-dial frosted-glass recipe (opacity `/60`, blur `xl`, saturate `150`).
- Added **Slide-deck mode — quick reference** inlining Mode A vs Mode B decision + canonical section inventories so a session doesn't have to load `slide-deck-rules.md` just to decide scope.

No rules removed. No conflict priority changes. `watchr` repo confirmed as the reference for pair #8 + reveal-card emoji exception.
