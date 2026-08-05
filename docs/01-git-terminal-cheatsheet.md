# Git in the Terminal — Cheatsheet

Everything here works in any terminal (macOS, Linux, Windows Git Bash / PowerShell).
GitHub Desktop and VS Code do the same operations with buttons — learn the terminal
first and the GUIs become self-explanatory.

---

## 0. One-time setup

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@sulavamea.com"

# Git opens an editor for commit messages, rebases, etc.
# Default is often vim (confusing if you don't know it). Pick nano:
git config --global core.editor "nano"
```

> **Nano survival guide:** type your message → `Ctrl+O` (write out) → `Enter` (confirm
> filename) → `Ctrl+X` (exit). If you ever land in **vim** instead: press `Esc`,
> type `:wq`, press `Enter` to save & quit (`:q!` quits without saving).

---

## 1. Getting a repo & looking around

```bash
git clone https://github.com/AhmedMHallag/git-github-upskilling.git
cd git-github-upskilling

git status                       # ALWAYS your first command — what state am I in?
git log --oneline                # compact history
git log --oneline --graph --all  # history as a graph, all branches
git log -p -2                    # last 2 commits WITH their diffs
git show <sha>                   # one commit in full detail
git blame app/calculator.py      # who last touched each line, and in which commit
git diff                         # changes not yet staged (working tree vs staging area)
git diff --staged                # what exactly is about to be committed
```

---

## 2. Branching

```bash
git branch                       # list local branches (* = where you are)
git branch -a                    # include remote branches

git switch -c feature/divide     # create + switch (modern)
git checkout -b feature/divide   # same thing (classic — you'll see both everywhere)

git switch main                  # jump back to main
git branch -d feature/divide     # delete a merged branch (keep things tidy!)
```

Branch naming used in this repo: `feature/<thing>`, `fix/<thing>`, `docs/<thing>`.

---

## 3. Staging & committing

The **staging area** is a draft of your next commit — you choose what goes in.

```bash
git add app/calculator.py        # stage one file
git add .                        # stage everything (careful with this one)
git add -p                       # stage hunk-by-hunk — review every change as you stage
git restore --staged <file>      # unstage (keeps your changes in the file)
git restore <file>               # ⚠ discard local changes in the file (gone!)

git commit -m "feat: add divide function"    # short message inline
git commit                       # opens the editor (nano) → write a longer message
git commit --amend               # fix the LAST commit (message or add forgotten file)
```

**Anatomy of a good longer message** (what the editor is for):

```text
feat: add divide function to calculator

Division was missing from the toolbox. Returns a/b and raises
ZeroDivisionError on b == 0, matching Python's built-in behaviour.

Closes #7
```

Rule of thumb: subject line ≤ 72 chars, imperative mood ("add", not "added"),
blank line, then the *why* in the body.

---

## 4. Stashing — "I need to switch NOW but I'm mid-change"

```bash
git stash push -m "wip: half-done greeting tweak"   # shelve tracked changes
git stash list                   # see what's shelved: stash@{0}, stash@{1}, ...
git stash show -p stash@{0}      # peek inside a stash
git stash pop                    # re-apply most recent stash AND drop it
git stash apply stash@{1}        # re-apply but keep it in the list
git stash drop stash@{0}         # throw one away
```

---

## 5. Cherry-picking — "I want THAT one commit over here"

```bash
git log --oneline origin/demo/cherry-pick-me   # find the commit you want
git cherry-pick <sha>                   # replay it onto YOUR current branch
git cherry-pick --abort                 # bail out if it conflicts and you panic
```

Typical real-world uses: a hotfix that must go to both `main` and a release
branch, or rescuing a commit made on the wrong branch.

---

## 6. Syncing with GitHub

```bash
git fetch origin                 # download remote state, touch nothing local
git pull origin main             # fetch + merge into your current branch
git push -u origin feature/divide   # first push: -u links local ↔ remote branch
git push                         # after that, plain push is enough
```

---

## 7. Undo, safely (bonus)

```bash
git revert <sha>                 # NEW commit that undoes an old one — safe on shared branches
git reset --soft HEAD~1          # uncommit last commit, keep changes staged
git reset --hard HEAD~1          # ⚠ destroy last commit AND its changes — local only!
git reflog                       # the "undo history" — finds "lost" commits
```

> On anything already pushed and shared: prefer `git revert`. `reset --hard`
> and force-pushes are for your own unpushed work.
