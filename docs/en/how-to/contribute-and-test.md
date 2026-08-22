# Contribute to and test the public ecosystem

Use this guide to add or test public Ultimate Odycer material without
claiming a playable MMO, a published protocol, or production compatibility.

## 1. Choose the right repository

| You want to... | Go here | Do not... |
|---|---|---|
| Fix or extend documentation | [ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs) | copy proprietary server docs |
| Add or version a JSON template | [ultod-json-template-registry](https://github.com/zedarvates/ultod-json-template-registry) | invent compatibility |
| Discuss a future client shell | one of the four documentation-only client starters | import existing game client code |
| Report a public bug or idea | [ultimate-odycer-feedback](https://github.com/zedarvates/ultimate-odycer-feedback) | paste secrets, logs, or player data |

Keep French and English pairs together in this docs repository. Follow each
target repository's license, scope, and publication checklist.

## 2. Test only what is public

A complete public check looks like this:

```text
docs hub
  validate_docs.py + unit tests + fresh-copy check
JSON registry
  pin version + SHA-256 + empty compatibility unless proven
client starter
  read SCOPE, ROADMAP, and server-compatibility; no hidden project
home-lab NPC path
  synthetic or measured capacity, loopback inference, fail-closed fallback
feedback tracker
  public issue with synthetic reproduction only
```

Passing docs validation proves documentation structure. It does not prove a
server, a headset, a protocol, or CCU.

## 3. Run the docs checks

From a local copy of this repository:

```powershell
rtk python scripts/validate_docs.py
rtk python -m unittest discover -s tests -v
rtk python scripts/fresh_copy_check.py
```

Expected: `validation: ok`, unit tests passed, and `fresh-copy: ok`.

## 4. Test a template without activating a world

1. Resolve one catalogue entry.
2. Record version and SHA-256.
3. Reject automatic runtime download.
4. Leave `compatibility` empty unless a named consumer, version, date, and
   evidence exist.
5. Treat the snapshot as data, not a grant of gold, items, or access.

Details: [use JSON templates](use-json-templates.md).

## 5. Test a client starter without inventing a network

Read the starter `SCOPE.md` and server-compatibility page. If alignment is
blocked, the allowed tests are documentation review, license/scope checks,
and local non-networked presentation experiments. A synthetic loopback
fixture is the first allowed network proof, and only after a public protocol
gate exists.

See [client architecture](../explanation/client-architecture.md).

## 6. Fail closed

Mark missing evidence `unavailable`. Do not invent opcodes, production URLs,
player identities, or certified compatibility. Do not expose a local LLM or
docs helper beyond loopback unless a private-LAN design is explicit.

## Related pages

- [Ecosystem overview](../explanation/ecosystem-overview.md)
- [Start a project](../tutorials/start-an-ultimate-odycer-project.md)
- [Operate a home lab](operate-a-home-lab.md)
- [CONTRIBUTING.md](../../../CONTRIBUTING.md)
