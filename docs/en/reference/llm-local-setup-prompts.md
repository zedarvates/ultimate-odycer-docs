# LLM prompts for continuing local setup

Replace only values inside braces. Never paste a password, JWT secret, private
key, database dump, or player data.

Every prompt keeps the same rules: read current state, invent nothing, preserve
data, advance in small steps, and request confirmation before sensitive action.

## 1. Turn an idea into a project brief

```text
Accompany me as a technical beginner preparing an Ultimate Odycer project. Ask
one question at a time about genre, period, gameplay loop, player count,
movement, persistence, platforms, and first-prototype scale. At the end, produce
a short brief separating facts, decisions, and unavailable elements. Do not
select an engine or topology before receiving my answers.
```

## 2. Recommend an engine, template, and topology

```text
First read the public local-setup-catalog and my brief below. Recommend Godot by
default unless an explicit constraint says otherwise. Compare only listed
templates and preserve their exact status. Choose among flat_map, planet,
mega_planet, and solar_system, favoring the smallest prototype able to prove the
gameplay loop. Explain the trade-off and ask for my agreement before fixing the
decision.

Brief: {SECRET_FREE_BRIEF}
```

## 3. Check Windows prerequisites

```text
Guide me with one non-destructive command at a time to check Windows, WSL,
Docker, and Docker Compose. For each command, state the expected result and wait
for my output. Do not propose a paid installation or automatic network
exposure. Never ask for a secret.
```

## 4. Verify a release without running it

```text
Help me verify an Ultimate Odycer archive without running it. Start from the
official page https://www.ultimateodycer.com/releases/ and stop if it lists no
release. Compare filename, platform, size, and SHA-256. Do not invent a URL,
version, digest, or command for an absent file. Here is only the public metadata
I copied: {SECRET_FREE_RELEASE_METADATA}
```

## 5. Diagnose Docker and PostgreSQL

```text
Analyze this local diagnostic without changing or deleting data. Start with
versions, Compose state, PostgreSQL health, and secret-free logs. Distinguish a
persistent volume from a backup. Forbid shutdown with volume removal, prune,
DROP of the active database, and password display. Propose one check at a time
with its expected result.

Command and error: {SECRET_FREE_ERROR}
```

## 6. Connect Godot

```text
Before any change, verify that the repository contains project.godot and states
explicit compatibility with my server version. Use only configuration files
documented by the template and localhost. Do not change the router, firewall,
or server authority. Help me prove login, world entry, visible avatar, and one
minimal action, one step at a time.

Public versions: {SECRET_FREE_VERSIONS}
```

## 7. Analyze a failed acceptance item

```text
This Ultimate Odycer acceptance item failed: {ITEM_AND_NEGATIVE_EVIDENCE}

Classify the result as failed, blocked, unavailable, or partial. Identify the
first missing proof and propose a non-destructive check. Do not turn a mock,
build, or valid documentation into runtime proof.
```

## 8. Plan the next step after setup

```text
Here is my secret-free local setup evidence: {EVIDENCE}
Here is my next objective: {OBJECTIVE}

First verify which gates are actually green. Propose the smallest next testable
milestone, likely files, observable result, and limitations. Preserve existing
work. Ask for confirmation before deletion, network exposure, purchase,
deployment, or publication.
```

## 9. Convert a creative need into a Kanboard card

```text
Read the creative production handbook and the public creative tools catalog.
Turn this need into a secret-free Kanboard card: {CREATIVE_NEED}. Fill in the
observable objective, authorized inputs, selected tool and alternatives, formats
and conversion, licensing/provenance/privacy, acceptance criteria, expected
evidence, LLM prompt, and current blocker. Check verified_on and official links.
Do not quote exact prices, upload files, or create or modify a Kanboard task.
```

## 10. Route a card through Botte Secrète

```text
Analyze this secret-free Kanboard card: {SECRET_FREE_CARD}. Propose a bounded
route among deterministic tools, a local LLM, and cloud services. Prefer local
and free/open-source tools. For cloud use, require review of privacy, retention,
training terms, and output rights. Return only a proposal and checks to run; do
not execute tools, mutate Kanboard, or move the card.
```

## 11. Review evidence before Done

```text
Compare this card's acceptance criteria with its evidence:
{SECRET_FREE_CARD_AND_EVIDENCE}. Classify every criterion as passed, failed,
blocked, partial, or unavailable. Reject proxy previews as runtime proof and
preserve negative evidence. Recommend Done only when all mandatory criteria are
proven. Do not mutate Kanboard automatically.
```

## Expected behavior from a good LLM

Good assistance:

- cites the file or output used;
- marks what is observed, estimated, decided, or unavailable;
- does not request secrets;
- checks `verified_on`, the pricing model, and official link without quoting
  exact prices;
- does not upload confidential assets to cloud services;
- does not mutate Kanboard automatically;
- proposes a reversible step;
- waits for the result before the next step;
- reports a blocker honestly.
