# Connect a Godot template to the local server

Status: **bounded proof guide**. The public Godot starters contain real Godot projects and transport-independent networking foundations, but **live compatibility with the canonical Zig server is not proven**.

## Before starting

- Godot Classic and VR target 4.7.2, but that target remains `NOT_PROVEN` until executable receipts exist.
- Both P0 branches now provide `tools/run_p0_local_proof.py`, a fail-closed one-command orchestrator for engine + synthetic proof using one exact Godot binary.
- Historical VR networking is `LEGACY_QUARANTINED`.
- The public intent contract contains no private Zig socket, endpoint, opcode, or framing.
- A recent date or detailed document is never a substitute for an exact server baseline.

## 1. Prove the engine and synthetic fixture locally

With **Godot 4.7.2-stable** available, run from the target PR checkout:

```text
python tools/run_p0_local_proof.py --godot <path-to-godot-4.7.2>
```

The orchestrator uses the same executable for both gates and stops at the first failure. It writes local receipts below `.evidence/`, which must remain uncommitted.

For VR, all proof in this command is XR-off. Even a complete success leaves OpenXR runtime, headset/controllers and Zig interoperability unproven.

## 2. Read contracts in order

1. client architecture;
2. `network-contract.md` (`network-intent-v1`, synthetic and transport-independent);
3. `server-network-contract.md` while preserving its **unpinned / compatibility-not-validated** status;
4. the target Godot repository proof-level and compatibility-manifest files.

## 3. Do not invent the transport

The future real adapter must be derived from a named `zig-server-v2` baseline. Until exact SHA/tree/toolchain evidence is captured, do not add assumed endpoints, opcodes, or framing to the public starter.

The current adapter/fixture is socket-free and may only prove bounded client behavior under controlled synthetic inputs.

## 4. Synthetic proof boundary

The prepared fixture covers:

- offline fail-closed behavior;
- simulated connect/authentication;
- bounded movement intent;
- synthetic authoritative event;
- malformed/unsupported input;
- client-authority-field rejection;
- disconnect/reconnect/resume;
- clean close.

A successful execution remains `SYNTHETIC_FIXTURE_ONLY`.

## 5. Future live proof

`REAL_SERVER_E2E` requires:

- exact client revision;
- exact Zig SHA/tree/toolchain;
- verified transport actually present at that Zig revision;
- auth + handoff + spawn;
- authoritative movement;
- reconnect;
- negative/adversarial tests;
- named logs/artifacts.

A menu, static scene, mock, synthetic fixture or headless Godot run is insufficient for live compatibility.
