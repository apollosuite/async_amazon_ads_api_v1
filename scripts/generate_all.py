"""Generate Pydantic models for all three product APIs and format the codebase.

Usage:
    uv run python scripts/generate_all.py
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT = Path(__file__).parent.parent
SRC = PROJECT / "src"
SCRIPTS = PROJECT / "scripts"


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"> {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd or PROJECT, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    if result.stdout:
        print(result.stdout)


def main() -> None:
    products = ["sp", "sb", "sd"]
    output_base = SRC / "async_amazon_ads_api_v1" / "models"

    for product in products:
        run(
            [
                sys.executable,
                str(SCRIPTS / "generate_models.py"),
                "--product",
                product,
                "--output-dir",
                str(output_base / product),
            ]
        )

    run(["uv", "run", "ruff", "check", "--fix", str(SRC)])
    run(["uv", "run", "black", str(SRC), str(SCRIPTS)])

    print("Done — all models regenerated and code formatted.")


if __name__ == "__main__":
    main()
