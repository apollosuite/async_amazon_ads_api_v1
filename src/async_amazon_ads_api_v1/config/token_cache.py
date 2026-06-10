"""Token cache implementations — file-based and Redis-backed."""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from redis.asyncio import Redis  # type: ignore[import-not-found]

# Global Redis client pool keyed by URL
_redis_clients: dict[str, Redis] = {}


def _get_redis_client(redis_url: str) -> Redis:
    """Return a shared async Redis client for the given URL."""
    if redis_url not in _redis_clients:
        try:
            from redis.asyncio import Redis
        except ImportError:
            raise ImportError(
                "Redis support requires the 'redis' extra: "
                "pip install async-amazon-ads-api-v1[redis]"
            ) from None
        _redis_clients[redis_url] = Redis.from_url(redis_url, decode_responses=True)
    return _redis_clients[redis_url]


async def close_all_redis() -> None:
    """Close all cached Redis connections. Call on application shutdown."""
    for client in _redis_clients.values():
        await client.aclose()
    _redis_clients.clear()


@dataclass
class _TokenData:
    """Serialisable token data written to the cache."""

    access_token: str
    expires_at: float
    refresh_token: str


class BaseTokenCache(ABC):
    """Abstract base class for token cache implementations."""

    @abstractmethod
    async def read(self) -> _TokenData | None:
        """Read cached token data, or ``None`` if absent/invalid."""

    @abstractmethod
    async def write(self, data: _TokenData) -> None:
        """Write token data to the cache."""


class FileTokenCache(BaseTokenCache):
    """Persistent token cache backed by a JSON file on disk.

    Uses ``sha256(client_id:refresh_token)[:16]`` as the cache key so that
    different credentials produce independent cache files.

    File I/O is offloaded to a thread pool to avoid blocking the event loop.
    """

    def __init__(self, cache_dir: Path, client_id: str, refresh_token: str) -> None:
        self._cache_file = cache_dir / f"token_{_cache_key(client_id, refresh_token)}.json"

    async def read(self) -> _TokenData | None:
        """Read cached token data from disk, or ``None`` if absent/invalid."""
        return await asyncio.to_thread(self._read_sync)

    async def write(self, data: _TokenData) -> None:
        """Atomically write token data to the cache file (tmp + rename)."""
        await asyncio.to_thread(self._write_sync, data)

    def _read_sync(self) -> _TokenData | None:
        if not self._cache_file.exists():
            return None
        try:
            raw = json.loads(self._cache_file.read_text(encoding="utf-8"))
            expires_at = raw.get("expires_at")
            if expires_at is not None and raw.get("access_token"):
                return _TokenData(
                    access_token=raw["access_token"],
                    expires_at=expires_at,
                    refresh_token=raw.get("refresh_token", ""),
                )
        except (OSError, json.JSONDecodeError, KeyError):
            pass
        return None

    def _write_sync(self, data: _TokenData) -> None:
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


class RedisTokenCache(BaseTokenCache):
    """Token cache backed by Redis.

    Requires the ``redis`` optional dependency::

        pip install async-amazon-ads-api-v1[redis]

    Redis clients are shared globally per URL. Use :func:`close_all_redis`
    to close all connections on application shutdown.

    Parameters
    ----------
    redis_url : str
        Redis connection URL (e.g. ``redis://localhost:6379/0``).
    client_id : str
        Amazon Ads client ID.
    refresh_token : str
        OAuth refresh token.
    key_prefix : str
        Redis key prefix. Defaults to ``amazon_ads:token:``.
    """

    def __init__(
        self,
        redis_url: str,
        client_id: str,
        refresh_token: str,
        key_prefix: str = "amazon_ads:token:",
    ) -> None:
        self._client = _get_redis_client(redis_url)
        self._key = f"{key_prefix}{_cache_key(client_id, refresh_token)}"

    async def read(self) -> _TokenData | None:
        """Read cached token data from Redis, or ``None`` if absent/expired."""
        raw = await self._client.get(self._key)
        if raw is None:
            return None
        try:
            data = json.loads(raw)
            expires_at = data.get("expires_at")
            if expires_at is not None and data.get("access_token"):
                return _TokenData(
                    access_token=data["access_token"],
                    expires_at=expires_at,
                    refresh_token=data.get("refresh_token", ""),
                )
        except (json.JSONDecodeError, KeyError):
            pass
        return None

    async def write(self, data: _TokenData) -> None:
        """Write token data to Redis with TTL based on ``expires_at``."""
        payload = {
            "access_token": data.access_token,
            "expires_at": data.expires_at,
            "refresh_token": data.refresh_token,
        }
        ttl = max(0, int(data.expires_at - time.time()))
        if ttl > 0:
            await self._client.set(self._key, json.dumps(payload), ex=ttl)
        else:
            await self._client.delete(self._key)


def _cache_key(client_id: str, refresh_token: str) -> str:
    return hashlib.sha256(f"{client_id}:{refresh_token}".encode()).hexdigest()[:16]
