# The prompts from "GPT-6.2 Astra vs Claude Fable 5.2: Who Wins?"

These are the three prompts from the Strongin AI YouTube video "GPT-6.2 Astra vs Claude Fable 5.2: Who Wins?". I gave the same prompts, word for word, to Claude Fable 5.2 and to GPT-6.2 Astra. The repo's MIT license covers only our own text.

How to use this file: paste one prompt into a coding agent (I used Codex for Astra), set it to high effort, and let it run to the end. Then run the same prompt on the other model and compare the result, the time and the cost.

## 1. The racing game

```text
Create a realistic racing game that I can play in my browser. Make the game as good as a video game release from a top video game company. Create only one level.
```

## 2. The manual car drivetrain

```text
Explain how a manual car sends power from the engine to the wheels by building an interactive 3D model of the whole drivetrain that runs in my browser.

It must include:
- A 4-cylinder engine with pistons, crankshaft, camshaft and valves, firing in the real order (1-3-4-2), with each valve opening at the right point in the cycle.
- A clutch I press with a pedal, and a 5-speed gearbox plus reverse, with synchros (they can be simplified), shifted with an H-pattern gear stick I can drag.
- A driveshaft and a differential, so when I steer into a corner the outer wheel visibly turns faster than the inner one.
- Real gear ratios and a final drive, with a tachometer and a speedometer. With the clutch fully engaged, road speed must match RPM, gear ratio, final drive and tyre size in every gear. With the clutch pressed or slipping, the engine and the wheels can turn at different speeds.
- Controls for throttle, clutch, gear stick, steering and slow motion, and a cutaway view so I can see inside the engine and the gearbox. Labels on every part, which I can turn off.
```

## 3. The film: "Seventy Years of AI Compute"

```text
Make a 2-minute documentary film, built entirely in code, called "Seventy Years of AI Compute": how the computing power used to train AI grew from the 1950s to today, and what that growth made possible.

Content:
- Research it first. Use real data, for example Epoch AI's training-compute dataset and the original papers. Save every fact and number with its source in facts.md. Every number and claim in the film must trace to that file; if you can't source it, leave it out.
- The centrepiece is a real chart of training compute over time on a log scale, with correct axes and units, that builds on screen as the story moves. Mark 6 to 8 landmark models at their real year and compute.

Sound:
- A narrator voice made with a free text-to-speech tool that runs on this Mac, with no API keys. Try installing a good open-source voice once; if that fails, use a built-in macOS voice. Write the script first, generate the voice, measure the real start and end time of every sentence, and cut the picture to those times. The narrator is never silent for more than 2 seconds.
- An original music score you compose and synthesize in code, under the voice and lowered while the narrator speaks.
```
