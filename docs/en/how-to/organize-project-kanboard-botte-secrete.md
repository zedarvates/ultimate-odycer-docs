# Organize the project with Kanboard and Botte Secrète

Kanboard keeps work visible. Botte Secrète prepares and routes LLM-assisted
tasks. Neither publishes automatically to the server.

## Recommended board

Columns: `Ideas → Design → Ready → In progress → Review → Validation → Blocked
→ Done`.

Swimlanes: world/maps, Godot client, server, Tools Suite, 3D/materials,
characters/animation, audio, UI/VFX/video, documentation/releases.

## Card template

```markdown
## Observable objective
## Authorized inputs
## Selected tool and alternatives
## Formats and conversion
## Licence, provenance, and privacy
## Acceptance criteria
## Expected evidence
## Secret-free LLM prompt
## Current blocker
```

Attach links and hashes instead of secrets or database dumps. Back up the
Kanboard database and attachments. Plug-ins are optional: the official directory
does not guarantee centralized code review.

## Route through Botte Secrète

```text
Kanboard card
→ Botte Secrète policy and capabilities
→ bounded prompt
→ deterministic tool, local LLM, or cloud
→ validation and evidence
→ human moves the card
```

Botte Secrète can reduce context/logs, select effort, discover skills/tools,
monitor budget, and run checkups. Local output still requires verification.

## Kanboard API

No automatic mutation by default. A future integration starts read-only, uses
HTTPS outside local deployment, stores tokens outside prompts, prefers the user
API with permissions, is idempotent, and requests confirmation before task
creation or movement. The application API exposes all procedures without
project permission checks and is not the default.

## Routing prompt

```text
Using this secret-free Kanboard card, classify the task as deterministic tool,
local LLM, or cloud reasoning. Reduce it to the smallest testable result. List
inputs, outputs, evidence, and risks. Do not mutate Kanboard. Ask before upload,
purchase, deletion, network exposure, deployment, or publication.
```
