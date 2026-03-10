import os
import time
import subprocess
import re
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- CONFIGURATION ---
# The exact path of your repository folder
FOLDER_TO_WATCH = "/Users/pattywoods/Desktop/Turn By Turn Chat RAG Files"

class GitAutoPusher(FileSystemEventHandler):
    def __init__(self):
        self.last_push_time = 0
        self.debounce_seconds = 5 # Waits 5 seconds after a change to batch multiple files together
        # Regex to match filenames like "File Name (1).md" or "My Document (2).txt"
        self.version_pattern = re.compile(r"(.+?)\s*\(\d+\)\.(.+)")

    def process_change(self):
        current_time = time.time()
        # Debounce: Prevent pushing 100 times if 100 files are added at once
        if current_time - self.last_push_time < self.debounce_seconds:
            return
            
        self.last_push_time = current_time
        print("\n[🤖 Agent Watcher] Changes detected! Syncing to GitHub...")
        
        try:
            # Change directory to the watched folder
            os.chdir(FOLDER_TO_WATCH)
            
            # Git commands to add, commit, and push
            subprocess.run(["git", "add", "."], check=True)
            
            # We use a timestamp for the automated commit message
            commit_msg = f"Auto-sync: {time.strftime('%Y-%m-%d %H:%M:%S')}"
            
            # If there's nothing to commit, git commit returns a non-zero exit code, 
            # so we capture the output to avoid crashing the script
            result = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
            
            if "nothing to commit" not in result.stdout:
                subprocess.run(["git", "push"], check=True)
                print("[✅ Agent Watcher] Successfully pushed to GitHub!")
            else:
                print("[🤖 Agent Watcher] No new changes to commit.")
                
        except subprocess.CalledProcessError as e:
            print(f"[❌ Agent Watcher] Git operation failed: {e}")

    def handle_versioning(self, file_path):
        """
        If a file like "Report (1).md" is added, it overwrites "Report.md" 
        and deletes the "(1)" version.
        """
        if not os.path.isfile(file_path):
            return

        directory, filename = os.path.split(file_path)
        match = self.version_pattern.match(filename)
        
        if match:
            base_name = match.group(1)
            extension = match.group(2)
            original_filename = f"{base_name}.{extension}"
            original_file_path = os.path.join(directory, original_filename)
            
            print(f"[🔄 Version Handler] Detected versioned file: '{filename}'")
            print(f"[🔄 Version Handler] Overwriting '{original_filename}' with latest content...")
            
            try:
                # Overwrite original with new version
                shutil.move(file_path, original_file_path)
                print(f"[✅ Version Handler] Successfully updated '{original_filename}' and removed '{filename}'.")
            except Exception as e:
                print(f"[❌ Version Handler] Failed to overwrite file: {e}")

    # Watch for these specific events
    def on_created(self, event):
        if not event.is_directory:
            # First handle versioning logic
            self.handle_versioning(event.src_path)
            # Then trigger the sync
            self.process_change()

    def on_modified(self, event):
        if not event.is_directory:
            self.process_change()

def start_watching():
    print(f"👀 Starting automated Git watcher on: {FOLDER_TO_WATCH}")
    print("Feature Enabled: Files with '(N)' in name will overwrite original version.")
    print("Waiting for changes...")
    
    event_handler = GitAutoPusher()
    observer = Observer()
    observer.schedule(event_handler, FOLDER_TO_WATCH, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1) # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
        print("\n[🛑 Agent Watcher] Stopped by user.")
    observer.join()

if __name__ == "__main__":
    # Ensure the folder actually exists
    if not os.path.exists(FOLDER_TO_WATCH):
        print(f"Error: The folder {FOLDER_TO_WATCH} does not exist. Please update the path.")
    else:
        # Move to the folder to ensure relative paths work if needed
        os.chdir(FOLDER_TO_WATCH)
        start_watching()
