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

Install all public skills:

```bash
npx skills@latest add danman231/agent-skills --all
```

For local review before this repo is published:

```bash
npx skills@latest add /Users/testuser/Developer/strongin_ai/agent-skills --list
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

## Examples

- [Design prompt](./examples/agent-architecture/design-prompt.md)
- [Review prompt](./examples/agent-architecture/review-prompt.md)

## Repository Layout

```text
agent-skills/
├── .claude-plugin/plugin.json
├── skills/
│   └── agent-architecture/
├── examples/
└── README.md
```

Public skills should be listed in two places:

1. `.claude-plugin/plugin.json`
2. the top-level `README.md`

When this repo has enough skills to need categories, add them then. Until then, keep the structure obvious and minimal.

## License

MIT
