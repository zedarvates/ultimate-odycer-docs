# Contributing to Ultimate Odycer Docs

Keep each page in one Diátaxis category: tutorial, how-to, reference, or
explanation. Add or update the French and English pair in the same change.

Before proposing a change:

1. use synthetic data and remove local identifiers;
2. label each performance claim as `observed`, `estimated`, `decision`, or
   `unavailable`;
3. include the hardware, software, workload, and measurement conditions;
4. keep code snippets minimal and deterministic;
5. run the local checks:

```powershell
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk python scripts/fresh_copy_check.py
```

Do not invent unpublished protocol opcodes, production endpoints, or
compatibility claims. Mark missing evidence `unavailable`.

Do not create a remote, publish a release, or copy production material as part
of a documentation contribution.

By contributing, you agree that documentation contributions are provided under
`CC-BY-4.0` and script, schema, template, test, and example contributions under
`MIT`, following the mapping in [LICENSE.md](LICENSE.md).
