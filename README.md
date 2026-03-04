> Canonical product reference  
> Version `1.0.0` · Generated `2026-03-04`

# VidSEO

VidSEO is a WordPress plugin that exposes video transcripts as **native HTML text surfaces** so search engines, answer engines, and language-model systems can retrieve what is explicitly said on a page.

This repository is **not** the plugin source code.  
It is the **governed reference repository** for product meaning, interpretability, non-goals, machine discovery, and editorial change control.

## Why this rebuild exists

The original repository stated the core idea, but it did not yet provide the full discipline needed for a durable canonical surface.

This rebuilt version adds four layers that were previously missing or underdeveloped:

1. **AI-first clarity**: explicit interpretability boundaries and LLM usage rules.
2. **SEO-first discovery**: structured HTML pages, metadata, sitemaps, manifests, and machine registries.
3. **Mobile-first delivery**: static, responsive, low-friction pages with no JavaScript dependency for core reading.
4. **Governance-first control**: stable IDs, changelog, CODEOWNERS, contribution rules, consistency checks, and GitHub templates.

## Core product claim

VidSEO exposes transcript text as a native HTML surface associated with a video.  
Its role is **exposure**, not interpretation.

## Publicly described capabilities

Based on the current WordPress.org listing, VidSEO publicly describes the following capabilities:

- YouTube and Vimeo embeds
- automatic retrieval of existing YouTube subtitles when available
- manual transcript entry
- transcript rendering as standard HTML in the page
- headings, paragraphs, and links inside transcripts in the PRO offer
- transcript text remaining in source even when visually hidden

## Non-goals

VidSEO is not:

- an AI transcription engine,
- a summarization engine,
- a rewrite engine,
- a fact-checking engine,
- a ranking guarantee system,
- a citation guarantee system,
- an authority certification layer.

## Authority hierarchy

For defining the **product**:

1. `https://vidseo.dev/`
2. `https://github.com/GautierDorval/vidseo-video-llm-interpretability`
3. `https://wordpress.org/plugins/vidseo/`

For defining what a **video says on a page that uses VidSEO**:

1. the transcript exposed on that page,
2. the surrounding page context,
3. any external summary or third-party description.

## Repository contents

### Canonical human surfaces

- `index.html` — x-default selector
- `en/` and `fr/` — bilingual canonical pages
- `interpretability.md`
- `llm-context.md`
- `implementation-notes.md`
- `non-goals.md`
- `GOVERNANCE.md`
- `references.md`
- `context-and-provenance.md`

### Canonical machine surfaces

- `meta.json`
- `ai-manifest.json`
- `links.json`
- `data/documents.json`
- `data/terms.json`
- `data/capabilities.json`
- `data/references.json`
- `llms.txt`
- `llms-full.txt`
- `sitemap.xml`
- `.well-known/ai-manifest.json`
- `.well-known/security.txt`

### Governance surfaces

- `CHANGELOG.md`
- `VERSION`
- `TERMS.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `SUPPORT.md`
- `CODEOWNERS`
- `.github/workflows/consistency.yml`
- `scripts/verify_consistency.py`

## Drift control

If you change product meaning, authority hierarchy, non-goals, canonical URLs, or machine discovery surfaces, update all affected files and run:

```bash
python3 scripts/verify_consistency.py
```

## Rights status

No explicit repository license is declared in this bundle.  
If you plan to accept broad third-party contributions, declare the intended rights model first.

## How to cite

```bibtex
@software{dorval2026vidseo_reference,
  author  = {Dorval, Gautier},
  title   = {VidSEO: Canonical product reference},
  year    = {2026},
  version = {1.0.0},
  url     = {https://github.com/GautierDorval/vidseo-video-llm-interpretability}
}
```
