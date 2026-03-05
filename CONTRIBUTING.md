# Contributing

## Repository rule

The public site is **product-first**.

That means:

- product pages should focus on VidSEO,
- governance belongs in repository policy files and machine-readable metadata,
- machine files should support discovery without becoming the site's main editorial topic.

## Before opening a pull request

1. Keep the main site product-focused.
2. Preserve English/French parity for meaning changes.
3. Rebuild the site.
4. Run consistency checks.
5. Update `CHANGELOG.md` if the public meaning changes.

## Commands

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_site.py
python3 scripts/verify_consistency.py
```

## Do not add

- ranking guarantees
- citation guarantees
- unsupported SEO promises
- invented product capabilities
- governance-heavy copy on primary product pages

## Preferred pattern

- explain what VidSEO does,
- explain how it works,
- explain the limits,
- keep policy and machine surfaces in secondary locations.
