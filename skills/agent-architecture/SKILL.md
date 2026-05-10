---
name: agent-architecture
description: Design or review reliable AI agent systems. Use this whenever the user is creating an AI agent workflow, multi-agent system, agentic automation, orchestrator, tool-using assistant, subagent setup, or is having reliability problems with agents. Helps split responsibilities, limit context, separate planning from execution, gate side effects, define structured outputs, add validation, logs, handoffs, rollback thinking, and human escalation for risky actions.
---

# Agent Architecture

Use this skill to turn an agent idea into a reliable operating design, or to diagnose why an existing agent system is behaving inconsistently.

The default posture is reliability through architecture, not faith that a model will behave consistently. Prefer small, observable, validated workflows over broad agents with too much context and too much authority.

## First pass

Start by identifying whether the user wants:

- **Design**: a new agent system, workflow, automation, or orchestrator.
- **Review**: an existing design, prompt chain, tool setup, repo workflow, or automation that is unreliable.
- **Repair**: a specific failure mode in an existing agent system.

If the user gave enough context, proceed. Ask only for missing details that change the architecture materially, such as the action being automated, what tools can cause side effects, where human approval is required, or what output another system consumes.

## Core defaults

Apply these defaults unless project instructions or the user explicitly override them:

- Prefer small, single-purpose agents over broad general agents.
- Give each agent minimal context and an explicit role.
- Separate planning, reasoning, and drafting from deterministic execution.
- Treat side effects as privileged actions.
- Prefer structured outputs over free-form outputs when outputs feed other steps.
- Require validation before public, destructive, financial, or production-facing actions.
- Prefer observable workflows with logs, clear handoffs, and rollback thinking.
- Add human escalation for risky or irreversible actions.

These are defaults, not rigid rules. Project-specific permissions, approval gates, and workflow details belong in the project's local instructions when present.

## Design workflow

### 1. Define the job

Write a one-paragraph statement of what the system is supposed to accomplish.

Include:
- The user-facing goal.
- The input sources.
- The expected final output.
- The tools or systems the agents may touch.
- The actions that are risky, expensive, public, destructive, financial, or production-facing.

### 2. Split responsibilities

Break the system into small roles. Avoid letting one agent both decide and execute risky actions.

Common role shapes:
- **Router**: classifies the request and chooses the next workflow.
- **Researcher**: gathers facts and citations without making changes.
- **Planner**: proposes the sequence of work and risk controls.
- **Drafter**: creates text, code, configuration, or structured proposals.
- **Executor**: performs deterministic tool calls or file operations.
- **Validator**: checks outputs against rules, tests, schemas, policies, or live state.
- **Human approver**: authorizes risky or irreversible actions.

Prefer fewer agents when a split does not reduce risk, context load, or complexity.

### 3. Set context boundaries

For each agent, define:
- What context it receives.
- What context it must not receive.
- What it can decide.
- What it cannot decide.
- What output format it must return.

Use minimal context. Give agents task-specific excerpts, schemas, examples, and constraints instead of full project dumps when possible.

### 4. Separate thinking from doing

Keep exploratory reasoning, planning, drafting, and side-effectful execution in separate stages when consequences matter.

Good pattern:
1. Gather or inspect information.
2. Produce a structured plan or diff proposal.
3. Validate the proposal.
4. Request approval when required.
5. Execute through deterministic tools.
6. Verify the result.
7. Log what happened and what remains.

### 5. Gate side effects

Treat these as privileged actions:
- Sending messages or emails.
- Posting publicly.
- Deleting, overwriting, purchasing, charging, deploying, merging, or publishing.
- Editing production data.
- Moving money or changing pricing.
- Triggering external workflows with real-world consequences.

For privileged actions, define:
- The approval gate.
- The exact preview the human sees.
- The validation that runs before execution.
- The rollback or recovery path.
- The log entry that proves what happened.

### 6. Structure machine-to-machine outputs

When one step feeds another, avoid prose-only handoffs.

Prefer schemas such as:

```json
{
  "status": "ready_for_approval",
  "summary": "Short human-readable summary",
  "inputs_used": [],
  "decisions": [],
  "actions_requested": [],
  "risks": [],
  "validation": {
    "checks_run": [],
    "passed": false,
    "notes": []
  },
  "next_step": "approval_required"
}
```

The exact schema should match the project, but every structured output should make state, risks, validation, and next action explicit.

### 7. Add validation

Define validation before execution, not after a failure.

Useful validation types:
- Schema validation for structured outputs.
- Unit tests, integration tests, linting, or build checks for code.
- Dry-run modes for external actions.
- Diff review for file edits.
- Live URL, API, or database checks for deployed state.
- Policy checks for public, paid, legal, medical, financial, or brand-facing outputs.
- Duplicate detection and idempotency checks for repeated jobs.

Validation should say what happens when it fails: retry, escalate, stop, or ask for human input.

### 8. Make the workflow observable

Design logs and handoffs so a fresh agent or human can reconstruct state.

Capture:
- Inputs used.
- Agent role that made each decision.
- Tool calls or deterministic commands run.
- Artifacts written.
- Validation results.
- Approval decisions.
- External side effects performed.
- Remaining blockers or next actions.

Keep logs concise and durable. Do not rely on chat history as the only record for important workflows.

## Review workflow

When reviewing an existing agent system, inspect it through these failure questions:

- Is one broad agent doing too many unrelated jobs?
- Does any agent receive more context than it needs?
- Are planning and execution mixed together?
- Can the model perform side effects without approval?
- Are machine-consumed outputs free-form when they should be structured?
- Is there validation before public, destructive, financial, or production-facing actions?
- Are failures observable, or does state disappear into chat history?
- Is there a recovery path if a tool call, deploy, send, or publish goes wrong?
- Is human escalation defined for risky or irreversible actions?

Then return the smallest architecture change that materially improves reliability.

## Output format

For design or review tasks, produce this structure unless the user asked for a different format:

```md
## Goal
[One paragraph describing the system's job.]

## Recommended Architecture
- [Role or stage]: [responsibility, inputs, outputs, allowed actions]

## Control Points
- Side effects:
- Approval gates:
- Structured outputs:
- Validation:
- Logs and handoffs:
- Rollback or recovery:

## Implementation Notes
- [Concrete changes to prompts, tools, files, schemas, queues, or runbooks.]

## Open Questions
- [Only questions that materially affect the design.]
```

For repair tasks, lead with the likely failure mode and the concrete fix.

## Practical rules

- Do not multiply agents just to make the system feel more advanced.
- Do not recommend autonomous execution for actions that need approval.
- Do not bury approval gates in prose; name where they happen.
- Do not use vague terms like "the agent should be careful" as a control. Replace them with validation, permissions, schema, tests, approval, or logging.
- Keep the architecture understandable enough that the user can explain how state moves through it.
