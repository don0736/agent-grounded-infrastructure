# Examples

AGI is designed so the user can give normal prompts and the harness routes the
agent to the right workflow.

## Generic Continue

```text
$agi continue
```

Expected behavior:

- read the current repo state and project instructions;
- find the active checkpoint or ledger;
- inspect recent failures, changed files, logs, or tests;
- choose one high-impact slice;
- validate before reporting;
- update the checkpoint when work spans sessions.

## Production Goal

```text
$agi make this app production-ready
```

Expected behavior:

- turn "production-ready" into a concrete rubric;
- avoid trying to fix everything at once;
- choose the first verifiable release gate;
- run the relevant test/runtime path;
- keep the goal alive until all required gates are actually done.

## Performance

```text
$agi make startup and playback faster
```

Expected behavior:

- prove the measurement path first;
- separate harness fixes from product fixes;
- avoid trusting one noisy run;
- report old pattern, new pattern, expected complexity or latency effect, and
  validation evidence.

## Android / ADB

```text
$agi validate this APK flow on device and fix the real blocker
```

Expected behavior:

- use emulator or real-device ADB when available;
- capture logcat, UI state, screenshots, or performance evidence;
- separate backend, API, auth, and player failures before editing;
- avoid screenshot-only proof for runtime/backend problems.

## Security

```text
$agi audit this app like a serious pre-release security review
```

Expected behavior:

- focus on auth, sessions, payments, provider URLs, tokens, logs, exported
  components, release config, and public API boundaries;
- validate findings before changing code;
- prioritize ship/revert/rework decisions over style comments.

## UI / Design

```text
$agi make this screen feel premium and validate the result visually
```

Expected behavior:

- inspect the current rendered UI;
- define the target state before editing;
- use design/Stitch/image/browser tooling when useful;
- validate with screenshots, UI tree, accessibility, and responsive states.

## Batch / Scraper / Database

```text
$agi fix this catalog backlog without wasting model turns item by item
```

Expected behavior:

- classify the population;
- build or reuse a batch runner;
- run a small validation sample;
- inspect aggregate output;
- scale only after the runner proves itself;
- return totals, failures, outliers, artifact paths, and next action.

