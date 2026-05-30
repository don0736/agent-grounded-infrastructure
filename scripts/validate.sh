#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

bash -n scripts/install.sh
bash -n scripts/sanitize-check.sh

python3 - <<'PY'
import pathlib
import sys

try:
    import tomllib
except ModuleNotFoundError:
    print("Python tomllib missing; use Python 3.11+ for TOML validation", file=sys.stderr)
    raise

root = pathlib.Path(".")
for path in list(root.glob("templates/**/*.toml")):
    with path.open("rb") as handle:
        tomllib.load(handle)
    print(f"TOML OK {path}")
PY

./scripts/sanitize-check.sh

echo "validate: PASS"

