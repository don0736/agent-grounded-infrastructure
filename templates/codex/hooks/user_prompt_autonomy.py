#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
prompt = payload.get("prompt", "")
normalized = prompt.lower()

notes = [
    "AGI reminder: interpret, execute, validate, then report. Use reasonable assumptions unless blocked."
]

if any(token in normalized for token in ["$agi", "autonom", "deleg", "parallel", "subagent", "end-to-end"]):
    notes.append("Delegation is allowed when it materially helps and scopes are bounded.")

if any(token in normalized for token in ["review", "audit", "code review", "pull request"]):
    notes.append("Review mode: lead with findings; prioritize bugs, regressions, security issues, and missing tests.")

if any(token in normalized for token in ["frontend", "ui", "browser", "playwright", "screenshot", "design", "visual", "premium", "pixel perfect"]):
    notes.append("UI/debug mode: reproduce or inspect rendered state first; change code only after the failure mode or target state is clear.")

if any(token in normalized for token in ["api", "sdk", "docs", "documentation", "latest", "current", "official"]):
    notes.append("If external behavior is version-sensitive, verify from primary or official documentation.")

if any(token in normalized for token in ["goal", "/goal", "long-running", "sem parar", "24 hours"]):
    notes.append("Goal mode: treat the active goal as the top-level objective and the ledger/checkpoint as detailed execution state; do not mark complete because one gate passed.")

validation_terms = ["validate", "verify", "check if", "worked", "review what was done", "read the handoff", "analyze", "audit", "inspect"]
execution_terms = ["implement", "fix", "change", "edit", "go ahead", "continue coding", "apply the fix"]

if any(term in normalized for term in validation_terms) and not any(term in normalized for term in execution_terms):
    notes.append("Validation-first mode: inspect current state and return a verdict before editing files.")

short_prompt = len(re.findall(r"\w+", normalized)) <= 18
quality_terms = ["world-class", "world class", "production-ready", "production ready", "premium", "best in class", "10/10"]
if short_prompt and any(term in normalized for term in quality_terms):
    notes.append("Broad-goal protocol: create an internal brief with objective, rubric, assumptions, local map, selected slice, and validation plan before editing.")

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": "\n".join(notes)
    }
}))

