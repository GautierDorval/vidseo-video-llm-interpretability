# Interpretability

Most search systems and language-model systems do not treat video itself as a stable, quotable, low-ambiguity evidence surface.

They work better when meaning is exposed as text.

## The interpretive gap

When important explanations live only inside audio or video, machines are pushed toward one of three weak behaviors:

- partial omission,
- probabilistic reconstruction,
- unsupported inference.

None of those behaviors is desirable when a page already contains a precise human-authored explanation inside the video.

## VidSEO's role

VidSEO addresses that gap by exposing transcript text as a native HTML surface associated with the embedded video.

This changes the machine situation in a very specific way:

- passages become retrievable,
- wording becomes quoteable,
- ambiguity decreases,
- downstream systems can rely less on guessing.

## What interpretability means here

In this repository, **interpretability** does not mean “the plugin interprets the video”.

It means the plugin helps **other systems interpret the page more safely** by giving them explicit text.

That is a narrower and more disciplined claim.

## What interpretability does not mean

It does **not** mean:

- semantic enrichment,
- factual validation,
- expert certification,
- ranking influence,
- model compliance guarantees.

VidSEO reduces a retrieval problem.  
It does not solve every downstream reasoning problem.

## Scope of authority

The authoritative surface provided by VidSEO is the transcript text exposed on the page.

If a fact is not present in the transcript, VidSEO should not be treated as having supplied that fact.
