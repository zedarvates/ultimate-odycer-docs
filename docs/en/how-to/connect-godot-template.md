# Connect a Godot template to the local server

Godot is the recommended client path. This page does not turn a documentation
foundation into a playable client.

> Public Godot templates are currently `under_construction`. Continue only if
> the selected repository contains a real Godot project and declares
> compatibility with your server version.

## 1. Check compatibility identifiers

Compare:

- the server archive's `VERSION`;
- compatibility declared by the template;
- PostgreSQL schema version;
- embedded documentation version;
- any selected Tools Suite modules.

A similar name or recent date is not an explicit compatibility match.

## 2. Open a copy of the template

Keep the downloaded template intact and work in a copy dedicated to your game.
Open that copy with the Godot version stated by the repository.

If the repository has no `project.godot`, stop: it remains a documentation
foundation.

## 3. Configure local addresses

Use only the mechanism documented by the template. Values must target
`localhost` for:

- login service;
- game server;
- WebAdmin, when installed.

Do not change the router or replace a local address with a general listener to
complete this tutorial.

## 4. Start the minimal path

In order:

1. healthy PostgreSQL;
2. login service;
3. game server;
4. Godot project;
5. local test account creation or use;
6. character entry into the world.

The client must never decide authoritative gold, health, speed, or another
gameplay statistic by itself.

## 5. Prove one minimal action

Expected evidence includes:

- accepted authentication;
- loaded world;
- visible test avatar;
- one authorized minimal action, such as movement;
- no fatal error in client or server logs.

A menu screen, static scene, or network mock is insufficient.

## 6. Restart

Stop the client and services cleanly, then start them again. Verify that the
expected configuration and test data persist in PostgreSQL.

Continue with the [acceptance checklist](../reference/local-setup-acceptance-checklist.md).
