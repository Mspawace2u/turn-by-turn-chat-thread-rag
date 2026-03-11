# **STEP 1: Codex Handoff**

*The **single, clean PRD \+ SPEC document** that consolidates everything into what Codex actually needs to build this RAG engine*

---

# **GEMVAULT — PRODUCT REQUIREMENTS DOCUMENT & TECHNICAL SPECIFICATION**

---

## **1\. PROJECT OVERVIEW**

**GemVault** is a local-first, 3-layer RAG (Retrieval-Augmented Generation) system that ingests raw LLM chat thread exports from multiple providers, processes them into searchable knowledge, and extracts structured insights ("gems") using thinking agents designed for neurodivergent thought patterns.

**Two distinct build targets:**

- **RAG Engine:** Headless local Python agent running on Mac Mini external hard drive  
- **RAG Frontend:** Branded Astro SSR \+ React SPA deployed to Vercel

**Dual-purpose architecture:** Config-driven so the same system can be deployed for the owner's personal use OR swapped via config file for client/student onboarding.

---

## **2\. ARCHITECTURE — 3 LAYERS**

```
LAYER 1: THE MINE
├── All raw chat threads (ChatGPT, Gemini, Claude, other MD)
├── Parsed → Normalized → Chunked into Semantic Exchange Units (SEUs)
├── Quality scored, deduplicated, embedded
├── Stored in ChromaDB (3 collections) + SQLite (metadata)
├── Queried via hybrid retrieval (vector + BM25 + metadata + rerank)
│
│   ↓ Mining Agent (thinking agent with ND-aware reasoning)
│
LAYER 2: THE VAULT
├── Curated gems extracted by the Mining Agent
├── Each gem has 4 pillars: Problem / Pattern / Bridge / Gap
├── Stored in dedicated ChromaDB collection + SQLite + Notion dashboard
├── Searchable by both agents AND humans
├── Task agents pull from here for downstream work
│
│   ↓ Gem Selector pulls relevant gems per project
│
LAYER 3: THE WORKBENCH
├── Active project context window
├── Subset of Vault gems relevant to current task
├── Ephemeral — spins up per project, tears down after
├── Task agents (Content, Dev, Strategy, Teaching) operate here
```

---

## **3\. TECH STACK**

| Component | Technology |
| :---- | :---- |
| **Build Agent** | Codex 5.4 (primary), Antigravity \+ Gemini 3.1 Pro (secondary) |
| **LDE** | Mac Mini external hard drive, macOS |
| **Engine Language** | Python 3.11+ |
| **API Framework** | FastAPI (local server, port 8000\) |
| **Vector Database** | ChromaDB (local persistent storage) |
| **Metadata Database** | SQLite |
| **Curation Dashboard** | Notion (via API) |
| **Embedding Model** | OpenAI `text-embedding-3-large` (3072 dimensions) |
| **LLM for Agents** | Codex 5.4 via OpenAI API (temperature 0.1) |
| **`Format Detection`** | engine/parsers/format\_detector.py — classifies every .md file before routing to parser |
| **Frontend Framework** | Astro (SSR mode) \+ React (.jsx) |
| **Styling** | Tailwind CSS (custom theme, NO generic Tailwind colors) |
| **Animations** | Framer Motion \+ CSS transitions |
| **Build Tool** | Vite |
| **Deployment** | Engine stays local · Frontend → GitHub → Vercel → custom domain |
| **Live Sync** | GitHub backup repo → webhook → auto-ingest pipeline |
| **Future Migration** | Cloudflare Workers \+ KV/Durable Objects (Phase 3, not in scope now) |

---

## **4\. DATA SOURCES & PARSERS**

### **DATA SOURCES, FORMAT DETECTION & INGESTION**

#### 4.1 Source Reality

All chat thread exports live in a **single flat folder** on the user's Desktop. There are no subdirectories organized by provider. Files arrive via two different Chrome extensions with two different naming/formatting conventions:

- **Extension A:** Filename IS the chat title (e.g., `Build a RAG for my IP.md`)  
- **Extension B:** Filename may be generic, but the chat title appears as the first H1 or H2 heading inside the document

Files contain one of two content types:

- **Turn-by-turn conversations** — back-and-forth dialogue between user and LLM  
- **Standalone assets** — outputs created inside chat threads (frameworks, code, docs, plans) exported as their own files

The user's existing Python script auto-pushes every new file in this folder to a GitHub backup repo.

#### 4.2 Format Detection (runs FIRST on every file)

`engine/parsers/format_detector.py` reads each `.md` file and classifies it before any parser touches it.

**Step 1 — Detect content type:**

| If the file contains... | Classification |
| :---- | :---- |
| `"You said:"` and `"ChatGPT said:"` | `turn_by_turn`, provider: `chatgpt` |
| `"You said:"` and `"Gemini said:"` | `turn_by_turn`, provider: `gemini` |
| `"You said:"` and `"Claude said:"` | `turn_by_turn`, provider: `claude` |
| `"Q:"` and `"A:"` (no provider name) | `turn_by_turn`, provider: `unknown` |
| None of the above patterns | `standalone_asset` |

**Step 2 — Extract title:**

| Priority | Method |
| :---- | :---- |
| 1 | First `# Heading` or `## Heading` found in the document |
| 2 | Filename minus `.md` extension, dashes and underscores converted to spaces |

**Step 3 — Route to correct parser:**

```
format_detector.py
       ↓
  ┌────────────────────────────────────────────┐
  │  detected_type == "turn_by_turn"?          │
  │                                            │
  │  YES →                                     │
  │    provider == "chatgpt" → chatgpt_parser  │
  │    provider == "gemini"  → gemini_parser   │
  │    provider == "claude"  → claude_parser   │
  │    provider == "unknown" → generic_turn    │
  │                                            │
  │  NO →                                      │
  │    detected_type == "standalone_asset"      │
  │    → asset_parser                          │
  └────────────────────────────────────────────┘
```

#### 4.3 Turn-by-Turn Parsers

Each provider parser handles the specific turn marker format for that provider and outputs the **unified message schema:**

```py
{
    "thread_id": "uuid",
    "source": "chatgpt | gemini | claude | unknown",
    "title": "extracted title",
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601",
    "participants": ["user", "assistant"],
    "messages": [
        {
            "role": "user | assistant",
            "content": "raw text",
            "timestamp": "ISO-8601 if available, null if not",
            "has_code": bool,
            "has_url": bool,
            "token_count": int
        }
    ],
    "metadata": {
        "topic_tags": [],
        "domain": "",
        "quality_score": 0.0,
        "conversation_type": ""
    }
}
```

Turn-by-turn threads then flow into: `seu_chunker.py` → `quality_scorer.py` → `embedder.py` → `chroma_store.py` \+ `sqlite_store.py`

#### 4.4 Standalone Asset Parser

Non-conversation files get a different schema and different chunking:

```py
{
    "asset_id": "uuid",
    "source": "chat_output",
    "title": "extracted title",
    "content": "full text",
    "created_at": "ISO-8601 from file metadata",
    "detected_type": "standalone_asset",
    "sections": [
        {
            "heading": "section heading or null for intro",
            "content": "section text",
            "has_code": bool,
            "has_list_structure": bool,
            "word_count": int
        }
    ],
    "metadata": {
        "topic_tags": [],
        "domain": "",
        "quality_score": 0.0,
        "has_code": bool,
        "has_framework": bool,
        "has_list_structure": bool,
        "word_count": int
    }
}
```

Standalone assets then flow into: `section_chunker.py` → `asset_quality_scorer.py` → `embedder.py` → `chroma_store.py` \+ `sqlite_store.py`

Assets are tagged as `"standalone_asset"` in ChromaDB metadata so retrieval can filter or boost them appropriately.

#### 4.5 Ingestion Modes

**Mode A — Manual Bulk Load (first time, 3-year backlog):**

User runs `make ingest`. Pipeline processes every `.md` file in `data/raw_imports/chat_exports/`. Each file goes through format detection → appropriate parser → chunking → scoring → embedding → storage.

**Mode B — Auto Live Sync (ongoing):**

User's existing Python script pushes new `.md` files to GitHub backup repo. GemVault listens via webhook at `POST /webhook/github` (with 60-minute polling fallback if webhook fails). `diff_detector.py` compares repo state against `data/sync_manifest.json`. Only new or changed files (detected by SHA-256 hash comparison) trigger the pipeline. Never double-processes.

```
# Config for live sync
github_sync:
  enabled: true
  repo: "your-username/chat-thread-backups"
  branch: "main"
  webhook_secret: "${GITHUB_WEBHOOK_SECRET}"
  watch_paths:
    - "**/*.md"
  auto_ingest: true
  polling_fallback_minutes: 60
```

#### 4.6 Sync Manifest

`data/sync_manifest.json` tracks every ingested file:

```json
{
    "last_sync": "2026-03-11T14:30:00Z",
    "ingested_files": {
        "Build a RAG for my IP.md": {
            "sha256": "a1b2c3...",
            "ingested_at": "2026-03-11T14:30:00Z",
            "detected_type": "turn_by_turn",
            "detected_provider": "chatgpt",
            "seus_generated": 12
        },
        "Pricing Framework v3.md": {
            "sha256": "d4e5f6...",
            "ingested_at": "2026-03-11T14:31:00Z",
            "detected_type": "standalone_asset",
            "sections_generated": 5
        }
    }
}
```

#### 4.7 Future Sources (built but disabled)

- **Notion:** `notion_parser.py` — enable in config when ready  
- **Google Drive:** `gdrive_parser.py` — enable in config when ready

---

## **5\. CHUNKING — SEMANTIC EXCHANGE UNITS (SEUs)**

**Do NOT chunk by token count.** Chat threads are dialogue. Chunk by **Semantic Exchange Units** — one complete thought-loop.

An SEU contains one or more user↔assistant exchanges that form a coherent topic unit. An SEU boundary occurs when:

- Cosine similarity between consecutive messages drops below **0.72**  
- Time gap between messages exceeds **30 minutes**  
- User explicitly starts a new topic

Minimum **2 messages** per SEU. Single-message exchanges are discarded.

Each SEU contains:

- `messages`: the raw exchange  
- `summary`: LLM-generated 1-2 sentence summary (this gets embedded, not raw text)  
- `key_entities`: extracted proper nouns, tools, concepts  
- `actionable_output`: any decision, code, plan, or framework produced  
- `embedding`: vector of the summary

Standalone assets (non-conversation files) are chunked differently — by section headings rather than SEUs. This is handled by engine/chunking/section\_chunker.py. Each section becomes its own embeddable unit with the standalone\_asset schema.

---

## **6\. QUALITY SCORING**

#### 6.1 Turn-by-Turn SEU Scoring (`engine/scoring/quality_scorer.py`)

Applied to every Semantic Exchange Unit chunked from conversation threads.

```
SCORE BOOSTERS:
+0.25  Contains code block that appears functional
+0.30  Concept was referenced again in a later thread (cross-reference detected)
+0.20  Contains a decision or framework
+0.10  Deep exchange (4+ messages in the SEU)
+0.10  Contains URLs or file references

SCORE KILLERS:
-0.50  Near-duplicate of another SEU (cosine similarity > 0.92)
-0.20  Shallow exchange (average message length < 50 characters)
-0.30  Assistant declined or couldn't help ("I can't", "I don't have access")

FLOOR: 0.0
CEILING: 1.0
MINIMUM SCORE TO EMBED: 0.4
```

#### 6.2 Standalone Asset Scoring (`engine/scoring/asset_quality_scorer.py`)

Applied to every section chunked from standalone asset files. Different signals because there are no turn-by-turn conversation dynamics to evaluate.

```
SCORE BOOSTERS:
+0.25  Contains code blocks
+0.25  Contains structured lists or frameworks (numbered lists, bullet hierarchies)
+0.20  Has multiple headings (well-organized document)
+0.15  Word count > 500 (substantial content)
+0.10  Contains URLs or external references
+0.30  Cross-referenced by a turn-by-turn thread (a conversation mentions this concept)

SCORE KILLERS:
-0.50  Near-duplicate of another asset section (cosine similarity > 0.92)
-0.20  Under 100 words (fragment, likely incomplete)

FLOOR: 0.0
CEILING: 1.0
MINIMUM SCORE TO EMBED: 0.3 (lower threshold — standalone assets are pre-curated by nature,
the user chose to export them as their own file, which is itself a signal of value)
```

#### 6.3 Cross-Reference Tracking (`engine/scoring/cross_reference_tracker.py`)

Runs after initial scoring. Scans all ingested SEUs and assets for concept overlap:

- If a concept from Asset X also appears in Conversation SEU Y, both get the cross-reference boost  
- If a concept from SEU A in Thread 1 reappears in SEU B in Thread 7 three months later, both get the cross-reference boost  
- Recurrence frequency is tracked and stored in SQLite `cross_refs` table  
- The Mining Agent uses this recurrence data as a primary signal for pattern detection

---

## **7\. STORAGE**

### **7.1 ChromaDB Collections**

| Collection | Contents | Used By |
| :---- | :---- | :---- |
| `knowledge_base` | SEU summaries \+ key entities | Standard query retrieval |
| `action_outputs` | Decisions, code, frameworks | Action-specific retrieval |
| `raw_archive` | Full raw text | Exact-match fallback |
| `curated_gems` | Vault gems (all 3 embeddings per gem) | Task agents, human browsing |
| `assets` | Standalone asset records with section data, quality scores, domain tags, file metadata, detected title, word count | Asset quality scorer, hybrid retriever (metadata filtering), mining agent (cross-reference discovery), Notion sync (dashboard display) |

### **7.2 SQLite Tables**

- `threads` — source metadata, dates, provider  
- `seus` — SEU records with quality scores, domain tags, types  
- `gems` — structured gem records (problem/pattern/bridge/gap)  
- `cross_refs` — which SEUs reference concepts from other SEUs  
- `tags` — taxonomy/domain tagging  
- `sync_manifest` — file ingestion tracking (hash, date, SEU count)

### **7.3 Notion**

Used as a **human-readable curation dashboard** for Vault gems. Not a primary database. Gems push to Notion after crystallization for manual review, tagging, and verification.

---

## **8\. RETRIEVAL — HYBRID 5-STAGE PIPELINE**

```
Stage 1: Vector search (ChromaDB cosine similarity) → top 20
Stage 2: BM25 keyword search → top 20
Stage 3: Reciprocal Rank Fusion merge of Stage 1 + 2
Stage 4: Metadata boosting:
         - quality_score > 0.7 → score × 1.3
         - has_decision or has_framework → score × 1.2
         - was_cross_referenced → score × 1.15
Stage 5: Cross-reference expansion (pull in related SEUs)
Stage 6: Rerank with cross-encoder → return final 5
```

---

## **9\. AGENTS**

### **9.1 Agent Types**

| Agent | Purpose |
| :---- | :---- |
| **Query Agent** | Standard RAG queries against The Mine |
| **Mining Agent** | Deep pattern extraction across threads (ND-aware) |
| **Classification Agent** | Auto-tags domains, sub-domains, conversation types |
| **Summarization Agent** | Generates SEU summaries for embedding |
| **Connection Agent** | Discovers unexpected cross-thread connections |

### **9.2 Task Agents (operate from Vault/Workbench)**

| Agent | Purpose |
| :---- | :---- |
| **Content Agent** | Pulls bridges/frameworks → content creation |
| **Dev Agent** | Pulls code artifacts → development tasks |
| **Strategy Agent** | Pulls patterns/gaps → strategic planning |
| **Teaching Agent** | Pulls gems → curriculum/cowork session design |

### **9.3 Shared LLM Parameters (all agents)**

```
provider: openai
model: codex-5.4
temperature: 0.1
top_p: 0.9
frequency_penalty: 0.3
max_tokens: 4096
```

---

## **10\. PROMPT ARCHITECTURE — 2-LAYER SYSTEM**

### **10.1 Standard Query Flow**

**Layer 1 — Human Query Card (what the user fills out):**

```
WHAT I NEED: [plain English description of desired outcome]
CONTEXT HINT: [optional — date range, topic, memory jogger]
FORMAT: Summary | Full Reconstruction | Code | Decision Framework | Compare Evolution
FRESHNESS: Most Recent | Historical Evolution | Everything
```

**Layer 2 — Machine System Prompt (injected via API):**

```
ROLE: Personal knowledge retrieval agent over user's own data corpus.
Every answer MUST be grounded in retrieved context. Never hallucinate
the user's own opinions.

STRICT RULES:
1. GROUNDING MANDATE — every claim maps to a cited chunk [S1], [S2], etc.
2. CONFIDENCE TIERS based on retrieval quality:
   TIER 1 (HIGH): avg quality > 0.7, similarity > 0.82 → full confidence
   TIER 2 (MEDIUM): avg quality 0.4-0.7, similarity 0.65-0.82 → flag uncertainty
   TIER 3 (LOW): avg quality < 0.4, similarity < 0.65 → do NOT reconstruct,
   say what's closest and ask user to explore adjacent threads
3. TEMPORAL AWARENESS — surface evolution of thinking across time
4. NEVER HALLUCINATE — if it's not in retrieved context, say so
5. ACTIONABLE OUTPUT PRIORITY — decisions/code/frameworks surface first
6. CROSS-REFERENCE SURFACING — mention connected threads

OUTPUT FORMAT:
📍 Direct Answer (with citations)
📚 Source Material (excerpts with dates)
🔗 Connected Threads
⚠️ Gaps & Caveats
```

### **10.2 Mining Query Flow**

**Layer 1 — Human Mining Card:**

```
CONCEPT/KEYWORD: [the idea/theme to trace]
LOOKING FOR: Problem | Pattern | Solution | Gap | Evolution | All
DEPTH: Surface Scan | Deep Mine | Obsidian Mode (find hidden connections)
SAVE TO VAULT: Yes | No (just show me)
```

**Layer 2 — Mining Agent System Prompt:**

```
ROLE: Deep pattern recognition agent over neurodivergent thinker's
externalized thought corpus. NOT simple retrieval — archaeological
reconstruction of scattered ideas.

THINKING FRAMEWORK (execute in order):
1. SURFACE MAP — explicit mentions, chronological
2. SHADOW MAP — implicit/connected mentions with reasoning
3. THREAD TRACE — origin → recurrences → mutations → combinations → resolution/open loops
4. PATTERN EXTRACTION — problem / pattern / bridge / gap
5. GEM CRYSTALLIZATION — output structured gem schema

NEURODIVERGENT AWARENESS RULES:
1. Tangents are NOT noise — trace the hidden connection
2. Repeated returns = high signal — flag recurrence frequency
3. Frustration = proximity to breakthrough — mine those moments hardest
4. Questions > Statements — treat rhetorical questions as thesis statements
5. The real insight is often in the parenthetical — don't skip asides
6. Metaphors are architecture — extract and formalize them

OUTPUT FORMAT:
🔍 Surface Map
👁️ Shadow Map
🧬 Thread Trace
💎 Extracted Gem
🕳️ Open Loops
🔗 Unexpected Connections
```

---

## **11\. GEM SCHEMA (Vault Records)**

```py
{
    "gem_id": "uuid",
    "concept": "core concept/keyword",
    "created_at": "ISO-8601",
    "mined_from": {
        "thread_count": int,
        "source_providers": ["chatgpt", "gemini", "claude"],
        "date_range": "earliest → latest",
        "total_seus_analyzed": int
    },
    "problem": {
        "statement": str,
        "evidence": ["S1", "S3"],
        "first_appeared": "date",
        "recurrence_count": int
    },
    "pattern": {
        "description": str,
        "evidence": ["S2", "S5"],
        "frequency": str,
        "triggers": [str]
    },
    "bridge": {
        "frameworks": [{
            "name": str,
            "description": str,
            "completeness": 0.0-1.0,
            "evidence": ["S4", "S8"]
        }],
        "action_steps": [str],
        "code_artifacts": [str]
    },
    "gap": {
        "unresolved": str,
        "closest_attempt": str,
        "suggested_next": str
    },
    "connections": ["other gem_ids"],
    "tags": [str],
    "confidence": "HIGH | MEDIUM | LOW",
    "human_verified": false,
    "embedding_problem": [float],
    "embedding_bridge": [float],
    "embedding_full": [float]
}
```

---

## **12\. API ENDPOINTS (FastAPI, local)**

| Method | Route | Purpose |
| :---- | :---- | :---- |
| `POST` | `/query` | Standard RAG query |
| `POST` | `/mine` | Gem mining request |
| `GET` | `/vault` | Browse curated gems |
| `POST` | `/vault` | Manually add/edit gem |
| `POST` | `/workbench` | Spin up project context |
| `POST` | `/ingest` | Trigger manual ingestion |
| `POST` | `/webhook/github` | GitHub auto-sync webhook |
| `GET` | `/health` | Status check |

CORS allowed origins: `http://localhost:4321` (Astro dev), `http://localhost:3000`

---

## **13\. FRONTEND DESIGN SYSTEM**

### **13.1 Brand Colors (strict adherence — no generic Tailwind colors)**

```
background: "#050505"
card: "#0f0f0f"
popover: "#121212"
foreground: "#fafafa"
secondary_foreground: "#c7cbd1"
muted_foreground: "#9da4af"
card_border: "#4b5563"
accent_primary: "#9b5cff"        # Electric Purple
accent_secondary: "#2de2e6"      # Totes Turquoise
accent_tertiary: "#ffe44d"       # Highlighter Yellow
borders: "border-white/5 or border-[#9b5cff]/10"
```

### **13.2 Typography**

Import from Google Fonts:

```
@import url('https://fonts.googleapis.com/css2?family=SUSE:wght@100;200;300;400;500;600;700;800&display=swap');
```

Also import SUSE Mono via preferred font loader.

- **Headings (font-sans):** SUSE, bold/black weights, `tracking-tighter`. No italics.  
- **Body & Accents (font-mono):** SUSE Mono, all paragraph text, buttons, nav, kickers. No italics.  
- **Kickers/Eyebrows:** font-mono, `text-xs` or `text-sm`, uppercase, `tracking-widest` or `tracking-[0.2em]`.

### **13.3 UI Components**

- **Cards:** `bg-[#1a1a1a]`, 1px subtle border, `rounded-2xl` or `rounded-[12px]`  
- **Glassmorphism header:** `backdrop-blur-md`, `bg-[#050505]/90`, sticky  
- **Buttons (Pill Style):** 1px gradient wrapper (`linear-gradient(90deg, #9b5cff, #2de2e6, #ffe44d, #9b5cff)`) animating infinitely. Inner fill transparent. Hover: fill turns accent color, text turns `#050505`, casts glow. Text: uppercase, font-mono, tracking-widest.  
- **Highlight bars:** `w-[2px] bg-gradient-to-b from-[#9b5cff] to-transparent shadow-[0_0_15px_#9b5cff]`  
- **Gradient text:** `bg-clip-text text-transparent bg-gradient-to-r from-[#9b5cff] via-[#2de2e6] to-[#ffe44d]`  
- **Glow pools:** Absolute positioned divs with accent colors, `blur-[100px] opacity-10`  
- **Alignment:** Left-aligned vertical axis. Massive negative space (`py-20`, `min-h-screen`, `gap-12`).

### **13.4 Animations**

- Hover states on all interactive elements: `transition-all duration-300`, `hover:-translate-y-1`  
- `animate-pulse` on active indicators and terminal-style cursors  
- Scoped `<style>` blocks in React components for custom animations (typewriter, vertical carousels)

### **13.5 Frontend Pages**

| Page | Purpose |
| :---- | :---- |
| `index.astro` | Main query interface — Query Card form \+ results display |
| `vault.astro` | Vault browser — gem grid, search, tag filters, connection graph |
| `mine.astro` | Mining interface — Mining Card form \+ gem extraction display |
| `workbench.astro` | Active project view — gem selector, task agent panel, output |

---

## **14\. GITHUB LIVE SYNC**

```
github_sync:
  enabled: true
  repo: "your-username/chat-thread-backups"
  branch: "main"
  webhook_secret: "${GITHUB_WEBHOOK_SECRET}"
watch_paths:
  - "**/*.md"    # flat folder, all markdown files, no subdirectory structure
  auto_ingest: true
  polling_fallback_minutes: 60
```

`sync_manifest.json` tracks every ingested file by SHA-256 hash. Never double-processes. Detects edits via hash change.

---

## **15\. MASTER CONFIG FILE**

```
# gemvault.config.yaml

project:
  name: "GemVault"
  version: "1.0.0"

sources:
  chat_exports:
    enabled: true
    path: "./data/raw_imports/chat_exports/"
    format: "markdown"
  notion:
    enabled: false
    api_key: "${NOTION_API_KEY}"
    database_ids: []
  google_drive:
    enabled: false
    credentials_path: "${GDRIVE_CREDENTIALS}"
    folder_ids: []

github_sync:
  enabled: true
  repo: ""
  branch: "main"
  webhook_secret: "${GITHUB_WEBHOOK_SECRET}"
  watch_paths:
    - "**/*.md"
  auto_ingest: true
  polling_fallback_minutes: 60

chunking:
  topic_shift_threshold: 0.72
  time_gap_minutes: 30
  min_messages_per_seu: 2
  quality_score_minimum: 0.4

embedding:
  provider: "openai"
  model: "text-embedding-3-large"
  dimensions: 3072
  batch_size: 100
  rate_limit_rpm: 3000

storage:
  chroma:
    persist_directory: "./data/chroma"
    mine_collections:
      - "knowledge_base"
      - "action_outputs"
      - "raw_archive"
    vault_collection: "curated_gems"
  sqlite:
    path: "./data/sqlite/gemvault.db"
  notion_dashboard:
    enabled: false
    database_id: ""

retrieval:
  top_k_initial: 20
  final_k: 5
  quality_boost_threshold: 0.7
  quality_boost_multiplier: 1.3
  cross_ref_boost_multiplier: 1.15
  reranker: "cross-encoder"

llm:
  provider: "openai"
  model: "codex-5.4"
  temperature: 0.1
  top_p: 0.9
  frequency_penalty: 0.3
  max_tokens: 4096

api:
  host: "127.0.0.1"
  port: 8000
  cors_origins:
    - "http://localhost:4321"
    - "http://localhost:3000"

branding:
  theme: "agent_army"
  background: "#050505"
  card: "#0f0f0f"
  popover: "#121212"
  foreground: "#fafafa"
  secondary_foreground: "#c7cbd1"
  muted_foreground: "#9da4af"
  card_border: "#4b5563"
  accent_primary: "#9b5cff"
  accent_secondary: "#2de2e6"
  accent_tertiary: "#ffe44d"
  font_ui: "SUSE"
  font_mono: "SUSE Mono"
```

---

## **16\. BUILD ORDER (dependency sequence)**

```
Phase 1  → setup.sh, config, .env, folder structure, SQLite init
Phase 2  → format_detector first, then parsers (chatgpt, gemini, claude, generic_turn, asset)
Phase 3  → schema models (unified message, standalone asset, SEU, gem, query card)
Phase 4  → chunking (SEU chunker for conversations, section chunker for assets, topic shift detector, deduplicator)
Phase 5  → scoring (quality scorer for SEUs, asset quality scorer for standalone files, cross-reference tracker, signal filters)
Phase 6  → embedding (embedder, batch processor)
Phase 7  → storage (chroma_store, sqlite_store)
Phase 8  → retrieval (vector search, BM25, RRF fusion, metadata filter, reranker)
Phase 9  → agents (summarization first, then classification, query, mining, connection)
Phase 10 → prompts (all system prompts, human card templates)
Phase 11 → translation layer (query translator, mining translator, confidence calc)
Phase 12 → vault (gem crystallizer, vault store, vault retriever, gem linker)
Phase 13 → workbench (manager, gem selector, task router)
Phase 14 → task agents (content, dev, strategy, teaching)
Phase 15 → API (FastAPI server, all routes, middleware)
Phase 16 → GitHub sync (watcher, diff detector, auto-ingest trigger, webhook route)
Phase 17 → frontend (design system components first, then pages, then hooks/lib)
Phase 18 → tests
Phase 19 → docs
Phase 20 → deploy frontend to Vercel
```

**Test each phase in terminal before moving to the next.**

---

## **17\. WHAT'S NOT IN SCOPE (Phase 3 / Future)**

- Cloudflare Workers migration for remote access  
- Notion as a source (connector built but disabled)  
- Google Drive as a source (connector built but disabled)  
- Multi-user auth  
- Mobile UI

