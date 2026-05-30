#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if ! command -v rg >/dev/null 2>&1; then
  echo "ERROR: ripgrep (rg) is required for sanitize-check." >&2
  exit 2
fi

patterns=(
  'ghp_[A-Za-z0-9_]{20,}'
  'github_pat_[A-Za-z0-9_]{20,}'
  'sk-[A-Za-z0-9_-]{20,}'
  'xox[baprs]-[A-Za-z0-9-]{20,}'
  'AKIA[0-9A-Z]{16}'
  '-----BEGIN (RSA |OPENSSH |EC |DSA |PRIVATE )?PRIVATE KEY-----'
  'BRAVE_API_KEY[[:space:]]*=[[:space:]]*"[^"]+"'
  'STITCH_API_KEY[[:space:]]*=[[:space:]]*"[^"]+"'
  'GITHUB_PERSONAL_ACCESS_TOKEN[[:space:]]*=[[:space:]]*"[^"]+"'
)

allow_placeholders='REPLACE_WITH_LOCAL_SECRET|YOUR_|EXAMPLE|placeholder|placeholder-only'

failed=0
for pattern in "${patterns[@]}"; do
  if rg -n --hidden --glob '!.git/**' --glob '!node_modules/**' --glob '!dist/**' --glob '!build/**' -e "$pattern" . \
    | rg -v "$allow_placeholders"; then
    failed=1
  fi
done

if [ "$failed" -ne 0 ]; then
  echo "ERROR: possible secret material found. Review output above." >&2
  exit 1
fi

echo "sanitize-check: PASS"

