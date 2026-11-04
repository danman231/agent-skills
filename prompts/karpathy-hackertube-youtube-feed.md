# The prompt and the rule from "Karpathy Fixed His YouTube Feed in 2 Hours With Claude. Here's the Idea You Can Copy"

Prompts from the Strongin AI YouTube video. Lines in quotation marks or quote blocks credited to HackerTube, its DATA.md or Andrej Karpathy are theirs, word for word; the repo's MIT license covers only our own text. Numbers were checked on hackertube.org and in the data zip (exported October 31, 2026) on November 3, 2026.

How to use this file: to copy HackerTube, download the zip and paste prompt 1 into Claude Code. To build the same kind of feed from a pile of your own, fill in the blanks in prompt 2.

## The rule

A thing makes the cut if **at least 3 different people** recommended it, **in at least 3 different months**, and Claude read each mention and checked that it's a **real recommendation**.

- 3 different people: one excited fan posting the same link over and over doesn't get in.
- 3 different months: one viral week doesn't get in either.
- Claude reads each mention: 3 people linking a video could be 3 people making fun of it. Claude labels each one as recommend, cite as a source, joke or criticize, and only recommendations count.
- The order is staying power, not likes or views. HackerTube's score is the number of different months people recommended a video in, plus 0.5 for each month with a strong recommendation.

On Hacker News that took well over a hundred thousand linked videos down to 6,454. Claude labelled 39,834 comments, and 16,184 of them were real recommendations, about four in ten.

## Get the data

- Page: https://hackertube.org/data
- Zip (17.8 MB): https://hackertube.org/download/hackertube-data.zip
- Inside is `DATA.md`, with a section that starts "For AI agents: start here". Unzip it into a folder, open Claude Code in that folder, and paste a prompt.
- License: ODC-By 1.0. If you publish something built on it, credit HackerTube (https://hackertube.org) and the open-index/hacker-news dataset.

## Prompt 1: the site's own prompt

HackerTube's prompt from https://hackertube.org/data, word for word:

> Read DATA.md in this folder. Using this data, build me a small local web app that shows a fresh mix of HN-recommended talks each day, lets me filter by topic and length, and remembers what I've watched. Walk me through getting a YouTube API key so you can add durations.

I added one line under it to aim it at my own task:

> I want it for my research on AI and programming, so the daily mix should be talks on AI and programming.

And I gave Claude three limits: no API key, no sign-in, and it has to open as a plain local file. Add your own limits as a last line, for example: "Don't use an API key or a sign-in. It has to open as a plain local file."

**What came back** (Claude Opus 5.5 in Claude Code, about five minutes): a local page with ten talks a day, picked from 775 that fit, with a topic filter. If you mark a talk watched, it stays out the next time you open the page. The length filter stays off until you add a YouTube API key, because the zip has no video lengths. Claude walks you through making the key.

## Prompt 2: point the rule at your own pile

Pick a pile where people recommend things you care about: a forum, a Slack or Discord channel, a subreddit, newsletter archives, reviews. Fill in the brackets and paste it into Claude Code in the folder that holds the pile.

```text
In this folder is [what the pile is, e.g. 5 years of messages from our team's #tools channel].
People in it recommend [what you want a feed of, e.g. tools, books, talks, papers].

Build me a feed from it with this rule:

1. Find every mention of a [thing] in the pile.
2. Read each mention with the text around it and label what the person was doing:
   recommending it, citing it as a source, joking about it, or criticizing it.
   Keep a short quote that shows why.
3. Skip mentions with almost no text of their own (a bare link isn't a recommendation).
4. Keep a [thing] only if at least [3] different people recommended it,
   in at least [3] different months.
5. Rank by the number of different months people recommended it in.
   Months with a strong recommendation count extra.
6. Show me the top 20, each with its quote, how many people recommended it, and in which months.

Before you build the feed, show me 20 labelled mentions picked at random so I can check the labels.
```

Change the two numbers to fit your pile. HackerBooks, the same idea for books on Hacker News, uses a looser rule: 2 different people bringing a book up is enough. A small pile may need 2 people and 2 months. A big pile can take more.

## Where it breaks

- **It's the pile's taste.** HackerTube is Hacker News' taste. If HN isn't your crowd, pick a different pile.
- **The labels aren't perfect.** DATA.md: "Stances, summaries and categories were written by an LLM: good, but expect a few percent of noise." That's why prompt 2 asks to see 20 labels before it builds.
- **YouTube API data has a time limit.** If your feed stores YouTube API data, like video lengths, YouTube's developer policies say you can keep it for at most 30 days. Then delete it or refresh it.

## What Karpathy did by hand

He says he only did a few things himself: made the YouTube API key in Google Cloud, booted up the server and bought the domain. Then, in his words, "I gave Claude the IP and told it update, secure, harden, deploy and optimize the code, and it did the whole thing." He used Claude Code on Opus 5.5 at Medium effort, the default. His post says the build took about 2 hours.

So the rule is your job, and the build is Claude's.

## Sources

- Karpathy's post: https://x.com/karpathy/status/2116957135661945283
- How HackerTube picks and ranks videos: https://hackertube.org/about
- The data and the site's prompt: https://hackertube.org/data
- Karpathy on what he did by hand: https://news.ycombinator.com/item?id=50321177
- The Hacker News thread: https://news.ycombinator.com/item?id=50319510
- HackerBooks (Show HN): https://news.ycombinator.com/item?id=50326821
- Hacker Papers, the same idea for arXiv papers, by Elvis Saravia: https://x.com/omarsar0/status/2117053859516285354
- Claude Code effort levels: https://code.claude.com/docs/en/model-config
- YouTube API developer policies: https://developers.google.com/youtube/terms/developer-policies
