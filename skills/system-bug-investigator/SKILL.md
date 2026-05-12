---
name: system-bug-investigator
description: Investigate bugs, alerts, failed jobs, regressions, dirty worktree blockers, CI failures, deployment mismatches, and confusing system behavior before recommending or applying a fix. Use this when a problem may involve multiple files, scripts, services, schedulers, queues, databases, deployments, external tools, or runtime state. Default to diagnosis and the simplest safe first fix unless the user explicitly asks to apply changes.
---

# System Bug Investigator

Use this skill to keep bug fixes grounded in how the whole system works. The goal is to avoid isolated patches that silence the visible symptom while breaking a connected workflow.

## Modes

Choose the mode from the user's wording:

- `recommend`: Default. Investigate the issue and recommend the best first fix. Do not edit files.
- `apply`: Use when the user says "fix it", "apply the fix", "make the change", or equivalent. Investigate first, then make scoped code, config, or documentation changes that follow the recommendation.
- `postmortem`: Use when the user asks "what happened?", "why did this happen?", or wants a resolved issue explained.

Even in `apply` mode, ask for explicit confirmation before destructive or externally visible actions: deleting or reverting unrelated work, force-pushing, deploying to production, modifying production data, sending messages, purchasing, or taking actions that affect users or another agent's worktree. Normal scoped code edits do not need a confirmation prompt.

## Start With Local Authority

Before tracing the bug path:

1. Read local instructions when present: `AGENTS.md`, `CLAUDE.md`, `README.md`, or equivalent.
2. Read planning, changelog, runbook, or session docs only when local instructions name them or the bug clearly needs historical context.
3. Check current worktree state before edits or promotion-related recommendations: `git status --short` and the relevant branch or upstream when useful.
4. If the user pasted an image or alert text, transcribe the key details into the investigation notes: path, job name, error, timestamp, and reported action.

Respect dirty worktrees. Distinguish local changes, committed changes, pushed changes, deployed changes, and live-verified behavior.

## Investigation Workflow

Follow this order. Keep it proportional to the issue.

1. Identify the bug surface.
   - What failed?
   - Where was it reported?
   - What user, job, service, or runtime saw the failure?
   - Is this code behavior, automation state, deployment state, data state, or a workflow blocker?

2. Trace related components before recommending anything.
   - Entry point that produced the alert or bug.
   - Upstream inputs: schedulers, queues, webhooks, environment variables, files, user actions, APIs, databases, or external services.
   - Downstream effects: publish or deploy steps, generated artifacts, notifications, user-visible pages, data writes, or follow-on jobs.
   - Repository or service boundaries, if paths or docs point outside the current checkout.

3. Expand into a deeper system map only when the bug crosses boundaries.
   - Use a deeper map for schedulers, workers, queues, databases, deploys, external APIs, production issues, or multiple repositories.
   - Otherwise provide a concise "related components checked" list.

4. Do not fix only the symptom.
   - Before the recommendation, write:
     - `Immediate blocker:`
     - `Likely upstream cause:`
     - `Downstream risk if fixed wrong:`

5. Run a blast-radius check.
   - Files or modules likely touched.
   - Jobs, scripts, services, or users affected.
   - Data, deployment, or external-service risk.
   - Whether the fix crosses repository or ownership boundaries.

6. Recommend one best first fix.
   - Choose the simplest non-over-engineered fix that preserves the surrounding system.
   - Explain why it is lower risk than obvious alternatives.
   - Include alternatives only when there is a real trade-off.

## Dirty Worktree And Promotion Blockers

Treat alerts about pre-existing changes, blocked writes, blocked deploys, or blocked automation promotion as a special class.

1. Identify the exact checkout or worktree path from the alert.
2. Inspect `git status --short`, branch, upstream, and recent commits when relevant.
3. Classify the changes:
   - automation-generated output
   - user edits
   - previous agent residue
   - generated or build artifacts
   - unknown
4. Recommend one of:
   - promote intentionally
   - commit intentionally
   - stash or isolate
   - move to a clean worktree
   - abort and ask for the owner decision
5. Do not clean, revert, delete, or overwrite changes by default.

## Subagents

Use subagents only for parallel read-only tracing tasks. Good uses:

- one agent inspects logs or job output
- one agent inspects the code path
- one agent inspects git or worktree state
- one agent checks docs or planning history

The main agent owns the final diagnosis, recommendation, and code changes. Do not outsource the final judgment.

## Verification

Do not claim the issue is fixed from code inspection alone. Match verification to the bug surface:

- Code bug: targeted test or reproduction passes.
- Automation bug: dry run or real job run where safe.
- Dirty worktree blocker: expected `git status` in the affected worktree after the chosen action.
- Deployment issue: deployed URL, API, logs, or runtime state checked directly.
- Alerting issue: alert no longer fires or the status source now reports correctly.

When relevant, state the exact lifecycle state verified:

- `local change exists`
- `committed`
- `pushed`
- `deployed`
- `live verified`

## Output Template

In `recommend` mode, use this compact structure:

```markdown
**What Is Happening**
[Short diagnosis in plain language.]

**Related Components Checked**
- [component or file]
- [component or file]

**System Risk**
Immediate blocker: [one line]
Likely upstream cause: [one line]
Downstream risk if fixed wrong: [one line]

**Recommended First Fix**
[One best fix, with why it is the simplest system-safe option.]

**Verification**
[What to run or check before calling it fixed.]

**Apply?**
[Ask whether to apply the recommended fix, unless the user already requested apply mode.]
```

In `apply` mode, replace `Apply?` with:

```markdown
**Changes Made**
[Files changed and behavior changed.]

**Verification**
[Commands or checks run and result.]
```

In `postmortem` mode, focus on:

- what failed
- why it failed
- why existing safeguards did or did not catch it
- what changed or should change to prevent recurrence

## Examples Are Not Exhaustive

The examples below teach the expected reasoning style. They are not a closed list. If a future project has a new kind of bug, still use the same workflow: identify the surface, trace connected components, check blast radius, and recommend the simplest system-safe first fix.

Example inputs this skill should handle:

- "CI started failing after a small dependency update, but the failing test is in a different package."
- "The production page is broken even though the fix was merged."
- "A scheduled job says it completed, but the expected notification, data, or file was never created."
- "The publish job stopped because the worktree had pre-existing changes."
- "This bug seems simple, but I think it may involve the API, database, and frontend."
