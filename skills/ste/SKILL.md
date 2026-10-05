---
name: ste
description: Write or rewrite text in ASD-STE100 Simplified Technical English (STE), at 80% strictness by default or full on request. Use when the user invokes /ste, asks for STE, Simplified Technical English, or "controlled English", or wants text made easier to read with STE rules. Also use when another skill (explain-page, explain-video) must write its words in STE.
---

# STE

STE is the controlled language of aerospace maintenance manuals. A tired mechanic at 3 a.m. must read a manual sentence once and do the right thing. Write every sentence for that reader.

## Strictness

| Level | When | What it means |
|---|---|---|
| `80%` (default) | Every request that does not say "full" or "strict" | All structure rules (sentence length, one instruction per sentence, active voice, one name per thing, no semicolons, no contractions, verbs for actions). Normal plain vocabulary. Real uncertainty stays. |
| `full` | The user says "full STE", "strict", or "100%" | Every rule as written, plus the STE dictionary. Use [references/dictionary-substitutions.md](references/dictionary-substitutions.md) for each word in doubt. |

The rule-by-rule table, with the 80% treatment of each rule, is in [references/rules.md](references/rules.md). Read it before the first STE text in a session.

## Core rules (both levels)

- **Sentence length:** maximum 20 words in an instruction, maximum 25 words in a description. Rule 8.6 tells you what counts as one word: numbers with units, file paths, code, names, quoted text, and parenthetical text.
- **Instructions:** one instruction in each sentence, in the command form. If the reader must know a condition first, start with it: "If the queue is not idle, wait 5 minutes."
- **Active voice.** Use the passive only when the actor is unknown.
- **Verbs for actions:** "do a check of the logs" → "check the logs". "Perform the installation" → "install".
- **One name per thing (Rule 1.11).** Choose a name for each item at its first use. Do not change it later in the text.
- **Paragraphs:** one topic in each paragraph, maximum six sentences. Use a vertical list for complex text.
- **Complete sentences:** keep the articles and connecting words (then, but, as a result). No contractions. No semicolons.
- **Noun clusters:** maximum three nouns in a row. "mini render queue restart flag" → "the restart flag for the render queue on the mini".
- **Warnings:** for a destructive or irreversible action, write WARNING or CAUTION, then the command, then the risk.

## Accuracy first

Rewriting into STE changes the form, never the facts. In a rewrite, the output must keep every fact, number, name, link, caveat, and uncertainty in the source. When a rule makes a sentence false or removes a caveat, keep the meaning and break the rule. At `full`, mark each such sentence with `[STE exception: <reason>]`.

When the source is ambiguous, do not guess the meaning. Ask, or write both readings and name the ambiguity.

## Steps

1. **Classify the text.** Find which parts are instructions (20-word limit) and which are descriptions (25-word limit). Completion: each paragraph or list has one of these two labels.
2. **Write or rewrite** with the core rules at the chosen level. For a rewrite, make a list of the facts in the source first. Completion: each fact from the source list is in the new text.
3. **Check** the text with the bundled checker:
   ```bash
   python3 ~/.claude/skills/ste/scripts/ste_check.py FILE --level 80   # or --level full; "-" reads stdin
   ```
   It flags long sentences, semicolons, contractions, possible passives, possible "-ing" nouns, long paragraphs, and inflated words. At `--level full` it also flags each word in the unapproved dictionary list. Correct each hard flag (`ERROR`). For each `REVIEW` flag, read the sentence and decide. Many are correct STE (example: "the failed job" is a correct past participle adjective). Completion: the checker shows zero `ERROR` lines, or each remaining one has an `[STE exception]` reason.
4. **Return the text only.** Do not add a list of changes unless the user asks for it. When another skill called this skill, give the text back to that skill.

## Examples

Before (29 words, passive, noun for an action, one name changed to another):
> The deployment was paused by the system because a render was in progress on the mini, and the restart will be performed once the job queue has been drained.

After (80%):
> The deploy script paused because a render was in progress on the mini. When the render queue is empty, the script restarts the service.

Before (an instruction with two actions and the condition at the end):
> Restart the daemon and check the log, but only if the kickstart failed.

After:
> If the kickstart failed, restart the daemon. Then check the log.
