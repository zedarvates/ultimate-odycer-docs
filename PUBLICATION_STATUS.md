# Publication status

Status: **public documentation repository**.

The reviewed documentation source is published at
[zedarvates/ultimate-odycer-docs](https://github.com/zedarvates/ultimate-odycer-docs).
This status applies only to this documentation repository. It does not publish
or license the proprietary server, hosted infrastructure, firmware backups,
production data, commercial components, credentials, or any running service.

## Local validation snapshot

- bilingual structure and internal links: passed;
- public-boundary pattern checks: passed;
- metric schema and estimated example checks: passed;
- `CC-BY-4.0` documentation and `MIT` tools mapping: applied and validated;
- deterministic calculator tests: 3 passed;
- SHA-256 source manifest: generated and verified;
- fresh-copy validation: passed;
- Gitleaks 8.30.0 directory scan: passed after archive-checksum verification and
  a successful synthetic-canary detection test.

Future changes must pass automated validation, secret scanning, manifest
regeneration, and fresh-copy verification before publication.

Passing repository validation proves only the structure and examples in these docs.
It does not certify a production server, an ESP32 firmware, an LLM model, a playable
client, a public network protocol, or the performance of any hardware.

Ecosystem architecture pages document public boundaries and contracts. They do not
publish proprietary Zig server source, live endpoints, or certified client/server
compatibility.
