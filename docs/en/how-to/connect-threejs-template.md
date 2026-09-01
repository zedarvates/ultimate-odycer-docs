# Connect the Three.js 2.5D template to a local server

Status: **synthetic fixture validated; live Zig compatibility not proven**.

The Three.js client now has a fail-closed `NetworkClient` and a green synthetic proof gate. This evidence remains `SYNTHETIC_FIXTURE_ONLY`.

## Transport reality

Current server documentation describes login/game as **raw binary TCP**. That description still needs to be tied to an exact Zig baseline before it can be called a verified canonical contract.

A browser must therefore not assume that a player WebSocket endpoint exists. Only two paths are acceptable before real E2E proof:

1. a documented and audited WebSocket ↔ TCP bridge/gateway;
2. a separately implemented and proven official WebSocket endpoint.

The WebAdmin WebSocket is not a gameplay channel.

## What is already proven

The synthetic fixture covers, among other things:

- connection lifecycle;
- synthetic handshake/auth;
- bounded movement;
- invalid and oversized frames;
- NaN/Infinity/overflow handling;
- fail-closed state;
- synthetic authoritative position updates.

This does not prove Zig TCP, a bridge, a player endpoint, or production authentication.

## Next proof

Before `REAL_SERVER_E2E`, capture:

- exact `zig-server-v2` SHA/tree/toolchain;
- transport contract actually present at that revision;
- exact bridge/endpoint if browser-based;
- exact Three.js client revision.

The minimal live scenario is: auth → realm/handoff → spawn → movement intent → authoritative update → second client observes → disconnect/reconnect, plus negative tests.

Never copy documented opcodes/framing into the public client as if they were verified until the P0 Zig baseline is pinned.
