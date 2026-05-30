#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
source = payload.get("source", "startup")

context = f"""AGI autonomy profile active for this {source} session.

Default behavior:
- interpret, execute, validate, then report
- broad goals require internal refinement before edits
- ask questions only for real blockers
- use bounded subagents only when they materially help"""

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": context
    }
}))

