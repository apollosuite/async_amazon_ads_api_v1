"""Generate all Pydantic models (and general API clients) and format the codebase.

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


def run_script(script: str, *args: str) -> None:
    run([sys.executable, str(SCRIPTS / script), *args])


def main() -> None:
    output_base = SRC / "async_amazon_ads_api_v1" / "models"

    for product in ("sp", "sb", "sd"):
        run_script(
            "generate_models.py",
            "--product",
            product,
            "--output-dir",
            str(output_base / product),
        )

    # Legacy & specialized v3/v4 models and clients
    for script in (
        "generate_sbv4_rules.py",
        "generate_sdv3_rules.py",
        "generate_sp_budget_rules.py",
        "generate_portfolios.py",
        "generate_legacy_accounts_models.py",
        "generate_legacy_profiles_models.py",
    ):
        run_script(script)

    # General API: models + auto-generated clients
    for script in ("generate_brandhome.py", "generate_brandstores.py"):
        run_script(script)

    run(["uv", "run", "ruff", "check", "--fix", str(SRC), str(SCRIPTS)])
    run(["uv", "run", "black", str(SRC), str(SCRIPTS)])

    print("Done — all models regenerated and code formatted.")


if __name__ == "__main__":
    main()
