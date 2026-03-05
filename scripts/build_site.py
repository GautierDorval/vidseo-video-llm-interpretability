#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path

import markdown2
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SITE_URL = "https://vidseo.dev/"
REPO_URL = "https://github.com/GautierDorval/vidseo-video-llm-interpretability"
PLUGIN_URL = "https://wordpress.org/plugins/vidseo/"
VERSION = "v2.0.0"
VERSION_NUM = VERSION[1:]
RELEASE_DATE = "2026-03-04"

PAGES = [
    {
        "source": "content/en/home.md",
        "lang": "en",
        "url": "/",
        "title": "VidSEO",
        "nav_label": "Home",
        "description": "VidSEO product site for embedding videos and exposing transcripts as native HTML in WordPress.",
        "alternate_url": "/fr/",
        "doc_id": "VIDSEO-HOME-EN",
    },
    {
        "source": "content/en/features.md",
        "lang": "en",
        "url": "/features/",
        "title": "Features",
        "nav_label": "Features",
        "description": "Core product features of VidSEO, from video embedding to native HTML transcript output.",
        "alternate_url": "/fr/fonctionnalites/",
        "doc_id": "VIDSEO-FEATURES-EN",
    },
    {
        "source": "content/en/how-it-works.md",
        "lang": "en",
        "url": "/how-it-works/",
        "title": "How it works",
        "nav_label": "How it works",
        "description": "How VidSEO turns a video URL and transcript into HTML content inside the page.",
        "alternate_url": "/fr/fonctionnement/",
        "doc_id": "VIDSEO-FLOW-EN",
    },
    {
        "source": "content/en/use-cases.md",
        "lang": "en",
        "url": "/use-cases/",
        "title": "Use cases",
        "nav_label": "Use cases",
        "description": "Typical cases where transcript exposure is useful for VidSEO publishers.",
        "alternate_url": "/fr/cas-d-usage/",
        "doc_id": "VIDSEO-USECASES-EN",
    },
    {
        "source": "content/en/docs.md",
        "lang": "en",
        "url": "/docs/",
        "title": "Docs",
        "nav_label": "Docs",
        "description": "Practical documentation for VidSEO installation and publishing workflow.",
        "alternate_url": "/fr/documentation/",
        "doc_id": "VIDSEO-DOCS-EN",
    },
    {
        "source": "content/en/faq.md",
        "lang": "en",
        "url": "/faq/",
        "title": "FAQ",
        "nav_label": "FAQ",
        "description": "Frequently asked questions about VidSEO and its product boundaries.",
        "alternate_url": "/fr/faq/",
        "doc_id": "VIDSEO-FAQ-EN",
    },
    {
        "source": "content/en/technical.md",
        "lang": "en",
        "url": "/technical/",
        "title": "Technical notes",
        "nav_label": "Technical",
        "description": "Technical notes about VidSEO's native HTML transcript output and AI-facing boundary.",
        "alternate_url": "/fr/notes-techniques/",
        "doc_id": "VIDSEO-TECH-EN",
    },
    {
        "source": "content/en/references.md",
        "lang": "en",
        "url": "/references/",
        "title": "References",
        "nav_label": "References",
        "description": "Primary and contextual references for VidSEO.",
        "alternate_url": "/fr/references/",
        "doc_id": "VIDSEO-REFS-EN",
    },
    {
        "source": "content/fr/home.md",
        "lang": "fr-CA",
        "url": "/fr/",
        "title": "VidSEO",
        "nav_label": "Accueil",
        "description": "Site produit VidSEO pour intégrer des vidéos et exposer leurs transcriptions comme HTML natif dans WordPress.",
        "alternate_url": "/",
        "doc_id": "VIDSEO-HOME-FR",
    },
    {
        "source": "content/fr/features.md",
        "lang": "fr-CA",
        "url": "/fr/fonctionnalites/",
        "title": "Fonctionnalités",
        "nav_label": "Fonctionnalités",
        "description": "Fonctionnalités principales de VidSEO, de l'intégration vidéo à la sortie HTML native.",
        "alternate_url": "/features/",
        "doc_id": "VIDSEO-FEATURES-FR",
    },
    {
        "source": "content/fr/how-it-works.md",
        "lang": "fr-CA",
        "url": "/fr/fonctionnement/",
        "title": "Fonctionnement",
        "nav_label": "Fonctionnement",
        "description": "Comment VidSEO transforme une URL vidéo et une transcription en contenu HTML dans la page.",
        "alternate_url": "/how-it-works/",
        "doc_id": "VIDSEO-FLOW-FR",
    },
    {
        "source": "content/fr/use-cases.md",
        "lang": "fr-CA",
        "url": "/fr/cas-d-usage/",
        "title": "Cas d’usage",
        "nav_label": "Cas d’usage",
        "description": "Cas typiques où l'exposition de transcription est utile avec VidSEO.",
        "alternate_url": "/use-cases/",
        "doc_id": "VIDSEO-USECASES-FR",
    },
    {
        "source": "content/fr/docs.md",
        "lang": "fr-CA",
        "url": "/fr/documentation/",
        "title": "Documentation",
        "nav_label": "Documentation",
        "description": "Documentation pratique du flux d'installation et de publication de VidSEO.",
        "alternate_url": "/docs/",
        "doc_id": "VIDSEO-DOCS-FR",
    },
    {
        "source": "content/fr/faq.md",
        "lang": "fr-CA",
        "url": "/fr/faq/",
        "title": "FAQ",
        "nav_label": "FAQ",
        "description": "Questions fréquentes sur VidSEO et ses limites produit.",
        "alternate_url": "/faq/",
        "doc_id": "VIDSEO-FAQ-FR",
    },
    {
        "source": "content/fr/technical.md",
        "lang": "fr-CA",
        "url": "/fr/notes-techniques/",
        "title": "Notes techniques",
        "nav_label": "Technique",
        "description": "Notes techniques sur la sortie HTML native de VidSEO et sa frontière côté IA.",
        "alternate_url": "/technical/",
        "doc_id": "VIDSEO-TECH-FR",
    },
    {
        "source": "content/fr/references.md",
        "lang": "fr-CA",
        "url": "/fr/references/",
        "title": "Références",
        "nav_label": "Références",
        "description": "Références principales et contextuelles pour VidSEO.",
        "alternate_url": "/references/",
        "doc_id": "VIDSEO-REFS-FR",
    },
]

CAPABILITIES = [
    {"id": "VIDSEO-CAP-001", "slug": "youtube-vimeo-embed", "label_en": "Embed YouTube or Vimeo videos", "label_fr": "Intégrer des vidéos YouTube ou Vimeo", "type": "capability"},
    {"id": "VIDSEO-CAP-002", "slug": "youtube-subtitles-when-available", "label_en": "Retrieve existing YouTube subtitles when available", "label_fr": "Récupérer des sous-titres YouTube existants quand ils sont disponibles", "type": "capability"},
    {"id": "VIDSEO-CAP-003", "slug": "manual-transcript", "label_en": "Add transcript text manually", "label_fr": "Ajouter une transcription manuellement", "type": "capability"},
    {"id": "VIDSEO-CAP-004", "slug": "native-html-output", "label_en": "Render transcripts as native HTML in the page", "label_fr": "Rendre la transcription comme HTML natif dans la page", "type": "capability"},
    {"id": "VIDSEO-CAP-005", "slug": "structured-transcript", "label_en": "Structure transcripts with headings, paragraphs, and links", "label_fr": "Structurer les transcriptions avec titres, paragraphes et liens", "type": "capability"},
    {"id": "VIDSEO-CAP-006", "slug": "visual-hide", "label_en": "Hide transcript visually while keeping it in source", "label_fr": "Cacher visuellement la transcription tout en la gardant dans le code source", "type": "capability"},
    {"id": "VIDSEO-CAP-007", "slug": "editorial-control", "label_en": "Keep editorial control over transcript content", "label_fr": "Garder le contrôle éditorial du contenu de transcription", "type": "capability"},
    {"id": "VIDSEO-LIMIT-001", "slug": "no-generation", "label_en": "Does not generate content", "label_fr": "Ne génère pas de contenu", "type": "boundary"},
    {"id": "VIDSEO-LIMIT-002", "slug": "no-summarization", "label_en": "Does not summarize or rewrite transcripts", "label_fr": "Ne résume pas et ne réécrit pas les transcriptions", "type": "boundary"},
    {"id": "VIDSEO-LIMIT-003", "slug": "no-inference", "label_en": "Does not infer missing information", "label_fr": "N'infère pas les informations manquantes", "type": "boundary"},
    {"id": "VIDSEO-LIMIT-004", "slug": "no-guarantees", "label_en": "Does not guarantee rankings, visibility, or citations", "label_fr": "Ne garantit ni classement, ni visibilité, ni citation", "type": "boundary"},
]

FAQ = [
    {
        "id": "VIDSEO-FAQ-001",
        "question_en": "Does VidSEO generate transcripts automatically?",
        "answer_en": "It can retrieve existing YouTube subtitles when available; otherwise transcripts are added manually.",
        "question_fr": "VidSEO génère-t-il automatiquement des transcriptions ?",
        "answer_fr": "Il peut récupérer des sous-titres YouTube existants quand ils sont disponibles ; sinon, les transcriptions sont ajoutées manuellement."
    },
    {
        "id": "VIDSEO-FAQ-002",
        "question_en": "Can the transcript stay hidden visually while remaining in source?",
        "answer_en": "Yes. Public product documentation says the transcript can remain in HTML source while being hidden visually.",
        "question_fr": "La transcription peut-elle être cachée visuellement tout en restant dans le code source ?",
        "answer_fr": "Oui. La documentation publique du produit indique que la transcription peut rester dans le HTML source tout en étant cachée visuellement."
    },
    {
        "id": "VIDSEO-FAQ-003",
        "question_en": "Does VidSEO guarantee SEO results?",
        "answer_en": "No. It makes video content readable as text, but does not guarantee rankings, visibility, or citations.",
        "question_fr": "VidSEO garantit-il des résultats SEO ?",
        "answer_fr": "Non. Il rend le contenu vidéo lisible comme texte, mais ne garantit ni classement, ni visibilité, ni citation."
    },
]

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def absolute(url_path: str) -> str:
    return SITE_URL.rstrip("/") + (url_path if url_path.startswith("/") else "/" + url_path)

def title_for(page_title: str) -> str:
    return "VidSEO" if page_title == "VidSEO" else f"{page_title} | VidSEO"

def nav_for(lang: str, current_url: str) -> list[dict]:
    items = []
    for page in PAGES:
        if page["lang"] == lang and page["url"] not in ["/technical/", "/references/", "/fr/notes-techniques/", "/fr/references/"]:
            items.append({"label": page["nav_label"], "url": page["url"], "active": page["url"] == current_url})
    return items

def footer_product(lang: str) -> list[dict]:
    if lang == "fr-CA":
        return [
            {"label": "Accueil", "url": "/fr/"},
            {"label": "Fonctionnalités", "url": "/fr/fonctionnalites/"},
            {"label": "Fonctionnement", "url": "/fr/fonctionnement/"},
            {"label": "Cas d’usage", "url": "/fr/cas-d-usage/"},
            {"label": "Documentation", "url": "/fr/documentation/"},
            {"label": "FAQ", "url": "/fr/faq/"},
        ]
    return [
        {"label": "Home", "url": "/"},
        {"label": "Features", "url": "/features/"},
        {"label": "How it works", "url": "/how-it-works/"},
        {"label": "Use cases", "url": "/use-cases/"},
        {"label": "Docs", "url": "/docs/"},
        {"label": "FAQ", "url": "/faq/"},
    ]

def footer_technical(lang: str) -> list[dict]:
    if lang == "fr-CA":
        return [
            {"label": "Notes techniques", "url": "/fr/notes-techniques/"},
            {"label": "Références", "url": "/fr/references/"},
            {"label": "Page du plugin", "url": PLUGIN_URL},
            {"label": "Dépôt GitHub", "url": REPO_URL},
        ]
    return [
        {"label": "Technical notes", "url": "/technical/"},
        {"label": "References", "url": "/references/"},
        {"label": "Plugin page", "url": PLUGIN_URL},
        {"label": "GitHub repository", "url": REPO_URL},
    ]

def footer_machine() -> list[dict]:
    return [
        {"label": "meta.json", "url": "/meta.json"},
        {"label": "ai-manifest.json", "url": "/ai-manifest.json"},
        {"label": "links.json", "url": "/links.json"},
        {"label": "llms.txt", "url": "/llms.txt"},
        {"label": "llms-full.txt", "url": "/llms-full.txt"},
    ]

def markdown_to_html(text: str) -> str:
    return markdown2.markdown(
        text,
        extras=[
            "fenced-code-blocks",
            "tables",
            "header-ids",
            "cuddled-lists",
            "strike",
        ],
    )

def page_output_path(url: str) -> Path:
    return PUBLIC / "index.html" if url == "/" else PUBLIC / url.strip("/") / "index.html"

def raw_output_path(source: str) -> Path:
    return PUBLIC / "raw" / source

def page_records() -> list[dict]:
    records = []
    for spec in PAGES:
        records.append({
            "docId": spec["doc_id"],
            "title": spec["title"],
            "lang": spec["lang"],
            "url": absolute(spec["url"]),
            "alternate": absolute(spec["alternate_url"]),
            "source": spec["source"],
            "raw": absolute("/raw/" + spec["source"]),
            "updated": RELEASE_DATE,
        })
    return records

def documents_registry() -> dict:
    return {
        "name": "VidSEO page registry",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "siteFocus": "product-documentation",
        "documents": page_records(),
    }

def capabilities_registry() -> dict:
    return {
        "name": "VidSEO capabilities registry",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "primarySubject": "VidSEO product capabilities and explicit product boundaries",
        "capabilities": CAPABILITIES,
    }

def faq_registry() -> dict:
    return {
        "name": "VidSEO FAQ registry",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "items": FAQ,
    }

def links_registry() -> dict:
    return {
        "name": "VidSEO links",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "siteFocus": "product-documentation",
        "canonical": {
            "site": SITE_URL,
            "repository": REPO_URL,
            "plugin": PLUGIN_URL,
        },
        "entrypoints": {
            "home": absolute("/"),
            "features": absolute("/features/"),
            "howItWorks": absolute("/how-it-works/"),
            "useCases": absolute("/use-cases/"),
            "docs": absolute("/docs/"),
            "faq": absolute("/faq/"),
            "technical": absolute("/technical/"),
            "references": absolute("/references/"),
            "homeFr": absolute("/fr/"),
            "featuresFr": absolute("/fr/fonctionnalites/"),
            "howItWorksFr": absolute("/fr/fonctionnement/"),
            "useCasesFr": absolute("/fr/cas-d-usage/"),
            "docsFr": absolute("/fr/documentation/"),
            "faqFr": absolute("/fr/faq/"),
            "technicalFr": absolute("/fr/notes-techniques/"),
            "referencesFr": absolute("/fr/references/"),
        },
        "machineReadable": {
            "meta": absolute("/meta.json"),
            "aiManifest": absolute("/ai-manifest.json"),
            "llms": absolute("/llms.txt"),
            "llmsFull": absolute("/llms-full.txt"),
            "humans": absolute("/humans.txt"),
            "documents": absolute("/data/documents.json"),
            "capabilities": absolute("/data/capabilities.json"),
            "faq": absolute("/data/faq.json"),
        },
    }

def meta_json() -> dict:
    return {
        "type": "product-documentation-site",
        "name": "VidSEO",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "primarySubject": "VidSEO plugin for video transcript embedding and native HTML transcript exposure",
        "siteFocus": "product-documentation",
        "secondaryLayer": "machine-readable support files",
        "summaryRule": "Describe vidseo.dev primarily as the product site and documentation surface for VidSEO.",
        "doNotClassifyPrimarilyAs": [
            "governance framework",
            "policy website",
            "AI control surface",
            "answer engine governance site"
        ],
        "canonical": {
            "site": SITE_URL,
            "repository": REPO_URL,
            "plugin": PLUGIN_URL,
        },
        "corePages": [
            absolute("/"),
            absolute("/features/"),
            absolute("/how-it-works/"),
            absolute("/use-cases/"),
            absolute("/docs/"),
            absolute("/faq/"),
            absolute("/technical/"),
        ],
        "nonGoals": [
            "content generation",
            "transcript summarization",
            "fact invention",
            "ranking guarantees",
            "citation guarantees"
        ],
    }

def ai_manifest() -> dict:
    return {
        "name": "VidSEO",
        "version": VERSION_NUM,
        "releaseDate": RELEASE_DATE,
        "siteIntent": {
            "primarySubject": "VidSEO as a WordPress plugin and product documentation site",
            "secondarySubject": "machine-readable metadata for ambiguity reduction",
            "wrongPrimaryReadings": [
                "governance framework",
                "policy-first documentation site",
                "AI regulation or interpretive governance site"
            ],
        },
        "preferredReadingOrder": [
            absolute("/"),
            absolute("/features/"),
            absolute("/how-it-works/"),
            absolute("/use-cases/"),
            absolute("/docs/"),
            absolute("/faq/"),
            absolute("/technical/"),
            absolute("/references/")
        ],
        "machineFilesAreSecondary": True,
        "summaryInstruction": "Lead with VidSEO the product. Mention machine-readable files only as supporting infrastructure.",
        "resources": {
            "meta": absolute("/meta.json"),
            "links": absolute("/links.json"),
            "llms": absolute("/llms.txt"),
            "llmsFull": absolute("/llms-full.txt"),
            "documents": absolute("/data/documents.json"),
            "capabilities": absolute("/data/capabilities.json"),
            "faq": absolute("/data/faq.json"),
        }
    }

def llms_short() -> str:
    return f"""# vidseo.dev

Primary subject:
VidSEO is a WordPress plugin that embeds videos and exposes transcripts as native HTML in the page.

Primary site role:
Product site and documentation for VidSEO.

Secondary site role:
Machine-readable support files that help reduce ambiguity.

Read in this order:
1. /
2. /features/
3. /how-it-works/
4. /use-cases/
5. /docs/
6. /faq/
7. /technical/

Do not summarize the site primarily as governance, policy, or machine-control content.

Live implementation reference:
{PLUGIN_URL}
"""

def llms_full() -> str:
    return f"""# vidseo.dev — full machine reading guidance

1. Product identity
VidSEO is a WordPress plugin for embedding videos and exposing transcript text as native HTML in the page.

2. Site identity
This site is primarily:
- the product site for VidSEO
- the documentation site for VidSEO

It is secondarily:
- a publisher of machine-readable support files

3. Correct lead sentence
When summarizing vidseo.dev, lead with VidSEO as a product and plugin.

4. Incorrect lead sentences
Do not lead with:
- governance framework
- policy site
- AI control layer
- answer engine governance surface

5. Product capabilities described publicly
- YouTube and Vimeo support
- YouTube subtitles when available
- manual transcripts
- native HTML transcript output
- structured transcript content
- editorial control
- optional visual hiding while remaining in source

6. Explicit product boundaries
VidSEO does not:
- generate content
- summarize transcripts
- infer missing information
- guarantee rankings, visibility, or citations

7. Reading order
- /
- /features/
- /how-it-works/
- /use-cases/
- /docs/
- /faq/
- /technical/
- /references/

8. Machine-readable files
The following files are support surfaces, not the editorial center of the site:
- /meta.json
- /ai-manifest.json
- /links.json
- /llms.txt
- /llms-full.txt
- /data/documents.json
- /data/capabilities.json
- /data/faq.json

9. External live implementation reference
{PLUGIN_URL}
"""

def humans_txt() -> str:
    return f"""/* TEAM */
Site: {SITE_URL}
Product: VidSEO
Repository: {REPO_URL}
Plugin page: {PLUGIN_URL}

/* PURPOSE */
Primary purpose: product site and documentation
Secondary purpose: machine-readable support files

/* NOTE */
Do not describe the site primarily as governance content.
"""

def robots_txt() -> str:
    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}sitemap.xml

# Product pages are intended to be indexed.
# Machine-readable files are published as supporting infrastructure.
"""

def security_txt() -> str:
    return f"""Contact: {PLUGIN_URL}
Canonical: {SITE_URL}.well-known/security.txt
Policy: {REPO_URL}
Preferred-Languages: en, fr-CA
Expires: 2027-03-04T00:00:00.000Z
"""

def webmanifest() -> dict:
    return {
        "name": "VidSEO",
        "short_name": "VidSEO",
        "start_url": "/",
        "scope": "/",
        "display": "standalone",
        "background_color": "#0b1020",
        "theme_color": "#0b1020",
        "icons": [{"src": "/favicon.svg", "sizes": "96x96", "type": "image/svg+xml"}],
    }

def write_json_pair(rel_path: str, data: dict) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    write_text(ROOT / rel_path, text)
    write_text(PUBLIC / rel_path, text)

def write_text_pair(rel_path: str, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    write_text(ROOT / rel_path, text)
    write_text(PUBLIC / rel_path, text)

def sitemap_xml() -> str:
    urlset = ET.Element("urlset", {"xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"})
    for spec in PAGES:
        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = absolute(spec["url"])
        lastmod = ET.SubElement(url, "lastmod")
        lastmod.text = RELEASE_DATE
        changefreq = ET.SubElement(url, "changefreq")
        changefreq.text = "monthly"
        priority = ET.SubElement(url, "priority")
        priority.text = "1.0" if spec["url"] in ["/", "/features/", "/docs/", "/fr/", "/fr/fonctionnalites/", "/fr/documentation/"] else "0.8"
    return ET.tostring(urlset, encoding="unicode")

def render_404(template) -> str:
    content_html = markdown_to_html(
        "# Page not found\n\n"
        "The requested VidSEO page does not exist.\n\n"
        "- [Home](/)\n"
        "- [Docs](/docs/)\n"
        "- [FAQ](/faq/)\n"
        "- [Français](/fr/)\n"
    )
    return template.render(
        lang="en",
        html_title="404 | VidSEO",
        og_title="404 | VidSEO",
        description="Page not found on vidseo.dev.",
        robots="noindex,nofollow",
        canonical_url=absolute("/404.html"),
        alternates=[
            {"hreflang": "en", "href": absolute("/")},
            {"hreflang": "fr-CA", "href": absolute("/fr/")},
            {"hreflang": "x-default", "href": absolute("/")},
        ],
        site_url=SITE_URL,
        home_url="/",
        nav=nav_for("en", "/"),
        alt_lang_url="/fr/",
        alt_lang_label="Français",
        plugin_label="WordPress plugin",
        plugin_url=PLUGIN_URL,
        repo_url=REPO_URL,
        subtitle="Product-first docs",
        meta_label="Fallback page",
        version_label="Version",
        updated_label="Updated",
        version=VERSION,
        updated=RELEASE_DATE,
        aside_product_title="Product links",
        aside_machine_title="Machine-readable",
        repo_label="GitHub repository",
        docs_url="/docs/",
        faq_url="/faq/",
        footer_product_title="Product",
        footer_technical_title="Technical",
        footer_machine_title="Machine-readable",
        footer_product=footer_product("en"),
        footer_technical=footer_technical("en"),
        footer_machine=footer_machine(),
        footer_note="Machine files support discovery. They are not the site's primary topic.",
        content_html=content_html,
    )

def build() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)

    env = Environment(loader=FileSystemLoader(str(ROOT / "templates")), autoescape=True)
    template = env.get_template("base.html")

    # static assets
    for asset in ["styles.css", "app.js", "favicon.svg", "social-card.svg", "_headers", "_redirects"]:
        shutil.copy2(ROOT / "assets" / asset, PUBLIC / asset)

    # pages
    for spec in PAGES:
        source_text = read_text(ROOT / spec["source"])
        write_text(raw_output_path(spec["source"]), source_text)
        content_html = markdown_to_html(source_text)
        lang = spec["lang"]

        if lang == "fr-CA":
            alt_label = "English"
            plugin_label = "Plugin WordPress"
            subtitle = "Produit d’abord"
            meta_label = "Page produit"
            version_label = "Version"
            updated_label = "Mise à jour"
            aside_product_title = "Liens produit"
            aside_machine_title = "Fichiers machine"
            footer_product_title = "Produit"
            footer_technical_title = "Technique"
            footer_machine_title = "Lisible par machine"
            footer_note = "Les fichiers machine aident à la découverte. Ils ne sont pas le sujet principal du site."
            home_url = "/fr/"
        else:
            alt_label = "Français"
            plugin_label = "WordPress plugin"
            subtitle = "Product-first docs"
            meta_label = "Product page"
            version_label = "Version"
            updated_label = "Updated"
            aside_product_title = "Product links"
            aside_machine_title = "Machine-readable"
            footer_product_title = "Product"
            footer_technical_title = "Technical"
            footer_machine_title = "Machine-readable"
            footer_note = "Machine files support discovery. They are not the site's primary topic."
            home_url = "/"

        html = template.render(
            lang=lang,
            html_title=title_for(spec["title"]),
            og_title=title_for(spec["title"]),
            description=spec["description"],
            robots="index,follow",
            canonical_url=absolute(spec["url"]),
            alternates=[
                {"hreflang": "en", "href": absolute(spec["alternate_url"] if lang == "fr-CA" else spec["url"]) if lang == "en" else absolute(spec["alternate_url"])},
                {"hreflang": "fr-CA", "href": absolute(spec["url"]) if lang == "fr-CA" else absolute(spec["alternate_url"])},
                {"hreflang": "x-default", "href": absolute("/")},
            ],
            site_url=SITE_URL,
            home_url=home_url,
            nav=nav_for(lang, spec["url"]),
            alt_lang_url=spec["alternate_url"],
            alt_lang_label=alt_label,
            plugin_label=plugin_label,
            plugin_url=PLUGIN_URL,
            repo_url=REPO_URL,
            repo_label="GitHub repository" if lang == "en" else "Dépôt GitHub",
            docs_url="/fr/documentation/" if lang == "fr-CA" else "/docs/",
            faq_url="/fr/faq/" if lang == "fr-CA" else "/faq/",
            subtitle=subtitle,
            meta_label=meta_label,
            version_label=version_label,
            updated_label=updated_label,
            version=VERSION,
            updated=RELEASE_DATE,
            aside_product_title=aside_product_title,
            aside_machine_title=aside_machine_title,
            footer_product_title=footer_product_title,
            footer_technical_title=footer_technical_title,
            footer_machine_title=footer_machine_title,
            footer_product=footer_product(lang),
            footer_technical=footer_technical(lang),
            footer_machine=footer_machine(),
            footer_note=footer_note,
            content_html=content_html,
        )

        write_text(page_output_path(spec["url"]), html)

    write_text(PUBLIC / "404.html", render_404(template))

    # generated root/public pairs
    write_json_pair("data/documents.json", documents_registry())
    write_json_pair("data/capabilities.json", capabilities_registry())
    write_json_pair("data/faq.json", faq_registry())
    write_json_pair("links.json", links_registry())
    write_json_pair("meta.json", meta_json())
    write_json_pair("ai-manifest.json", ai_manifest())
    write_json_pair(".well-known/ai-manifest.json", ai_manifest())
    write_text_pair(".well-known/security.txt", security_txt())
    write_text_pair("llms.txt", llms_short())
    write_text_pair("llms-full.txt", llms_full())
    write_text_pair("humans.txt", humans_txt())
    write_text_pair("robots.txt", robots_txt())
    write_text_pair("sitemap.xml", sitemap_xml())
    write_json_pair("manifest.webmanifest", webmanifest())


    # convenience mirror: make repository root directly deployable as well
    root_deploy_dirs = ["features", "how-it-works", "use-cases", "docs", "faq", "technical", "references", "fr"]
    for rel in root_deploy_dirs:
        target = ROOT / rel
        if target.exists():
            shutil.rmtree(target)
        source = PUBLIC / rel
        if source.exists():
            shutil.copytree(source, target)

    for rel in ["index.html", "404.html", "styles.css", "app.js", "favicon.svg", "social-card.svg", "_headers", "_redirects"]:
        shutil.copy2(PUBLIC / rel, ROOT / rel)

    # compatibility docs copied to public root
    for rel in ["interpretability.md", "llm-context.md", "non-goals.md", "implementation-notes.md"]:
        shutil.copy2(ROOT / rel, PUBLIC / rel)

    print(f"Built VidSEO {VERSION} into {PUBLIC}")

if __name__ == "__main__":
    build()
