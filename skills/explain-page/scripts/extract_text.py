#!/usr/bin/env python3
"""Extract reader-facing text from an explainer page for ste_check.py.

Usage: extract_text.py RENDERED_DOM.html [SOURCE.html]

From the rendered DOM: visible text, one block per paragraph (blank line between blocks),
headings as '#' lines (ste_check.py skips them), list items as '- ' lines, SVG <text> labels.
From SOURCE.html: the string values of a `const COPY = {...}` object, if one exists. That is
where the build rules put the text for states that the first render does not show.
"""
import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "section", "article", "header", "footer", "main", "aside", "figure",
         "figcaption", "blockquote", "td", "th", "dd", "dt", "label", "button", "summary",
         "details", "caption", "nav", "tr", "table", "ul", "ol", "br", "text"}
HEAD = {"h1", "h2", "h3", "h4", "h5", "h6", "title"}
SKIP = {"script", "style", "noscript", "code", "pre", "template"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.buf, self.skip, self.mode = [], [], 0, None

    def flush(self):
        t = re.sub(r"\s+", " ", "".join(self.buf)).strip()
        if t:
            prefix = {"h": "# ", "li": "- "}.get(self.mode, "")
            self.out.append(prefix + t)
        self.buf, self.mode = [], None

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
            if tag == "code":
                self.buf.append(" CODE ")
            return
        if tag in BLOCK or tag in HEAD or tag == "li":
            self.flush()
            self.mode = "h" if tag in HEAD else "li" if tag == "li" else None

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if tag in BLOCK or tag in HEAD or tag == "li":
            self.flush()

    def handle_data(self, data):
        if not self.skip:
            self.buf.append(data)


def copy_strings(src):
    m = re.search(r"\bCOPY\s*=\s*\{", src)
    if not m:
        return []
    depth, i = 0, m.end() - 1
    while i < len(src):
        depth += {"{": 1, "}": -1}.get(src[i], 0)
        if depth == 0:
            break
        i += 1
    body = src[m.end():i]
    strings = re.findall(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\'\\]|\\.)*)\'|`((?:[^`\\]|\\.)*)`', body)
    return [re.sub(r"<[^>]+>", "", next(s for s in g if s)) for g in strings
            if any(g) and len(next(s for s in g if s).split()) >= 3]


def main():
    p = Text()
    p.feed(open(sys.argv[1], encoding="utf-8", errors="replace").read())
    p.flush()
    blocks = p.out
    if len(sys.argv) > 2:
        extra = copy_strings(open(sys.argv[2], encoding="utf-8").read())
        if extra:
            blocks += ["# COPY object (text for other states)"] + extra
    print("\n\n".join(blocks))


if __name__ == "__main__":
    main()
