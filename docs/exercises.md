# Hands-On Exercises

The live script for the session. Every exercise is self-contained; commands
are copy-pasteable. Facilitator demos first, then everyone repeats.

> Prerequisite: you completed the [README setup](../README.md#-setup-do-this-before-the-session)
> and `pytest` is green.

> **We all share this repo**, so namespace every branch with your name:
> `feature/<YourName>/<thing>` — e.g. `feature/AhmedA/divide` instead of
> `feature/divide` (the exercises below use the short names for readability).
> That way everyone can build the same feature without collisions, and the
> branch dropdown on GitHub groups each person's work together. In the live
> session we'll fully merge **one** volunteer's PR; everyone else completes
> the whole ritual and then closes their PR without merging — you still did
> every step.

---

## Exercise 1 — Read the history (5 min)

Get comfortable *looking* before touching anything.

```bash
git status
git log --oneline                     # the story of this repo, one line per commit
git log --oneline --graph --all       # same, as a graph, including other branches
git show HEAD                         # the latest commit in full
git blame app/calculator.py           # who wrote each line, in which commit
```

**Goal:** you can answer "what happened here recently, and who did it?"

---

## Exercise 2 — Your first feature branch: `divide()` (10 min)

The calculator can't divide. Fix that — *on a branch*.

```bash
git switch -c feature/divide     # in the live session: feature/<YourName>/divide
```

Edit `app/calculator.py` and implement:

```python
def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    return a / b
```

Then open `tests/test_calculator.py` and **delete the `@pytest.mark.skip(...)` line**
above `test_divide`. Run the tests:

```bash
pytest        # 6 passed — including your new divide test
```

Now stage *interactively* — review each change as you stage it:

```bash
git add -p                            # 'y' to stage a hunk, 'n' to skip, '?' for help
git status                            # both files staged?
```

Commit **without** `-m` — this opens the editor (nano):

```bash
git commit
```

Write a proper message (subject, blank line, body — see the
[cheatsheet](01-git-terminal-cheatsheet.md#3-staging--committing)), then
`Ctrl+O`, `Enter`, `Ctrl+X`.
*(Landed in **vim** instead of nano? Press `Esc`, type `:wq`, hit `Enter` —
then run `git config --global core.editor "nano"` from the README setup.)*

**Stay on this branch** — Exercise 5 pushes it.

---

## Exercise 3 — Stash rescue (5 min)

You're mid-edit when an urgent request comes in. Simulate it:

```bash
# still on feature/divide — start "half-finished" work:
echo "# WIP: refactoring idea, do not commit" >> app/greetings.py

git switch main                       # ⚠ git may warn or carry changes along — mess!
git switch feature/divide             # go back, let's do it properly

git stash push -m "wip greeting refactor idea"
git status                            # clean! now you can switch safely
git stash list

git stash pop                         # bring the work back...
git status
git restore app/greetings.py          # ...and discard it (it was just a demo line)
```

**Goal:** switching branches never again means losing or dragging along work.

---

## Exercise 4 — Cherry-pick a colleague's commit (5 min)

A `farewell()` function already exists — as a single commit on the branch
`demo/cherry-pick-me`. Pull *that commit only* onto your branch:

```bash
git fetch origin demo/cherry-pick-me
git log --oneline origin/demo/cherry-pick-me   # find the "farewell" commit, copy its sha

git switch feature/divide
git cherry-pick <sha>

git log --oneline                     # the commit is now (also) yours
pytest                                # farewell tests came along with it
```

**Goal:** you can move a single commit between branches — without merging
everything else that branch contains.

---

## Exercise 5 — The PR ritual (10 min)

Ship `feature/divide` (which now also carries `farewell()`):

```bash
git push -u origin feature/divide
```

Git prints a ready-made **"Create a pull request"** link — open it.
Fill in the template (what / why / how tested) and create the PR. Then:

1. Watch the **Checks** tab: `02 - Python CI` runs lint + a 3-version test
   matrix in parallel, then `build`. Green ✅ appears on the PR.
2. Pair up: your neighbour opens your PR, reads the diff in **Files changed**,
   leaves one comment, and **approves**.
3. **Squash & merge**, then click **Delete branch**.
   *(Live session: only the volunteer's PR gets merged — everyone else closes
   theirs without merging after step 2.)*
4. Locally: `git switch main && git pull && git branch -d feature/divide`

**Also try:** the same flow in **GitHub Desktop** (Branch → New branch, commit
checkboxes, Push, "Create Pull Request") and in **VS Code** (Source Control
view + GitHub Pull Requests extension). Same Git, different buttons.

---

## Exercise 6 — Break the build (5 min)

See CI actually protect `main`:

```bash
git switch -c fix/deliberately-broken   # live session: fix/<YourName>/deliberately-broken
```

Edit `app/calculator.py`: make `add()` return `a + b + 1`. Push and open a PR:

```bash
git commit -am "fix: improve addition"      # (-a = stage all tracked changes)
git push -u origin fix/deliberately-broken
```

The PR shows a red ❌ — click into the failing job, read pytest's output, and
notice you can spot the bug *from the log alone*. Fix it, push again, watch it
turn green. Then close the PR without merging and delete the branch (it was
just a drill).

**Goal:** red CI is information, not punishment. Read the log, fix, push.

---

## Exercise 7 — Environments & the approval gate (5 min)

*(Facilitator setup: environments `dev`, `staging`, `production` exist, and
`production` has a required reviewer — see the README checklist.)*

1. Actions tab → **03 - Environments Demo** → **Run workflow** (pick any version).
2. Watch `deploy-dev` → `deploy-staging` run sequentially (`needs:`).
3. The run **pauses** at `deploy-production`: *"Waiting for review"*.
4. The reviewer approves → production "deploys" 🎉.
5. Check each job's log: `${{ vars.REGION }}` resolved differently per environment.

**Goal:** you've seen delivery gates without a single secret or cloud resource.

---

## Exercise 8 — Build your own workflow, live (10 min)

You've *run* our pre-built pipelines — now write one from zero. Ten lines of
YAML is a complete, working workflow.

Start clean, on a fresh branch:

```bash
git switch main && git pull
git switch -c feature/<YourName>/first-workflow
```

Create a new file `.github/workflows/hello-<yourname>.yml` — your name in the
filename, since we all push to the same repo:

```yaml
name: Hello <YourName>

on:
  push:
    paths:
      - ".github/workflows/hello-<yourname>.yml"   # runs only when THIS file changes

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Hello from my very first workflow!"
```

Ship it and watch it run:

```bash
git add .github/workflows/hello-<yourname>.yml
git commit -m "ci: add my first workflow"
git push -u origin feature/<YourName>/first-workflow
```

Open the **Actions** tab: your workflow's name appears in the left sidebar —
click the run, click the job, unfold the step, read your echo. That's the
whole loop: YAML in the repo → machine in the cloud → logs in the browser.

**Level it up** — add one thing at a time, push after each, watch what changes:

1. A step that reads the event context:

   ```yaml
      - run: echo "Pushed by ${{ github.actor }} to ${{ github.ref_name }}"
   ```

2. A step in a different language — steps can run anything the runner has:

   ```yaml
      - run: print("Hello from Python on a GitHub runner!")
        shell: python
   ```

3. A second job — and watch the Actions graph make it wait for the first:

   ```yaml
     celebrate:
       needs: say-hello
       runs-on: ubuntu-latest
       steps:
         - run: echo "say-hello finished, so now I get to run 🎉"
   ```

> **Why `on: push` and not the Run-workflow button?** The
> `workflow_dispatch` button only appears for workflows that already exist on
> the *default branch* (`main`). Your file lives on your own branch, so we
> trigger on push instead — that's also why `01-hello-world.yml` (which IS on
> main) has the button and yours doesn't yet.

Cleanup: no PR for this one — when you're done, delete the branch locally
(`git switch main && git branch -D feature/<YourName>/first-workflow`) and on
GitHub (**Branches** page → 🗑).

Want more building blocks after the session? The course repo that inspired
this one has a folder of small, focused example workflows:
[03-core-features](https://github.com/AhmedMHallag/github-actions-tut/tree/main/03-core-features).

**Goal:** you *wrote* a workflow from scratch, triggered it, and read its logs —
jobs, steps, expressions and `needs:` are now things you've typed, not just seen.

---

## Exercise 9 — Do it all again with Claude Code (10 min)

Everything above, but you only *describe* the work
([setup instructions](04-claude-code.md)):

```bash
cd git-github-upskilling
claude
```

Then, in the chat, one step at a time:

```text
> Implement a power(a, b) function in app/calculator.py with tests,
  following the existing style.

> Run the tests.

> Create a branch feature/<YourName>/power, stage everything and commit
  with a proper message, then push and open a PR.
```

While the PR is open, go to GitHub and comment on it:

```text
@claude please review this PR — anything missing?
```

...and watch the [04-claude.yml](../.github/workflows/04-claude.yml) workflow
answer as a reviewer.

**Goal:** connect the dots — Claude isn't magic, it's doing the *exact* ritual
you just learned by hand, and you can read every step it takes.

---

## Bonus (if time allows / homework)

- `git worktree add ../upskilling-2 -b try/worktree` — two checkouts, one repo
  ([why this matters with Claude](04-claude-code.md#6-parallel-claude-sessions-with-worktrees-power-move))
- `git commit --amend` — fix your last commit message
- `git revert <sha>` — undo a merged commit *safely* on main
- Ask Claude: `explain the difference between merge and rebase using this repo's history`
