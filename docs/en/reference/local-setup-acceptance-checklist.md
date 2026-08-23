# Local setup acceptance checklist

Check an item only when you hold the stated evidence. Use `not applicable`,
`blocked`, or `unavailable` instead of inventing success.

## Project

- [ ] The brief describes the gameplay loop, players, and scale.
- [ ] Engine and template are named with their real status.
- [ ] The selected topology is justified.
- [ ] The hardware profile is labeled `estimated` or `observed`.

## Release

- [ ] The official page actually listed the archive.
- [ ] The downloaded SHA-256 matches exactly.
- [ ] Server version matches the embedded documentation.
- [ ] Optional modules belong to the same compatibility family.

## PostgreSQL

- [ ] PostgreSQL is healthy.
- [ ] The named volume survives a restart.
- [ ] Logs confirm PostgreSQL with no active SQLite fallback.
- [ ] A dump exists outside the Docker volume.
- [ ] The dump SHA-256 matches.
- [ ] Restoration into the verification database succeeded.

## Server and network

- [ ] Login and game services start from the verified archive.
- [ ] The health check reports a healthy state.
- [ ] Local WebAdmin responds when installed.
- [ ] No Internet port was opened automatically.
- [ ] Secrets appear in neither logs nor LLM prompts.

## Godot

- [ ] The repository contains a real compatible Godot project.
- [ ] The client reaches local login and game services.
- [ ] A test character enters the world.
- [ ] The avatar is visible and performs one authorized minimal action.
- [ ] Client and server logs contain no fatal error.

## Restart

- [ ] Services stop cleanly.
- [ ] Configuration survives restart.
- [ ] Expected test data persists in PostgreSQL.

## Verdict

- **Passed:** every applicable item is proven.
- **Partial:** the local server works, but an optional component is absent.
- **Blocked:** a release, playable template, or required dependency is absent.
- **Failed:** a required check produced negative evidence.

Validation of this documentation does not check any runtime item for you.
