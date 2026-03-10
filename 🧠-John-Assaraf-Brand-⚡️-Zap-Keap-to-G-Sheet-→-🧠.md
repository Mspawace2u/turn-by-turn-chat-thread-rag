## Q: 
Hi, are you the right version of ChatGPT to use to walk me through step by step how to set up an automation in Zapier, explained like I’m totally new to Zapier and building automations, who doesn’t know how to code but comfortable with tech tools.

## A: 
Yes, I can definitely help you with that! I'll walk you through setting up automations in Zapier, step by step, starting from the basics and explaining everything clearly without needing any coding skills. I'll break down each part of the process, and you'll be able to follow along and set up the automation at your own pace.

Let me know what specific automation you're looking to build, and we can get started!

## Q: 
Okay, I need to get my subscriber database in order. I use Keap for my newsletter and the Groundhog plugin in Wordpress for my paid membership subscribers. I’d like to start with Keap first. I want to use a multi-page Google Sheet to store the information for sorting and future analysis. Page 1 will have the Keap subscriber contact information. What I need collected is: - date added to database - email status (active, unsubscribed, etc) - contact id - first name - last name - tag ids associated with contact record - tag category ids associated with contact record - broadcast ids associated with contact record - campaign ids associated with contact record Page 2 will have a recording of the Keap tags and categories, and will record: - tag id - tag description - category id associated with tag - category id - category description Page 3 will record Keap broadcast email records and will include: - date sent - time sent - total emails sent - open rate - click rate - opt-outs - bounces - complaints - broadcast id - broadcast description - broadcast subject line - link to view the broadcast email in browser - tag id(s) associated with broadcast - tag id(s) excluded from broadcast - category id(s) associated with broadcast Page 4 will record Keap campaigns and will include: - date published - campaign id - campaign name - emails sent - emails delivered - open rate - click rate - opt outs - bounces - complaints - campaign trigger(s) - link to view the campaign workflow in Keap dashboard - tag id(s) added or associated with campaign workflow - tag id(s) excluded from campaign - category id(s) associated with campaign Here is how I’d like this zap to work: Step 1 - collect all the records for page 1 with email status Confirmed, Confirmed (Legacy), Unengaged Marketable, and Unconfirmed only Step 2 - collect all the records for page 2 from newest to oldest records Step 3 - collect all the records for page 3 from newest to oldest records Step 4 - collect all the records for page 4 from newest to oldest records This will likely take some time to run, which I want to allow it to do before adding in the weekly update to the contact log. Can you walk me through how to build this?

## A: 
Yes, I can absolutely walk you through how to build this Zap! I’ll guide you through each step so you can automate this process of collecting and organizing your Keap data into your Google Sheets. Since you want to set up a Zap that collects specific data across multiple pages in your Google Sheet, I’ll focus on creating a Zap that fetches data from Keap and inserts it into Google Sheets.

Here’s a step-by-step breakdown of how we’ll build this automation:

* * *

### **Step 1: Set Up Your Google Sheets**

Before starting the Zap, you’ll need to have your Google Sheet set up with the four pages as described. Here’s how you can structure it:

*   **Page 1**: Keap subscriber contact information.
    
*   **Page 2**: Keap tags and categories.
    
*   **Page 3**: Keap broadcast email records.
    
*   **Page 4**: Keap campaign records.
    

For each sheet, make sure you have the appropriate column headers in place for each of the data points you want to collect (e.g., date, email status, first name, tag ids, etc.).

* * *

### **Step 2: Set Up the Trigger in Zapier**

Since we’re working with Keap, you'll need to set up the first trigger to collect contact records with certain email statuses.

1.  **Choose Your Trigger App**:
    
    *   In your Zapier dashboard, click **Create Zap**.
        
    *   Search for **Keap** (formerly Infusionsoft).
        
    *   Choose the **New Contact** trigger (this will let you capture all new contacts as they are added).
        
2.  **Set Up Your Trigger**:
    
    *   Connect your Keap account to Zapier if you haven’t already.
        
    *   In the setup step, filter by **Email Status**.
        
        *   For **Email Status**, select the values: Confirmed, Confirmed (Legacy), Unengaged Marketable, and Unconfirmed.
            
    *   Test your trigger to ensure that it pulls in a contact record that matches these statuses.
        

* * *

### **Step 3: Add Filters (Optional)**

You can add a filter to make sure that only certain records are added to Google Sheets.

*   After setting the trigger, click on **+** to add a new action.
    
*   Search for **Filter by Zapier**.
    
*   Set the filter to ensure that only contacts with the desired email statuses (Confirmed, Unengaged Marketable, etc.) pass through to the next step.
    

* * *

### **Step 4: Set Up Actions to Add Data to Google Sheets**

Now we’ll set up the actions to add the contact data to the Google Sheet.

1.  **Action 1: Google Sheets – Add Row (for Page 1: Contact Info)**:
    
    *   In this step, you’ll select **Google Sheets** as your app and choose **Create Spreadsheet Row**.
        
    *   Connect your Google Sheets account if you haven’t already.
        
    *   Select the **Spreadsheet** and **Worksheet** (Page 1 in your case).
        
    *   Map the data from the Keap contact (like date added, email status, contact id, first name, etc.) to the corresponding columns in your Google Sheet.
        
2.  **Action 2: Google Sheets – Add Row (for Page 2: Tags and Categories)**:
    
    *   Add a new action to insert the tags and categories into **Page 2**.
        
    *   Choose **Google Sheets**, and select **Create Spreadsheet Row** again.
        
    *   Set up this action to populate the **tag id**, **tag description**, and associated **category ids**.
        
    *   Map the data accordingly (you’ll need to check the available data from Keap and make sure you map it correctly to the tags and categories).
        
3.  **Action 3: Google Sheets – Add Row (for Page 3: Broadcast Records)**:
    
    *   Similar to the other actions, add another **Google Sheets** action for **Page 3** (broadcast records).
        
    *   Use **Create Spreadsheet Row** again and map the data from Keap broadcasts (date sent, total emails sent, open rate, etc.).
        
4.  **Action 4: Google Sheets – Add Row (for Page 4: Campaign Records)**:
    
    *   Lastly, add an action to populate **Page 4** (Keap campaigns).
        
    *   Use the same **Create Spreadsheet Row** action and map the campaign data (date published, emails sent, campaign id, etc.).
        

* * *

### **Step 5: Handle Updates (for Weekly Contact Log)**

After you have all your actions set up, you can set up a schedule for the Zap to run weekly and update the contact log.

1.  **Schedule the Zap to Run Weekly**:
    
    *   Add a **Schedule by Zapier** action.
        
    *   Set the frequency to **Weekly**.
        
    *   Make sure this runs after all the data from Keap has been collected, allowing time for the process to complete.
        

* * *

### **Step 6: Test Your Zap**

Once you have everything set up:

*   Run tests to ensure that each action is collecting the correct data and populating the correct columns in the Google Sheets.
    
*   Check that the data appears as expected and that the trigger only collects contacts with the specified email status.
    

* * *

### **Step 7: Turn On Your Zap**

Once everything looks good in the tests, you can turn your Zap on, and it will start running automatically!

* * *

### Notes for Consideration:

*   **Batch Processing**: Since you’re looking to collect and process a large amount of data, you may want to check if Zapier’s free or standard plan can handle it, or if you need to upgrade for more tasks per month.
    
*   **Data Volume**: If the amount of data being processed grows large, consider setting up a filter or condition to only collect a subset (e.g., records created within the past week) to keep things manageable.
    
*   **Time Delays**: Depending on how much data you're pulling, there may be delays. If needed, we can add a **Delay** action between steps to make sure each step completes before the next one runs.
    

* * *

This setup should get you started with automating your Keap data collection and organizing it into Google Sheets. Let me know if you'd like to go deeper into any of these steps or need further help troubleshooting along the way!

