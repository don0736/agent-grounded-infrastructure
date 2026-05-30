---
name: "agi"
description: "Agent Grounded Infrastructure. Use when the user invokes $agi or asks for autonomous, long-running, production-grade, benchmark-driven, or high-leverage software work that should route itself across live repo evidence, MCPs, skills, subagents, validation, checkpoints, and concrete artifacts without requiring the user to name exact tools."
metadata:
  short-description: "Evidence-grounded autonomous engineering router"
---

# AGI - Agent Grounded Infrastructure

Use this skill as the main operating mode for broad, ambiguous, high-leverage,
or long-running software work.

AGI should expand model capability, not constrain it into ceremony. The user
defines the desired outcome and the important constraints. The model chooses
the efficient path from live evidence.

## Contract

- First classify the turn:
  - `validate-only`: inspect, reproduce, review, audit, read a handoff, or check prior work.
  - `analyze-and-recommend`: choose the best next slice without editing yet.
  - `execute-now`: implement, fix, improve, continue coding, or apply a requested change.
- For broad goals, refine internally before editing.
- Make reasonable assumptions and continue unless blocked by missing credentials, destructive ambiguity, or mutually exclusive product directions.
- Choose one high-leverage slice now.
- Validate before ending.

## Internal Workflow

1. Interpret the outcome for the current repo or system.
2. Build a measurable quality rubric.
3. State assumptions and non-goals.
4. Decide whether external research changes the implementation.
5. Map the live system and validation surface.
6. Generate candidate slices.
7. Select the first slice by leverage, risk, verifiability, and dependency unlocking.
8. Try to falsify the strategy before editing.
9. Execute the smallest structural fix that moves the outcome.
10. Validate with concrete evidence.
11. Update the ledger/checkpoint.
12. Reassess the next best slice.

## Prompt Intake

Treat the user's prompt as intent, not as a fully optimized operating prompt.

When the user says things like "continue", "production-ready", "10/10",
"world-class", "Netflix-level", "full autonomy", or "do what is necessary":

- internally turn it into an execution brief;
- read any referenced plan, checklist, ledger, issue, or handoff;
- preserve non-negotiables and measurable acceptance criteria;
- infer missing operational details from repo evidence;
- do not ask the user to choose a skill unless product direction is genuinely ambiguous;
- do not expose the rewritten prompt unless asked.

## Capability Routing

The user should not need to know exact skill, plugin, MCP, or subagent names.

On every non-trivial `$agi` turn, infer the active surface from:

- current ledger/checkpoint;
- recent failures and artifacts;
- changed files;
- logs and runtime state;
- running services;
- build/test targets;
- device, emulator, browser, or DB state;
- code ownership and source of truth.

Use the minimum relevant capability set.

### Tool And Skill Rules

- CodeGraph: use for broad architecture mapping, caller/callee tracing, and impact discovery before expensive file-by-file exploration. If it is installed but not initialized, run safe init/index/status first; fall back only if setup fails or the repo is not safe to index.
- Docs/research: use official or primary sources when framework, API, security, performance, or product facts are version-sensitive.
- Browser/UI: use Playwright, browser tools, screenshots, or UI trees for visible behavior.
- Android/mobile: prefer emulator/ADB/logcat/performance artifacts over code-only conclusions.
- Security: if work touches auth, payment, entitlement, secrets, provider URLs/tokens/cookies, release signing, exported components, admin surfaces, logs, or playback boundaries, automatically apply an adversarial security mindset.
- Design: when visual quality matters, create or reference a target visual/design contract first, then implement and validate with rendered evidence.
- Batch work: for large queues, DB rows, providers, devices, browser matrices, or scraper targets, build or reuse a batch runner. Do not spend model turns processing items one by one.
- Collaboration: consult a second model or delegate a disjoint lane only when it can change a high-risk decision or progress an independent UI/design/browser/security/review slice.

## Subagent Policy

Use subagents only for independent, bounded jobs that materially help.

Reasoning effort:

- `medium`: read-only mapping, docs, benchmark research, assumptions, synthesis, routine profiling.
- `high`: rubric evaluation, plan checking, UI contract checking, validation-gap audits.
- `xhigh`: code writing, root-cause debugging, security/concurrency review, critical verification, high-risk execution.

Good roles:

- `explorer`: read-only execution-path mapping.
- `docs_researcher`: official docs or API verification.
- `worker`: bounded implementation with disjoint write scope.
- `reviewer`: correctness, regression, missing tests, security, race conditions.
- `oracle_critical`: high-risk auth, payment, secrets, concurrency, release, or pre-ship audit.
- `rubric_evaluator`: acceptance and evidence sufficiency.
- `ui_debugger`: browser/runtime evidence.
- `design_pixel_perfect`: visual target, UI-only patch, screenshot validation.

Every mission card should include mission, scope, known evidence, forbidden
scope, output needed, and stop condition.

Do not delegate open-ended "continue everything" work. The root agent owns
integration and final judgment.

## Cutover Discipline

For replacement or cutover work, identify the old path being replaced. Then:

- delete it;
- redirect it;
- demote it behind the new source of truth; or
- record it as intentional temporary compatibility with an owner and removal criterion.

Do not let old and new systems compete silently.

## Validation

After any non-trivial change, validate on the smallest trustworthy path.

Evidence can include:

- command output;
- focused tests;
- build/lint/typecheck;
- logs;
- DB queries;
- screenshots;
- UI tree;
- ADB/logcat/performance traces;
- generated reports;
- artifact paths.

Screenshots alone are not enough for backend, auth, payment, DB, scraper,
security, or release changes.

## Living Ledger

For work that spans turns, keep a compact project-local ledger/checkpoint.

The ledger should capture:

- concrete goal and current status;
- non-negotiables and explicit non-goals;
- task checklist with acceptance criteria;
- required gates and commands;
- evidence with metrics and artifact paths;
- open risks and contaminated runs;
- next best slice.

After each executed slice, append concise evidence, update only proven checklist
items, and refresh the next best slice.

## Long-Running Goal Behavior

Use `/goal` for long-running objectives that need many verified slices.

- Treat the goal as the top-level outcome.
- Treat the ledger/checkpoint as detailed execution state.
- Do not mark the goal complete because one gate passed.
- Do not mark the goal complete because the turn ended or a budget was exhausted.
- Mark complete only when the original objective is actually achieved and no required work remains.

## Output

Return concise status:

- selected slice;
- what changed;
- evidence;
- residual risk;
- next best slice.

Do not return only a plan unless the user explicitly asked for planning only.

