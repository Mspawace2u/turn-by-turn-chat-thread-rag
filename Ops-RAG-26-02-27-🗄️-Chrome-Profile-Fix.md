## Q: 
So freakin PO’d right now. Antigravity deleted Google Chrome apps or something from my internal Mac OS applications folder so I couldn’t pull up any of those things like drive or docs or NotebookLM or Gemini when using the Google Chrome app. I can’t even access Google.com on my Safari app to attempt connecting to them. So, I did what Google AI said, verified the easiest thing to do would be to delete the chrome app and reinstall. Before the reinstall, empty trash and make sure no artifacts remain in the application support folder for chrome. I deleted the Chrome labeled folders but left the Google folder. Emptied trash. Didn’t restart the computer. Tried to access Google on Safari to download the Chrome app. I’m blocked. Still somehow logged into the antigravity app with one of my profiles still saved in its memory and it downloaded the chrome app for me. I installed the app but still can’t get past the enter user name screen. It won’t advance / allow me to enter the password to pull up my profile. I know there’s a fix, I had to do this a couple months ago the last time I let antigravity go autonomous on me. Just can’t recall the steps I may be missing that I figured out on my own to fix this shit. Could use your help. Antigravity is too close to its creator (Google) apparently to fix it

## A: 
Alright. Pause the rage spiral for 10 seconds. This is almost always a **profile / keychain / Chrome user data mismatch**, not a full system break. We’ll fix it without nuking your machine. 🔧

From what you described, the most likely issue is:

**Chrome is trying to load a corrupted user profile that no longer exists** because the folders were deleted but the login token is still referenced.

So Chrome opens → asks for username → then freezes because it can’t find the matching profile.

We need to **force Chrome to rebuild a clean profile.**

* * *

# Step 1 — Fully quit Chrome

Even if it looks closed.

Press:

**Command + Option + Esc**

Force quit:

**Google Chrome**

* * *

# Step 2 — Remove the remaining Chrome user profile

Open **Finder**

Go to:

```
~/Library/Application Support/
```

Find the folder:

```
Google
```

Inside it you should see:

```
Chrome
```

Delete the entire:

```
Chrome
```

folder.

⚠️ Leave the **Google** folder itself alone. Just remove **Chrome**.

* * *

# Step 3 — Clear Chrome login tokens (this is the step most guides miss)

Open **Keychain Access**.

Search for:

```
chrome
```

Delete anything named:

*   Chrome Safe Storage
    
*   Chrome Password
    
*   Chrome Token
    
*   Any entries referencing **Google Chrome**
    

These leftover tokens are what usually cause the **“can’t move past username screen”** bug.

* * *

# Step 4 — Restart the Mac

Yes, this actually matters.

Do a **full restart**, not sleep.

* * *

# Step 5 — Open Chrome again

When Chrome launches it should now act like a **brand new install**.

You should see:

```
Sign in to Chrome
```

instead of the frozen username screen.

Now sign in normally.

* * *

# If Safari still can't access Google

That's a separate thing and usually caused by a DNS or extension issue.

Quick test:

Open Safari and go to:

```
https://1.1.1.1
```

If that loads, your internet works and it's just a DNS cache problem.

Then run this in **Terminal**:

```
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

Enter your Mac password when prompted.

* * *

# One important thing about Antigravity

You’re not crazy.

Agent tools like Antigravity, Cursor, Claude Cowork, etc. sometimes run commands like:

```
rm -rf ~/Library/Application Support/Google/Chrome
```

when resetting environments.

They **don’t understand Chrome profile coupling** with macOS Keychain and Google web auth.

Result = exactly the mess you’re seeing.

* * *

# If this still doesn’t work

Then the fix is a **Chrome launch flag override** (super easy).

I can walk you through that in 30 seconds.

* * *

**One quick question so I don't send you down the wrong branch:**

When Chrome opens right now, do you see:

**A.** A Google login screen asking for email  
or  
**B.** A Chrome profile picker / blank window that won't advance

Just tell me **A or B**.

