# Git & GitHub Upskilling — Hands-On Session

Welcome! This repo is the playground for our 90-minute session on **modern Git workflows,
GitHub, CI/CD with GitHub Actions, and Claude Code**.

Everything we do today happens in this repo: you will clone it, branch it, break it,
fix it, and ship it — first manually in the terminal, then through GitHub's UIs,
and finally with Claude Code doing the heavy lifting.

> **The one rule of today:** `main` is always green. Everything else is a short-lived
> branch that gets merged through a pull request. That's trunk-based development,
> and it's the whole session in one sentence.

---

## 🗓 Agenda (90 minutes)

| Time | Topic | Material |
|------|-------|----------|
| 00:00 – 00:10 | **Why we're here** — trunk-based development, history & motivation of CI/CD | [docs/02](docs/02-branching-and-prs.md) |
| 00:10 – 00:35 | **Git in the terminal** — clone, log, branch, stage, commit (incl. the editor), stash, cherry-pick | [docs/01](docs/01-git-terminal-cheatsheet.md) · Exercises 1–4 |
| 00:35 – 00:50 | **The PR ritual** — push, open a PR, review, green checks, merge (terminal, GitHub Desktop, VS Code) | [docs/02](docs/02-branching-and-prs.md) · Exercise 5 |
| 00:50 – 01:10 | **GitHub Actions** — CI/CD, YAML, workflows/jobs/steps, runners, variables, parallel vs sequential, environments | [docs/03](docs/03-github-actions.md) · Exercises 6–7 |
| 01:10 – 01:25 | **Claude Code** — setup, connecting to GitHub, commits/PRs/reviews from the terminal, `@claude` in PRs | [docs/04](docs/04-claude-code.md) · Exercise 8 |
| 01:25 – 01:30 | **Wrap-up** — Q&A · next session teaser: Bicep + Azure Key Vault | — |

The full hands-on script with copy-pasteable commands is in
**[docs/exercises.md](docs/exercises.md)**.

---

## 🗺 What's in this repo

```
├── app/                      # A tiny Python "toolbox" — the code we practice on
│   ├── calculator.py         #   add / subtract / multiply (+ divide, YOUR feature)
│   ├── greetings.py          #   greet (+ farewell, waiting on demo/cherry-pick-me)
│   └── cli.py                #   python -m app.cli greet Ada
├── tests/                    # pytest suite — this is what CI runs
├── docs/                     # Session guides & cheatsheets (see agenda above)
├── .github/
│   ├── workflows/
│   │   ├── 01-hello-world.yml        # The smallest possible workflow
│   │   ├── 02-python-ci.yml          # Real CI: parallel lint + test matrix → build
│   │   ├── 03-environments-demo.yml  # dev → staging → production with approval gates
│   │   └── 04-claude.yml             # @claude mentions in issues & PRs
│   └── pull_request_template.md
└── CLAUDE.md                 # Project instructions for Claude Code (also a demo!)
```

The app is deliberately tiny and dependency-free: **the code is not the point —
the workflow around the code is.** A feature = a branch = a small PR.

---

## 🚀 Setup (do this before the session)

You need: **Git**, **Python 3.11+**, **VS Code**. Optional but recommended:
[GitHub Desktop](https://desktop.github.com/) and [Claude Code](https://code.claude.com/docs/en/quickstart).

```bash
# 1. Clone the repo (HTTPS is fine; SSH if you have keys set up)
git clone https://github.com/AhmedMHallag/git-github-upskilling.git
cd git-github-upskilling

# ...and make git open nano (not vim) for commit messages
git config --global core.editor "nano"

# 2. Create a virtual environment and install dev tools
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Prove everything works
pytest                            # tests should pass (one is skipped — that's your feature)
python -m app.cli greet "$(whoami)"
```

If `pytest` is green, you're ready.

---

## 🧑‍🏫 Facilitator checklist (pre-session)

- [ ] Everyone has a GitHub account and is able to clone this repo
- [ ] Everyone is added as a **collaborator** (Settings → Collaborators) so they
      can push branches and open PRs — or have attendees fork instead
- [ ] In **Settings → Environments**: create `dev`, `staging`, `production`;
      on `production` add yourself under **Required reviewers** (this is the approval-gate demo)
- [ ] Optionally add a variable `REGION` (e.g. `westeurope`) on each environment
      to show per-environment configuration
- [ ] Run `/install-github-app` from Claude Code once, so `@claude` works in PRs
      (see [docs/04](docs/04-claude-code.md))
- [ ] Branch `demo/cherry-pick-me` exists (used in Exercise 4)

> **Note on secrets:** this session needs **no cloud credentials and no GitHub secrets**
> (the one exception is the Claude API key you add during `/install-github-app` setup).
> Environments are demoed with plain variables and approval rules.
> How secrets *would* fit in — and why we'll mostly avoid them with Key Vault + OIDC —
> is covered in [docs/03](docs/03-github-actions.md#secrets-vs-variables).

---

## 📖 Credits & further watching

The GitHub Actions portion is inspired by DevOps Directive's excellent
[GitHub Actions: Beginner to Pro](https://youtu.be/Xwpi0ITkL3U) course.
