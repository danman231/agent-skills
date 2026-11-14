# The full table from "Gemini 4 Hydrogen vs 6 Models, Ranked by Cost per Job"

These numbers come from the Strongin AI YouTube video "Gemini 4 Hydrogen vs 6 Models, Ranked by Cost per Job". The scores, costs per task and times are Artificial Analysis's (read November 12, 2026), and the prices come from Google's, Anthropic's and OpenAI's pricing pages. The repo's MIT license covers only our own text, not their numbers.

How to use this file: find your job in the first table, then compare those models' score, cost per task and time in the second. Then try the model on one of your own prompts, because the benchmarks don't tell all.

## Which model for which job

| Job | Model |
|---|---|
| Fast everyday work, and anything where the facts matter | Gemini 4 Hydrogen |
| Hydrogen's level for the lowest cost per job | GPT-6.1 Sol |
| Coding in the terminal | Claude Sonnet 5.5 or Gemini 4 Carbon, not Hydrogen |
| Big batches of simple work | Claude Haiku 5.5 or GPT-6.1 Terra |
| Your hardest problems | Gemini 4 Carbon |

## Every model's score, cost per task and time

Artificial Analysis runs the same nine tests on every model (its Intelligence Index) and tracks what each run costs and how long it takes. A higher score is better.

| Model | Setting | Score | Cost per task | Time per task |
|---|---|---|---|---|
| Gemini 4 Hydrogen | high (the default) | 51 | $1.87 | 8.3 min |
| Gemini 4 Hydrogen | xhigh | 54 | $3.16 | 13.5 min |
| Gemini 4 Argon | high | 50 | $4.97 | 30.6 min |
| Gemini 4 Carbon | high | 60 | $5.48 | 28.1 min |
| Claude Sonnet 5.5 | xhigh | 50 | $4.09 | 14.7 min |
| Claude Sonnet 5.5 | max | 55 | $10.02 | 33.0 min |
| Claude Haiku 5.5 | max | 36 | $0.41 | 14.8 min |
| GPT-6.1 Sol | high | 50 | $0.59 | 7.8 min |
| GPT-6.1 Sol | max | 55 | $1.27 | 22.0 min |
| GPT-6.1 Terra | max | 51 | $0.96 | 14.2 min |
| Gemini 3.8 Flash | high | 31 | $7.77 | 14.8 min |
| Claude Opus 5.5 | xhigh | 57 | $6.05 | 15.8 min |

Argon's and Carbon's costs per task use today's price of $2 in and $10 out.

## Price per million tokens

| Model | In | Out |
|---|---|---|
| Gemini 4 Hydrogen (free tier in Google AI Studio) | $1.50 | $7.50 |
| Gemini 4 Carbon and Argon, through November 30, 2026 | $2 | $10 |
| Gemini 4 Carbon and Argon, from December 1, 2026 | $4 | $20 |
| Gemini 3.8 Flash | $0.75 | $3.75 |
| Claude Sonnet 5.5 | $2 | $10 |
| Claude Haiku 5.5 (prompts under 100,000 tokens) | $0.10 | $0.50 |
| GPT-6.1 Sol | $2 | $10 |
| GPT-6.1 Terra | $1 | $5 |

What you pay for a job is the tokens the model uses times the price per token. At their top settings, across the full set of tests, GPT-6.1 Sol wrote about 64 million output tokens and Hydrogen wrote 304 million. That is why Sol costs less per job even with a higher price per token.

## How often each model makes things up

Artificial Analysis asks every model hard expert questions with no tools and tells it to say when it doesn't know. This is how often a model gave a wrong answer when it didn't have the right one, instead of a partial answer or saying it didn't know. Lower is better.

| Model | Wrong answers |
|---|---|
| Gemini 4 Carbon and Gemini 4 Argon | 4% |
| Gemini 4 Hydrogen | 8% |
| Claude Sonnet 5.5 | 43% |
| GPT-6.1 Sol | 52% |

## Coding in the terminal (Terminal-Bench 4.0)

| Model | Score |
|---|---|
| Gemini 4 Carbon | 65 |
| Claude Sonnet 5.5 | 64 |
| Gemini 4 Hydrogen | 54 |

Turning Hydrogen up to xhigh didn't move its score here.

## Sources

- Artificial Analysis leaderboard: https://artificialanalysis.ai/leaderboards/models
- Artificial Analysis on Gemini 4 Hydrogen: https://x.com/ArtificialAnlys/status/2120941511223185722
- AA-Omniscience: https://artificialanalysis.ai/evaluations/omniscience
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Anthropic pricing: https://platform.claude.com/docs/en/about-claude/pricing
- OpenAI pricing: https://developers.openai.com/api/docs/pricing
