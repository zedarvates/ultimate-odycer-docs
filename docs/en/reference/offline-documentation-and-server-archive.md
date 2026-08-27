# Offline documentation and server archive

This reference distinguishes the three Ultimate Odycer documentation outputs.
It is intended for technical beginners assisted by an LLM and for operators
who verify an archive before running it.

> **Public status:** no public server archive is currently downloadable. The
> [official releases page](https://www.ultimateodycer.com/releases/) remains
> the only source for a future file and its SHA-256. A local documentation
> build is not a server release.

## Three outputs that must remain distinct

| Output | Purpose | Evidence provided | Does not prove |
|---|---|---|---|
| Markdown sources | canonical French and English content | repository validation | Web publication |
| Offline HTML bundle | local reading without a Web service | file manifest and digests | executable server |
| Server archive | server, deployment files, and compatible docs | release manifest and published SHA-256 | production deployment |

The Web site and offline bundle must derive from the same sources. Manually
maintaining a second HTML copy would create divergent content.

## Offline HTML bundle contract

The bundle root contains:

```text
index.html
docs-build-manifest.json
assets/
en/
fr/
```

`docs-build-manifest.json` declares at least:

- schema `ultimate-odycer.docs-build.v1`;
- `documentation_version`;
- source commit;
- entrypoint `index.html`;
- French and English languages;
- `compatibility.server`;
- size and SHA-256 for every file.

Opening one page is insufficient. A file missing from, added to, or changed
against the manifest invalidates the bundle.

## Future server archive contract

After extraction, a conforming archive contains at least:

```text
VERSION
SHA256SUMS.txt
RELEASE-MANIFEST.json
deploy/QUICKSTART.md
docs/index.html
docs/docs-build-manifest.json
```

`RELEASE-MANIFEST.json` links the release to `docs/index.html`, the
documentation version, source commit, and documentation-manifest digest. The
`docs/docs-build-manifest.json -> compatibility.server` value must exactly
match the content of `VERSION`.

The Tools Suite remains optional. A server archive must not claim to contain
the Dungeon, City, Architecture, Creature, or Avatar editors or Asset Factory
unless the release actually lists them as compatible modules.

## Beginner Windows verification

1. Require the file and its SHA-256 on the official page.
2. Compare the archive SHA-256 before extraction.
3. Extract that version into a new directory.
4. Require the six paths listed above.
5. Compare documentation compatibility with the server version:

```powershell
$releaseVersion = (Get-Content .\VERSION -Raw).Trim()
$docsManifest = Get-Content .\docs\docs-build-manifest.json -Raw | ConvertFrom-Json
if ($docsManifest.compatibility.server -ne $releaseVersion) {
    throw "Documentation is incompatible with this server version"
}
```

6. Open `docs/index.html` from the extracted directory. Essential pages must
   remain readable without a network connection.
7. Continue with `deploy/QUICKSTART.md` from that same archive.

A failed step produces a `failed` or `blocked` verdict. Do not replace a
missing file or edit a manifest to force success.

## Questions and answers

### Can I add the documentation ZIP to the server ZIP myself?

Not to create an official release. The server packager must verify both
manifests, compatibility, and every digest before producing the archive. A
manual copy is only an uncertified local directory.

### `docs/index.html` opens. Is the release valid?

No. This only proves that one file can be opened. The archive SHA-256,
manifests, version, executables, and extracted payload must also be verified.

### The manifest says `unavailable`.

This is a local documentation proof without a compatible public server
version. Do not associate it with an invented version number.

## Reusable LLM prompt

```text
Help me verify this Ultimate Odycer archive without running it. Use only the
official releases page and the extracted VERSION, SHA256SUMS.txt,
RELEASE-MANIFEST.json, docs/index.html, and docs/docs-build-manifest.json files.
Compare the server version and compatibility.server exactly, then classify
every check as passed, failed, blocked, or unavailable. Do not invent a version
or digest, edit a manifest, request a secret, or continue after the first
failure.
```

Continue with the [acceptance checklist](local-setup-acceptance-checklist.md)
or the [advanced index](local-setup-advanced-index.md).
