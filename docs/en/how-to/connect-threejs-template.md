# Connecting the Three.js 2.5D template to a local server

Status: **how-to for future work; no browser compatibility exists today**.

This page extends the general [server network contract](../reference/server-network-contract.md)
with what it means specifically for a web client. It does not turn the
documentation template into a playable client.

## Why the template cannot connect today

- The canonical login and game services speak raw binary TCP. Browsers can
  only open WebSocket or HTTP connections, so direct connection is impossible.
- The Three.js template scope requires documented server-authoritative
  contracts before any networking code. That evidence now partially exists in
  the contract reference, but the transport gap remains.
- WebAdmin WebSocket traffic is administrative telemetry, not a game channel;
  reusing it for gameplay would violate server authority boundaries.

## Two acceptable paths forward

1. A documented bridge/gateway process: a small local proxy that terminates
   WebSocket from the browser and speaks the binary TCP protocol to the
   server. It must be published with its own security review, framing rules,
   and loopback fixture.
2. An official WebSocket endpoint added to the canonical server behind its
   existing handshake, version negotiation, and JWT admission rules, with the
   same authority guarantees.

A third path, reimplementing protocol logic inside an unreviewed web page, is
rejected by both projects publication rules.

## What a compliant web client must implement once a path exists

- Frame encoding and decoding exactly as specified in the contract reference,
  including big-endian integers and length-prefixed envelopes.
- The session flow: handshake with JWT token, character list/select, world
  spawn select with nonce, then position updates at a bounded rate.
- Binary replication batch parsing (opcode 80) with interpolation between
  batches and no client-side authority.
- TLS expectations matching the server configuration; plain connections fail
  when TLS is required.
- Reconnection through the one-shot session resume token when provided.

## Local test discipline

When a bridge or endpoint lands, validate on loopback first:

1. Start the local server stack from the [Windows install guide](install-local-server-windows.md).
2. Confirm the login service answers a handshake on its configured port.
3. Complete account creation, login, character create/select, and one world
   spawn through the web client.
4. Record versions of server, gateway, and browser runtime in a compatibility
   matrix entry, then update the templates SERVER-COMPATIBILITY decision.

Until step 3 has been performed with named artifacts, this page remains a plan,
not a capability statement.
