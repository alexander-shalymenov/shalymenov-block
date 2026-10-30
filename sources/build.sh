#!/usr/bin/env bash
set -euo pipefail
PROJECT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
exec "${PYTHON:-python}" "$PROJECT_ROOT/tools/build.py" --sources "$PROJECT_ROOT/sources" --output "$PROJECT_ROOT/build/ttf" --web-output "$PROJECT_ROOT/build/webfonts" "$@"
