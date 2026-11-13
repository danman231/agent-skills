# The prompts from "Use Fable 5.2 as the Boss, Not the Worker"

These come from the Strongin AI YouTube video "Use Fable 5.2 as the Boss, Not the Worker". The repo's MIT license covers only our own text.

The advice and numbers come from Anthropic's guide, "Which Claude model should you build with? Fable, Opus, Sonnet, or Haiku": https://claude.dev/blog/which-claude-model-should-you-build-with/ . The log-reader file is the example from that guide, as read in the video (the description line is ours). The Explore file is our own version of the fix the guide describes.

How to use this file: in Claude Code, save each subagent file in your project's .claude/agents/ folder with the name shown, then start a new session so Claude Code picks it up.

## 1. Give Fable only the boss jobs

No prompt for this one. This is the task table from the video, from Anthropic's guide:

- Start most of your work on Opus 5.5 at medium effort.
- Save Fable 5.2 for major refactors and migrations, architecture planning, and leading many subagents. Plus deep research, and scientific or quantitative analysis.
- Move up to Fable 5.2 when Opus 5.5 at high effort still falls short, or for long unattended runs.
- Give Haiku or Sonnet the work where a mistake is cheap to spot, like finding files, running tests and reading logs.
- Keep code edits and judgment calls on the main model.

Daisy Hollman, who works on Claude Code at Anthropic, put it more simply: use Opus "for more specific tasks where you're already pretty sure you know what you want," and use Fable "for more creative tasks when you're not entirely sure what you want."

## 2. Put your workers on Haiku or Sonnet

A subagent runs in its own context window and hands back a summary, and you pay for its tokens at the rate of the model it runs on. One line in the subagent's file sets that model: model: haiku, or model: sonnet.

Save this as .claude/agents/log-reader.md:

```text
---
name: log-reader
description: Use after a test run. Reads the test output and logs and lists each failure.
tools: Read, Grep, Glob, Bash
model: haiku
---

Read the logs you're given. For each failure, report the file, the test name and the first error line. Don't edit any files.
```

To put your own subagents on a cheaper model by default, set the environment variable CLAUDE_CODE_SUBAGENT_MODEL (for example to haiku). It covers the subagents that don't name their own model. It doesn't cover the built-in Explore and Plan subagents.

## 3. Fix the Explore subagent

In current versions of Claude Code, the built-in Explore subagent runs on your session's model instead of always running on Haiku. So when your session is on Fable or Opus, every file read and code search Explore does is billed at that model's rate. The fix from the guide: make your own subagent named Explore, with model: haiku.

Save this as .claude/agents/Explore.md:

```text
---
name: Explore
description: Searches and reads the codebase for the main model. Use to find files, find where something is defined or used, and answer questions about how the code is laid out.
tools: Read, Grep, Glob
model: haiku
---

Find what the main model asked for. Search with Glob and Grep, and read only the parts of files you need. Report the file paths and line numbers you found, with a short note on what each one holds. Don't edit any files, and don't suggest changes. Stop when you have answered the question.
```

One catch: on the Anthropic API, the haiku alias now means Haiku 5.5, and that needs Claude Code 2.1.293 or later.

## 4. Keep the code edits on the boss

No prompt for this one. Keep code edits and judgment calls on your main model.

Claude Code's opusplan alias does the opposite: it plans with Opus in plan mode, then carries out the plan with Sonnet, which puts your edits on Sonnet. Before you make opusplan your default, measure it on your own tasks.

## 5. Raise effort before you move up a model

No prompt for this one. When a worker isn't good enough, don't jump straight to Fable. Take these three steps, in order:

1. Make sure the model can check its own work, with a test, a build or a script.
2. Raise the effort one level.
3. Move to the next model up, and start it at a lower effort than you used on the smaller one.

If you can check results automatically, run everything at low effort, then re-run just the failures at high.

When you do switch models mid-session, run /compact first. A move from Fable to any other generally available model drops its reasoning, and your first turn on the new model pays the cache-write price on the whole conversation.
