#!/usr/bin/env python3
"""Check text against the mechanical ASD-STE100 rules.

Usage: ste_check.py FILE|- [--level 80|full] [--type auto|procedure|description]

ERROR  = a hard rule failure (sentence length, semicolon, contraction, paragraph length).
REVIEW = a pattern that is often non-STE but can be correct (passive, -ing, word choice).
Exit code 1 when there is at least one ERROR.

Markdown aware: skips code fences and tables, treats each list item as a sentence,
counts inline code, links, file paths, numbers with units, and parentheses as one word.
"""
import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DICT_FILE = HERE.parent / "references" / "dictionary-substitutions.md"

INFLATED = {
    "utilize": "use", "utilise": "use", "leverage": "use", "facilitate": "help",
    "ensure": "make sure", "commence": "start", "terminate": "stop", "obtain": "get",
    "perform": "do", "assist": "help", "approximately": "about", "additionally": "also",
    "subsequently": "then", "prior": "before", "sufficient": "enough", "numerous": "many",
    "endeavor": "try", "initiate": "start", "demonstrate": "show", "indicate": "show",
    "in order to": "to", "due to the fact that": "because", "at this point in time": "now",
    "a number of": "some", "robust": "(say what it does)", "seamless": "(say what it does)",
    "delve": "examine", "streamline": "(say what changes)",
}
BE = r"(?:is|are|was|were|be|been|being)"
IRREGULAR_PP = (
    "built|done|given|made|run|sent|set|shown|taken|written|known|found|kept|left|"
    "put|read|seen|told|begun|broken|chosen|driven|frozen|hidden|stolen|thrown|worn"
)
PASSIVE = re.compile(rf"\b{BE}\s+(?:\w+ly\s+)?(?:\w+ed|{IRREGULAR_PP})\b", re.I)
CONTRACTION = re.compile(r"\b\w+(?:n't|'re|'ll|'ve|'d|'m)\b|\b(?:it|that|there|what|he|she|who)'s\b", re.I)
ING_NOUN = re.compile(r"\b(?:the|a|an|this|of|for|by)\s+(\w{3,}ing)\b", re.I)
ING_OK = {"string", "thing", "nothing", "something", "anything", "everything", "ring",
          "spring", "king", "ceiling", "morning", "evening", "building", "setting",
          "warning", "wiring", "bearing", "housing", "fitting", "coupling", "mounting",
          "spacing", "timing", "routing", "logging", "caching", "pricing", "meaning"}
INSTRUCTION_START = re.compile(
    r"^(?:\d+[.)]\s*)?(?:(?:if|when|before|after|until|to)\b[^,]*,\s*)?(?:then\s+|also\s+)?"
    r"(add|apply|ask|check|click|close|copy|delete|do|edit|give|install|keep|make|move|"
    r"open|put|read|remove|replace|restart|run|save|send|set|start|stop|tell|turn|use|"
    r"wait|write|examine|push|pull|commit|deploy|verify|test|look|find|go|let)\b",
    re.I,
)


def load_unapproved():
    words = {}
    if not DICT_FILE.exists():
        return words
    for line in DICT_FILE.read_text().splitlines():
        m = re.match(r"^\| ([a-z][a-z\- ]*) \((\w+)\) \| (.+?) \|$", line)
        if m:
            words.setdefault(m.group(1), f"{m.group(3)} [{m.group(2)}]")
    return words


def mask(text):
    """Replace items that count as one word (Rule 8.5, 8.6) with a single token."""
    text = re.sub(r"`[^`]*`", "CODE", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", lambda m: m.group(1), text)
    text = re.sub(r"\([^()]*\)", "PAREN", text)
    text = re.sub(r"\"[^\"]*\"|“[^”]*”", "QUOTE", text)
    text = re.sub(r"(?:~|\.{0,2})?/[\w./~\-]+|\b[\w\-]+\.(?:sh|py|md|js|ts|json|toml|html|plist|txt)\b", "PATH", text)
    text = re.sub(r"\b\d[\d.,:]*(?:\s?(?:%|ms|s|sec|min|h|GB|MB|KB|TB|px|x|k)\b)?", "NUM", text)
    text = re.sub(r"\*\*|__|\*|_", "", text)
    return text


def words(sentence):
    return [w for w in re.split(r"\s+", sentence.strip()) if re.search(r"\w", w)]


def split_sentences(par):
    par = re.sub(r"\s+", " ", par).strip()
    parts = re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"`*\[(])", par)
    return [p for p in parts if words(p)]


def blocks(text):
    """Yield (line_no, kind, text). kind = 'para' or 'item'."""
    in_fence = False
    buf, start = [], 0
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if s.startswith("```"):
            in_fence = not in_fence
            if buf:
                yield start, "para", " ".join(buf); buf = []
            continue
        if in_fence or s.startswith("|") or s.startswith("<") or s.startswith("#") or re.match(r"^-{3,}$", s):
            if buf:
                yield start, "para", " ".join(buf); buf = []
            continue
        if not s:
            if buf:
                yield start, "para", " ".join(buf); buf = []
            continue
        item = re.match(r"^(?:[-*+]|\d+[.)])\s+(.*)", s)
        if item:
            if buf:
                yield start, "para", " ".join(buf); buf = []
            yield i, "item", item.group(1).lstrip("> ")
            continue
        if not buf:
            start = i
        buf.append(s.lstrip("> "))
    if buf:
        yield start, "para", " ".join(buf)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--level", choices=["80", "full"], default="80")
    ap.add_argument("--type", choices=["auto", "procedure", "description"], default="auto")
    a = ap.parse_args()
    text = sys.stdin.read() if a.file == "-" else Path(a.file).read_text()
    unapproved = load_unapproved() if a.level == "full" else {}

    errors = reviews = sentences = 0
    longest = 0

    def flag(kind, line, msg, snippet):
        nonlocal errors, reviews
        if kind == "ERROR":
            errors += 1
        else:
            reviews += 1
        snippet = snippet if len(snippet) <= 110 else snippet[:107] + "..."
        print(f"{kind:6} line {line}: {msg}\n         > {snippet}")

    for line, kind, block in blocks(text):
        sents = split_sentences(block)
        if kind == "para" and len(sents) > 6:
            flag("ERROR", line, f"paragraph has {len(sents)} sentences (max 6, Rule 6.6)", block[:80])
        for s in sents:
            sentences += 1
            n = len(words(mask(s)))
            longest = max(longest, n)
            if a.type == "procedure":
                limit = 20
            elif a.type == "description":
                limit = 25
            else:
                limit = 20 if INSTRUCTION_START.match(s) else 25
            if n > limit:
                flag("ERROR", line, f"{n} words (max {limit}, Rule {'5.1' if limit == 20 else '6.3'})", s)
            if ";" in mask(s):
                flag("ERROR", line, "semicolon (Rule 8.1)", s)
            for m in CONTRACTION.finditer(s):
                flag("ERROR", line, f"contraction '{m.group(0)}' (Rule 4.2)", s)
            for m in PASSIVE.finditer(s):
                flag("REVIEW", line, f"possible passive '{m.group(0)}' (Rule 3.6)", s)
            for m in ING_NOUN.finditer(s):
                if m.group(1).lower() not in ING_OK:
                    flag("REVIEW", line, f"possible -ing noun '{m.group(1)}' (Rule 3.5)", s)
            low = s.lower()
            for w, alt in INFLATED.items():
                if re.search(rf"\b{re.escape(w)}\b", low):
                    flag("REVIEW", line, f"inflated '{w}' -> {alt}", s)
            if unapproved:
                for w in sorted(set(re.findall(r"[a-z][a-z\-]+", low))):
                    if w in unapproved and w not in INFLATED:
                        flag("REVIEW", line, f"'{w}' not approved -> {unapproved[w]}", s)

    print(f"\nSTE check ({a.level}): {sentences} sentences, longest {longest} words, "
          f"{errors} ERROR, {reviews} REVIEW")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
