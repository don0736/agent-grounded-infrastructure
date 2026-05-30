# Release Checklist

Use this before publishing to GitHub.

## Required

- [ ] `./scripts/validate.sh` passes.
- [ ] `./scripts/sanitize-check.sh` passes.
- [ ] `git status --short` only shows intended files.
- [ ] README explains what AGI is and is not.
- [ ] Install docs work from a fresh clone.
- [ ] MCP docs list required secrets without including any.
- [ ] AI reviewer docs explain how to evaluate the harness.
- [ ] License is present.

## Recommended

- [ ] Create a clean GitHub repository.
- [ ] Push one initial commit.
- [ ] Add screenshots or terminal output showing dry-run install.
- [ ] Pin a short X post:
  - what AGI is;
  - why it improves Codex;
  - how to install;
  - what makes it different from prompt dumps.

## Launch Positioning

Short version:

> AGI is a public Codex harness for long-running, evidence-grounded engineering:
> skills, MCP routing, subagent roles, checkpoints, and validation discipline in
> one installable repo.

