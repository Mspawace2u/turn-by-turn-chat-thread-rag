# Automator Routing Setup — SPA Spec Repo Files

Use this guide to update the existing macOS Automator + Python routing workflow so downloaded markdown files that start with `spa-spec-repo-` move into the SPA spec repo instead of the turn-by-turn chat thread repo.

This guide is written for both:

- Patty, for human-readable setup logic
- an agent coder, for safe implementation handoff

---

## Goal

When a markdown file lands in the Downloads folder, route it based on filename.

SPA spec files should follow this naming convention:

```txt
spa-spec-repo-[app-name]-v1.md
```

Example:

```txt
spa-spec-repo-rules-generator-v1.md
```

Any file starting with:

```txt
spa-spec-repo-
```

should be moved to:

```txt
/devops-ip-rag/spa-spec-repo
```

The full local path will include the drive, user, Desktop, or synced folder structure before that repo path. Set the exact full path inside the Python script or Automator configuration.

---

## Core Routing Rule

```txt
Downloads Folder/
├── If filename starts with: spa-spec-repo-
│   └── Move to: /devops-ip-rag/spa-spec-repo
├── Else if filename matches turn-by-turn chat thread rules
│   └── Move to existing chat thread repo
└── Else
    └── Leave alone or follow existing rules
```

The `spa-spec-repo-` rule must run before the broader markdown routing rule.

Order matters.

If the general `.md` rule runs first, it may move SPA spec files to the wrong repo.

---

## Filename Convention

Use this format:

```txt
spa-spec-repo-[app-name]-v1.md
```

Rules:

- Start every SPA spec repo file with `spa-spec-repo-`
- Use the final app/folder name from the LDE path as `[app-name]`
- Use `-v1`, `-v2`, etc. for versioning
- Do not use a double underscore
- Do not add `-spec` after the version
- Keep names lowercase and hyphenated

Example LDE path:

```txt
/Volumes/Sandbox/agents/rules-generator
```

Correct filename:

```txt
spa-spec-repo-rules-generator-v1.md
```

Incorrect filenames:

```txt
spa-spec-repo-rules-generator__v1-spec.md
spa-spec-repo-rules-generator-v1-spec.md
spa-spec-repo-/Volumes/Sandbox/agents/rules-generator-v1.md
```

---

## Human Setup Steps

### 1. Locate the existing Automator workflow

Find the Automator workflow that currently watches the Downloads folder.

Likely behavior:

```txt
Downloads Folder/
└── Automator folder action
    └── runs a Python script or shell command
```

Do not rebuild the whole workflow unless necessary.

The likely better move is to update the Python routing logic.

---

### 2. Locate the Python script

Find the script currently used by Automator.

Look for clues such as:

- Automator “Run Shell Script” action
- a `.py` file path inside Automator
- a script stored in a local automation folder
- rules that move markdown downloads into the turn-by-turn chat thread repo

Before editing it, duplicate the file as a backup.

Suggested backup format:

```txt
original-script-name.backup.py
```

---

### 3. Add the SPA spec repo route first

The new route should be checked before any broad `.md` rule.

Pseudo-logic:

```python
if filename.startswith("spa-spec-repo-") and filename.endswith(".md"):
    move_to_spa_spec_repo()
elif existing_chat_thread_rule_matches(filename):
    move_to_chat_thread_repo()
else:
    use_existing_behavior()
```

This prevents the current broad markdown rule from grabbing SPA spec files first.

---

### 4. Set the full destination path

Use the actual local path to the nested SPA spec repo.

Placeholder:

```txt
/FULL/LOCAL/PATH/devops-ip-rag/spa-spec-repo
```

Example shape only:

```txt
/Users/[mac-user]/Desktop/[synced-folder]/devops-ip-rag/spa-spec-repo
```

Do not guess the path.

Verify it from Finder or Terminal before saving the script.

---

### 5. Add an exclusion to the chat-thread rule

The existing turn-by-turn chat thread repo rule should ignore any file that starts with:

```txt
spa-spec-repo-
```

Pseudo-logic:

```python
if filename.startswith("spa-spec-repo-"):
    route_to_spa_spec_repo()
elif filename.endswith(".md"):
    route_to_chat_thread_repo()
```

Do not use:

```python
if filename.endswith(".md"):
```

as the first condition unless SPA spec files are already excluded.

That is how routing gets rude.

---

### 6. Test with fake files

Create test files in Downloads:

```txt
spa-spec-repo-rules-generator-v1.md
regular-chat-thread-export.md
random-notes.txt
```

Expected result:

```txt
spa-spec-repo-rules-generator-v1.md
└── moves to /devops-ip-rag/spa-spec-repo

regular-chat-thread-export.md
└── moves according to existing chat thread rule

random-notes.txt
└── stays put or follows existing non-md behavior
```

Run the test before trusting the automation.

---

## Agent Coder Handoff Prompt

```md
# Task: Update macOS Automator Python Routing for SPA Spec Repo Files

You are updating an existing macOS Automator folder-action workflow that watches the Downloads folder and routes downloaded markdown files into local repos.

## Objective

Add a new routing condition for SPA spec repo markdown files.

Any downloaded `.md` file whose filename starts with:

```txt
spa-spec-repo-
```

must move to the local SPA spec repo folder:

```txt
/FULL/LOCAL/PATH/devops-ip-rag/spa-spec-repo
```

The exact full local path must be verified before editing.

## Required Filename Convention

```txt
spa-spec-repo-[app-name]-v1.md
```

Rules:

- `[app-name]` is only the final app/folder name from the LDE pathway
- no double underscore
- no `-spec` after `v1`
- filename must start with `spa-spec-repo-`

## Safety Requirements

Before editing:

1. Locate the existing Automator workflow.
2. Locate the Python script Automator runs.
3. Confirm the current routing behavior.
4. Back up the current Python script.
5. Verify the full destination path exists.

Do not rewrite the whole script unless necessary.

## Routing Logic Required

The SPA spec repo condition must run before the broader markdown / chat-thread condition.

Use this order:

```python
if filename.startswith("spa-spec-repo-") and filename.endswith(".md"):
    move file to SPA spec repo
elif existing chat-thread markdown rule matches:
    move file to chat-thread repo
else:
    preserve existing behavior
```

## Do Not

- Do not move SPA spec files into the turn-by-turn chat thread repo.
- Do not remove existing routing rules.
- Do not change unrelated Automator behavior.
- Do not guess the destination path.
- Do not delete files during testing.
- Do not overwrite existing files without a collision-safe rule.

## Collision Handling

If the destination already contains a file with the same name, do not overwrite silently.

Use one of these options:

- append a timestamp
- append `-copy`
- stop and report the collision

Prefer timestamp if no existing convention is present.

## Test Cases

Create or use test files:

```txt
spa-spec-repo-rules-generator-v1.md
regular-chat-thread-export.md
random-notes.txt
```

Expected behavior:

```txt
spa-spec-repo-rules-generator-v1.md
→ /devops-ip-rag/spa-spec-repo

regular-chat-thread-export.md
→ existing chat-thread repo route

random-notes.txt
→ unchanged unless existing rules say otherwise
```

## Completion Report

Return:

- script file edited
- backup file created
- destination path confirmed
- routing logic added
- tests run
- test results
- anything not verified
```

---

## Example Python Routing Snippet

Use this as a pattern only. Adapt to the existing script.

```python
from pathlib import Path
import shutil
from datetime import datetime

SPA_PREFIX = "spa-spec-repo-"
SPA_DESTINATION = Path("/FULL/LOCAL/PATH/devops-ip-rag/spa-spec-repo")

def safe_move(source_path: Path, destination_dir: Path) -> Path:
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination_path = destination_dir / source_path.name

    if destination_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        destination_path = destination_dir / f"{source_path.stem}-{timestamp}{source_path.suffix}"

    shutil.move(str(source_path), str(destination_path))
    return destination_path

def route_file(file_path: str):
    source_path = Path(file_path)
    filename = source_path.name

    if not source_path.is_file():
        return None

    if filename.startswith(SPA_PREFIX) and source_path.suffix == ".md":
        return safe_move(source_path, SPA_DESTINATION)

    # Existing routing rules continue below this line.
    # Example:
    # if source_path.suffix == ".md":
    #     return safe_move(source_path, CHAT_THREAD_DESTINATION)

    return None
```

---

## Verification Checklist

Before calling the update complete:

- SPA prefix rule runs before the general markdown rule
- SPA destination path exists or is created safely
- SPA file routes to the correct repo
- normal chat-thread markdown file still routes correctly
- unrelated files are not moved by accident
- no files are overwritten silently
- backup exists

---

## Final Operating Principle

The filename should tell Automator enough to route the file.

The repo path belongs in the script.

No filename lasagna.  
No double underscores.  
No redundant `-spec`.
