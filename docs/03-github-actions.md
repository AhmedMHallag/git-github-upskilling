# GitHub Actions — CI/CD Fundamentals

## What is CI/CD?

- **Continuous Integration (CI):** every change is merged into the trunk
  frequently, and every change is automatically built and tested. Broken code
  is caught in minutes, in the PR — not in production three weeks later.
- **Continuous Delivery/Deployment (CD):** the path from "merged" to "running
  in production" is automated (delivery = one manual approval allowed;
  deployment = fully automatic).

GitHub Actions is GitHub's built-in automation platform: it runs your
pipelines right next to your code, triggered by anything that happens in the
repo (pushes, PRs, issues, schedules, button clicks...).

## The anatomy (learn these 5 words)

```
Workflow  (one YAML file in .github/workflows/)
 └─ triggered by EVENTS (on: push, pull_request, workflow_dispatch, schedule…)
 └─ Jobs   (each job gets its OWN fresh virtual machine — the runner)
     └─ Steps (run in order, on the same machine, sharing the filesystem)
         ├─ run:  a shell command            (echo, pytest, pip install…)
         └─ uses: a reusable ACTION          (actions/checkout@v4, …)
```

- **Runner** — the machine a job runs on. GitHub-hosted (`ubuntu-latest`,
  `windows-latest`, `macos-latest`) or **self-hosted** (your own VM — common
  for private networks or special hardware).
- **Action** — a reusable, versioned building block from the
  [Marketplace](https://github.com/marketplace?type=actions)
  (`actions/checkout`, `actions/setup-python`, `azure/login`, …). You can
  also author your own — that's how platform teams share pipeline logic.

## YAML in 60 seconds

```yaml
key: value                # strings rarely need quotes
number: 3                 #  ⚠ but "3.10" DOES need quotes — unquoted it becomes 3.1
list:
  - first
  - second
nested:
  key: value              # indentation (2 spaces) = structure; NEVER tabs
multiline: |
  line one
  line two
```

That's ~90% of the YAML you'll ever write in workflows. (Bicep next session
uses its own language — but everything around it stays YAML.)

## The workflows in this repo

| File | Teaches |
|------|---------|
| [01-hello-world.yml](../.github/workflows/01-hello-world.yml) | smallest workflow, triggers, runners, expressions |
| [02-python-ci.yml](../.github/workflows/02-python-ci.yml) | real CI: parallel jobs, matrix, `needs:`, marketplace actions, artifacts |
| [03-environments-demo.yml](../.github/workflows/03-environments-demo.yml) | environments, approval gates, per-environment variables |
| [04-claude.yml](../.github/workflows/04-claude.yml) | event-driven automation beyond CI: @claude in PRs |

## Parallel vs sequential jobs

Jobs run **in parallel by default**. `needs:` creates order:

```yaml
jobs:
  lint:                   # ┐
  test:                   # ┴ no needs → run at the same time
  build:
    needs: [lint, test]   # waits for BOTH to succeed
```

In `02-python-ci.yml` you can watch it live: `lint` and the three `test`
matrix jobs fan out simultaneously, then `build` runs last.

Steps *within* a job are always sequential — they share one machine.

## Variables & referencing

Three `env:` levels (workflow → job → step, inner wins), plus contexts you
reference with `${{ ... }}` expressions:

| Context | Example | What it is |
|---------|---------|------------|
| `github` | `${{ github.actor }}` | who/what triggered the run |
| `env` | `${{ env.APP_NAME }}` | your own variables |
| `matrix` | `${{ matrix.python-version }}` | current matrix value |
| `inputs` | `${{ inputs.version }}` | workflow_dispatch inputs |
| `vars` | `${{ vars.REGION }}` | repo/environment **Variables** (Settings) |
| `secrets` | `${{ secrets.API_KEY }}` | repo/environment **Secrets** (masked) |
| `needs` | `${{ needs.build.outputs.x }}` | outputs of earlier jobs |

## Environments

An **environment** (Settings → Environments) is a named deployment target —
`dev`, `staging`, `production` — that a job opts into with `environment: <name>`.
Each environment carries:

- **Protection rules** — e.g. *required reviewers*: the job waits until a
  human approves. This is the "manual gate to production" pattern, built in.
- **Its own variables and secrets** — same workflow YAML, different values
  per environment (`${{ vars.REGION }}` = `westeurope` in dev, `northeurope` in prod…).
- **Deployment history** — who shipped what, when, to where.

Run `03-environments-demo.yml` from the Actions tab and watch it stop at
`production` waiting for approval.

## Secrets vs variables

- **Variables** (`${{ vars.* }}`): plain config — regions, app names, flags.
  Readable in the UI, fine to expose in logs.
- **Secrets** (`${{ secrets.* }}`): credentials — masked in logs, write-only
  in the UI. Environment-scoped secrets are only released to jobs targeting
  that environment (so a `dev` job can never read `production` secrets).

**How we'll actually handle secrets at work (next session):** application
secrets live in **Azure Key Vault**, provisioned by Bicep — not in GitHub.
And for the pipeline's own login to Azure we'll use **OIDC federated
credentials** (`azure/login`), where GitHub exchanges a short-lived signed
token with Azure — *no password or key is stored in GitHub at all*; the
client/tenant/subscription IDs it needs are just variables. So a well-built
Azure pipeline can genuinely have **zero GitHub secrets**.

That's why today's session skips secrets — the only one you'll ever see in
this repo is Claude's API key, added during `/install-github-app` setup
(and that makes a nice 60-second look at the Secrets settings page).

## Where to go deeper

- The course this repo's structure is inspired by:
  [GitHub Actions: Beginner to Pro](https://youtu.be/Xwpi0ITkL3U) (DevOps Directive)
- [Workflow syntax reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
