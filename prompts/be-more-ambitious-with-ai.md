# Every prompt from "A Claude Engineer's 3 Ways to Get More Out of AI"

Prompts from the Strongin AI YouTube video. Felix Rieseberg's quoted lines stay his; the repo's MIT license covers only our summaries.

From Felix Rieseberg's tutorial "How to be more ambitious: A tutorial for humans with models" (October 13, 2026): https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

Lines in quote blocks or quotation marks are his, word for word; the other lines summarise his techniques. His examples use Acme Inc, an imagined company preparing its quarterly business review (QBR). Swap in your own task and data.

How to use this file: paste all of it into your AI along with a description of your work, and ask "Which of these apply to me, and how would you rewrite them for my task?"

## The deeper-version prompt (paste it in front of any task)

> I want a deeper version of this task, not a bigger one. Before rewriting it: (1) say what a top professional in this field would do here that I'm not asking for; (2) name the rawest material they would start from instead of what has already been digested for me; (3) name the specific methods and tools they would use; (4) say what, other than you or me, would show the result is right. Then rewrite my prompt to ask for exactly that.

## Altitude: ask for the goal beyond the goal

Felix's question first: "what do you want to happen next? What's the goal beyond the goal?"

1. Give it as much data as you can, then:
   > Tell me what changed this quarter, why, and what we should do about it.
2. Ask for decisions:
   > Work out which three decisions are most urgent in the face of everything you've learned, and start working on potential directions with for/against arguments.
3. Go after the purpose of the task itself:
   > The review exists so leadership catches problems early and moves money and people to the right places. Design a better way to do that than a quarterly deck, show from our own history that it would have caught things sooner, and run it beside the current one for a quarter.

## Depth: work like the best expert in the field

1. Insist on the experts' instruments: when it reaches for markdown tables, insist on databases and statistical models.
2. Pick an unreasonable goal and tell the model it's very reasonable. His example: a site that loads in 10 seconds, where you'd settle for 5? Ask for 200 milliseconds. If it says that's impossible, tell it the problem is solvable and it needs to keep going.
3. Challenge what you know:
   > We believe churn is an onboarding problem. Try to reproduce that from the raw data.
4. Produce new knowledge:
   > Build a simulation of our customers that reproduces the last year from our logs. Then find the earliest signal of churn we don't know about yet, and show it predicts on data it has not seen.
5. Use an outside judge: "Do not ask the model to judge itself." Check the result with something outside the model, ideally a tool it can run.

## Range: bring in other fields

1. Replace the nouns with verbs (from *The Art of Innovation*, Tom Kelley and Jonathan Littman). His example: a quarterly review isn't "a deck". It's "getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes".
2. Assemble the crew: imagine the stakes are huge and ask who you'd bring in. His crew: an analyst, a journalist, an editor, a motion and audio designer, and a red team of a short seller and a forensic accountant.
   His warning: "Don't ask the model to write like a short seller, ask it to do what a short seller does to research their position."

## What it needs

Felix: every technique needs the model to have a computer and access to your data (through connectors or other means).
