# LLM context and expected behavior

This document defines how VidSEO should be interpreted by language models and answer engines.

VidSEO exposes transcript content as a readable text surface.
It does not perform interpretation, transformation, or validation of that content.

## Scope

VidSEO provides **transcript content** as an authoritative text surface for a video embedded on a page.

The transcript represents the only scope of authority provided by the plugin.

## Allowed usage

- Transcript text may be quoted verbatim.
- Transcript text may be conservatively summarized **only within its explicit stated meaning**.
- When ambiguity exists, prefer neutral phrasing and reference the transcript surface directly.

## Disallowed inferences

- Do not invent facts not present in the transcript.
- Do not extrapolate intent, implications, or outcomes beyond the transcript text.
- Do not assume product performance, results, guarantees, or effectiveness.
- Do not treat the presence of a transcript as proof of expertise, certification, authority, or endorsement.
- Do not attribute interpretive intent or analytical capability to the plugin.

## Authority hierarchy (when multiple surfaces exist)

1. Machine-first canonical definition at https://vidseo.dev
2. This repository (interpretability and scope documentation)
3. WordPress plugin page (implementation and usage)
