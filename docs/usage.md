# Usage

AGI is meant to make the entrypoint simple. The user says `$agi`, and the
harness should infer the right workflow from the live project state.

## Basic Prompt

```text
$agi continue from the current state. Pick the next highest-impact slice,
validate it with concrete evidence, and update the checkpoint.
```

## Strong Long-Running Prompt

```text
$agi resume the active goal from live repo state. Use code, tests, logs,
runtime artifacts, and the project ledger as source of truth. Choose the next
slice that moves the real product, try to falsify the strategy before editing,
make the smallest structural change, validate with concrete evidence, and
refresh the checkpoint.
```

## When You Want Validation Only

```text
$agi inspect the last run and return a verdict. Do not edit files. Tell me what
is proven, what is weak, and what the next best slice is.
```

## When You Want Design Work

```text
$agi improve this screen's visual quality. If visual direction is ambiguous,
create a target first, then implement the smallest UI-only patch and validate
with screenshots.
```

## When You Want Security Work

```text
$agi perform an authorized security pass on this app. Focus on auth, payment,
session, provider leakage, release config, logs, and playback boundaries.
Validate findings with concrete evidence before changing code.
```

## What AGI Should Do Automatically

- Read repo-local instructions and ledgers.
- Use CodeGraph for broad mapping if available.
- Initialize CodeGraph when it is safe and missing.
- Use ADB/emulator/logcat for Android behavior.
- Use Playwright/browser tools for UI and web behavior.
- Use docs/MCPs for version-sensitive facts.
- Spawn bounded subagents only when the job is independent and useful.
- Prefer batch runners for repetitive queues instead of reasoning item by item.
- Update checkpoints only when evidence exists.

## The User Should Not Need To Say

- "Use CodeGraph for this."
- "Use ADB for Android."
- "Use Playwright for browser evidence."
- "Use a reviewer subagent."
- "Use the design skill."
- "Update the checkpoint."

Those are routing decisions. `$agi` should choose them when the repo evidence
justifies them.

## What AGI Should Not Do

- Pretend one green test proves the product.
- Keep old and new paths competing silently.
- Ask the user to choose a skill for normal work.
- Spend xhigh reasoning on read-only mapping unless safety-critical.
- Copy secrets, cookies, profiles, sessions, or local account state.

See [`examples.md`](examples.md) for more copy-paste prompts.
