# Repository Instructions

This repo contains public Agent Skills and related AI agent documentation.

## Skill Organization

Installable public skills live under `skills/<skill-name>/`.

## Public Skill Checklist

Every public/installable skill must be listed in:

1. `.claude-plugin/plugin.json`
2. the top-level `README.md`

Each README skill entry should link directly to its `SKILL.md` and include a one-line description.

Add category folders only when the repo has enough public skills to justify the extra structure.

## Skill Format

Each skill must be a folder containing `SKILL.md` with YAML frontmatter:

```yaml
---
name: skill-name
description: What this skill does and when an agent should use it.
---
```

Keep skills concise. Move detailed examples or long reference material into adjacent files only when that helps progressive disclosure.

Before publishing changes, run `npx skills@latest add . --list` from the repo root to confirm the installer can discover the public skills.
