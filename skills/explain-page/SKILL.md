---
name: explain-page
description: Build an interactive HTML explainer page that the user can play with to understand a system, a concept, or work an agent just did. Use when the user invokes /explain-page, asks for an interactive explainer, an explorable, a simulator, "a page I can play with", or "explain what you changed/did" as a page. Beginner-level static pictures belong to eli5, not this skill.
---

# Explain page

An **explorable**: a small, discardable web app that makes one mechanism visible. The reader changes something and sees the result. This is the oversight tool: when agents do the legwork, the reader uses this page to understand and check that legwork.

The reader is the user at their own level. They know their own systems and their own business. They do not know the internals of each script, library, or field. Do not explain things the user already knows. Explain the part that is new.

## Branches

- **Topic:** a concept, a system, or a tool ("how prompt caching works", "how the render queue chooses a job").
- **Work review:** the agent's own work, or another agent's work: a git diff, a commit range, a PR, a session transcript, logs, or a list of decisions ("explain what you changed in deploy.sh"). Read [references/work-review.md](references/work-review.md) before the plan step.

## Steps

1. **Find the one question.** Write the question that the page must answer in one sentence. Write the answer in one sentence. Completion: both sentences exist, and the answer is something that the reader can check.
2. **Ground it.** Read the real source: the code, the diff, the logs, the config, the docs in the repo. For current external facts, search with Firecrawl (`firecrawl search "..." --scrape`) or Exa (`mcp__exa__web_search_exa`). Use built-in web search only when those tools fail. Write down each claim that the page will make, with its source: `file:line`, a command output, or a URL. Memory files and session notes are leads, not evidence. Completion: each claim has one status label (below).
3. **Choose the interaction.** Find the one thing that the reader can change that shows the mechanism. Use the menu below. The interaction must run the real logic: port the actual rule, threshold, or formula into JavaScript, and cite its source in the page. Completion: you can write "When the reader changes X, the page shows Y, because of rule Z (source)." If no interaction shows more than a picture can, build a static diagram page and say why.
4. **Plan the page.** Write the section list: what the reader sees first, then what the reader can try, then the evidence. Keep this order:
   1. The question and the one-sentence answer, above the fold.
   2. The interactive part.
   3. "What this means for you": the decision or the action, if there is one.
   4. Evidence: sources, what you verified, and what remains UNVERIFIED.

   Completion: each section has one job, and no section repeats another.
5. **Write the words in STE.** Load the `ste` skill (Claude Code: the Skill tool. Codex: read `~/.claude/skills/ste/SKILL.md`). Use 80% strictness for all text on the page: headings, labels, notes, tooltips, and the text of each state. Step 7 extracts the page text and checks it. Completion: you wrote all text with the STE rules.
6. **Build the page.** Follow the build rules below. Save it to the output path. Completion: the file exists, and it opens from disk with no network.
7. **Check it.** Run:
   ```bash
   ~/.claude/skills/explain-page/scripts/check_page.sh PAGE.html
   ```
   It makes full-height screenshots (desktop 1280 px, mobile 390 px, dark), reports horizontal overflow, prints console errors, and writes the page text to `_check/<name>-text.md`. Then:
   - Run `python3 ~/.claude/skills/ste/scripts/ste_check.py _check/<name>-text.md --type description`. Correct each ERROR in the page.
   - Look at all three screenshots.
   - Operate each control with a browser tool (Claude in Chrome, the browser-use skill, or Playwright). Claude in Chrome does not open `file://` URLs. Serve the folder first: `python3 -m http.server 8765 --bind 127.0.0.1 --directory <folder>`, and stop the server when you finish. Make sure that each control changes the output, and that the output agrees with the source rule for at least two input values. To read the numbers of many states, you can click the real buttons with JavaScript and read the page values. Use at least one real click.

   Completion: zero console errors, no overflow, zero STE ERROR lines, no clipped or overlapping labels in the screenshots, and each control is tested. If no browser tool can operate the controls, write UNVERIFIED next to each control that you did not test.
8. **Hand off.** Give the path and the one-sentence answer. Name what is UNVERIFIED. Do not repeat the page in chat. In Claude Code, publish the page with the Artifact tool only when the user asks for a link or wants to share the page.

## Status labels

Use these three labels on the page and in the hand-off, with these meanings only:

- **VERIFIED**: you checked it in this run (a command output, a file read, a test).
- **UNVERIFIED**: a source says it, but you did not check it in this run (memory, notes, a commit message, a control you could not operate).
- **ASSUMED**: no source. You inferred it.

## Interaction menu

| The mechanism is... | Interaction |
|---|---|
| a process or a state machine | step-through: Next / Back, with the current state lit up and its trigger shown |
| a formula, a cost, a threshold, a limit | sliders with live results; mark the real current value |
| a change (before vs after) | a toggle between the old and the new behavior, on the same input |
| a branching rule or a failure mode | a scenario picker: "What happens if...?" with the path through the system lit up |
| an architecture | a clickable map: each component opens its job, its inputs, and its outputs |
| a sequence in time | a scrubbable timeline |
| understanding to test | predict, then reveal: the reader chooses an answer before the page shows the result |

Combine two at most. One good control is better than five weak ones.

## Build rules

- One self-contained `.html` file: inline CSS, inline JavaScript, inline SVG. No CDN, no external font, no network request, no build step. The file must work in Codex, offline, and from `file://`.
- Define the colors as CSS variables on `:root`. Add a dark theme in `@media (prefers-color-scheme: dark)`. Give `body` an explicit background.
- Responsive to 390 px width, with no horizontal scroll. Minimum 44 px touch targets.
- If you use motion, also support `prefers-reduced-motion`. The page must be complete without animation.
- Show the real numbers and the real names from the source (file names, job names, values). Do not use placeholder data that looks real. When you must use example data, label it "example".
- Put the source citation next to the rule that it supports, in small text.
- Plain vanilla JavaScript. Keep the logic in one `model` object, separate from the drawing code, so that a reader can compare the model to the source rule.
- Put the text for each state that the first render does not show (step texts, scenario results) in one `const COPY = {...}` object. The text extractor reads it for the STE check.
- Each section has one job. If two sections say the same thing, keep it in the section where the reader acts on it.

## Output path

Save outside the repo, so that explainers do not add files to the project:

```
~/Explainers/<project>/YYYYMMDD-HHMM-<slug>.html
```

`<project>` is the base name of `git rev-parse --show-toplevel`. If there is no git repo, use the base name of the current directory. If the current directory is the home directory, use `general`. Create the folder (`mkdir -p`) before you save the page. Screenshots go in `~/Explainers/<project>/_check/`. If the user gives a different location, use that location.
