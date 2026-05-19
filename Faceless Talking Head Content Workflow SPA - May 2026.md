## `FOR NDs LIKE ME`

# **Content Automation SPA Master Build Plan**

#### **How to Use This Document**

- `Work top to bottom, one checkbox at a time`  
- `Never skip ahead to a later phase`  
- `Each checkbox is a single, completable action — not a project`  
- `If a step feels too big, stop and break it into smaller steps before starting it`  
- `Done means done. Checked means checked. Move on.`

---

## **Before You Touch Any Code — One-Time Account Setup**

##### `These are prerequisites for ALL versions. Do these first, in order. Nothing else starts until this list is complete.`

- [ ] `Create account at neon.tech — free, no credit card needed`  
- [ ] `Create account at replicate.com — free to create`  
- [ ] `Fund Replicate account with $10 prepaid credits (covers ~900 voice generations)`  
- [ ] `Enable auto-reload in Replicate billing settings at $5 threshold`  
- [ ] `Create account at hedra.com — free tier`  
- [ ] `Confirm you have access to Hedra API key in developer settings`  
- [ ] `Log into dash.cloudflare.com — confirm R2 is available on your account`  
- [ ] `Create an R2 bucket — name it something like content-pipeline-media`  
- [ ] `Confirm your Cloudflare Workers plan is downgraded to free — you don't need paid`  
- [ ] `Get your Claude API key at console.anthropic.com → API Keys`  
- [ ] `Confirm your Loops account is active and API key is accessible`  
- [ ] `Record a clean voice sample — 15–30 seconds, quiet room, no music, WAV or MP3`  
- [ ] `Upload that voice sample to your R2 bucket — copy and save the URL somewhere`  
- [ ] `Save your AI avatar image — upload it to R2 as well, copy and save the URL`  
- [ ] `Create a single secure document or password manager note with all API keys and URLs recorded`

`One rule: Don't start V1 build steps until every box above is checked.`

---

## **V1 — The Core Pipeline**

##### `Goal: One topic in → one approved, polished video out → you download and schedule manually`

### **V1 STEP 1 — Neon Database Schema**

*`Nothing else can be built until the database exists. This is the foundation.`*

- [ ] `Create a new Neon project for this app specifically`  
- [ ] `Create a jobs table with these columns:`  
      - `id (UUID, primary key)`  
      - `topic (text)`  
      - `script (text, nullable)`  
      - `status (text)`  
      - `audio_url (text, nullable)`  
      - `raw_video_url (text, nullable)`  
      - `polished_video_url (text, nullable)`  
      - `created_at (timestamp)`  
      - `updated_at (timestamp)`  
- [ ] `Confirm these status values are documented somewhere you can reference:`

```
pending_script
script_generating
awaiting_script_approval
script_approved
script_rejected
audio_generating
video_generating
video_polishing
awaiting_video_approval
video_approved
video_rejected
ready_to_download
failed
```

- [ ] `Test the connection from your SPA codebase to Neon — confirm it connects cleanly`

---

### **V1 STEP 2 — SPA Shell \+ Dashboard UI**

*`Build the interface before the logic. You need somewhere to see what's happening.`*

- [ ] `Create the main dashboard page — shows a list of all jobs with their current status`  
- [ ] `Each job in the list shows: topic, status badge, created date`  
- [ ] `Create a "New Video" input form — single text field for topic/brief, submit button`  
- [ ] `Create the Gate 1 approval screen — shows script text, Approve button, Edit button, Reject button`  
- [ ] `Create the Gate 2 approval screen — shows video preview player, Approve button, Reject button`  
- [ ] `Create a Download button on approved jobs — pulls final video URL from R2`  
- [ ] `Confirm all screens are mobile-friendly — you may approve from your phone`

---

### **V1 STEP 3 — Script Generation Endpoint**

*`First automated worker. Cheapest step. Build and test this in isolation before connecting anything else.`*

- [ ] `Create an API route that accepts a job_id and topic`  
- [ ] `Route calls Claude API with your topic + a system prompt defining your brand voice and script format`  
- [ ] `Script is stored in Neon jobs table under the correct job_id`  
- [ ] `Job status updates to awaiting_script_approval`  
- [ ] `Test this endpoint manually — submit a topic, confirm script appears in DB`  
- [ ] `Confirm script quality looks right before moving on`

---

### **V1 STEP 4 — Email Alert System**

*`Wire up Loops now so every status change notifies you. Build this before the expensive steps.`*

- [ ] `Create a Loops transactional email template for Gate 1 — "Your script is ready to review"`  
- [ ] `Create a Loops transactional email template for Gate 2 — "Your video is ready to approve"`  
- [ ] `Create a Loops transactional email template for completion — "Your video is ready to download"`  
- [ ] `Add Loops API call to script generation endpoint — fires when status hits awaiting_script_approval`  
- [ ] `Test the full alert — submit a topic, confirm email arrives with correct content`

---

### **V1 STEP 5 — Voice Generation Endpoint**

*`This is where Replicate credits get spent. Only build after Gate 1 is working.`*

- [ ] `Create an API route that accepts a job_id`  
- [ ] `Route pulls the approved script from Neon for that job`  
- [ ] `Route calls Replicate API using model: bzikst/xtts-v2-fork:35f3f05f8ed49b1808760f01caeb85a78b7b8967b838f0e4021e75a3e621fc8d`  
- [ ] `Pass the script text + your voice sample R2 URL as the speaker reference`  
- [ ] `Poll Replicate until the job completes`  
- [ ] `Download the returned audio file and upload it to your R2 bucket`  
- [ ] `Store the R2 audio URL in Neon jobs.audio_url`  
- [ ] `Update job status to audio_generating → video_generating on completion`  
- [ ] `Test with one approved script — confirm audio file sounds like you`

---

### **V1 STEP 6 — Avatar Video Endpoint**

*`Hedra takes the audio and your avatar image and produces a raw talking head video.`*

- [ ] `Create an API route that accepts a job_id`  
- [ ] `Route pulls audio_url and uses your stored avatar image R2 URL`  
- [ ] `Route calls Hedra API — passes audio URL + avatar image URL`  
- [ ] `Poll Hedra until video generation completes`  
- [ ] `Download the raw video and upload it to your R2 bucket`  
- [ ] `Store the R2 raw video URL in Neon jobs.raw_video_url`  
- [ ] `Update job status to video_polishing`  
- [ ] `Test with one audio file — confirm the avatar lip-syncs correctly`

---

### **V1 STEP 7 — Video Polish Step**

*`Remotion takes the raw video and makes it publish-ready. Captions, titles, music, overlays.`*

- [ ] `Install Remotion in your project: npx create-video or add to existing project`  
- [ ] `Build a Remotion composition that accepts: raw video URL, script text, job metadata`  
- [ ] `Composition adds: captions (auto-generated from script), title card, background music, outro`  
- [ ] `Create an API route that triggers the Remotion render for a given job_id`  
- [ ] `Rendered video uploads to R2 bucket`  
- [ ] `Store the R2 polished video URL in Neon jobs.polished_video_url`  
- [ ] `Update job status to awaiting_video_approval`  
- [ ] `Fire Loops Gate 2 email alert`  
- [ ] `Test end to end — confirm polished video looks publish-ready`

---

### **V1 STEP 8 — Video Preview \+ Download**

*`The final piece of the UI. You need to be able to watch and download the finished video.`*

- [ ] `Wire the Gate 2 approval screen to pull polished_video_url from Neon`  
- [ ] `Confirm video streams directly from R2 in the dashboard player — no buffering issues`  
- [ ] `Approve button updates job status to video_approved → ready_to_download`  
- [ ] `Reject button updates job status to video_rejected and allows re-triggering polish step`  
- [ ] **`Download button`** `pulls the polished video file from R2 to your device`  
- [ ] `Fire Loops completion email on approval`  
- [ ] `Test the full end-to-end pipeline one complete time with a real topic`

---

### **V1 Complete — Definition of Done**

`V1 is finished when you have submitted a real topic, approved a real script, heard your voice clone read it, watched your avatar lip-sync it, approved the polished video, downloaded it, and posted it manually to your platform of choice.`

**`Do not start V2 until you have done this 10 times with real content you actually posted.`**

---

## **V2 — Batch Mode \+ Workflow Orchestration**

##### `Goal: Submit multiple topics at once, pipeline runs in parallel, approve in batches`

*`Only start V2 after V1 has produced 10 real posted videos.`*

### 

### **V2 STEP 1 — Add Inngest**

*`Inngest is the orchestration layer that makes parallel jobs and HITL pauses reliable at scale.`*

- [ ] `Create account at inngest.com — free tier`  
- [ ] `Save Inngest API key to your secure key document`  
- [ ] `Install Inngest SDK in your project: npm install inngest`  
- [ ] `Create your Inngest client and connect it to your SPA`  
- [ ] `Confirm Inngest dashboard shows your app connected`

---

### **V2 STEP 2 — Rebuild Pipeline as Inngest Workflow**

*`Each V1 API route becomes an Inngest step function. This is the core V2 migration.`*

- [ ] `Convert script generation to an Inngest step function`  
- [ ] `Add waitForEvent pause after script generation — waits for your approval signal`  
- [ ] `Convert voice generation to an Inngest step function with auto-retry on failure`  
- [ ] `Convert avatar video generation to an Inngest step function with auto-retry`  
- [ ] `Convert video polish to an Inngest step function`  
- [ ] `Add waitForEvent pause after video polish — waits for your approval signal`  
- [ ] `Wire dashboard Approve/Reject buttons to send the correct Inngest resume events`  
- [ ] `Test a single job through the new Inngest pipeline end to end before adding batch`

---

### **V2 STEP 3 — Batch Input UI**

*`Now that the pipeline is durable, you can safely run multiple jobs in parallel.`*

- [ ] `Replace single topic input with a batch input form — accepts 5–10 topics at once`  
- [ ] `Each submitted topic creates a separate job record in Neon`  
- [ ] `Each job triggers its own Inngest workflow run independently`  
- [ ] `Dashboard job list shows all active jobs with individual status badges`  
- [ ] `Test submitting 3 topics at once — confirm 3 independent pipelines run in parallel`

---

### **V2 STEP 4 — Batch Approval UI**

*`Review and approve multiple scripts or videos in one session instead of one at a time.`*

- [ ] `Build a Gate 1 batch screen — shows all jobs with status awaiting_script_approval in one view`  
- [ ] `Each script is expandable/readable inline`  
- [ ] **`Approve All`** `button and individual approve/reject per script`  
- [ ] `Build a Gate 2 batch screen — shows all jobs with status awaiting_video_approval in one view`  
- [ ] `Each video is previewable inline`  
- [ ] `Individual approve/reject per video`  
- [ ] `Test approving a batch of 3 scripts at once — confirm all 3 pipelines resume correctly`

---

### **V2 STEP 5 — Retry Logic \+ Cost Tracking**

*`Protect yourself from silent failures and surprise costs.`*

- [ ] `Add retry configuration to Hedra and Replicate Inngest steps — 3 retries with backoff`  
- [ ] `Add failed status handling — job moves to failed state after max retries, email alert fires`  
- [ ] `Add a cost estimate field to each job in Neon — calculated from Replicate + Hedra usage`  
- [ ] `Add a cost summary view to dashboard — total spend this month, average cost per video`  
- [ ] `Test a simulated failure — confirm retry fires and job recovers automatically`

---

### **V2 Complete — Definition of Done**

`V2 is finished when you can submit 5 topics on Monday morning, approve all 5 scripts in one batch session, and have 5 finished videos waiting for your Gate 2 approval by end of day — without touching anything in between.`

---

## **V3 — Browser Automation Publishing**

##### `Goal: Eliminate manual scheduling — Playwright posts approved videos directly to your platform`

*`Only start V3 after V2 batch mode is running smoothly and manual scheduling has become your actual bottleneck.`*

### **V3 STEP 1 — Build Playwright Agent for Primary Platform**

*`Start with one platform only. Do not expand until this works reliably.`*

- [ ] `Install Playwright: npm install playwright`  
- [ ] `Identify your primary posting platform — the one you post to most`  
- [ ] `Store your social login credentials as environment variables — never in code`  
- [ ] `Build a Playwright script that:`  
      - `Opens your platform in a headless browser`  
      - `Logs in using your stored credentials`  
      - `Navigates to the upload/create flow`  
      - `Uploads the video file from R2`  
      - `Pastes the caption`  
      - `Sets the publish time`  
      - `Submits the post`  
- [ ] `Test this script manually and repeatedly before connecting it to the pipeline`  
- [ ] `Confirm it handles login session expiry gracefully — re-authenticates when needed`

---

### **V3 STEP 2 — Caption \+ Hashtag Generation**

*`Claude writes platform-optimized captions so you don't have to.`*

- [ ] `Add a caption generation step to the Inngest workflow — fires after Gate 2 approval`  
- [ ] `Claude API call takes: script text, platform name, your brand voice guidelines`  
- [ ] `Returns: platform-optimized caption + relevant hashtags`  
- [ ] `Store caption and hashtags in Neon job record`  
- [ ] `Display caption in Gate 2 approval screen — editable before you approve`  
- [ ] `Test caption quality across a few videos before automating`

---

### **V3 STEP 3 — Publish Scheduler UI**

*`Set when each video posts from inside your dashboard.`*

- [ ] `Add platform selector to Gate 2 approval screen — which platform(s) to post to`  
- [ ] `Add publish time picker — date and time per platform`  
- [ ] `Store platform + publish time in Neon job record on approval`  
- [ ] `Connect Playwright agent to Inngest as the final workflow step`  
- [ ] `Inngest waits until scheduled publish time, then triggers Playwright`  
- [ ] `Neon job status updates to publishing → published on completion`  
- [ ] `Loops email fires confirming successful post`

---

### **V3 STEP 4 — Stability \+ Expansion**

*`Make it reliable before you trust it. Expand only after it's proven.`*

- [ ] `Run V3 on your primary platform for at least 2 weeks before expanding`  
- [ ] `Add fallback handling — if Playwright fails, email alert fires and you post manually`  
- [ ] `Keep native scheduling as a permanent fallback — never remove it`  
- [ ] `Only after primary platform is stable: expand Playwright to a second platform`  
- [ ] `Repeat stability testing before adding a third`

---

### **V3 Complete — Definition of Done**

`V3 is finished when you can approve a video on Tuesday, set a Thursday publish time, and wake up Thursday to a confirmation email that it posted — without touching anything in between.`

---

## **V4 — Future Considerations**

##### `Do not build any of this yet. File it away.`

| `Feature` | `What It Unlocks` | `When To Consider It` |
| :---- | :---- | :---- |
| `Google Flow B-roll integration` | `Auto-generated cinematic B-roll in Remotion` | `When your videos feel visually flat` |
| `XTTS-v2 voice sample refresh` | `Re-train clone on new voice samples` | `When clone quality drifts from your real voice` |
| `Viral scoring agent` | `Claude scores video before Gate 2` | `When you're producing more than you can review` |
| `Auto-topic generation` | `Claude generates topic ideas from trending content` | `When topic ideation becomes your bottleneck` |
| `Content calendar view` | `Full scheduling calendar inside your SPA` | `When you're managing 30+ videos per month` |

---

## **Master Reference — All API Keys \+ Where To Get Them**

| `Key` | `Where To Get It` | `Needed In` | `Cost` |
| :---- | :---- | :---- | :---- |
| `Claude API`  | `console.anthropic.com → API Keys` | `V1 Day 1` | `Pay per token` |
| `Replicate API` | `replicate.com → Account Settings` | `V1 Day 1` | `Prepaid ~$0.011/run` |
| `Hedra API` | `hedra.com → Developer Settings` | `V1 Day 1` | `Free tier` |
| `Cloudflare R2` | `dash.cloudflare.com → R2` | `V1 Day 1` | `Free tier` |
| `Loops API` | `loops.so → Settings → API` | `V1 Day 1` | `Free tier` |
| `Inngest API` | `inngest.com → API Keys` | `V2` | `Free tier` |
| `Playwright` | `npm install playwright` | `V3` | `Free / open source` |
| `Social Logins` | `LI, IG, SS, FB Mac passwords` | `V3` | `Free`  |

---

## **The One Rule That Protects Everything**

##### `Earn each version before you build the next one.`

- `V1 proves the pipeline works.`   
- `V2 makes it scale.`   
- `V3 makes it hands-off.` 

`Skipping ahead is how half-built systems get abandoned.`