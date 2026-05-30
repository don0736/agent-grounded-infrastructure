# AGI - Agent Grounded Infrastructure

AGI is a copy-paste Codex harness for people who want their agent to work for
hours or days without becoming sloppy, repetitive, or detached from reality.

It is not "artificial general intelligence" and it is not a prompt dump.

**AGI means Agent Grounded Infrastructure:** one router skill, one operating
model, bounded subagents, MCP routing, optional hooks, validation discipline,
and public-safe templates that make Codex behave like a grounded engineering
partner.

> Give the model freedom to solve the problem, but force every important move
> through live code, logs, tests, runtime evidence, ownership, and checkpoints.

[![Validate](https://github.com/don0736/agent-grounded-infrastructure/actions/workflows/validate.yml/badge.svg)](https://github.com/don0736/agent-grounded-infrastructure/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-white?labelColor=black&style=flat-square)](LICENSE)

## TL;DR

```bash
git clone https://github.com/don0736/agent-grounded-infrastructure.git
cd agent-grounded-infrastructure
./scripts/validate.sh
./scripts/install.sh --dry-run
./scripts/install.sh
```

Then open Codex and use one command:

```text
$agi continue
```

That is the point. You should not need to remember which skill, MCP, subagent,
browser tool, ADB flow, CodeGraph command, security pass, or design lane to use.
AGI routes the work from the live state of the repo.

## Ask Your AI If This Is Worth Installing

Paste this into Codex, ChatGPT, Claude, Gemini, or any code agent:

```text
Review this GitHub repo and tell me if it is worth installing for long-running
Codex engineering work:

https://github.com/don0736/agent-grounded-infrastructure

Judge it by whether it solves real agent failure modes: stale context, weak
validation, wrong-layer fixes, subagent theater, repetitive manual loops,
premature "done", and secret leakage. Read the README, docs, templates, and
scripts. Return: install verdict, strongest ideas, risks, and what you would
change before using it.
```

There is a fuller reviewer prompt in
[`docs/ai-evaluation-prompt.md`](docs/ai-evaluation-prompt.md).

## What Problem It Solves

Strong models still fail in boring ways:

- they edit before understanding the execution path;
- they fix the player when the backend is broken;
- they process queues item by item instead of writing a batch runner;
- they leave old and new code paths competing;
- they call one green test "production ready";
- they spawn subagents without scope;
- they lose the thread after compaction or a long session;
- they ask the user which tool to use when the repo already tells them.

AGI turns broad prompts into grounded execution:

1. read the repo, docs, logs, runtime, and checkpoint;
2. choose the highest-leverage slice;
3. try to disprove the strategy before editing;
4. make the smallest structural change;
5. validate with concrete evidence;
6. update the checkpoint;
7. keep the goal alive until the real objective is done.

## The One Command Interface

Use `$agi` with any normal prompt:

```text
$agi make this app production-ready
```

```text
$agi find why playback is slow and fix the real bottleneck
```

```text
$agi audit auth, payments, logs, provider tokens, and release config
```

```text
$agi improve this UI until it feels premium, then validate with screenshots
```

```text
$agi continue the active goal from the current checkpoint
```

AGI should infer the right route: CodeGraph, tests, Playwright, ADB/logcat,
Android emulator QA, security scan, design, Stitch, browser automation, docs
research, batch runner, or a bounded subagent.

## What Lands On Disk

The installer copies the same public-safe structure used by this harness:

```text
~/.codex/
  skills/agi/SKILL.md
  agents/default.toml
  agents/explorer.toml
  agents/worker.toml
  agents/reviewer.toml
  agents/oracle_critical.toml
  agents/rubric_evaluator.toml
  agents/docs_researcher.toml
  agents/design_pixel_perfect.toml
  agents/ui_debugger.toml
  hooks/session_start_autonomy.py
  hooks/user_prompt_autonomy.py
  hooks/stop_autonomy.py
  hooks.json
  config.example.toml

~/AGENTS.md
~/.gemini/GEMINI.md   # optional companion rules for Gemini/Antigravity
```

No private sessions, profiles, API keys, tokens, cookies, logs, databases, or
account state are included.

## Real Use Case This Came From

This harness was built while running a large Android streaming app stack with:

- Android APK work;
- scraper/backend/database work;
- real-device ADB and logcat validation;
- browser/UI validation;
- security and release checks;
- long `/goal` sessions that ran for days;
- repeated account/session resumes without losing operational state.

One of the main design requirements was simple:

> A generic "continue" prompt should not make the agent dumb. It should read
> the current evidence, pick the real next slice, validate it, and leave a
> checkpoint for the next model.

AGI packages that operating model without shipping the private project.

## What This Repo Contains

- [`skills/agi/SKILL.md`](skills/agi/SKILL.md) - the main AGI router skill.
- [`templates/AGENTS.md`](templates/AGENTS.md) - global operating rules.
- [`templates/codex/config.example.toml`](templates/codex/config.example.toml) - sanitized Codex config shape.
- [`templates/codex/agents/`](templates/codex/agents/) - bounded subagent roles.
- [`templates/codex/hooks/`](templates/codex/hooks/) - optional lightweight autonomy hooks.
- [`templates/gemini/GEMINI.md`](templates/gemini/GEMINI.md) - optional Gemini/Antigravity companion.
- [`docs/mcp-reference.md`](docs/mcp-reference.md) - MCP inventory and required credentials.
- [`docs/copy-paste-codex-setup.md`](docs/copy-paste-codex-setup.md) - exact install/copy structure.
- [`docs/examples.md`](docs/examples.md) - prompt examples and expected behavior.
- [`scripts/install.sh`](scripts/install.sh) - local installer with backups and dry-run.
- [`scripts/validate.sh`](scripts/validate.sh) - static validation.
- [`scripts/sanitize-check.sh`](scripts/sanitize-check.sh) - secret leak scanner.

## Install It With An Agent

Paste this into Codex from a normal shell:

```text
Install AGI from https://github.com/don0736/agent-grounded-infrastructure.
Read the README and docs/installation.md first. Run validate, run install
with --dry-run, explain what files will be copied, then install only the
public-safe harness. Do not copy private tokens, sessions, profiles, cookies,
logs, or account state.
```

Or do it manually:

```bash
git clone https://github.com/don0736/agent-grounded-infrastructure.git
cd agent-grounded-infrastructure
./scripts/validate.sh
./scripts/install.sh --dry-run
./scripts/install.sh
```

Then copy only the relevant parts of
`~/.codex/config.example.toml` into your private `~/.codex/config.toml` and add
your own MCP credentials locally.

## MCPs Are Optional, But Powerful

AGI knows how to route to these when configured:

| MCP / Tool | Why it matters |
| --- | --- |
| CodeGraph | architecture mapping, callers/callees, impact tracing |
| Git / GitHub | diffs, commits, repo search, publishing |
| Playwright / browser tools | UI proof, screenshots, console/network evidence |
| Android testing plugin | emulator, ADB, logcat, performance evidence |
| OpenAI docs | version-sensitive OpenAI/Codex behavior |
| Stitch | design system and frontend visual direction |
| Fetch / search tools | source-backed research |

Missing MCPs are not fatal. AGI should use the best available evidence and
record why it fell back.

## Public Safety

Before you publish or modify this repo:

```bash
./scripts/sanitize-check.sh
```

This repository deliberately ships placeholders only. Never commit:

- real `~/.codex/config.toml`;
- `~/.codex/sessions`;
- `~/.codex-profiles`;
- API tokens;
- browser cookies;
- account state;
- project logs;
- local databases.

## Why This Is Different From A Bigger Prompt

AGI is not trying to tell the model every step. It defines the operating
constraints that keep a strong model useful:

- outcome first;
- evidence over confidence;
- live code over stale memory;
- bounded subagents;
- batch runners for repetitive work;
- checkpoints for long goals;
- explicit cutover when replacing old paths;
- validation before closure.

The model still chooses the solution path. AGI makes it prove the path.

## License

MIT.
