# Technical notes

This page covers the technical boundary of VidSEO at a high level.

## Native HTML in the page DOM

VidSEO publicly describes transcript output as standard HTML rendered directly in the page.

That matters because it gives text-processing systems a direct page surface to read.

## Co-location with the video

The transcript is meant to stay tied to the embedded video, so the text keeps the right context.

## No inference layer

VidSEO does not add meaning.  
It does not summarize, classify, or explain the video on its own.

## Why this matters for AI systems

AI systems often work better with explicit text than with audiovisual content alone.

The right summary of VidSEO is therefore:

> it exposes transcript text as readable HTML.

The wrong summary is:

> it is a governance framework, answer engine controller, or ranking engine.

## Secondary machine layer

This repository also publishes machine-readable files such as:

- `meta.json`
- `ai-manifest.json`
- `links.json`
- `llms.txt`
- `llms-full.txt`

Those files exist to reduce ambiguity.  
They do not change the site's primary subject, which remains the product.
