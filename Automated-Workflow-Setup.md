## Q: 
I have to set up an automated workflow with the tools I currently have in place. If I tell you the outcome I want, the tools I have, and the trigger event, can you walk me through it step by step like you’re explaining it to a newbie to tech tools and the software in okay?

## A: 
Absolutely. Just share the specifics—what outcome you're aiming for, the list of tools you have, and what event should trigger the workflow—and I'll break it down into clear, step-by-step instructions, no fluff. Looking forward to the details so we can get you set up.

## Q: 
Great. I have Calendly, Airtable, Google Calendar, Tally, and Slack in play. I also have Zapier I can use if I need to. This is what I want to happen: 1. Trigger: a call is booked through Calendly and assigned to me. I already have the Calendly app connected to Slack, so it alerts me every time a new booking comes in. 2. When I receive a message in my app thread from Calendly, I want the matching record searched for in the easiest of two places: Either find the record in a message thread in a public channel on Slack that collects responses from the Tally form and sends them to Slack Or Find the record in one of the tabs inside an Airtable board. 3. When the match is found, I want to have their Tally form responses added to the description of the Google Calendar event that Calendly created for the booking. What is the easiest, best, most native, shortest set of steps I’d need to take for this automation

## A: 
Here's a straightforward plan:

### 1. Trigger: Calendly Booking

*   **Set up a Zap in Zapier** with Calendly as the trigger. Choose the “Invitee Created” (or similar) event so that every time a booking is made (and assigned to you), the Zap kicks off.
    

### 2. Determine Your Data Source (Slack vs. Airtable)

*   **Branch with Paths (if needed):**
    
    *   **Path A:** If you want to search a Slack channel thread where Tally form responses are posted.
        
    *   **Path B:** If the record isn’t in Slack, then search for it in Airtable.
        
*   **Tip:** Use a unique identifier common between Calendly and the Tally responses (like an email or booking ID) to search.
    

### 3. Search for the Matching Record

*   **For Slack (Path A):**
    
    *   **Action Step:** Use Zapier’s Slack integration to “Search Messages.”
        
    *   **Query:** Use the unique identifier (e.g., email) from the Calendly booking to search the public channel/thread where Tally responses land.
        
*   **For Airtable (Path B):**
    
    *   **Action Step:** Use the Airtable “Find Record” action.
        
    *   **Search By:** The same unique identifier.
        
*   **Note:** Use a Paths setup so that if the Slack search finds a match, it proceeds with that; if not, it goes to the Airtable search.
    

### 4. Extract Tally Form Data

*   Once a record is found (whether from Slack or Airtable), pull the Tally form responses from that record. Make sure you clearly identify which fields (answers) you want to include.
    

### 5. Update the Google Calendar Event

*   **Action Step:** Use Google Calendar’s “Update Event” action.
    
    *   **Target:** The event that Calendly created.
        
    *   **Update Field:** Append or set the event’s description with the Tally form responses you extracted.
        
    *   **Mapping:** Map the Tally response data to the description field. You might format it as bullet points or a simple paragraph for clarity.
        

### 6. Test and Activate

*   **Test Your Zap:** Run tests to ensure the search correctly finds the matching record, and that the Google Calendar event gets updated as expected.
    
*   **Activate the Zap:** Once it’s working smoothly, turn it on.
    

### Recap

1.  **Trigger:** New Calendly booking.
    
2.  **Search:** Use a unique identifier to find a matching Tally response in either a Slack thread or an Airtable record (with branching paths).
    
3.  **Update:** Append the Tally responses to the description of the corresponding Google Calendar event.
    

This setup uses Zapier’s multi-step and Paths features to keep things native and streamlined—no need for complex coding. It’s a clear, efficient way to link your existing tools and automate your workflow.

## Q: 
Problem with the trigger - the Calendly account that runs the round robin assignments isn’t mine. When a call is assigned to me, it does go to my alias specifics associated Calendly account which syncs the event to Google Calendar. Will I need to choose a different trigger?

## A: 
Yes. Since you don’t have direct access to that Calendly account, you can trigger your automation from the event that lands in your Google Calendar. Here’s a clear outline:

1.  **Trigger Change:**  
    Instead of using the Calendly trigger, use Google Calendar’s “New Event” trigger in Zapier on the calendar where your alias events appear.
    
    *   **Tip:** Add a filter step to check that the event was created via Calendly (for example, by looking for a specific keyword or structure in the event details).
        
2.  **Continue With Your Workflow:**  
    Once the trigger fires on the new Google Calendar event, you can proceed with the rest of your steps:
    
    *   **Search for the Matching Record:** Use Paths in Zapier to check Slack for the Tally form response (or fall back to Airtable if needed), using a unique identifier.
        
    *   **Update the Event:** Once the Tally data is found, update the Google Calendar event’s description with the Tally form responses.
        

This approach ensures you’re capturing the event from your calendar without needing direct access to the original Calendly account.

## Q: 
Are there any alternative ways you see to build this automation? For example, if we use Slack and its native app integrations and possible workflows? So, to give you an idea of the tech stack, this is what’s happening to deliver a booking to me. 1. Customer fills out a Tally form to book the call. 2. PipeDream captures the information and passes it into our Airtable CRM board, specifically into a table for onboarding calls 3. Once the customer books a call time on the admin Calendly calendar, Calendly assigns it to the next available OS that can hold the call at the requested time 4. The assigned OS agent is booked through their own Calendly account which is linked and synced to their Google Calendar Potential ways we can find and match the Tally form replies to our assigned bookings that wouldn’t require admin access to the tech stack would be: 1. Pull the Tally info from the public slack channel to match to our Google Calendar bookings 2. Have the admin set up an Airtable message automation to send the details of the Tally form and booking to a public slack channel but with the ability to tag the assigned OS agent in the channel (which are all dynamic values)

## A: 
Here are a couple of alternative approaches that might let you keep things more “in Slack” or use a native Airtable automation—no need to wrestle with admin Calendly access.

* * *

### Option 1: Slack-Centric Workflow

1.  **Leverage Slack Workflow Builder:**  
    • **Trigger:** Instead of triggering off Calendly directly, have Slack notice when a new booking message (from your Calendly alias) arrives in your designated channel or thread.  
    • **Action:** Create a workflow that automatically searches for the matching Tally info in the public Slack channel. (This might involve a custom step or even a lightweight Slack app if you need to perform a message search by unique identifier like email or booking ID.)
    
2.  **Matching Process in Slack:**  
    • If a matching Tally record is found in the channel, use Slack’s workflow to either update a pinned message, post a new message, or alert you with the Tally details.  
    • This notification can include a link or quick action to update the corresponding Google Calendar event.
    
3.  **Manual or Automated Google Calendar Update:**  
    • If you’re comfortable with a semi-automated process, the Slack alert can include all the Tally info so you can manually update the Google Calendar event.  
    • Alternatively, a secondary step (via Zapier or a custom Slack action) could automatically update the event if you expose a Google Calendar integration.
    

* * *

### Option 2: Airtable-to-Slack Automation

1.  **Airtable Automation as the Hub:**  
    • Since your PipeDream already sends Tally responses into an Airtable CRM board, use Airtable’s built-in automation to trigger when a new record is added or updated.
    
2.  **Post to a Public Slack Channel:**  
    • Set up the Airtable automation to send a Slack message that includes both the Tally form details and the booking information from Calendly.  
    • Use dynamic fields in Airtable to tag the assigned OS agent in Slack (since the agent’s identifier is stored in the record). This gives immediate visibility and a call to action.
    
3.  **Bridging to Google Calendar:**  
    • With the Tally details and booking info delivered via Slack, the assigned OS agent (or a secondary automation step) can then update the Google Calendar event’s description.  
    • This could be as simple as having the OS agent click a link to a pre-filled update form or using another lightweight Zapier integration that listens for a specific Slack message format.
    

* * *

### Key Points to Consider

*   **Data Consistency:**  
    Whichever route you choose, ensure you have a unique identifier (like an email or booking ID) that ties the Tally form response to the Google Calendar event. This makes the matching process more robust.
    
*   **Native vs. Hybrid:**  
    Slack’s Workflow Builder is great for notifications and simple actions but might hit limitations when it comes to performing external searches or updates on Google Calendar. If you need more complex actions, a hybrid solution with Airtable automations or a lightweight Zapier integration can fill in the gaps.
    
*   **Ease of Setup:**  
    If you’re looking for the most “native” method with minimal coding, the Airtable automation route might be simpler. You’re already capturing the data in Airtable, and its integration with Slack is straightforward and robust.
    

Both alternatives bypass the need to access the admin Calendly account directly while still providing a way to tie together the Tally, booking, and calendar event data. Choose the one that fits your comfort level with each tool and the complexity you’re willing to manage.

Does this help clarify your options?

## Q: 
Not really. I just want the easiest fully automated way to make this happen with the least amount of connections possible. Can’t I have the trigger for this be when I have a call assigned to my Calendly alias (that shows up in Slack from the app plugin, and also to my Gmail address)? Then it initiates the Slack channel search with the Tally responses to find the email address of the invitee? Then it parses the answers given in the associated Slack message and updates the details of my associated Google Calendar event (that’s already synced to Calendly)?

## A: 
Here's the simplest fully automated approach with minimal connections:

1.  **Trigger on Your Calendly Alias Event:**  
    • Use Zapier’s Slack integration to trigger when your Calendly alias sends a new message in your Slack channel (the Calendly app plugin message).  
    • This message should include key details like the invitee’s email address.
    
2.  **Extract the Invitee Email:**  
    • In the Zap, add a step to parse the Slack message text and extract the invitee’s email address (using Zapier’s built-in text extraction or Formatter by Zapier).
    
3.  **Search for the Tally Responses in Slack:**  
    • Next, add a Slack “Find Message” (or “Search Messages”) action that looks through the public Slack channel where Tally responses are posted.  
    • Use the email address as your search query so it finds the matching Slack message with the Tally form answers.
    
4.  **Parse the Tally Response Details:**  
    • Once the matching Slack message is found, use another Formatter step (if necessary) to extract and format the Tally form answers from that message.
    
5.  **Update the Google Calendar Event:**  
    • Finally, add a Google Calendar “Update Event” action.  
    • Map the event using the details from the original Calendly-triggered Slack message (like the event ID or link provided in that message) and update its description field to include the parsed Tally responses.
    

By triggering off your Calendly alias Slack notification, then searching the Tally responses channel by email, you avoid additional connections (using only Slack and Google Calendar via Zapier). This streamlined method keeps everything automatic and ties your invitee’s Tally data to the corresponding Google Calendar event with minimal fuss.

This setup uses just three connections:

*   Slack (for the Calendly alias trigger and message search),
    
*   Formatter (for parsing text), and
    
*   Google Calendar (for updating the event).
    

That’s it—simple, direct, and fully automated.

## Q: 
You’ll have to walk me through the set up step by step as if I’m new to Zapier and automations, remember? Parsing is a pain for me. And I also need to make sure this is a dynamic not a static trigger

## A: 
Let's break this down into a step-by-step Zapier setup. I’ll assume you have a basic Zapier account and your Slack and Google Calendar accounts already connected. We’re going to set up a Zap that fires every time your Calendly alias posts a message in Slack (the Calendly app message). Then it will extract the invitee’s email, search your Tally responses in Slack for that email, parse the details, and update the corresponding Google Calendar event.

Below are the detailed steps:

* * *

### **Step 1: Create a New Zap**

1.  **Log in to Zapier.**  
    Click “Make a Zap” in your dashboard.
    
2.  **Name Your Zap.**  
    Give it a descriptive name like “Calendly Tally Update for My Google Calendar.”
    

* * *

### **Step 2: Set Up the Trigger – Slack New Message**

1.  **Choose Slack as the Trigger App:**
    
    *   In “Choose App & Event,” search for **Slack**.
        
    *   For the Trigger Event, select **“New Message Posted to Channel”** (or a similar trigger that captures the Calendly alias message).
        
2.  **Connect Your Slack Account:**
    
    *   Follow the prompts to connect your Slack account if you haven’t already.
        
3.  **Configure the Trigger:**
    
    *   **Channel:** Select the Slack channel where your Calendly alias posts its booking messages.
        
    *   **Trigger Filter (Optional):** If you only want messages from the Calendly app, you can add a filter in the next step or use Zapier’s built-in filters. For example, you could require that the message text contains “Calendly” or your unique Calendly alias identifier.
        
4.  **Test Your Trigger:**
    
    *   Zapier will pull in a sample message. Confirm it looks like a Calendly booking message with the details you expect (including the invitee’s email).
        

* * *

### **Step 3: Extract the Invitee Email from the Slack Message**

1.  **Add a Formatter Step:**
    
    *   Click “+” to add a new action.
        
    *   Choose **“Formatter by Zapier”** as the app.
        
    *   For the Action Event, select **“Text”**.
        
2.  **Configure the Formatter:**
    
    *   Under “Transform,” choose **“Extract Email Address”** (Zapier has options for finding patterns in text).
        
    *   **Input:** Map in the message text field from the Slack trigger.
        
    *   **Test:** Run the test step. Zapier should return the invitee’s email address.
        

_Tip:_ If the email isn’t in a clean format, you might need to use a “Split Text” action to isolate it. But in most Calendly messages, the email is clearly included.

* * *

### **Step 4: Search Slack for the Tally Response**

1.  **Add a Slack “Find Message” Step:**
    
    *   Click “+” to add another action.
        
    *   Choose **Slack** again as the app.
        
    *   For the Action Event, choose **“Find Message”** or **“Search Messages”** (whichever is available in your Zapier setup).
        
2.  **Configure the Search:**
    
    *   **Search Query:** Use the email you extracted in Step 3 as your query.
        
    *   **Channel:** Choose the Slack channel where the Tally responses are posted (make sure this is the public channel where all Tally messages appear).
        
3.  **Test Your Search:**
    
    *   Ensure Zapier finds the correct Slack message that includes the Tally responses associated with that email.
        

* * *

### **Step 5: Parse the Tally Form Responses**

1.  **Examine the Found Message:**
    
    *   In your test sample, review the Slack message. Ideally, the Tally responses are structured (for example, each answer on a new line or separated by a unique delimiter).
        
2.  **Add Another Formatter Step (if necessary):**
    
    *   If you need to extract specific parts, add another **“Formatter by Zapier”** action.
        
    *   Choose **“Text”** and then use the **“Split Text”** or **“Extract Pattern”** function.
        
    *   **Input:** Map the text from the Slack Tally response message.
        
    *   **Configure:** Define your delimiter (for example, if answers are on separate lines, use a line break) or a regex pattern if you’re comfortable with that.
        
    *   **Test:** Confirm that the formatter isolates the key details you want to add to your Google Calendar event description.
        

_Note:_ If your Tally responses are simple and all you need is the whole text block, you might not need to split it further. You can directly use the message text.

* * *

### **Step 6: Update Your Google Calendar Event**

1.  **Add a Google Calendar Step:**
    
    *   Click “+” to add another action.
        
    *   Choose **Google Calendar** as the app.
        
    *   For the Action Event, select **“Update Event”**.
        
2.  **Connect Your Google Calendar Account:**
    
    *   If not connected yet, follow the prompts to add your account.
        
3.  **Configure the Update Event Action:**
    
    *   **Event ID:**  
        You need to update the event created by Calendly. In the initial Slack Calendly message (Step 1), there should be an event ID or a link that identifies the event. Map this field using the data from the Slack trigger.
        
    *   **Description Field:**  
        In the description box, insert the Tally response details that you extracted and parsed in Step 5. You can also add some text to label the responses (e.g., “Tally Form Responses:”).
        
4.  **Test Your Google Calendar Step:**
    
    *   Run the test to ensure that the event in your Google Calendar is updated with the Tally information.
        

* * *

### **Step 7: Finalize and Activate Your Zap**

1.  **Review Your Zap:**
    
    *   Double-check that each step is properly connected and that the data flows correctly from the trigger to the final action.
        
    *   Make sure the trigger is dynamic. Every time a new Calendly alias message appears in Slack, it should run through these steps.
        
2.  **Turn On Your Zap:**
    
    *   Click the “Turn on Zap” button.
        
3.  **Monitor the First Few Runs:**
    
    *   Check your Slack channel and Google Calendar to ensure that when a new booking comes in, the Tally responses are correctly found and added to your event details.
        

* * *

### **Key Points to Remember**

*   **Dynamic Trigger:**  
    By using the Slack message (from your Calendly alias) as the trigger, you ensure that the Zap is dynamic. It fires every time a new booking message is posted, not just once.
    
*   **Parsing:**  
    If parsing seems tricky, try using the basic “Extract Email” option first. Only add extra formatter steps if the Tally data isn’t cleanly passed along.
    
*   **Testing:**  
    Test each step individually in Zapier. It helps you catch any issues early and understand how the data moves from one step to the next.
    

This step-by-step should give you the fully automated workflow with minimal connections, keeping it straightforward without needing any admin access to the Calendly account. Let me know if you need further clarification on any of the steps!

