---
name: explain-video
description: Make a narrated, 3Blue1Brown-style explainer video (MP4) on any topic, system, or piece of agent work, with a teaching script in STE and on-device Kokoro narration, built and rendered with HyperFrames. Use when the user invokes /explain-video, asks for an explainer video, a "3b1b-style" video, or wants something explained as a video.
---

# Explain video

A **3b1b explainer**: one question, a concrete example first, and pictures that move only to show change. The narration points at what is on screen. The screen carries the idea.

This skill owns the **teaching**: the question, the facts, the script, and the scene plan. HyperFrames owns the **build**: the composition, the voice synthesis, and the render. Do not write composition HTML from this skill.

## Budget and stop rule

- **One render.** After the render, only verify.
- **At most one re-render**, and only when a step-7 check fails, or when a frame file is newer than the MP4.
- After that, hand off with a list of the remaining problems. Do not polish further.
- **Time box: 60 minutes** from the hand-off to HyperFrames to the finished render. When the build passes 60 minutes, stop, report the state, and ask the user.

A typical 80-second video took 29 minutes from start to render on this Mac (measured 2026-10-03): about 1 minute of voice, 4–17 minutes for each frame worker running in parallel, and 50 seconds of render.

## Length

Scale the length to the content. Most videos are 1 to 4 minutes.

| Content | Length | HyperFrames workflow |
|---|---|---|
| One idea, one mechanism | 45 s – 2 min | `faceless-explainer` |
| A mechanism with 2–4 parts, or a before/after | 2 – 3 min | `faceless-explainer` |
| More than 3 minutes of real teaching | 3 – 6 min | `general-video` |
| More than 6 minutes | Split into parts of 2–4 min each. Ask the user before you make more than one part. | — |

Kokoro speaks 169–184 words per minute at speed 1.0 (measured 2026-10-03 with `am_michael` and `af_heart`). Plan with 165 words per minute. Write each acronym as the voice must say it ("N V M"), and count it as one word, because the voice says the letters fast.

## Steps

1. **Find the one question.** Write the question that the video answers, and the answer, in one sentence each. Completion: both sentences exist, and a viewer could repeat the answer after one viewing.
2. **Ground it, without secrets.** Read the real source: code, diff, logs, docs. For external facts, search with Firecrawl (`firecrawl search "..." --scrape`) or Exa (`mcp__exa__web_search_exa`). If Firecrawl fails (example: HTTP 402), use Exa, then Tavily (`tvly search`). List each claim with its source. Use quotation marks only for exact words from a source. A paraphrase gets no quotation marks, on screen or in the plan. HyperFrames copies the input into project files that every worker reads. Thus, copy only the lines that you need, and replace each API key, token, or password with `<redacted>`. Completion: each claim has a source or the label "assumed", and the plan contains no secret values.
3. **Write the teaching plan** in `TEACHING-PLAN.md` in the output folder. Use the 3b1b rules below. Include: the question, the answer, the length with its reason, the claims with sources, and a scene table (scene, what the viewer sees, what moves and why, the narration). Completion: each scene teaches one idea, and the scene order builds from concrete to general.
4. **Write the narration in STE.** Load the `ste` skill (Claude Code: the Skill tool. Codex: read `~/.claude/skills/ste/SKILL.md`). Use 80% strictness. Spoken STE: short sentences, one idea in each sentence, active voice, no contractions, the same name for each thing in all scenes. Spell out symbols that a voice reads badly ("~" → "about", "→" → "to"). Save the narration as `narration.txt`, one paragraph for each scene. Run `ste_check.py narration.txt --type description`. Completion: zero ERROR lines, and spoken words ÷ 165 is inside the planned length.
5. **Confirm once.** Show the user the question, the answer, the length, and the scene list in 10 lines or fewer. Ask: "Build and render this?" Skip this step if the user said "just build it", if the run is non-interactive (example: a scheduled job), or if the user already approved the plan. Completion: the user approved, or the step was skipped for one of these reasons.
6. **Build with HyperFrames.** Follow the build handoff below. Completion: `renders/video.mp4` exists, and its narration is the text of `narration.txt`.
7. **Verify the MP4.** Do all of these checks on the rendered file, not on the composition:
   - `ffprobe` shows a video stream and an audio stream. The duration is inside the planned range.
   - `ffmpeg -i OUT.mp4 -af volumedetect -f null - 2>&1 | grep mean_volume` shows a value above −35 dB. A lower value means silent or almost silent narration.
   - `npx hyperframes transcribe OUT.mp4 -d <scratch folder>` writes `transcript.json` in that folder. Read the words from it and compare them with `narration.txt`. Each scene's key words are in the transcript. A product name that the speech recognizer misspells ("Cloud Code" for "Claude Code") is UNVERIFIED by ear, not a failure.
   - `~/.claude/skills/explain-video/scripts/contact_sheet.sh OUT.mp4 <folder>/contact-sheet.png` makes a contact sheet of 9 evenly spaced frames. You can also give it the scene midpoints as arguments. Look at each frame. Text is legible, nothing is clipped, and each frame shows the idea that its narration describes. A number in the middle of a count-up animation is correct if a later frame of the same scene shows the final value.
   - No file in `compositions/` is newer than the MP4.

   Completion: all checks pass, or one re-render (stop rule) fixed them, or the hand-off names each failed check.
8. **Hand off.** Give the MP4 path, the real duration, the contact sheet path, and the one-sentence answer. Name what is UNVERIFIED and the remaining problems. To send the file to the user on another device in Claude Code, use SendUserFile.

## 3b1b rules

- **Open with the question**, in the viewer's terms, in the first 10 seconds. Show the puzzle, not a title card.
- **Give the answer twice.** HyperFrames requires the message by the second scene. Thus, give a one-line preview of the answer in scene 2, and the full answer at the end, over the complete picture.
- **Concrete before general.** Show one real case with real numbers or real names. Then show the rule.
- **One idea in each scene.** If a scene needs "and also", split the scene.
- **The picture carries the idea.** The narration points at it: "Watch the queue on the left."
- **Build it piece by piece.** Add one element at a time. Keep the earlier elements on screen, so the viewer sees the whole system grow.
- **One stage.** An element that appears in more than one scene (a bar, a box, a timeline) keeps the same position, size, and name in all scenes. Write its position and size (in pixels on the 1920x1080 canvas) into the scene table. The preset's `frame.md` owns the colors, so do not choose colors in the plan.
- **Keep the caption band clear.** HyperFrames puts captions in the bottom 17% of the frame (below y 896 on 1080p). Put no content there.
- **Motion means change.** Move a thing only to show cause and effect, flow, or change in time. No decorative motion.
- **Let the key reveal land.** HyperFrames sets each scene to the length of its narration, so silence cannot be added. After a key reveal, write one short sentence that names what the viewer sees ("That is three quarters of the time."). The picture holds while the voice says it.

## Build handoff

Use `faceless-explainer` for videos up to 3 minutes. Use `general-video` for longer ones, with the same brief.

1. **Load the skills.** Load `/hyperframes`, then the workflow skill (`/faceless-explainer`). Read the workflow's steps. This skill already answers the intent interview, so skip the interview.
2. **Work in the output folder.** `cd` to the output folder before `init`, so that `videos/` is not created in the user's repo. Name the project from the topic in kebab-case, without a timestamp (a HyperFrames rule):
   ```bash
   cd <output folder> && npx hyperframes init "videos/<kebab-topic>" --non-interactive --example=blank --skill=faceless-explainer
   ```
3. **Write `BRIEF.md` yourself**, immediately after `init`, in the project root. Copy `narration.txt` to `user_script.txt` in the project root.
   ```markdown
   ---
   workflow: faceless-explainer
   flow: automation
   storyboard: no
   message: "<the one-sentence answer>"
   destination: youtube
   aspect: 1920x1080
   language: en
   audience: "<the user at their level, or the named audience>"
   length: <planned length, for example 75s>
   angle: concept
   narration: yes
   vo_mode: verbatim
   voice: <kokoro voice id>
   ---

   ## Intent

   <The question and the answer. One sentence on the audience.>

   ## Customizations

   - Narration: use user_script.txt word for word (VO_MODE verbatim). One paragraph = one frame.
   - Scene plan: follow ../../TEACHING-PLAN.md (scene table, positions of shared elements, 3b1b rules).

   ## Notes

   - Render approved by the user: at the preview-or-render question, the answer is "render". Render after lint and check pass.
   - Voice: Kokoro, offline, voice <id>. Pass `--voice <id>` to audio.mjs (the faceless-explainer default is am_michael).
   ```
   Use `storyboard: yes` only when the user asked to review sketches. Record only the values that the user confirmed (`prefs.mjs record`), not the defaults. This rule wins over the faceless-explainer gate that asks to record `style_preset`: when the user did not choose the preset, do not record it, and write "style_preset not recorded: not confirmed by the user" in the hand-off.
4. **Run the workflow steps** from its Step 0 gate onward, with these additions:
   - **Shared stage:** the frame packets do not include the brief's video direction. Write the "one stage" positions to `_stage.md` in the project root, and give that file to each frame worker in its dispatch.
   - **Real timings:** the scene windows in the teaching plan are estimates. After `audio.mjs sync-durations`, give each worker the real frame duration and the word times from `audio_meta.json`. A speech-recognizer word time can end after the frame end. Animate to the frame end, not to the last word.
   - **Fonts:** after the frames are built, make sure that the preset's font files are in `assets/fonts/`. If they are not there, copy them from the preset folder.
   - **Intentional overlap:** text drawn over other text on purpose (a lit state over a dim state) fails `check` with `content_overlap`. Put `data-layout-allow-overlap` on each text element. The attribute is not inherited.
5. **Before the render**, make sure that each frame worker has stopped. A worker that reports "finished" can still be running in the background. Wait until no worker is active, and then render.

## Voice

- Default: Kokoro, on this Mac, free. Voice `af_heart`. Other English voices: `am_michael`, `am_adam`, `af_nova`, `af_sky`, `bf_emma`, `bm_george`. Use the voice that the user chose before, if HyperFrames remembers one. Always pass `--voice <id>` explicitly.
- Kokoro needs `HYPERFRAMES_PYTHON`. Claude Code (`~/.claude/settings.json` → `env`) and Codex (`~/.codex/config.toml` → `[shell_environment_policy.set]`) set it for each session. If it is empty (`echo $HYPERFRAMES_PYTHON`), the session started before the config change. Then prefix each `npx hyperframes` command and each `node .../audio.mjs` command with `HYPERFRAMES_PYTHON=$HOME/.local/share/hyperframes-kokoro/.venv/bin/python`.
- ElevenLabs: use it only when the user asks for it and `ELEVENLABS_API_KEY` exists.

## Output path

Save outside the repo:

```
~/Explainers/<project>/YYYYMMDD-HHMM-<slug>/
  TEACHING-PLAN.md
  narration.txt
  videos/<kebab-topic>/     (the HyperFrames project; render in renders/video.mp4)
  <slug>.mp4                (copy of the final render)
  contact-sheet.png
```

`<project>` is the base name of `git rev-parse --show-toplevel`. If there is no git repo, use the base name of the current directory. If the current directory is the home directory, use `general`. If the user gives a different location, use that location.
