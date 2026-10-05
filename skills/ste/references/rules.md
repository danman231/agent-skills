# ASD-STE100 writing rules (Issue 9, January 2025)

Rule statements are condensed from the official specification (asd-ste100.org, Issue 9). The `80%` column says how the default level treats each rule. `full` applies every rule as written.

## Section 1 — Words

| Rule | Statement | 80% |
|---|---|---|
| 1.1 | Use approved dictionary words, technical nouns, and technical verbs. | Use the plainest common word. Replace inflated words (utilize → use). |
| 1.2 | Use approved words only as their approved part of speech. | Relaxed. |
| 1.3 | Use approved words only with their approved meanings. | Keep: one meaning per word in one text. |
| 1.4 | Use only approved forms of verbs and adjectives. | Relaxed. |
| 1.5–1.6 | Technical nouns are allowed when they fit a technical noun category (names of parts, tools, systems, files, commands). | Keep. Domain names (deploy.sh, launchd, Trello card) stay. |
| 1.7 | Do not use technical nouns as verbs ("grease the bolt"). | Keep, except for verbs the field already uses ("commit", "deploy"). |
| 1.8–1.10 | Use the field's approved technical nouns. Choose short, clear ones. No slang or jargon as technical nouns. | Keep. |
| 1.11 | Do not use different technical nouns for the same item. | Keep, strictly. Pick one name per thing and use only that name. |
| 1.12–1.13 | Technical verbs are allowed (in a technical verb category). Do not use technical verbs as nouns. | Keep. |
| 1.14 | Use American English spelling. | Keep. |

## Section 2 — Noun clusters

| Rule | Statement | 80% |
|---|---|---|
| 2.1 | Write noun clusters of no more than three words. | Keep. |
| 2.2 | When a technical noun has more than three words, write it in full once, then use a hyphen, a shorter name, or a rewrite. | Keep. |

## Section 3 — Verbs

| Rule | Statement | 80% |
|---|---|---|
| 3.1–3.2 | Use only: infinitive, imperative, simple present, simple past, simple future, past participle as an adjective. | Prefer these. Present perfect ("has stopped") is allowed when it carries real meaning. |
| 3.3 | Use the past participle only as an adjective ("the damaged part"). | Relaxed. |
| 3.4 | Do not use auxiliary verbs to make complex verb constructions ("will have been installed"). | Keep. |
| 3.5 | Use the "-ing" form only in a technical noun or as a modifier in one. | Keep for nouns: "the installation of" → "install". |
| 3.6 | Use the active voice. In descriptions, use the passive only when the agent is unknown. | Keep. |
| 3.7 | Use a verb to show an action, not a noun ("do an inspection of" → "inspect"). | Keep, strictly. |

## Section 4 — Sentences

| Rule | Statement | 80% |
|---|---|---|
| 4.1 | Write short and clear sentences. | Keep. |
| 4.2 | Do not omit words or use contractions to make sentences shorter. | Keep. No telegraphic style, no contractions. |
| 4.3 | Use a vertical list for complex text. | Keep. |
| 4.4 | Use connecting words and phrases (then, but, as a result) to connect related sentences. | Keep. |
| 4.5 | Use an article (the, a, an) or a demonstrative (this, these) before a noun when applicable. | Keep. |

## Section 5 — Procedures (instructions)

| Rule | Statement | 80% |
|---|---|---|
| 5.1 | Maximum 20 words in each sentence. | Keep. |
| 5.2 | One instruction in each sentence, unless the actions occur at the same time. | Keep. |
| 5.3 | Write instructions in the imperative (command) form. | Keep. |
| 5.4 | When the reader must know a condition first, start with it, then a comma, then the command. | Keep. |
| 5.5 | Notes give information, not instructions. | Keep. |

## Section 6 — Descriptive writing

| Rule | Statement | 80% |
|---|---|---|
| 6.1 | Give information gradually. | Keep. |
| 6.2 | Use key words and key phrases to give the text a logical structure. | Keep. |
| 6.3 | Maximum 25 words in each sentence. | Keep. |
| 6.4–6.5 | Use paragraphs to show related information. One topic in each paragraph. | Keep. |
| 6.6 | No more than six sentences in each paragraph. | Keep. |

## Section 7 — Safety instructions

| Rule | Statement | 80% |
|---|---|---|
| 7.1 | Use a word that shows the risk level (WARNING, CAUTION). | Keep for destructive or irreversible actions. |
| 7.2 | Start a safety instruction with a clear command or condition. | Keep. |
| 7.3 | Give the risk or the possible result. | Keep. |

## Section 8 — Punctuation and word counts

| Rule | Statement | 80% |
|---|---|---|
| 8.1 | Standard punctuation is allowed, but not the semicolon. | Keep. |
| 8.2 | Use hyphens to connect words that are directly related. | Keep. |
| 8.3 | Parentheses are allowed for references, identifiers, step numbers, abbreviations, singular/plural, short explanations, and alternatives. | Keep. |
| 8.4 | In a vertical list, a colon counts as the end of a sentence. | Keep. |
| 8.5 | Text in parentheses counts as one word. | Keep. |
| 8.6 | Each counts as one word: a number, a number with its unit, an abbreviation, an alphanumeric identifier, quoted text, a title or label, a proper noun. | Keep. File paths and code count as one word. |
| 8.7 | A hyphenated word counts as one word. | Keep. |

## Section 9 — Word choice

| Rule | Statement | 80% |
|---|---|---|
| 9.1 | When a word swap is not sufficient, use a different sentence construction. | Keep. |
| 9.2 | Use each approved word correctly. | Keep. |
| 9.3 | Do not make phrasal verbs ("set up", "find out", "turn off"). | Prefer one verb (install, learn, stop). Common phrasal verbs are allowed when no clear single verb exists. |
| 9.4 | Use a consistent style for terminology and wording. | Keep. |

## Modal verbs and uncertainty

The STE dictionary approves CAN, MUST and WILL. It does not approve "should", "could" or "might" (use MUST, or CAN for possibility).

- `full`: obey the dictionary.
- `80%`: keep "probably", "may" and "might" when the uncertainty is real. Uncertainty is a fact about the evidence. Do not delete it to obey a style rule.
