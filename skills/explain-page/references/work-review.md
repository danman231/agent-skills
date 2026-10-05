# Work review branch

Use this branch when the page explains work that an agent did. The reader must be able to answer these questions after one pass:

1. What changed?
2. Why did it change?
3. What does it affect (the blast radius)?
4. What can go wrong, and how would the reader know?
5. How was it verified, and what is still UNVERIFIED?
6. What must the reader decide, if anything?

## Gather the evidence

- **Diff:** `git diff`, `git show <sha>`, or `git log -p <range>`. Read each changed file in full where the diff alone hides the behavior.
- **Callers:** for each changed function, script, or config key, find what uses it (`grep -rn`). The callers are the blast radius.
- **Runtime:** for scheduled jobs, daemons, or services, read the real config (launchd plist, cron entry, deploy script) and the most recent log lines. A change that the code shows but the runtime does not load is not live. Say so. When a manual script feeds a scheduled job (or the opposite), give each part its own status.
- **Verification:** collect the actual test output, command output, or screenshots from the session. Do not write "tested" without the output. A step that did not run is UNVERIFIED.
- **Transcript or decision trail:** when the input is a session, list each decision, the reason given, and who made it (the user or the agent).

## Page shape for work review

- Above the fold: one sentence for what changed, one sentence for why, and status chips:
  - LIVE: the runtime uses the change now.
  - NOT LIVE: the change exists, but the runtime does not use it.
  - PARTLY LIVE: some parts are live. List what remains.
  - NOT YET RUN: the change is in place for a manual script or a future job, but no run has used it yet.
  - Add a chip for commit or push state when it matters ("committed, not pushed").
- Interaction: the before/after toggle on a real input is the default choice. Use a scenario picker when the change is about failure handling ("What happens if the mini restarts during a render?").
- A blast-radius map: the changed parts, and each caller or job that touches them.
- A risk table: risk, how the reader would see it, and what to do.
- Evidence: each claim with its source (`file:line`, command, log line). Put a status label (VERIFIED, UNVERIFIED, or ASSUMED, as SKILL.md defines them) on each claim.
- Decision box: only when the reader must decide something. One decision, with the recommended option first.

## Honesty rules

- Show the reader the uncomfortable parts first: failed checks, skipped steps, and side effects.
- Do not make the work look more complete than it is. A partly done task gets the PARTLY LIVE chip and a list of what remains.
- If the agent and the evidence disagree, show the evidence.
