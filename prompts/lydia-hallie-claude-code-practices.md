# The prompts from "5 Claude Code Jobs Anthropic Says to Stop Doing Yourself"

These come from the Strongin AI YouTube video "5 Claude Code Jobs Anthropic Says to Stop Doing Yourself". The repo's MIT license covers only our own text.

The five jobs and the advice come from Lydia Hallie, who works on Claude Code at Anthropic, in her talk "Rethinking Claude Code Best Practices" (AI Engineer): https://www.youtube.com/watch?v=vlfCjWuv4es . The four-line done prompt is hers, as read in the video. The autoMode lines and the deny rule are the examples from Anthropic's Claude Code docs, as read in the video. The hook settings are our own version of the hooks she describes.

How to use this file: go through the five jobs in order and copy what you need. Settings go in a Claude Code settings file: your user settings are ~/.claude/settings.json, a project's are .claude/settings.json in the repo. Replace anything in [brackets] with your own.

## 1. Stop steering: cut your CLAUDE.md

No prompt for this one. The steps:

1. In a Claude Code session, run the command below. It checks your CLAUDE.md and your skills for instructions written for older models, paths to files that don't exist, and lines that contradict each other.

```text
/doctor prompt-audit
```

2. Read the report. Nothing in your files changes until you ask Claude to apply the fixes.
3. Cross out lines like "IMPORTANT: always use the auth helper", "Think hard and be thorough" and "Keep going until it's done". With today's models they can make the model go off track.
4. Keep only what Claude can't see in your code, like Lydia's one line: "src/legacy still serves our mobile apps." Your stack and where things live, Claude can read itself.
5. Aim for under 200 lines per CLAUDE.md file (Anthropic's docs). A rule that can't have exceptions belongs in a hook (job 4).

## 2. Stop approving: tell auto mode what you trust

New terminal and VS Code sessions start in auto mode. By default it trusts only the folder you're working in and your repo's remotes, so anything else gets blocked. Tell it what you trust in plain English, the way you'd explain your setup to a new engineer.

This goes in your user settings, ~/.claude/settings.json. Auto mode doesn't read autoMode from a project's settings file, so a repo can't hand itself permissions. Keep "$defaults" in each list: a list without it throws away the built-in rules.

Anthropic's example:

```json
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: github.example.com/acme-corp and all repos under it"
    ],
    "allow": [
      "$defaults",
      "Deploying to the staging namespace is allowed: staging is isolated from production and resets nightly"
    ]
  }
}
```

Your version:

```json
{
  "autoMode": {
    "environment": [
      "$defaults",
      "Source control: [your GitHub org or repos]",
      "[Another place you trust, in plain English]"
    ],
    "allow": [
      "$defaults",
      "[An action that is safe in your setup, and why]"
    ]
  }
}
```

Rather not write it yourself? Run this and Claude Code drafts the entries from your project and your recent sessions:

```text
/auto-mode-setup
```

## 3. Stop saying no to everything: rules only for what you can't take back

Lydia's one question for each thing Claude might do:

```text
If Claude gets this wrong once, can I take it back?
```

- Yes (edits to code, tests or docs, anything git can revert): leave it to the model.
- No (it deletes something for good, exposes a secret or sends something outside): make it a rule.

The deny rule from the video. Deny rules are checked before the auto mode classifier, so this one doesn't depend on it:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)"
    ]
  }
}
```

Now Claude's file tools, and commands like cat, can't open your .env file.

One limit: a deny rule sees the command, not what the command opens. If npm test runs a dependency that reads your .env, the rule never sees it. Turn on the sandbox for that, and the operating system blocks the file:

```text
/sandbox
```

The sandbox covers shell commands only. Claude's file tools run outside it, so keep the deny rule too.

## 4. Stop checking by eye: make "done" a test

Lydia's prompt, four lines:

```text
Move auth over to the new API.
It's done when the auth tests pass and nobody gets logged out.
Split it into tasks, each with its own test.
Show me the test output.
```

Your version:

```text
[The job you want done].
It's done when [one thing you can check, like a test that passes].
Split it into tasks, each with its own test.
Show me the test output.
```

The last line is there because you weren't around to watch.

A prompt isn't a guarantee. For anything that has to run every time, use hooks, scripts Claude Code runs at set points:

- Every edit runs your linter (PostToolUse).
- Every task Claude marks complete runs that task's tests (TaskCompleted).
- When Claude wants to stop, the whole suite runs (Stop).

The catch: most test tools exit with code 1 when a test fails, and in Claude Code exit code 1 is a non-blocking error, so the task gets marked completed anyway. Your hook has to exit with code 2. That's what sends Claude back to fix it, with your hook's error output as the reason.

Our version of the three hooks. Put it in your project's .claude/settings.json and swap in your own lint and test commands:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "[your lint command] 1>&2 || exit 2" }
        ]
      }
    ],
    "TaskCompleted": [
      {
        "hooks": [
          { "type": "command", "command": "[your test command] 1>&2 || exit 2" }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          { "type": "command", "command": "[your full test suite command] 1>&2 || exit 2" }
        ]
      }
    ]
  }
}
```

"1>&2" sends the tool's output to the error stream, which is what Claude reads when the hook exits with code 2. If a Stop hook can never pass, Claude keeps going back; the hooks docs explain the stop_hook_active field your script can check: https://code.claude.com/docs/en/hooks

## 5. Stop starting every session: Projects

No prompt for this one. The steps:

1. Open Projects from the sidebar in Claude Code (public beta, on the Pro, Max and Ultra plans).
2. Talk to the one project conversation. Tell it what needs doing; it starts a thread for each task and keeps track of what comes back.
3. In Project settings > General, set the Coordinator model to Fable (it decides and judges) and the Thread model to Opus 5.5 (it does the work). That's Lydia's setup. You set the two separately, and a new project runs Opus everywhere until you change it.
4. You don't manage context: threads compact on their own.

## Start with these two

If you only do two, do the done check and the can-I-take-it-back rule. Today:

1. Run /doctor prompt-audit and read what it flags.
2. End your next prompt with this:

```text
It's done when [one thing you can check].
```

Sources: Lydia Hallie's talk (link above). Anthropic's docs: https://code.claude.com/docs/en/best-practices , https://code.claude.com/docs/en/auto-mode-config , https://code.claude.com/docs/en/permissions , https://code.claude.com/docs/en/sandboxing , https://code.claude.com/docs/en/hooks , https://code.claude.com/docs/en/claude-projects
