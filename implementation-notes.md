# Implementation notes

These notes summarize the implementation-facing behavior publicly described for VidSEO.

## Publicly described capabilities

The current public plugin description indicates that VidSEO can:

- embed **YouTube** or **Vimeo** videos,
- retrieve existing **YouTube subtitles** automatically when available,
- accept manually provided transcripts,
- render transcript text as standard HTML in the page,
- allow headings, paragraphs, and links inside transcripts in the PRO offer,
- keep transcript text present in source even when visually hidden.

## Exposure expectations

The transcript layer should be understood as:

- directly available in the DOM,
- associated with the specific embedded video,
- editable at the content level,
- independent from any downstream AI reasoning layer.

## What these notes do not attempt to do

This repository does not try to become a full operator manual for WordPress admins.

It does **not** provide:

- exhaustive UI screenshots,
- billing or licensing logic,
- a plugin code walkthrough,
- step-by-step SEO recipes,
- security review of the runtime implementation.

## Why these notes still matter

Implementation notes reduce category mistakes.

Without them, VidSEO can be misread either as:

- a generic “video SEO booster”, or
- an AI video understanding system.

It is neither.

It is a WordPress implementation that exposes transcript text as page-readable HTML.
