# Trunk-Based Development & the PR Ritual

## Why this session exists

Shipping software used to look like: months of work on long-lived branches,
a terrifying "merge week", manual deployments from someone's laptop, and a
release nobody wanted to be on call for. CI/CD grew out of exactly that pain:
**integrate continuously, keep the mainline releasable, automate the checks.**

## Trunk-based development in one picture

```
main  ──●──●──●──●──●──●──●──●──▶   always green, always releasable
           \      /  \    /
            ●──●─      ●─           short-lived branches (hours–days, not weeks)
         feature/divide  fix/typo
```

The rules we follow:

1. **`main` is the trunk.** It must always pass CI and be releasable.
2. **Branches are short-lived.** A branch holds *one* small change and merges
   within a day or two. If it's getting big, split it.
3. **Nothing lands without a PR.** Even one-line changes. The PR is where
   review, CI checks and sign-off happen.
4. **Small PRs get good reviews.** A 50-line PR gets read; a 2000-line PR
   gets skimmed and rubber-stamped.
5. **Delete branches after merging.** The history lives in `main`.

Contrast: *GitFlow* (develop/release/hotfix branches everywhere) optimizes for
scheduled big-bang releases. Trunk-based optimizes for continuous delivery —
which is where we're heading with GitHub Actions.

## The PR ritual

Every change follows the same loop:

```
branch  →  commit(s)  →  push  →  open PR  →  CI goes green  →  review  →  merge  →  delete branch
```

1. **Branch** — `git switch -c feature/divide`
2. **Commit** — small, well-messaged commits (see the [cheatsheet](01-git-terminal-cheatsheet.md))
3. **Push** — `git push -u origin feature/divide`
4. **Open the PR** — GitHub even prints a ready-made link when you push.
   Fill in the template: *what, why, how tested*.
5. **Green checks** — our [CI workflow](../.github/workflows/02-python-ci.yml)
   runs lint + tests on every PR. Red ❌? You fix it before anyone reviews.
6. **Review** — a teammate reads the diff, comments, requests changes or
   approves. Review the *code*, respect the *person*.
7. **Merge** — squash-merge keeps `main`'s history clean (one commit per PR).
8. **Delete the branch** — GitHub offers the button right after merging.

> **Draft PRs** are great for early feedback: open the PR as a draft while
> you're still working — CI runs, people can peek, nobody is asked to review yet.

## Three ways to do the same thing

| Step | Terminal | GitHub Desktop | VS Code |
|------|----------|----------------|---------|
| Branch | `git switch -c ...` | Branch menu → New branch | branch name in status bar → Create new branch |
| Stage  | `git add -p` | tick checkboxes per file/line | Source Control view → `+` per file |
| Commit | `git commit` | message box → Commit | message box → ✓ Commit |
| Push   | `git push -u origin ...` | Push origin button | Sync/Publish button |
| PR     | link printed on push, or GitHub website | "Create Pull Request" button | GitHub Pull Requests extension |

They all drive the same Git underneath. Use the terminal to *understand*,
use whichever UI makes you *fastest* day-to-day.

## Worktrees (advanced teaser)

One repo, several working directories — no stashing needed to work on two
branches at once:

```bash
git worktree add ../upskilling-hotfix -b fix/urgent-thing
# → a second folder with a new fix/urgent-thing branch checked out; your current folder is untouched
git worktree list
git worktree remove ../upskilling-hotfix
```

This becomes really powerful with Claude Code: run one Claude session per
worktree and it develops several features *in parallel* without them stepping
on each other. More in [docs/04](04-claude-code.md).
