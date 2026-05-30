# Security Policy

## Reporting

If you find a secret leak, unsafe install behavior, or instruction that could
cause broad destructive action by default, open a GitHub issue with:

- affected file;
- risk;
- reproduction steps;
- suggested fix if known.

Do not include real credentials in issues.

## Secret Handling

This repository should contain only placeholders. Real MCP/API credentials
belong in each user's private local config.

Run before publishing or opening a PR:

```bash
./scripts/sanitize-check.sh
```

If a real secret was pushed, rotate it. Removing it from the next commit is not
enough.

