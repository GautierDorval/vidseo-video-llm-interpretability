# Architecture

VidSEO has two architectures that matter:

1. the **product architecture** that exposes transcripts on a WordPress page,
2. the **reference architecture** that defines how the product is described and discovered.

## Layer 1. Product layer

Publicly described capabilities indicate that VidSEO can:

- embed supported video sources,
- associate a transcript with a given video,
- render the transcript as HTML on the page,
- let the transcript remain close to the video context.

This is the operational product layer.

## Layer 2. Exposure layer

The critical design claim is not “video SEO magic”.  
It is **text exposure**.

The transcript becomes a first-class surface inside the DOM rather than an inaccessible media-only payload. This is the layer that matters for crawlers, answer engines, and retrieval-based systems.

## Layer 3. Machine-surface layer

This repository adds a second exposure system around the product itself:

- `meta.json`
- `ai-manifest.json`
- `links.json`
- `llms.txt`
- `data/documents.json`
- `data/terms.json`
- `data/capabilities.json`

Together, these files reduce ambiguity about product meaning, scope, and authority.

## Layer 4. Governance layer

Meaning without governance drifts.  
Governance without machine surfaces stays implicit.

The governance layer therefore includes:

- version tracking in `VERSION`,
- release history in `CHANGELOG.md`,
- stable terminology in `TERMS.md`,
- maintainership in `CODEOWNERS`,
- contribution rules in `CONTRIBUTING.md`,
- consistency checks in `scripts/verify_consistency.py`,
- CI enforcement in `.github/workflows/consistency.yml`.

## Why this architecture matters

A plugin can be useful while still being poorly interpreted by machines.  
A repository can be elegant while still being semantically unstable.

This architecture is designed to avoid both failures:

- the product exposes video meaning as text,
- the repository exposes product meaning as governed reference data.
