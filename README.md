# Turn By Turn Chat RAG Files 🚀

This repository contains a collection of markdown files, project summaries, and automation scripts for the Turn By Turn Chat RAG project.

## 🤖 Automated Git Sync (Agent Watcher)

To ensure this folder is always backed up to GitHub in real-time, I've included a powerful Git sync utility: `git_sync.py`.

### Key Features:
- **Instant Sync**: Automatically detects when you add or modify a file and pushes it to GitHub after a short delay (5 seconds of silence).
- **Native Notifications**: Displays a macOS notification banner whenever a sync is successful or fails.
- **Version Handling**: If you download or save a versioned file (e.g., `MyNotes (1).md`), the script automatically overwrites the original `MyNotes.md` and removes the duplicate version.
- **Fail-Safe History**: Works with a clean Git history approach to avoid conflicts and security blockades.

### 💡 Pro-Tip: Disabling Notifications
Once you are comfortable with the auto-pusher and no longer need the visual confirmation, you can simply ask the agent:
> *"Please disable the macOS notifications in the git sync script."*

### 🚀 How to Use

#### Method 1: Desktop Shortcut (Mac Only)
Simply double-click the **`start_watcher.command`** file on your Desktop. This will open a Terminal window and start the sync service automatically.

#### Method 2: Manual Terminal Command
If you prefer running it manually, navigate to this folder and run:
```bash
python3 git_sync.py
```

## 🛠 Setup & Requirements
- **Python 3.9+**
- **Watchdog Library**: `pip install watchdog`

## ⏭️ Development Focus
- Google Apps Script debugging for email and calendar automation.
- RAG (Retrieval-Augmented Generation) thread management.
- Brand alignment and asset generation.

---
*Created and maintained with love by your Antigravity AI Agent.*
