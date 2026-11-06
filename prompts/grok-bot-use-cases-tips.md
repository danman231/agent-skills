# The 20 prompts from "20 Grok Bot Use Cases for Your Life, Business and Work"

Prompts from the Strongin AI YouTube video. Where a job says "xAI's original", the video reads xAI's own starter prompt and this file gives our reworded version, so use the link if you want their exact words. The repo's MIT license covers only our own text. Product details come from xAI's docs, read on November 4, 2026. Check them again before you rely on them.

How to use this file: fill in the [brackets], then paste the prompt into your Bot. Start with job 9. Every prompt ends on a stop line, the point where the Bot waits for you, so keep that line when you change the rest.

## Life

### 1. Bring your memory over from ChatGPT or Claude

No prompt to write for this one, because Grok Bot gives you the prompt.

1. Open Settings, then General, and choose Start Import.
2. Paste Grok Bot's prompt into your other assistant.
3. Paste that assistant's answer into the second box and choose Add to Memory.

### 2. Make one Bot your chief of staff

Your primary Bot is your main contact. Give every other Bot one job.

```text
Every morning, look at what changed in the last 24 hours in the email, calendar and notes you can access. Compare it with my priorities below and leave out anything unrelated. For each item you keep, tell me where it came from, why it matters, what you'd do next, and if you need a decision from me. Don't message anyone or move any meetings.

My priorities: [paste them]
```

xAI's original: https://docs.x.ai/grok-bot/use-cases

### 3. Talk instead of typing, then have it say the job back

Command or Control D starts dictation on desktop. On an iPhone 15 Pro or later, you can set the Action Button to Grok Bot, Start Voice Chat.

The say-it-back tip is from Lauren Tan, by way of RoboNuggets. Our wording:

```text
Before you start, tell me in your own words what you understood and what you plan to do. Then wait for me to confirm.
```

### 4. Have it phone a business for you

Keep the ask plain: who to call, what you need, what you want back.

```text
Call [business] at [phone number]. Ask [what you need]. Send me a note with what they said and [what you want back].
```

### 5. Send it shopping

```text
Find the best deal on this, compare the top three, and don't buy until I pick one. Then track the order.
```

### 6. Pay with a card you approve each time

No prompt for this one. A card saved in Vault fills in at checkout without asking you each time, and no setting makes it ask. To approve each payment yourself, don't save the card. Connect Link instead. The Bot then asks you to approve a one-time card for that one purchase, showing the merchant, items and total, and you choose Pay, Pay another way, or Deny.

### 7. Let it sign in without seeing your passwords

No prompt for this one. Connect 1Password (8.12.42 or later). You approve each login in 1Password, 1Password fills it in, and your Bots never see the values.

### 8. Give it your phone's apps

Grok Bot can use Calendar, Contacts, Location and Alarms on iPhone and Android, plus Reminders and Home on iPhone. It reaches your phone only while Grok Bot is open on it.

```text
Add [event] to my calendar on [date] at [time].
```

```text
Look up [name] in my contacts.
```

## Business

### 9. A morning inbox pass that flags and drafts, but never sends

This is the one to paste tonight.

```text
Every weekday at 8 AM, go through my inbox. Flag what's urgent, draft replies to anything that needs one, and leave them as drafts. Don't send anything.
```

### 10. Give it its own email address

```text
Get yourself an email address.
```

You get one address at mail.grokbot.com for your Bots. It has no inbox view and no new-mail notifications, and you can't rename or delete it, so pick the name carefully.

An email a routine writes from that address waits as a draft until you press Send. An email you ask for in chat goes out once Auto Review allows it. To stop every send, open Settings, then General, then Custom Rules under Auto-review, and add this rule:

```text
Ask first before sending any external email.
```

### 11. A skill that writes like you

```text
Create a skill that writes like me, from my sent emails.
```

Nat Eliason did this on Founders School. His Bot went through about 120 emails and came back with a "Write Like Nat" style guide. The drafts from job 9 can then sound like you.

### 12. Have it watch X for you

Grok Bot can search, read and monitor X without you connecting an X account, and it's read-only.

```text
Every Monday, look on X for what people said about [your product or industry] in the last week. Send me a short roundup with a link to each post. Don't post or reply to anything.
```

You can also tag @bot under a post. xAI's example: "@bot summarize this thread and send the key points to my Slack". Tagging isn't available for accounts in the UK, the EU, Australia, Iceland, Liechtenstein or Norway.

### 13. Ask for a page, not paragraphs

A page is something a Bot builds for you to read: a report, a memo, a dashboard or a tracker.

```text
Put the three quotes from this thread side by side on a page: a comparison table, then a few lines on which one you'd pick and why.
```

xAI's original: https://docs.x.ai/grok-bot/files-and-results

### 14. Research leads, and stop before you contact anyone

```text
Go through the [number] companies in [your list]. Rank them by how well they fit [your ideal customer] and any recent signs they're looking to buy. Find up to three people to contact at each one, then write an email and a LinkedIn message for each person, in the style of the examples I've attached. Leave out anyone we're already contacting. Give me the list to review. Don't contact or enroll anyone.
```

For hiring, the same shape:

```text
Find [number] candidates for [role]. Show me the evidence for each one, and draft a message to each in my voice. Don't contact anyone.
```

xAI's originals: https://docs.x.ai/grok-bot/use-cases

## Work

### 15. Once a task works, save it as a skill

A skill is a reusable set of instructions that all your Bots can use. Start with a task you already do every day, get it right by hand, then save it. Put the stop line in the skill.

```text
Turn what we just did into a skill named "[name]". Write down where the data comes from, what counts as a problem, how the result should look, and this rule: [contacting a customer always needs my approval].
```

xAI's original: https://docs.x.ai/grok-bot/skills-routines-and-automations

### 16. Put it on a schedule, with a failure rule

The last sentence is the failure rule. An hourly schedule, a short interval or a Slack trigger on a busy channel can use a week of usage in a day, so set routines daily. If your weekly usage runs out early, pause the routines you don't need first.

```text
Run the "[skill name]" skill every weekday at 8 AM on [your list]. Post the results here with links. Don't contact any customers. If you can't get fresh data, tell me it failed. Don't use older data instead.
```

xAI's original: https://docs.x.ai/grok-bot/skills-routines-and-automations

### 17. Start work from an event instead of a clock

A routine can start from a Slack message, an email to the Bot's address, a webhook, or tools like GitHub and Linear. Avoid broad listeners like "every new message", because they create noise and use up your usage.

```text
When a message in #[channel] has a ticket link and the words "[trigger phrase]", open the ticket, try to reproduce the problem in staging, and post what you found in this chat. Ask me before you post anything in Slack.
```

xAI's original: https://docs.x.ai/grok-bot/skills-routines-and-automations

### 18. Teach it a task by doing it once

No prompt for this one.

1. In the desktop app, open a one-to-one chat and the Bot's computer view.
2. Choose Teach a task and describe the result you're about to show it.
3. Do the workflow once. It records your screen for up to ten minutes, with no microphone audio, and saves the path as a skill.

Treat that skill as a draft. Add the decision rules and failure handling one example can't show, and test it on a safe example before you schedule it.

### 19. Give it teammates in one group chat

Start a new chat with Command or Control Shift N and add two to six Bots. Give each stage one owner.

```text
@Researcher: collect the source material, with a link for each claim.
@Writer: use those findings to write the launch draft.
@Reviewer: compare the draft with the sources and tell me only about problems that block it.
Nobody publishes anything.
```

If they message each other too much (every Bot reply counts toward your usage, even the ones between Bots):

```text
Don't message other Bots. Ask me first.
```

xAI's original: https://docs.x.ai/grok-bot/chat-and-collaboration

### 20. Hand coding off to Cursor and get a video back

Alex Finn asked for a button change on his landing page. The work went to a Cursor cloud agent, and his chat got a recorded video and before-and-after screenshots. Our wording:

```text
Hand this to Cursor: [the change you want on which page]. Send me a video of it working and before-and-after screenshots. Don't publish it until I've checked it.
```
