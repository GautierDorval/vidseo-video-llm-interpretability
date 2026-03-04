#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
GENERATED = "2026-03-04"

required_json_versions = [
    "meta.json",
    "ai-manifest.json",
    "links.json",
    "data/documents.json",
    "data/terms.json",
    "data/capabilities.json",
    "data/references.json",
    ".well-known/ai-manifest.json",
]

errors: list[str] = []

def load_json(rel: str):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Failed to load {rel}: {exc}")
        return {}

for rel in required_json_versions:
    data = load_json(rel)
    if not data:
        continue
    version = data.get("version") or data.get("reference_version") or data.get("schemaVersion")
    if version != VERSION:
        errors.append(f"Version mismatch in {rel}: {version!r} != {VERSION!r}")

meta = load_json("meta.json")
if meta.get("generated") != GENERATED:
    errors.append("meta.json generated date mismatch")

manifest = load_json("ai-manifest.json")
wk_manifest = load_json(".well-known/ai-manifest.json")
if manifest != wk_manifest:
    errors.append("ai-manifest.json and .well-known/ai-manifest.json differ")

documents = load_json("data/documents.json").get("documents", [])
terms = load_json("data/terms.json").get("terms", [])

for doc in documents:
    variants = doc.get("variants", {})
    for lang, variant in variants.items():
        url = variant.get("url")
        if not url:
            continue
        if url == "/":
            path = ROOT / "index.html"
        else:
            path = ROOT / url.lstrip("/") / "index.html"
        if not path.exists():
            errors.append(f"Missing HTML page for document {doc.get('id')} variant {lang}: {path.relative_to(ROOT)}")
    md_source = doc.get("markdownSource")
    if md_source and md_source.endswith(".md"):
        if not (ROOT / md_source.lstrip("/")).exists():
            errors.append(f"Missing markdown source for document {doc.get('id')}: {md_source}")

for term in terms:
    variants = term.get("variants", {})
    for lang, variant in variants.items():
        url = variant.get("url")
        path = ROOT / url.lstrip("/") / "index.html"
        if not path.exists():
            errors.append(f"Missing HTML page for term {term.get('id')} variant {lang}: {path.relative_to(ROOT)}")

sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
required_urls = ["/", "/en/", "/fr/", "/en/principles/", "/fr/principes/"]
for required in required_urls:
    canonical = "https://vidseo.dev/" + required.lstrip("/")
    if canonical not in sitemap:
        errors.append(f"Sitemap missing URL {canonical}")

llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
for token in [VERSION, "/data/documents.json", "/data/terms.json", "/llms-full.txt"]:
    if token not in llms:
        errors.append(f"llms.txt missing {token}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if VERSION not in readme:
    errors.append("README.md missing version")
if "VidSEO is a WordPress plugin" not in readme:
    errors.append("README.md missing expected product description")

citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
if f'version: "{VERSION}"' not in citation:
    errors.append("CITATION.cff missing or mismatching version")

security = (ROOT / ".well-known/security.txt").read_text(encoding="utf-8")
for token in ["Contact:", "Policy:", "Expires:"]:
    if token not in security:
        errors.append(f".well-known/security.txt missing {token}")

for rel in ["styles.css", "favicon.svg", "robots.txt", "humans.txt", "links.json", "meta.json"]:
    if not (ROOT / rel).exists():
        errors.append(f"Missing required file {rel}")

html_files = list(ROOT.rglob("*.html"))
link_pattern = re.compile(r'(?:href|src)=["\']([^"\']+)["\']')

for html_file in html_files:
    text = html_file.read_text(encoding="utf-8")
    for target in link_pattern.findall(text):
        if (
            target.startswith("http://")
            or target.startswith("https://")
            or target.startswith("#")
            or target.startswith("mailto:")
            or target.startswith("javascript:")
        ):
            continue
        resolved = (html_file.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"Broken local link in {html_file.relative_to(ROOT)} -> {target}")

if errors:
    print("Consistency check failed:")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("Consistency check passed.")
