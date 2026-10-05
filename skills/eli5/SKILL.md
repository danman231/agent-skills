---
name: eli5
description: Explain any topic to a complete beginner as a visual, self-contained HTML artifact with big pictures, plain language, and very few words. Use this skill whenever the user invokes /eli5, says "ELI5", "explain like I'm five", "explain this visually", asks for a beginner-friendly visual explanation, or wants a complex system, codebase, process, or concept made understandable to someone with no prior knowledge.
---

# ELI5

Turn the requested topic into a short visual story for someone who knows nothing about it.

The result is a browser-openable HTML artifact, not a long chat explanation. Teach through pictures first, labels second, and prose last.

## Understand the Topic

Ground the explanation before drawing it:

1. Identify the one question the artifact must answer.
2. If the topic concerns the user's code, workflow, or files, inspect the real implementation and local project instructions first.
3. If accuracy depends on current external facts, verify them with the appropriate research tools.
4. Choose the smallest useful mental model. Omit exceptions and advanced detail unless leaving them out would make the core explanation false.

Do not confuse simple language with childish language. Be warm and direct without talking down to the reader.

## Build a Visual Story

Use three to six numbered sections. Each section should introduce one new idea and visually build on what came before.

Choose the visual form that matches the topic:

- process or automation: boxes connected by arrows
- system or architecture: a small component map
- sequence or history: a left-to-right timeline
- hierarchy: nested containers or a simple tree
- abstract idea: a concrete analogy beside the real concept
- comparison: two large side-by-side scenes
- quantity or scale: a simple bar, stack, or size comparison

Draw the explanation with semantic HTML, CSS, and inline SVG. Use large labeled shapes, arrows, icons, and restrained color. Do not merely describe a diagram that could have been shown.

## Keep the Words Sparse

Aim for:

- title: no more than 12 words
- opening summary: one or two short sentences
- section heading: one plain-language sentence
- diagram labels: one to six words each
- supporting note: one short sentence when needed

Avoid dense paragraphs, walls of bullets, large tables, unexplained acronyms, code dumps, and decorative filler. If a real technical term matters, introduce the plain-language idea first and put the term in parentheses.

Finish with one prominent `Remember this` sentence containing the durable takeaway.

## Artifact Requirements

Create one self-contained `.html` file with:

- inline CSS and inline SVG
- no external CDN, font, image, script, or network dependency
- a clean light background, strong dark text, and one restrained accent color unless the topic provides a meaningful palette
- large typography and generous whitespace
- responsive behavior for desktop and mobile
- accessible contrast, semantic headings, and useful labels for diagrams
- no framework, build step, or development server

Use subtle motion only when it materially clarifies a sequence. Respect `prefers-reduced-motion`. The explanation must remain complete when animation is disabled.

Save the file in the current workspace under:

`artifacts/eli5/YYYYMMDD-HHMM-<short-topic-slug>.html`

If the repository already defines a more appropriate artifacts directory, follow that convention. Do not publish or upload the artifact unless the user explicitly asks.

## Quality Check

Before handing it off, open or render the artifact when the environment supports it and verify:

- the first viewport states what is being explained
- the main relationship is understandable from the pictures alone
- the steps read in an obvious order
- labels do not overlap or clip at desktop and mobile widths
- the artifact contains no unsupported claims or invented project details
- a beginner can repeat the `Remember this` takeaway after one pass

Return a concise message linking the HTML file and stating what it explains. Do not duplicate the artifact as a long Markdown explanation.

## Example Requests

- `/eli5 how does this Discord bot work?`
- `ELI5 what happens when I type a URL into a browser`
- `Explain our nightly publishing automation visually for someone new to the business`
- `Make a beginner-friendly visual explaining embeddings versus a normal database`

