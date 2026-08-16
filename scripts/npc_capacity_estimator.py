# SPDX-License-Identifier: MIT

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass


class CapacityError(ValueError):
    """Raised when a capacity scenario is not physically meaningful."""


@dataclass(frozen=True)
class CapacityInput:
    reply_seconds: float
    npc_interval_seconds: float
    utilization: float = 0.5
    streams: int = 1
    basis: str = "scenario"

    def validate(self) -> None:
        if not math.isfinite(self.reply_seconds) or self.reply_seconds <= 0:
            raise CapacityError("reply_seconds must be finite and greater than zero")
        if not math.isfinite(self.npc_interval_seconds) or self.npc_interval_seconds <= 0:
            raise CapacityError(
                "npc_interval_seconds must be finite and greater than zero"
            )
        if not math.isfinite(self.utilization) or not 0 < self.utilization <= 1:
            raise CapacityError("utilization must be greater than zero and at most one")
        if self.streams <= 0:
            raise CapacityError("streams must be greater than zero")
        if self.basis not in {"scenario", "measured"}:
            raise CapacityError("basis must be scenario or measured")


def estimate_capacity(inputs: CapacityInput) -> dict[str, object]:
    inputs.validate()
    raw_replies_per_minute = inputs.streams * 60.0 / inputs.reply_seconds
    planned_replies_per_minute = raw_replies_per_minute * inputs.utilization
    active_npcs = planned_replies_per_minute * inputs.npc_interval_seconds / 60.0

    return {
        "basis": inputs.basis,
        "inputs": asdict(inputs),
        "raw_replies_per_minute": round(raw_replies_per_minute, 3),
        "planned_replies_per_minute": round(planned_replies_per_minute, 3),
        "supported_active_npcs": math.floor(active_npcs),
        "supported_active_npcs_theoretical": round(active_npcs, 3),
        "queue_policy": "serialize_per_stream",
        "note": (
            "Scheduling estimate only; not a dialogue-quality or simultaneous-NPC proof."
        ),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert short-reply latency into active-NPC scheduling capacity."
    )
    parser.add_argument("--reply-seconds", required=True, type=float)
    parser.add_argument("--npc-interval-seconds", required=True, type=float)
    parser.add_argument("--utilization", type=float, default=0.5)
    parser.add_argument("--streams", type=int, default=1)
    parser.add_argument(
        "--basis", choices=("scenario", "measured"), default="scenario"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    arguments = parser.parse_args(argv)
    inputs = CapacityInput(
        reply_seconds=arguments.reply_seconds,
        npc_interval_seconds=arguments.npc_interval_seconds,
        utilization=arguments.utilization,
        streams=arguments.streams,
        basis=arguments.basis,
    )
    try:
        result = estimate_capacity(inputs)
    except CapacityError as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
