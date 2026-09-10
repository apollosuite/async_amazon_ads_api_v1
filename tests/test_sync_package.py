from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def test_sync_package_isolated_suite() -> None:
    """Run the synchronous package test suite in a clean, isolated Python subprocess.

    Because both packages share the import name `ads_api`, running them in
    separate processes prevents module cache collisions in sys.modules.
    """
    project_root = Path(__file__).resolve().parents[1]
    sync_src = str(project_root / "packages" / "sync" / "src")
    sync_tests = str(project_root / "tests" / "sync")

    cmd = [sys.executable, "-m", "pytest", sync_tests]
    env = dict(os.environ)
    env["TESTING_SYNC"] = "1"
    env["PYTHONPATH"] = sync_src
    env["NO_PROXY"] = "localhost,127.0.0.1"
    env["no_proxy"] = "localhost,127.0.0.1"
    env["UV_CACHE_DIR"] = "/tmp/uv_cache"

    res = subprocess.run(cmd, env=env, cwd=project_root, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout)
        print(res.stderr, file=sys.stderr)
    assert res.returncode == 0, f"Sync package tests failed:\n{res.stdout}\n{res.stderr}"
