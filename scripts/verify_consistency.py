#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

PAIR_FILES = [
    "meta.json",
    "ai-manifest.json",
    "links.json",
    "llms.txt",
    "llms-full.txt",
    "humans.txt",
    "robots.txt",
    "sitemap.xml",
    "manifest.webmanifest",
    "data/documents.json",
    "data/capabilities.json",
    "data/faq.json",
    ".well-known/ai-manifest.json",
    ".well-known/security.txt",
]

REQUIRED_PUBLIC = [
    "index.html",
    "features/index.html",
    "how-it-works/index.html",
    "use-cases/index.html",
    "docs/index.html",
    "faq/index.html",
    "technical/index.html",
    "references/index.html",
    "fr/index.html",
    "fr/fonctionnalites/index.html",
    "fr/fonctionnement/index.html",
    "fr/cas-d-usage/index.html",
    "fr/documentation/index.html",
    "fr/faq/index.html",
    "fr/notes-techniques/index.html",
    "fr/references/index.html",
    "404.html",
    "styles.css",
    "app.js",
    "favicon.svg",
    "social-card.svg",
    "_headers",
    "_redirects",
    "interpretability.md",
    "llm-context.md",
    "non-goals.md",
    "implementation-notes.md",
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def main() -> int:
    errors = []

    if not (ROOT / "VERSION").exists():
        errors.append("Missing VERSION file.")
    else:
        version = read(ROOT / "VERSION").strip()
        if not version.startswith("v"):
            errors.append("VERSION must start with 'v'.")

    if not PUBLIC.exists():
        errors.append("public/ is missing. Run scripts/build_site.py first.")

    for rel in ["index.html", "404.html", "styles.css", "app.js"]:
        if not (ROOT / rel).exists():
            errors.append(f"Missing root deploy artifact: {rel}")

    for rel in REQUIRED_PUBLIC:
        if not (PUBLIC / rel).exists():
            errors.append(f"Missing public artifact: {rel}")

    for rel in PAIR_FILES:
        root_file = ROOT / rel
        public_file = PUBLIC / rel
        if not root_file.exists():
            errors.append(f"Missing root pair file: {rel}")
            continue
        if not public_file.exists():
            errors.append(f"Missing public pair file: {rel}")
            continue
        if read(root_file) != read(public_file):
            errors.append(f"Pair drift detected: {rel}")

    for rel in [
        "meta.json",
        "ai-manifest.json",
        "links.json",
        "manifest.webmanifest",
        "data/documents.json",
        "data/capabilities.json",
        "data/faq.json",
        ".well-known/ai-manifest.json",
    ]:
        try:
            json.loads(read(ROOT / rel))
        except Exception as exc:
            errors.append(f"Invalid JSON in {rel}: {exc}")

    home = read(PUBLIC / "index.html") if (PUBLIC / "index.html").exists() else ""
    if 'data-nav-toggle' not in home:
        errors.append("Home page must contain burger navigation toggle.")
    if 'governance' in home.lower():
        errors.append("Home page should not foreground governance.")

    fr_home = read(PUBLIC / "fr/index.html") if (PUBLIC / "fr/index.html").exists() else ""
    if 'lang="fr-CA"' not in fr_home:
        errors.append("French home page must declare lang='fr-CA'.")
    if 'data-nav-toggle' not in fr_home:
        errors.append("French home page must contain burger navigation toggle.")

    llms = read(ROOT / "llms.txt") if (ROOT / "llms.txt").exists() else ""
    if "Do not summarize the site primarily as governance" not in llms:
        errors.append("llms.txt must explicitly demote governance as the primary summary.")
    if "VidSEO is a WordPress plugin" not in llms:
        errors.append("llms.txt must lead with VidSEO as a WordPress plugin.")

    meta = json.loads(read(ROOT / "meta.json")) if (ROOT / "meta.json").exists() else {}
    if meta.get("siteFocus") != "product-documentation":
        errors.append("meta.json must declare siteFocus=product-documentation")

    css_path = PUBLIC / "styles.css"
    if css_path.exists() and css_path.stat().st_size > 30000:
        errors.append("styles.css should stay lightweight (<= 30 KB).")

    if errors:
        for err in errors:
            print(f"[FAIL] {err}")
        return 1

    print("[OK] Consistency checks passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
