# Every prompt and setting from "How Do You Know Your AI Agent Actually Tested Its Work?"

Prompts and settings from the Strongin AI YouTube video. Lines in quotation marks or quote blocks credited to Anthropic, Zach Lloyd or a maker's docs are theirs, word for word; the repo's MIT license covers only our own text. Prices and settings were checked on the makers' pages on October 24, 2026. Check them again before you rely on them.

How to use this file: paste all of it into your coding agent with a short description of your project, and ask "Set this up for my project: which parts apply, and what do I change?"

## The loop

1. The builder agent makes the change and records the feature in use.
2. A different model watches the recording and answers PASS or FAIL.
3. On FAIL, the builder fixes what the reviewer saw, records again, and the reviewer watches again.
4. It stops only on PASS. You see the last recording and the verdict, not every round.

Why a different model: models rate their own work higher (arXiv 2404.13076), and Anthropic's Claude Code docs say "A fresh context improves code review since Claude won't be biased toward code it just wrote."

## Step 1: make the agent record the change

If you test in a browser, Playwright records every test with one setting:

```ts
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  use: { video: 'on' },   // 'retain-on-failure' keeps only the videos of failing tests
});
```

The values are `'off'`, `'on'`, `'retain-on-failure'` and `'on-first-retry'`. The videos land in `test-results/`.

No Playwright? Use Computer Use, which takes screenshots as it tests. In my view it's best in ChatGPT right now.

Builder prompt:

> Make this change. Then record the feature working: write or update a Playwright test that uses the feature the way a person would, run it with `video: 'on'`, and give me the path to the video. The change isn't done until that recording exists.

## Step 2: hand the recording to a different model

The reviewer prompt:

> Here is the change and its recording. Does this show the fix working? Answer PASS or FAIL, then what you saw.

**Codex:** one line in `~/.codex/config.toml`. It sets the model that `/review` uses. If you don't set it, `/review` uses the model you're already working with.

```toml
review_model = "<model>"
```

**Claude Code:** a reviewer subagent with its own `model:` line. Save this as `.claude/agents/reviewer.md`. `model:` takes `haiku`, `sonnet`, `opus` or a full model ID.

```markdown
---
name: reviewer
description: Watches the recording of a change and answers PASS or FAIL. Use after every change that has a recording.
tools: Read, Bash
model: haiku
---
You review someone else's change. You get a description of the change and frames from a recording of it in use.
Does this show the fix working? Answer PASS or FAIL, then what you saw in the frames.
If the frames don't show the feature being used, answer FAIL.
```

## Which models can watch the recording

- **Gemini** takes the video file itself. To read text on screen, set the media resolution to high.
- **Kimi K3.1 Pro** takes video too.
- **Claude** takes images, so give it frames, one a second. One way to make them (needs ffmpeg):

```bash
mkdir -p frames && ffmpeg -i test-results/<test-folder>/video.webm -vf fps=1 frames/%03d.png
```

## What one review costs

A 30-second recording at 1280×800, one frame a second, is about 40,000 input tokens on Claude. The cost repeats on every pass of the loop.

| Reviewer | One 30-second review (input) |
|---|---|
| Claude Opus 5.5 | about 16¢ |
| Claude Haiku 5.5 | under ½¢ |
| Gemini 3.8 Flash (watches the video file, high media resolution) | under 1¢ |

Prices per million tokens, input / output, on October 24, 2026:

| Model | Price |
|---|---|
| Kimi K3.1 Pro | $2 / $10 (the same as Claude Sonnet 5.5) |
| Claude Sonnet 5.5 | $2 / $10 |
| DeepSeek Flash (`deepseek-flash`) | 15¢ to 30¢ in, depending on the time of day |
| Claude Haiku 5.5 | 10¢ / 50¢ |
| GPT-6 Luna | 10¢ / 50¢ |

Before you trust a cheap reviewer's PASS, test it. In my one run, on one change to my own app, Opus 5.5 said FAIL and Haiku 5.5 listed the same problem but still said PASS. In the loop, that PASS would have ended it right there. Give your reviewer a change you know is broken and see whether it says FAIL.

## Close the loop

Builder prompt for every change:

> After each change: record the feature working, send the recording to the reviewer, and read its answer. On FAIL, fix what the reviewer saw, record again and send the new recording. Stop only when the reviewer says PASS. Then show me the last recording and the reviewer's answer.

## Win the time back on the build side

- **Claude Code:** `/model opusplan` uses Opus while you plan, then switches to Sonnet to build.
- **Codex:** `model_reasoning_effort` in `~/.codex/config.toml` sets how hard the model thinks. The levels depend on the model, from `low` up.

```toml
model_reasoning_effort = "low"
```

- **End the PRD with the check.** Anthropic's docs say a good spec should "end with an end-to-end verification step that proves the feature works." For example:

```markdown
## Verification
Run <test name> with video recording on. The reviewer model watches the recording and must answer PASS.
The recording must show: <what a person sees when the feature works>.
```

## Sources

- ShengHui Wang's test of coding agents gaming tests: https://x.com/KevinShengHui/status/2103132319183990952
- Models rate their own writing higher (arXiv 2404.13076): https://arxiv.org/abs/2404.13076
- Zach Lloyd (Warp) on screen-recording artifacts in every PR: https://x.com/zachlloydtweets/status/2113655321189359831
- Stephanie Jarmak's AI Engineer talk: https://www.youtube.com/watch?v=A3FL_zTQKU0
- Anthropic, Claude Code best practices: https://code.claude.com/docs/en/best-practices
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code model configuration (`opusplan`): https://code.claude.com/docs/en/model-config
- Codex config reference (`review_model`, `model_reasoning_effort`): https://learn.chatgpt.com/docs/config-file/config-reference
- Playwright videos: https://playwright.dev/docs/videos
- Gemini video understanding: https://ai.google.dev/gemini-api/docs/video-understanding
- Claude pricing: https://platform.claude.com/docs/en/about-claude/pricing
- Kimi pricing: https://platform.kimi.ai/docs/pricing/chat
