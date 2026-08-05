# Claude Code — the Modern Workflow

Everything from the first hour of this session — branching, staging, committing,
pushing, opening PRs, reviewing — Claude Code can do *for* you, from a chat in
your terminal. You stay in charge of *what* ships; Claude handles the mechanics.

## 1. Install & first run

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# or via npm, if you prefer
npm install -g @anthropic-ai/claude-code
```

Then, **inside the repo folder**:

```bash
cd git-github-upskilling
claude
```

First launch opens a browser to log in (Claude subscription or Anthropic
Console account). After that you're in a chat that can read the repo, run
commands (with your permission), and edit files.

## 2. Connecting Claude Code to GitHub

Three pieces, from "useful" to "magic":

1. **The `gh` CLI** — install [GitHub CLI](https://cli.github.com/) and run
   `gh auth login` once. Claude Code uses `gh` under the hood to open PRs,
   read PR comments, check CI status, etc. This is the main bridge to GitHub.
2. **`/install-github-app`** — run this *inside* Claude Code. It installs the
   Claude GitHub App on your repo and walks you through storing the API key
   secret, which powers
   the [04-claude.yml](../.github/workflows/04-claude.yml) workflow — after
   this, anyone can mention **@claude** in an issue or PR and Claude responds,
   reviews, and even pushes fixes.
3. **Claude Code on the web** — [claude.ai/code](https://claude.ai/code) runs
   the same agent in a cloud sandbox connected straight to your GitHub repos:
   assign it a task from your phone, get a PR back.

## 3. Living in Claude Code instead of the IDE

You can simply *say* what you did manually in hour one:

| You type | Claude does |
|----------|-------------|
| `implement divide() in the calculator, with tests` | writes code + tests, runs pytest |
| `stage and commit this with a good message` | `git add`, well-formed commit message |
| `push and open a PR` | `git push -u`, PR with filled-in template via `gh` |
| `what changed in the last 5 commits?` | reads & summarizes `git log -p` |
| `review PR #3 and leave comments` | fetches the diff, reviews, comments |
| `fix the failing CI on my PR` | reads the Actions logs, patches, pushes |
| `write a README for this module` | drafts docs from the actual code |

Useful commands inside the chat: `/help`, `/init` (generates a CLAUDE.md),
and plan mode (cycle modes with Shift+Tab) to review a plan before any file
is touched.

## 4. CLAUDE.md — teach Claude your house rules

The [CLAUDE.md](../CLAUDE.md) at the repo root is loaded automatically at
session start. Ours tells Claude how to run tests, our branch naming, and our
commit-message style — so its commits look like *ours*. Run `/init` in any
repo to bootstrap one.

## 5. @claude on GitHub (no terminal at all)

Once the GitHub App is installed (step 2.2):

- Comment `@claude please review this PR` → review appears as comments.
- Comment `@claude implement this` on an issue → Claude opens a PR.
- Comment `@claude fix the failing test` on a PR → commit lands on the branch.

This is CI/CD thinking applied to code review itself: the feedback loop runs
where the code lives.

## 6. Parallel Claude sessions with worktrees (power move)

```bash
git worktree add ../upskilling-feature-a feature/a
git worktree add ../upskilling-feature-b feature/b
# terminal 1: cd ../upskilling-feature-a && claude
# terminal 2: cd ../upskilling-feature-b && claude
```

Two Claudes, two branches, zero conflicts — each worktree is an isolated
checkout of the same repo. This is how you parallelize yourself.

## Safety notes (tell the team)

- Claude asks before running commands or editing files — read the prompts,
  especially for `git push` and anything destructive.
- Review Claude's diffs like any teammate's PR. The PR ritual doesn't change
  just because the author is an AI.
- Never paste real credentials into any chat; that's what Key Vault is for.
