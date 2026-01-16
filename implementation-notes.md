# Implementation notes

VidSEO operates entirely at the content exposure level.

## Transcript exposure

Video transcripts are rendered as native HTML elements within the page DOM.
They are not embedded as external files (e.g. VTT-only, JSON-only) and do not rely on third-party APIs at runtime.

This allows crawlers and language models to:
- read transcript text directly,
- locate specific passages,
- associate transcript content with the embedded video context.

## Structure and proximity

Transcripts are colocated with the video embed on the page.
This proximity preserves contextual association without requiring inference across unrelated sections.

The transcript structure may include:
- paragraphs,
- headings,
- links,
- standard HTML formatting.

No semantic transformation is applied by VidSEO.

## No processing layer

VidSEO does not process, analyze, or modify transcript content.
All interpretation, summarization, or reasoning occurs downstream, outside the plugin’s scope.
