# Repository Instructions

This repo contains public Agent Skills and related AI agent documentation.

## Skill Organization

Installable public skills live under these category folders:

- `skills/agent-workflows/` - agent design, orchestration, review, and reliability workflows
- `skills/productivity/` - general workflow tools
- `skills/research/` - research and synthesis workflows

Non-public skill folders:

- `skills/in-progress/` - drafts not ready for public install
- `skills/deprecated/` - retired skills kept for reference

## Public Skill Checklist

Every public/installable skill must be listed in:

1. `.claude-plugin/plugin.json`
2. the top-level `README.md`
3. the relevant category `README.md`

Skills in `in-progress/` and `deprecated/` must not appear in `.claude-plugin/plugin.json`.

Each skill entry should link directly to its `SKILL.md` and include a one-line description.

## Skill Format

Each skill must be a folder containing `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill does and when an agent should use it.
---
```

Keep skills concise. Move detailed examples or long reference material into adjacent files only when that helps progressive disclosure.

## Validation

Before publishing changes, run:

```bash
./scripts/list-skills.sh
./scripts/validate-skill-manifest.sh
```
