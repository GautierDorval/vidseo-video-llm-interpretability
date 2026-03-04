# Governance

Reference version: `1.0.0`  
Generated: `2026-03-04`

The purpose of governance is to keep VidSEO's meaning stable across human-readable pages, machine-readable files, and future releases.

## Content classes

- **Normative**: defines meaning, scope, exclusions, or required rules.
- **Informative**: explains or contextualizes without redefining meaning.
- **Contextual**: references external material without changing product meaning.

## Stable identifiers

The following identifiers must remain stable after publication:

- `VIDSEO-DOC-*`
- `VIDSEO-TERM-*`
- `VIDSEO-T-*`
- canonical slugs that may already be externally linked

## Change classes

### Patch
Typos, formatting, translation cleanup, metadata repair, layout improvements.

### Minor
New informative pages, added translations, new term pages, expanded machine surfaces without changing product scope.

### Major
Any change to:

- the definition of VidSEO,
- the interpretability boundary,
- non-goals,
- authority hierarchy,
- canonical URL strategy.

## Required updates for meaning changes

When normative meaning changes, update the relevant surfaces and run the consistency check:

- `VERSION`
- `CHANGELOG.md`
- `meta.json`
- `ai-manifest.json`
- `links.json`
- `data/documents.json`
- `data/terms.json`
- `data/capabilities.json`
- `llms.txt`
- `sitemap.xml`

## Review criteria

A contribution should not be merged if it:

- introduces ranking or citation guarantees,
- introduces hidden AI capability claims,
- changes authority hierarchy without explanation,
- leaves broken machine surfaces,
- creates English/French mismatch on canonical pages.

## Maintainer authority

Final authority for normative product meaning remains with the maintainer of the canonical surfaces.
