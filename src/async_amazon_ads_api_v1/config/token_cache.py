"""File-based token cache for cross-process reuse."""

from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class _TokenData:
    """Serialisable token data written to the cache file."""

    access_token: str
    expires_at: float
    refresh_token: str


class TokenCache:
    """Persistent token cache backed by a JSON file on disk.

    Uses ``sha256(client_id:refresh_token)[:16]`` as the cache key so that
    different credentials produce independent cache files.
    """

    def __init__(self, cache_dir: Path, client_id: str, refresh_token: str) -> None:
        self._cache_file = cache_dir / f"token_{_cache_key(client_id, refresh_token)}.json"

    def read(self) -> _TokenData | None:
        """Read cached token data from disk, or ``None`` if absent/invalid."""
        if not self._cache_file.exists():
            return None
        try:
            data = json.loads(self._cache_file.read_text(encoding="utf-8"))
            expires_at = data.get("expires_at")
            if expires_at is not None and data.get("access_token"):
                return _TokenData(
                    access_token=data["access_token"],
                    expires_at=expires_at,
                    refresh_token=data.get("refresh_token", ""),
                )
        except (OSError, json.JSONDecodeError, KeyError):  # fmt: skip
            pass
        return None

    def write(self, data: _TokenData) -> None:
        """Atomically write token data to the cache file (tmp + rename)."""
        self._cache_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "access_token": data.access_token,
            "expires_at": data.expires_at,
            "refresh_token": data.refresh_token,
        }
        tmp = self._cache_file.with_suffix(f".tmp.{os.getpid()}")
        try:
            tmp.write_text(json.dumps(payload), encoding="utf-8")
            tmp.chmod(0o600)
            tmp.rename(self._cache_file)
        finally:
            if tmp.exists():
                tmp.unlink(missing_ok=True)


def _cache_key(client_id: str, refresh_token: str) -> str:
    return hashlib.sha256(f"{client_id}:{refresh_token}".encode()).hexdigest()[:16]
