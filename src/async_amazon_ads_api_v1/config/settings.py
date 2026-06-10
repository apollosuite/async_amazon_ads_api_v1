"""Core configuration — :class:`AmazonAdsConfig` as a Pydantic model."""

from __future__ import annotations

import asyncio
import time
from enum import StrEnum
from pathlib import Path

import httpx
from pydantic import BaseModel, PrivateAttr, model_validator

from async_amazon_ads_api_v1.config.region import ENDPOINT_MAP, Region
from async_amazon_ads_api_v1.config.token_cache import (
    BaseTokenCache,
    FileTokenCache,
    RedisTokenCache,
    _TokenData,
)


class CacheBackend(StrEnum):
    """Supported token cache backends."""

    FILE = "file"
    REDIS = "redis"


class AmazonAdsConfig(BaseModel):
    """Holds authentication and client-level settings.

    Pydantic-powered configuration with:

    - **Field validation** — types, ranges, and cross-field invariants are
      checked automatically via ``model_validator``.
    - **Computed ``base_url``** — derived from *region* and optional
      *endpoints* overrides.
    - **Optional token cache** — when *token_cache_dir* is set (file) or
      *cache_backend* is ``redis``, the access token is persisted across
      process invocations.
    """

    model_config = {"arbitrary_types_allowed": True}

    # ── Auth ──────────────────────────────────────────────────────────
    client_id: str
    access_token: str | None = None
    refresh_token: str | None = None
    client_secret: str | None = None
    profile_id: str | None = None

    # ── Endpoint ──────────────────────────────────────────────────────
    region: Region = Region.NA
    endpoints: dict[str, str] | None = None

    # ── Token ─────────────────────────────────────────────────────────
    token_url: str = "https://api.amazon.com/auth/o2/token"
    token_cache_dir: str | None = None
    cache_backend: CacheBackend = CacheBackend.FILE
    redis_url: str | None = None

    # ── Behaviour ─────────────────────────────────────────────────────
    timeout: float = 60.0
    max_retries: int = 3
    raw_response: bool = False

    # ── Runtime state (excluded from serialisation / schema) ──────────
    _token_cache: BaseTokenCache | None = PrivateAttr(None)
    _token_refresh_lock: asyncio.Lock = PrivateAttr(default_factory=asyncio.Lock)
    _token_expires_at: float | None = PrivateAttr(None)

    @model_validator(mode="after")
    def _validate_and_init(self) -> AmazonAdsConfig:
        if not self.client_id:
            raise ValueError("client_id is required and cannot be empty")
        if not self.access_token and not (self.refresh_token and self.client_secret):
            raise ValueError("Either access_token or both refresh_token and client_secret must be provided")
        if self.timeout <= 0:
            raise ValueError("timeout must be a positive number")
        if self.max_retries < 0:
            raise ValueError("max_retries cannot be negative")

        if self.cache_backend == CacheBackend.REDIS:
            if not self.redis_url:
                raise ValueError("redis_url is required when cache_backend is 'redis'")
            if self.refresh_token is not None:
                self._token_cache = RedisTokenCache(
                    redis_url=self.redis_url,
                    client_id=self.client_id,
                    refresh_token=self.refresh_token,
                )
        elif self.token_cache_dir is not None and self.refresh_token is not None:
            self._token_cache = FileTokenCache(
                cache_dir=Path(self.token_cache_dir).expanduser(),
                client_id=self.client_id,
                refresh_token=self.refresh_token,
            )
        return self

    @property
    def base_url(self) -> str:
        if self.endpoints:
            return self.endpoints[self.region.value]
        return ENDPOINT_MAP[self.region.value]

    # ── Token refresh ─────────────────────────────────────────────────

    async def refresh_access_token(self) -> str:
        """Exchange the refresh token for a new access token.

        Uses ``refresh_token`` + ``client_secret`` to call the Amazon LWA
        token endpoint and updates ``access_token`` in-place.

        The token is cached in memory for the lifetime of this object, and
        optionally persisted when a cache backend is configured so that
        subsequent invocations can reuse it without an HTTP call.

        Returns
        -------
        str
            The new access token.

        Raises
        ------
        RuntimeError
            If ``refresh_token`` or ``client_secret`` are not configured.
        httpx.HTTPError
            If the token endpoint request fails.
        """
        if not self.refresh_token or not self.client_secret:
            raise RuntimeError("refresh_token and client_secret must be set to refresh the access token")
        if await self._is_token_valid():
            return self.access_token  # type: ignore[return-value]
        async with self._token_refresh_lock:
            if await self._is_token_valid():
                return self.access_token  # type: ignore[return-value]
            async with httpx.AsyncClient() as client:
                resp = await client.post(
                    self.token_url,
                    data={
                        "grant_type": "refresh_token",
                        "refresh_token": self.refresh_token,
                        "client_id": self.client_id,
                        "client_secret": self.client_secret,
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                self.access_token = data["access_token"]
                expires_in = data.get("expires_in", 3600)
                self._token_expires_at = time.time() + expires_in - 60
                if "refresh_token" in data:
                    self.refresh_token = data["refresh_token"]
            await self._write_token_cache()
        return self.access_token

    async def _is_token_valid(self) -> bool:
        """Return ``True`` if a cached access token is still within its expiry window."""
        if self.access_token is not None and self._token_expires_at is not None:
            if time.time() < self._token_expires_at:
                return True
        await self._load_token_cache()
        return (
            self.access_token is not None
            and self._token_expires_at is not None
            and time.time() < self._token_expires_at
        )

    async def _load_token_cache(self) -> None:
        if self._token_cache is None:
            return
        data = await self._token_cache.read()
        if data is not None:
            self.access_token = data.access_token
            self._token_expires_at = data.expires_at
            self.refresh_token = data.refresh_token

    async def _write_token_cache(self) -> None:
        if self._token_cache is None or self.access_token is None or self._token_expires_at is None:
            return
        await self._token_cache.write(
            _TokenData(
                access_token=self.access_token,
                expires_at=self._token_expires_at,
                refresh_token=self.refresh_token or "",
            )
        )
