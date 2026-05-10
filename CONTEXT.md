# Strongin AI Agent Skills Context

This repo is a public collection of reusable AI agent skills and notes.

## Language

**Skill**: A portable folder of instructions centered on a `SKILL.md` file. Skills teach agents reusable procedures.

**Public skill**: A skill intended for others to install. Public skills are listed in `.claude-plugin/plugin.json` and the README catalog.

**Draft skill**: A skill being developed or tested. Draft skills live under `skills/in-progress/` and are not listed in the plugin manifest.

**Agent workflow**: A repeatable operating design for an AI agent or set of agents, including roles, context boundaries, tools, validation, side-effect gates, and logs.

## Repository Rules

- Keep installable skill content portable and free of private local paths.
- Prefer small, focused skills over broad collections of loosely related instructions.
- Keep public docs useful for humans browsing GitHub.
- Keep `SKILL.md` files useful for agents executing work.
