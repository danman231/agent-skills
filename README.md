# Strongin AI Agent Skills

A public collection of agent skills, AI workflow notes, and practical agent architecture patterns.

The goal is simple: make AI agents more reliable by giving them reusable operating instructions, not just bigger prompts. These skills are meant to be small, inspectable, adaptable, and useful across Claude Code, Codex, Cursor, and other agents that support the Agent Skills convention.

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

Most agent failures are not caused by a lack of intelligence. They come from weak operating design:

- one broad agent doing too many jobs
- too much irrelevant context
- planning and execution mixed together
- side effects with no approval gate
- free-form handoffs where structured outputs are needed
- no validation before publishing, deploying, sending, or deleting
- no durable logs, recovery path, or human escalation

Skills help turn those lessons into repeatable behavior. Instead of explaining the same workflow from scratch every time, you install the skill and let the agent load the right operating pattern when the task calls for it.

## Skills

### Agent Workflows

- **[agent-architecture](./skills/agent-workflows/agent-architecture/SKILL.md)** - Design or review reliable AI agent systems, multi-agent workflows, tool-using assistants, side-effect gates, validation, logs, handoffs, and rollback paths.

### Productivity

No public productivity skills yet.

### Research

No public research skills yet.

## Docs

- [Agent patterns](./docs/agent-patterns/README.md) - Notes and patterns for designing reliable agent systems.
- [Prompts](./docs/prompts/README.md) - Reusable prompt patterns and examples.
- [Notes](./docs/notes/README.md) - Public notes about AI agents, workflow design, and skill development.

## Examples

- [Design prompt](./examples/agent-architecture/design-prompt.md)
- [Review prompt](./examples/agent-architecture/review-prompt.md)

## Repository Layout

```text
agent-skills/
├── .claude-plugin/plugin.json
├── skills/
│   ├── agent-workflows/
│   ├── productivity/
│   ├── research/
│   ├── in-progress/
│   └── deprecated/
├── docs/
├── examples/
└── scripts/
```

Public skills must be listed in three places:

1. `.claude-plugin/plugin.json`
2. the top-level `README.md`
3. the relevant category `README.md`

Drafts can live under `skills/in-progress/`, but they should not be listed in `.claude-plugin/plugin.json` until they are ready for public install.

## License

MIT
