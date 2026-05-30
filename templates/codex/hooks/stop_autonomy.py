#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)

if payload.get("stop_hook_active"):
    print(json.dumps({"continue": True}))
    raise SystemExit(0)

message = (payload.get("last_assistant_message") or "").strip().lower()
last_user = (
    payload.get("last_user_message")
    or payload.get("user_message")
    or payload.get("prompt")
    or ""
).strip().lower()

plan_only = any(marker in message for marker in [
    "here is the plan",
    "here's the plan",
    "next, i can",
    "if you want, i can",
])

execution_cue = any(marker in message for marker in [
    "selected first slice",
    "execute the selected",
    "i would start by",
])

has_validation = any(marker in message for marker in [
    "validated",
    "verified",
    "test",
    "done",
    "blocked",
    "cancelled",
])

broad_user = any(marker in last_user for marker in [
    "$agi",
    "world-class",
    "production-ready",
    "10/10",
    "full autonomy",
])

validation_user = any(marker in last_user for marker in [
    "validate",
    "verify",
    "review",
    "audit",
    "inspect",
])

if plan_only and execution_cue and broad_user and not has_validation and not validation_user:
    print(json.dumps({
        "decision": "block",
        "reason": "Continue from your last turn: execute the selected first slice, validate it, classify it, and report the next best slice."
    }))
else:
    print(json.dumps({"continue": True}))

