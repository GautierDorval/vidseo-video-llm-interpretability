# Principles

VidSEO should be documented, interpreted, and presented under four non-negotiable principles.

## 1. AI-first

VidSEO exists to reduce interpretive guessing around video content.

That means the repository must privilege:

- explicit text over implied meaning,
- deterministic machine-readable files over opaque prose,
- conservative claims over persuasive overstatement,
- stable URLs and stable identifiers over ad-hoc naming.

Any edit that increases ambiguity about whether VidSEO **generates**, **analyzes**, or **guarantees** outcomes should be rejected.

## 2. SEO-first

VidSEO helps machines understand what a video says by exposing transcript text directly on the page.

The repository must therefore favor:

- crawlable HTML,
- canonical metadata,
- stable document structure,
- descriptive titles and summaries,
- structured data and discovery files,
- low-friction access to key definitions.

SEO-first here does **not** mean ranking promises. It means discoverability, clarity, and clean retrieval.

## 3. Mobile-first

The canonical site should remain readable and fast on small screens before it is optimized for wide screens.

Required implications:

- single-column reading is the default,
- typography scales fluidly,
- navigation remains finger-friendly,
- pages do not depend on JavaScript for core reading,
- payload remains light.

## 4. Governance-first

The meaning of VidSEO must not drift across pages, manifests, registries, or future edits.

Governance-first means:

- stable document IDs,
- stable term IDs,
- explicit content classes (`normative`, `informative`, `contextual`),
- versioning and changelog discipline,
- repeatable consistency checks,
- clear maintainer authority.

## Editorial consequences

These four principles imply a writing rule:

> Say exactly what VidSEO does, say exactly what it does not do, and leave no rhetorical space for downstream systems to imagine hidden capabilities.

That rule applies equally to README content, HTML pages, JSON surfaces, issue templates, and future releases.
