# Connect a Godot template to the local server

Status: **bounded proof guide**. The public Godot starters now contain real Godot projects and transport-independent networking foundations, but **live compatibility with the canonical Zig server is not proven**.

## Before starting

- Godot Classic and VR target 4.7.2, but that target remains `NOT_PROVEN` until the local validator produces its JSON receipt.
- Historical VR networking is `LEGACY_QUARANTINED`.
- The public intent contract contains no private Zig socket, endpoint, opcode, or framing.
- A recent date or detailed document is never a substitute for an exact server baseline.

## 1. Prove the engine before networking

Run the repository validator with **Godot 4.7.2-stable** and retain the local `.evidence/` receipt. For VR, a headless run with `--xr-mode off` proves engine loading only; it does not prove OpenXR, headset runtime, or networking.

Stop if engine proof fails.

## 2. Read contracts in order

1. client architecture;
2. `network-contract.md` (`network-intent-v1`, synthetic and transport-independent);
3. `server-network-contract.md` while preserving its **compatibility-not-validated** status;
4. the target Godot repository proof-level and compatibility-manifest files.

## 3. Do not invent the transport

The future real adapter must be derived from a named `zig-server-v2` baseline. Until exact SHA/tree/toolchain evidence is captured, do not add assumed endpoints, opcodes, or framing to the public starter.

The current abstract adapter may only model:

```text
disconnected -> connecting -> authenticating -> online
```

without a real socket.

## 4. First allowed synthetic proof

The next acceptable step is a local synthetic fixture covering:

- simulated handshake;
- simulated authentication;
- bounded movement intent;
- inbound authoritative event;
- malformed payload;
- disconnect/reconnect;
- rejection of client-authority fields.

This evidence must remain `SYNTHETIC_FIXTURE_ONLY`.

## 5. Future live proof

`REAL_SERVER_E2E` requires:

- exact client revision;
- exact Zig SHA/tree/toolchain;
- auth + handoff + spawn;
- authoritative movement;
- reconnect;
- negative tests;
- named logs/artifacts.

A menu, static scene, mock, or headless Godot run is insufficient.
