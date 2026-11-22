# The prompts from "Claude Opus 5.5 vs GPT-6.2 Sol: Same 3 Jobs, Side by Side"

These are the three prompts from the Strongin AI YouTube video, the same prompt word for word for both GPT-6.2 Sol (in Codex) and Claude Opus 5.5 (in Claude Code), one run each. The repo's MIT license covers only our own text.

How to use this file: copy a prompt into Codex, Claude Code or another coding agent, in an empty folder, and fill in anything in [brackets]. Each prompt asks the model to test its own work and to have a second agent try to break it, so read its final report against what it actually built.

## 1. A 3D drum machine you can play

```text
Build an interactive 3D drum machine and synth that runs in my browser, so I can make a beat and watch it play.

It must include:
- A 16-step sequencer with at least kick, snare, closed hat, open hat and clap, and a simple bass synth whose 16 steps each take a note.
- Every sound made in code with the Web Audio API. No samples, no outside files, no network.
- A 3D scene in which each sound has its own object that moves on its hit (the kick pushes a speaker cone, the hats shake something small), plus a playhead you can see moving across the steps.
- Tempo from 70 to 160 BPM, swing, a volume per track, and a mute per track.
- Three preset beats in different styles, and a way to clear and draw my own.

Rules:
- Timing must be tight. Schedule the audio ahead on the audio clock, not with setTimeout, so the beat doesn't drift. Each visual hit must land within one frame of its sound.
- One self-contained HTML file with everything inline, running at 60 fps on a laptop. Test it opened from disk.
- Before you call it done, check it yourself: expose the state on window, run each preset in a headless browser, take screenshots and look at them, and log the scheduled time of every hit for one bar to prove the timing.
- When you think it's done, start one subagent that didn't build it. It must try to break it, test every requirement itself, and not trust your summary.
- Check elapsed time only with `date`. Never estimate it. Stop at 1 hour by the clock.
- Build everything yourself in this folder. Don't use any existing skills or files from my other projects.
```

## 2. A six-legged robot walking over rough ground

```text
Build a six-legged robot that walks across rough 3D terrain in my browser, animated entirely by code, with feet that stay planted on the ground.

It must include:
- A six-legged robot, each leg with at least three joints, built from simple shapes. No model files, no outside assets, no network.
- Procedural walking: every leg's joints are solved with inverse kinematics every frame, using a tripod gait (three legs on the ground at a time). No pre-made animation.
- Planted feet: a foot on the ground must not slide or sink into the terrain. When a foot is about to drift out of reach, the leg lifts, swings and lands on a new spot on the surface.
- Rough terrain with hills, a slope steep enough to make the robot tilt, and a few rocks or steps to climb over. The body leans and keeps its height above the ground as the terrain changes.
- Controls: arrow keys or WASD to walk and turn, a speed slider, a button to show the leg targets and joints, and a slow-motion toggle. A camera that follows the robot, which I can orbit with the mouse.

Rules:
- One self-contained HTML file with everything inline, running at 60 fps on a laptop. Test it opened from disk.
- Before you call it done, check it yourself: expose the state on window, drive the robot over flat ground, up the slope and over a step in a headless browser, measure how far each planted foot moves while it's down (it should stay within 1% of a leg's length), take screenshots and look at them, and fix what's wrong.
- When you think it's done, start one subagent that didn't build it. It must try to break it, test every requirement itself, and not trust your summary.
- Check elapsed time only with `date`. Never estimate it. Stop at 1 hour by the clock.
- Build everything yourself in this folder. Don't use any existing skills or files from my other projects.
```

## 3. A website for my free resources

This one was built from a copy of my public agent-skills repo. To use it for your own project, put a copy of your repo in the folder first and change the first two paragraphs to describe your project and who it's for.

```text
Build a website for Strongin AI's free resources: my public collection of agent skills and the prompts from my videos. A copy of the repo is in [the folder with a copy of your repo].

Who it's for: people who watch my YouTube channel, Strongin AI, about using AI tools like Claude Code and Codex, and who want the skills and prompts I show in my videos.

It must:
- Say at the top, in one line, what this is and why someone would use it. A visitor should be able to install a skill or copy a prompt in under a minute.
- List every skill and every prompt in the repo. Give each a one-line summary written from its actual file, and give each skill its install command with a copy button.
- Have a page for each skill and each prompt, showing its full text in a readable way.
- Look distinctive, not like a generic AI template. The design is your choice.
- Work well on a phone and on a desktop, load fast, and pass basic accessibility checks: contrast, keyboard use, alt text.
- Use only real content from the repo. Don't invent features, numbers, quotes, testimonials or links.

Rules:
- Static HTML, CSS and JavaScript in this folder, with no build step needed to view it. index.html must work opened from disk.
- Never edit or delete anything in [the folder with a copy of your repo].
- Check it yourself before you call it done: take screenshots at 390 px and 1440 px wide in a headless browser, look at them, and fix what's wrong. Click every copy button and every link.
- When you think it's done, start one subagent that didn't build it. It visits as a first-time viewer, tries to break it, checks every item above itself, and doesn't trust your summary. Fix what it finds.
- Check elapsed time only with `date`. Never estimate it. Stop at 1 hour by the clock.
- Build everything yourself in this folder. Don't use any existing skills or files from my other projects.
```
