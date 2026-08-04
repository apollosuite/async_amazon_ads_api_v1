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
    scripts = (
        # Main products
        "generate_sp.py",
        "generate_sb.py",
        "generate_sd.py",
        # Legacy & specialized v3/v4 models and clients
        "generate_sbv4_rules.py",
        "generate_sdv3_rules.py",
        "generate_spv3_rules.py",
        "generate_portfolios.py",
        "generate_profiles_models.py",
        "generate_accounts_models.py",
        # General API: models + auto-generated clients
        "generate_brandhome.py",
        "generate_brandstores.py",
    )

    for script in scripts:
        run_script(script)

    run(["uv", "run", "ruff", "check", "--fix", str(SRC), str(SCRIPTS)])
    run(["uv", "run", "black", str(SRC), str(SCRIPTS)])

    print("Done — all models regenerated and code formatted.")


if __name__ == "__main__":
    main()
