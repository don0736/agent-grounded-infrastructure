# Contributing

AGI should stay small, installable, and evidence-oriented.

## What Fits

- Improvements that reduce common agent failure modes.
- Better install validation.
- Better public-safe MCP documentation.
- Better examples that show concrete evidence workflows.
- Small, durable rules that generalize across projects.

## What Does Not Fit

- Huge prompt dumps.
- Private configs, sessions, tokens, cookies, account state, or logs.
- One-project-only rules.
- Instructions that make the model mechanical instead of evidence-driven.
- Extra subagent roles without a clear bounded use case.

## Pull Request Standard

Before opening a PR:

```bash
./scripts/validate.sh
```

Explain:

- what failure mode the change addresses;
- why it belongs in the harness instead of one user's local config;
- how it was validated;
- whether it changes install behavior.

