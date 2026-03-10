## A: 
# Product Requirements Document (PRD)

**Project Name:** The Antigravity Loop **Current Phase:** Prototype (V.1) **Primary Stack:** Python (Backend Orchestration), Astro + React + Tailwind (Frontend UI), SQLite/ChromaDB (Local Data), Gemini 3 (AI Core).

## 1. Product Overview & Vision

The Antigravity Loop is an asynchronous, AI-driven project management translator designed specifically for neurodivergent (ND) solo-founders and blended (human + AI) globally distributed teams.

Traditional PM tools cause friction by forcing users to categorize, tag, and structure thoughts before they are ready. The Antigravity Loop solves this by separating _capture_ from _structuring_. It allows the user to dump raw, multimodal chaos into a frictionless inbox, uses an AI agent to extract a strict 9-point execution framework, and displays only the immediate next micro-action.

## 2. Target Audience & User Profiles

*   **The ND Solo-Founder:** Needs a place to brain-dump without losing momentum; suffers from executive dysfunction when faced with compound tasks or context-switching.
    
*   **The Asynchronous Doer:** Wants to be unleashed on a single task without attending status meetings or navigating complex boards.
    
*   **The AI Agent:** Needs highly structured, unambiguous JSON payloads to execute programmatic tasks.
    

## 3. Core Workflow (The Loop)

1.  **Frictionless Capture (Input):** User drops unstructured text, voice, or links into a Notion "Ugly Inbox".
    
2.  **AI Translation (Processing):** A local Python script polls the Notion API and feeds the data to a local Gemini Agent.
    
3.  **Contextual Memory (RAG):** The system queries ChromaDB to reference past frameworks to reduce repetitive instructions.
    
4.  **Structuring (Extraction):** The AI extracts the 9-Point Mission Framework (strictly enforcing the "No-Compound Micro-Action" rule) and outputs valid JSON.
    
5.  **Dashboard Routing (Storage/UI):** Data is written to SQLite and displayed on a Vercel-hosted Astro/React dashboard for visual review and editing.
    
6.  **Execution Handoff (Alerts):** Python triggers a native macOS notification pushing _only_ the single next micro-action to the user.
    

## 4. Key Features & Requirements (V.1 Prototype)

*   **The 9-Point Extractor:** AI must strictly adhere to the `extractor_prompt.md` rules. If data is missing, it must flag the field with `REQUIRES_INPUT` rather than hallucinating.
    
*   **Editable UI Source of Truth:** The Vercel dashboard must allow the user to easily edit `REQUIRES_INPUT` fields. This UI update must write back to the local SQLite database.
    
*   **Single-Action Alerts:** The notification system must never send a batch of tasks. It only alerts the user of Micro-Action #1.
    

## 5. Design & UX Guidelines (The Vibe)

_To be filled by the founder prior to V.1 Tech Spec generation to ensure cognitive comfort and brand alignment._

*   **Primary Font (Headings):** [Insert Google Font]
    
*   **Secondary Font (Body):** [Insert Google Font]
    
*   **Color Palette:** [Insert Hex Codes for Background, Primary Accent, Warning/Requires Input, Text]
    
*   **Styling Rules:** [e.g., Heavy drop shadows, rounded corners, dark mode default, minimalist borders]
    

## 6. Out of Scope for V.1

*   External SMS or WhatsApp notifications.
    
*   Multi-user authentication (multiplayer mode).
    
*   Ingesting data from Apple iCloud Files or Google Workspace (Notion API only for V.1).
    
*   Cloud-hosted databases (Strictly local SQLite/Chroma for V.1).
    

## 7. Success Metrics for Prototype

*   **Time to Capture:** Takes < 5 seconds to offload a thought.
    
*   **Extraction Accuracy:** Agent correctly parses the 9-point framework without hallucination > 90% of the time.
    
*   **Execution Rate:** Increase in single micro-actions completed per day due to reduced context-switching anxiety.

