# CLAUDE.md

Project instructions for Claude Code. This file is loaded automatically when a
Claude session starts in this repo — it's also a live demo of how teams teach
Claude their conventions (see docs/04-claude-code.md).

## What this repo is

A hands-on Git/GitHub/Actions training repo. The Python app under `app/` is
intentionally tiny — exercises in `docs/exercises.md` build on it, so keep
changes consistent with what the docs describe.

## Commands

```bash
pip install -r requirements.txt   # dev tools (pytest, ruff)
pytest                            # run tests — must pass before any commit
ruff check .                      # lint — must be clean before any commit
python -m app.cli greet Ada       # run the demo CLI
```

## Conventions

- Branch names: `feature/<thing>`, `fix/<thing>`, `docs/<thing>`. During shared
  training sessions, namespace with the author: `feature/<YourName>/<thing>`
  (e.g. `feature/AhmedA/divide`).
- Commit messages: conventional-commit style subject (`feat: ...`, `fix: ...`,
  `docs: ...`, `ci: ...`, `test: ...`, `chore: ...`), imperative mood,
  ≤ 72 chars; add a body explaining *why* for non-trivial changes.
- Small PRs: one feature or fix per branch, merged via squash.
- Code style: type hints on public functions, docstrings, no dependencies
  beyond the standard library for `app/` code.
- Always run `pytest` and `ruff check .` before committing.
