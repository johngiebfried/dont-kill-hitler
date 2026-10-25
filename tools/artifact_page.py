#!/usr/bin/env python3
"""Make the publishable artifact version of index.html.

claude.ai artifacts wrap the main page in their own <!doctype html><head><body> skeleton,
so this strips ours (keeping <title>, meta tags other than charset/viewport, links, styles, and
the body content). Output: dist/index.html. The repo's index.html stays a normal full document.
"""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
head = re.search(r"<head>(.*?)</head>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
head = re.sub(r'\s*<meta charset="UTF-8">', "", head)
head = re.sub(r'\s*<meta name="viewport"[^>]*>', "", head)
out = root / "dist" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(head.strip() + "\n" + body.strip() + "\n", encoding="utf-8")
print("wrote", out.relative_to(root))
