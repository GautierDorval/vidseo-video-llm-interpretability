# Contributing

Thank you for helping keep the VidSEO reference surface precise.

## Before you open a pull request

Make sure your proposal does **not**:

- imply that VidSEO generates, analyzes, or validates video meaning,
- imply ranking, traffic, or citation guarantees,
- redefine canonical terminology without updating the term registry,
- change machine-discovery files silently,
- introduce unsupported implementation claims.

## Required update discipline

If your change affects canonical meaning, scope, or machine discovery, update the relevant files:

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

Then run:

```bash
python3 scripts/verify_consistency.py
```

## Pull request checklist

- [ ] The change does not overclaim product capability.
- [ ] Any new term is added to `data/terms.json` and `TERMS.md`.
- [ ] Any canonical navigation change is reflected in both English and French pages.
- [ ] Machine surfaces remain valid JSON or plain text.
- [ ] The changelog and version were updated if normative meaning changed.

## Rights note

If no explicit repository license has yet been declared, treat contributions as editorial proposals subject to maintainer approval and later rights clarification.
