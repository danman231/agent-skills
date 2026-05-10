#!/usr/bin/env bash
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"

cd "$repo"
find skills -name SKILL.md -not -path '*/in-progress/*' -not -path '*/deprecated/*' | sort
