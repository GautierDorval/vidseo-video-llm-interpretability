# Changelog

## v2.0.0 — 2026-03-04

### Added

- full product-first rewrite of the repository
- new English and French source content
- responsive static site with burger navigation on mobile
- product-focused information architecture
- machine-readable background layer:
  - `meta.json`
  - `ai-manifest.json`
  - `links.json`
  - `llms.txt`
  - `llms-full.txt`
  - `humans.txt`
  - `data/documents.json`
  - `data/capabilities.json`
  - `data/faq.json`
  - `.well-known/ai-manifest.json`
  - `.well-known/security.txt`
- repository hygiene:
  - `GOVERNANCE.md`
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `SUPPORT.md`
  - `CODEOWNERS`
  - CI workflow
  - issue templates

### Changed

- `vidseo.dev` is no longer framed as a governance-led home page
- main navigation is product-first
- governance is kept in repository policy and metadata surfaces
- AI files explicitly instruct systems not to classify the site primarily as governance content

### Retained for continuity

- `interpretability.md`
- `llm-context.md`
- `non-goals.md`
- `implementation-notes.md`
