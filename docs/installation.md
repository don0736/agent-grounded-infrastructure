# Installation

## Requirements

- Linux or macOS shell.
- Codex CLI installed.
- Python 3.11+ recommended for TOML validation.
- Optional MCP server binaries installed for the capabilities you want.

## Install

```bash
./scripts/validate.sh
./scripts/install.sh --dry-run
./scripts/install.sh
```

The installer writes:

- `skills/agi` into `$CODEX_HOME/skills/agi`;
- Codex agent templates into `$CODEX_HOME/agents`;
- hook templates into `$CODEX_HOME/hooks`;
- `config.example.toml` into `$CODEX_HOME/config.example.toml`;
- `templates/AGENTS.md` into `$HOME/AGENTS.md` if no file exists;
- `templates/gemini/GEMINI.md` into `$HOME/.gemini/GEMINI.md` if requested or
  if the directory already exists.

Existing files are backed up unless you run with `--dry-run`.

## Environment Variables

```bash
export CODEX_HOME="$HOME/.codex"
export AGI_INSTALL_GEMINI=1
```

## MCP Credentials

Do not commit secrets. Add them only to your private local config.

Typical optional secrets:

- `GITHUB_PERSONAL_ACCESS_TOKEN`
- `BRAVE_API_KEY`
- `STITCH_API_KEY`

See `docs/mcp-reference.md`.

## After Install

Open Codex and run:

```text
$agi inspect this repo and tell me the highest-leverage first slice. Do not
edit files until you have mapped the live code and validation surface.
```

For long work:

```text
/goal $agi turn this project into a production-ready release. Work by verified
slices, validate with artifacts, and keep a compact checkpoint after each
material slice.
```

