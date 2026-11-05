# The prompts from "An Anthropic Engineer's 5 Checks Before You Trust AI"

Prompts from the Strongin AI YouTube video. Lines in quotation marks or quote blocks credited to Addy Osmani or Thariq Shihipar are theirs, word for word; the repo's MIT license covers only our own text.

How to use this file: you don't need all five on every task. Start with check 1. If being wrong is cheap, like picking between three similar hotels, skip them and let AI pick.

## Check 1: write your guess down before you ask

No prompt for this one. Before you run an agent on anything that isn't trivial, write one line saying what you think the answer will be. A bad guess is fine.

Examples: "I think the second supplier is cheaper." "I think the email needs 3 sentences, not 10."

### No idea what to expect? Ask for a blind spot pass

Thariq Shihipar's example, from Anthropic's field guide:

> I don't know what color grading is but I need to grade this video. Can you teach me to understand my unknown unknowns about color grading, so that I can prompt better?

Swap color grading and the video for your own task. Thariq uses the literal words "blind spot pass" and "unknown unknowns".

## Check 2: ask it what it decided for you

Paste this when the work is done:

```text
List every decision and assumption you made that I didn't ask for.
```

Then this one, Addy Osmani's own question:

```text
Did I miss anything?
```

## Check 3: read what it ran before its summary

No prompt for this one. Before you read the summary, look at the command it ran and what came back. When a check goes green, Addy's advice: "ask what it proved. Then ask what it didn't."

Not code? Open a couple of the source documents and check that the summary is accurate. Then check the one number your recommendation depends on.

## Check 4: decide what done means before it starts

Put this in the prompt, and swap the first sentence for your own finish line, like a test passing or a screenshot:

```text
Done means every number links to its source. When you finish, show me the proof for each one, not a summary.
```

## Check 5: make it quiz you before you ship

Thariq's prompt, from the same field guide. His rule: "I only merge after I pass the quiz perfectly."

> I want to make sure I understand everything that's happened in this change. Give me a HTML report on the changes for me to read and understand with context, intuition, what was done, etc. and a quiz at the bottom on the changes that I must pass.

If you don't merge code, swap merge for whatever you do: send it, publish it, present it.

For a document, no prompt needed. Addy's version: close it and try to write out the main argument from memory.

## Try it today

1. Before your next prompt, write down what you think will happen.
2. After it's done, write down one thing it didn't check.

## Sources

- Addy Osmani, "Critical thinking when agents do the work": https://x.com/addyosmani/status/2117512471930167377
- Thariq Shihipar, "A field guide to Claude Fable 5: Finding your unknowns": https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns
