# SPDX-License-Identifier: MIT

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "MANIFEST.sha256"
EXCLUDED_PARTS = {
    ".git",
    ".worktrees",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "build",
    "dist",
}


def included_files() -> list[Path]:
    return sorted(
        (
            path
            for path in ROOT.rglob("*")
            if path.is_file()
            and path != MANIFEST
            and not any(
                part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts
            )
        ),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )


def build_manifest() -> str:
    lines = []
    for path in included_files():
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    return "\n".join(lines) + "\n"


def main() -> int:
    MANIFEST.write_text(build_manifest(), encoding="utf-8", newline="\n")
    print(f"manifest: wrote {len(included_files())} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
