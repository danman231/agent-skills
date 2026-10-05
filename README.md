# Strongin AI Agent Skills

A public collection of agent skills and practical AI workflow notes.

These skills are meant to be small, inspectable, adaptable, and useful across Claude Code, Codex, Cursor, and other agents that support the Agent Skills convention.

## Quickstart

List the available skills:

```bash
npx skills@latest add danman231/agent-skills --list
```

Install the Agent Architecture skill:

```bash
npx skills@latest add danman231/agent-skills --skill agent-architecture
```

Install the System Bug Investigator skill:

```bash
npx skills@latest add danman231/agent-skills --skill system-bug-investigator
```

Install the four "make AI explain it" skills (based on Andrej Karpathy's Oct 2026 post on understanding LLM output):

```bash
npx skills@latest add danman231/agent-skills --skill ste --skill eli5 --skill explain-page --skill explain-video
```

Install all public skills:

```bash
npx skills@latest add danman231/agent-skills --all
```

For local review before this repo is published:

```bash
npx skills@latest add <path-to-local-checkout> --list
```

## Why This Exists

I use skills to turn repeatable AI workflows into portable instructions.

The goal of this repo is to collect small, practical skills that make agents better at specific jobs: designing systems, reviewing workflows, researching, writing, coding, planning, using tools, or working with external apps.

A good skill captures the parts of a workflow that should not have to be re-explained every time:

- what the agent should pay attention to
- what steps it should follow
- what it should avoid
- what outputs are useful
- where validation, human review, or handoff matters

The point is not to create a giant agent framework. The point is to make useful workflows easier to reuse, inspect, adapt, and share.

## Skills

### agent-architecture

**[agent-architecture](./skills/agent-architecture/SKILL.md)** helps design and review reliable AI agent systems. It focuses on role boundaries, context control, side-effect gates, structured outputs, validation, logging, rollback paths, and human escalation.

### system-bug-investigator

**[system-bug-investigator](./skills/system-bug-investigator/SKILL.md)** helps investigate bugs, failed jobs, regressions, dirty worktree blockers, CI failures, deployment mismatches, and confusing system behavior before recommending or applying the simplest safe first fix. It also produces a concise, browser-openable HTML explainer that visually shows the issue, the fix, and the verification path for non-technical readers.

### ste

**[ste](./skills/ste/SKILL.md)** writes or rewrites text in ASD-STE100 Simplified Technical English, the controlled language of aircraft maintenance manuals: short sentences, one instruction per sentence, active voice, one name per thing. 80% strictness by default (the softer version Karpathy suggests), full STE on request. Includes `scripts/ste_check.py`, which flags long sentences, passives, contractions and other rule breaks. Requires: python3.

### eli5

**[eli5](./skills/eli5/SKILL.md)** explains any topic to a total beginner as one visual HTML page: big pictures, few words, 3–6 numbered steps. Adapted from Thariq's (@trq212) `eli5` skill in [anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community) (Apache-2.0), extended with source-checking, a visual form per kind of topic, and word limits.

### explain-page

**[explain-page](./skills/explain-page/SKILL.md)** builds an interactive HTML explainer page you can play with (a simulator, a clickable map, a before/after toggle) to understand a system, a concept, or work an agent just did. Every claim is labeled VERIFIED or UNVERIFIED, and every control is tested before hand-off. Writes its text with `ste`. Requires: python3, Google Chrome (macOS path in `scripts/check_page.sh`).

### explain-video

**[explain-video](./skills/explain-video/SKILL.md)** makes a narrated 3Blue1Brown-style explainer video (MP4): a teaching plan, narration written in STE, a free local voice (Kokoro), and a render with [HyperFrames](https://github.com/heygen-com/hyperframes). It then checks its own audio, transcript, and frames. Most videos are 1–4 minutes. Requires: the `ste` skill, Node + HyperFrames (with its `faceless-explainer` / `general-video` skills and Kokoro voice setup), ffmpeg, python3. Optional: an ElevenLabs API key.

> Script paths in these skills assume Claude Code's default skills folder (`~/.claude/skills/<name>/`). If your agent installs skills elsewhere, point the paths at that folder.

## Repository Layout

```text
agent-skills/
├── .claude-plugin/plugin.json
├── skills/
│   ├── agent-architecture/
│   ├── eli5/
│   ├── explain-page/
│   ├── explain-video/
│   ├── ste/
│   └── system-bug-investigator/
└── README.md
```

Public skills should be listed in two places:

1. `.claude-plugin/plugin.json`
2. the top-level `README.md`

When this repo has enough skills to need categories, add them then. Until then, keep the structure obvious and minimal.

## License

MIT
