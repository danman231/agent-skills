#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
manifest="$repo/.claude-plugin/plugin.json"

if [ ! -f "$manifest" ]; then
  echo "missing .claude-plugin/plugin.json" >&2
  exit 1
fi

python3 - "$repo" <<'PY'
import json
import pathlib
import re
import sys

repo = pathlib.Path(sys.argv[1])
manifest = repo / ".claude-plugin" / "plugin.json"
data = json.loads(manifest.read_text())

errors = []
skills = data.get("skills")
if not isinstance(skills, list):
    errors.append("manifest skills must be a list")
    skills = []

for rel in skills:
    if not isinstance(rel, str):
        errors.append(f"manifest skill entry is not a string: {rel!r}")
        continue
    skill_dir = (repo / rel).resolve()
    try:
        skill_dir.relative_to(repo.resolve())
    except ValueError:
        errors.append(f"manifest skill points outside repo: {rel}")
        continue
    if "in-progress" in pathlib.Path(rel).parts or "deprecated" in pathlib.Path(rel).parts:
        errors.append(f"draft/deprecated skill cannot be public: {rel}")
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(f"missing SKILL.md for manifest entry: {rel}")
        continue
    text = skill_md.read_text()
    if not text.startswith("---\n"):
        errors.append(f"missing YAML frontmatter: {skill_md.relative_to(repo)}")
        continue
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append(f"invalid YAML frontmatter block: {skill_md.relative_to(repo)}")
        continue
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*.+$", frontmatter, re.M):
        errors.append(f"missing name in frontmatter: {skill_md.relative_to(repo)}")
    if not re.search(r"^description:\s*.+$", frontmatter, re.M):
        errors.append(f"missing description in frontmatter: {skill_md.relative_to(repo)}")

if errors:
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    sys.exit(1)

print(f"validated {len(skills)} public skill(s)")
PY
