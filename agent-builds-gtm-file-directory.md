# **File Directory**

Claude Opus 4.6 defines this as the full monorepo structure.

```
growthops/
│
├── README.md                          # Project overview + setup instructions
├── .gitignore                         # Node modules, .env, etc.
├── .env                               # Shared environment variables (gitignored)
├── .env.example                       # Template for .env (committed)
├── package.json                       # Root package.json (workspaces config)
│
├── agents/
│   │
│   ├── shared/                        # Shared utilities across all agents
│   │   ├── notionClient.js            # Singleton Notion API client
│   │   ├── notionHelpers.js           # Common Notion CRUD operations
│   │   ├── notifier.js                # MacOS popup notification wrapper
│   │   ├── logger.js                  # Standardized logging (console + Notion)
│   │   ├── rateLimiter.js             # Shared rate limiting logic
│   │   ├── retryHandler.js            # Shared retry/backoff logic
│   │   ├── budgetTracker.js           # API cost tracking across agents
│   │   ├── envManager.js              # Read/write .env helper (for auto DB IDs)
│   │   └── constants.js               # Shared enums (statuses, agent names, etc.)
│   │
│   ├── social-intel-collector/        # AGENT 1
│   │   ├── index.js                   # Entry point + CRON scheduler
│   │   ├── scraper.js                 # Google Dorks + Puppeteer browser automation
│   │   ├── scorer.js                  # OpenAI pain scoring logic
│   │   ├── notionWriter.js            # Leads DB creation + lead writing
│   │   ├── config.js                  # Search terms, thresholds, rate limits
│   │   ├── package.json               # Agent-specific dependencies
│   │   └── README.md                  # Agent-specific docs + usage
│   │
│   ├── outreach-generator/            # AGENT 2
│   │   ├── index.js                   # Entry point + mode selector
│   │   ├── notionReader.js            # Fetch leads with status "New"
│   │   ├── messageGenerator.js        # OpenAI personalized message creation
│   │   ├── notionUpdater.js           # Write messages + update status + comments
│   │   ├── approvalWatcher.js         # Poll Notion for HITL approvals
│   │   ├── loopsSender.js             # Send via Loops API or flag manual
│   │   ├── config.js                  # Voice doc, templates, rate limits
│   │   ├── package.json               # Agent-specific dependencies
│   │   └── README.md                  # Agent-specific docs + usage
│   │
│   ├── discovery-prep-assistant/      # AGENT 3
│   │   ├── index.js                   # Entry point + polling/CLI modes
│   │   ├── statusWatcher.js           # Poll Notion for "Booked" status
│   │   ├── scraper.js                 # Puppeteer LinkedIn + website scraping
│   │   ├── researcher.js              # Gemini research synthesis
│   │   ├── notionWriter.js            # Call Prep DB creation + doc writing
│   │   ├── config.js                  # Research prompts, scraping settings
│   │   ├── package.json               # Agent-specific dependencies
│   │   └── README.md                  # Agent-specific docs + usage
│   │
│   └── workflow-orchestrator/         # AGENT 4
│       ├── index.js                   # Entry point + CRON + CLI mode selector
│       ├── agentRunner.js             # Spawn child processes, monitor, timeout
│       ├── businessRules.js           # Budget caps, lead thresholds, rate limits
│       ├── notionManager.js           # Commands DB + Logs DB creation + mgmt
│       ├── hitlManager.js             # HITL checkpoint detection + resume
│       ├── statusDashboard.js         # ASCII CLI status display
│       ├── config.js                  # All thresholds and settings
│       ├── package.json               # Agent-specific dependencies
│       └── README.md                  # Agent-specific docs + usage
│
├── dashboard/                         # VERCEL FRONTEND (Astro + React)
│   │
│   ├── astro.config.mjs               # Astro SSR config (Vercel adapter)
│   ├── tailwind.config.mjs            # Tailwind config (design system tokens)
│   ├── package.json                   # Dashboard dependencies
│   ├── tsconfig.json                  # TypeScript config (if using TS)
│   ├── vercel.json                    # Vercel deployment config
│   │
│   ├── public/
│   │   ├── favicon.svg                # GrowthOps favicon
│   │   └── fonts/
│   │       ├── SUSE-Variable.woff2    # Heading font
│   │       └── SUSEMono-Variable.woff2 # Body/code font
│   │
│   ├── src/
│   │   │
│   │   ├── layouts/
│   │   │   └── MainLayout.astro       # Base layout (nav, sidebar, dark mode)
│   │   │
│   │   ├── pages/
│   │   │   ├── index.astro            # Dashboard home (pipeline overview)
│   │   │   ├── leads.astro            # Leads view (table + filters)
│   │   │   ├── outreach.astro         # Outreach view (message approval)
│   │   │   ├── call-prep.astro        # Call prep view (research docs)
│   │   │   ├── system.astro           # System view (logs + health)
│   │   │   └── api/
│   │   │       ├── leads.js           # API route: fetch/update leads
│   │   │       ├── outreach.js        # API route: approve/send messages
│   │   │       ├── call-prep.js       # API route: fetch/update call prep
│   │   │       ├── commands.js        # API route: trigger agents
│   │   │       ├── logs.js            # API route: fetch system logs
│   │   │       └── status.js          # API route: system health check
│   │   │
│   │   ├── components/
│   │   │   │
│   │   │   ├── layout/
│   │   │   │   ├── Sidebar.jsx        # Navigation sidebar
│   │   │   │   ├── TopBar.jsx         # Top bar (status indicators + actions)
│   │   │   │   └── ActionBadge.jsx    # HITL action notification badges
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   ├── PipelineOverview.jsx    # Lead counts by status (cards)
│   │   │   │   ├── TodayMetrics.jsx        # Today's activity numbers
│   │   │   │   ├── AgentStatusPanel.jsx    # Agent last-run indicators
│   │   │   │   └── HITLActionQueue.jsx     # Pending human actions list
│   │   │   │
│   │   │   ├── leads/
│   │   │   │   ├── LeadsTable.jsx          # Filterable/sortable leads table
│   │   │   │   ├── LeadRow.jsx             # Individual lead row
│   │   │   │   ├── LeadDetail.jsx          # Expanded lead view (slide-out)
│   │   │   │   ├── LeadFilters.jsx         # Filter controls
│   │   │   │   └── PainScoreBadge.jsx      # Visual pain score indicator
│   │   │   │
│   │   │   ├── outreach/
│   │   │   │   ├── MessageApprovalQueue.jsx # Leads awaiting approval
│   │   │   │   ├── MessageComparison.jsx    # Side-by-side V1/V2/V3
│   │   │   │   ├── ApproveButton.jsx        # One-click approve action
│   │   │   │   ├── ManualSendQueue.jsx      # Copy-to-clipboard queue
│   │   │   │   └── SentHistory.jsx          # Sent message log
│   │   │   │
│   │   │   ├── call-prep/
│   │   │   │   ├── CallPrepList.jsx         # Upcoming calls list
│   │   │   │   ├── CallPrepDetail.jsx       # Full prep doc view
│   │   │   │   ├── CallNotes.jsx            # During/after call notes
│   │   │   │   ├── OutcomeLogger.jsx        # Outcome dropdown + value input
│   │   │   │   └── CalendarView.jsx         # Calendar-style call view
│   │   │   │
│   │   │   ├── system/
│   │   │   │   ├── ActivityLog.jsx          # System logs feed
│   │   │   │   ├── CommandHistory.jsx       # Agent commands history
│   │   │   │   ├── BudgetTracker.jsx        # API cost visualization
│   │   │   │   ├── ErrorLog.jsx             # Errors with resolution
│   │   │   │   └── HealthIndicators.jsx     # System health status
│   │   │   │
│   │   │   └── shared/
│   │   │       ├── StatusBadge.jsx          # Reusable status pill
│   │   │       ├── DataCard.jsx             # Reusable metric card
│   │   │       ├── Modal.jsx               # Reusable modal wrapper
│   │   │       ├── Toast.jsx               # Notification toasts
│   │   │       ├── LoadingSpinner.jsx       # Loading state
│   │   │       ├── EmptyState.jsx           # No data state
│   │   │       ├── CopyButton.jsx           # Copy-to-clipboard
│   │   │       └── AgentTriggerButton.jsx   # "Run Agent X" button
│   │   │
│   │   ├── lib/
│   │   │   ├── notion.js              # Notion API client for dashboard
│   │   │   ├── formatters.js          # Date, currency, text formatters
│   │   │   └── constants.js           # Shared constants (colors, statuses)
│   │   │
│   │   └── styles/
│   │       └── global.css             # Global styles + Tailwind imports
│   │
│   └── README.md                      # Dashboard-specific docs
│
└── docs/
    ├── prd-agent-1-social-intel-collector.md
    ├── prd-agent-2-outreach-generator.md
    ├── prd-agent-3-discovery-prep-assistant.md
    ├── prd-agent-4-workflow-orchestrator.md
    ├── prd-dashboard.md
    ├── architecture-overview.md        # System architecture diagram
    ├── notion-database-schemas.md      # All DB schemas in one place
    ├── api-cost-estimates.md           # Budget breakdown
    └── deployment-guide.md             # How to deploy everything

```

---

## **🎯 KEY ARCHITECTURAL DECISIONS IN THIS STRUCTURE:**

### **1\. Shared Utilities (`agents/shared/`)**

This is what makes it a **framework** not just 4 scripts:

- `notionClient.js` \= One Notion connection, all agents use it  
- `logger.js` \= Standardized logging format across all agents  
- `rateLimiter.js` \= One rate limiter, shared rules  
- `budgetTracker.js` \= Tracks API spend across ALL agents (prevents budget blowout)  
- `constants.js` \= Status enums, agent names, etc. defined ONCE

**Why this matters:** When you build your next workflow (course creator), you copy `agents/shared/` and it just works.

### **2\. Each Agent Has Its Own `package.json`**

- Agents can have different dependencies  
- Can be deployed independently later (Cloudflare Workers)  
- Can be versioned independently  
- Keeps installs lean

### **3\. Dashboard API Routes (`dashboard/src/pages/api/`)**

- Vercel serverless functions that talk to Notion  
- Dashboard frontend calls these routes (not Notion directly)  
- Keeps Notion API key server-side only (security)  
- Each route handles one domain (leads, outreach, commands, etc.)

### **4\. Component Organization by Domain**

- `components/dashboard/` \= Home page components  
- `components/leads/` \= Leads page components  
- `components/outreach/` \= Outreach page components  
- `components/shared/` \= Reusable across all pages

**Why:** You find things fast. ND brain doesn't have to hunt.

### **5\. Docs Folder**

- All PRDs live here  
- Architecture overview for when you forget how it works  
- Deployment guide for when you need to redeploy  
- **Also useful when selling:** "Here's the documentation for the system I'm building you"

---

