"""OAuth token refresh, validation, and caching."""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass

import httpx

from ads_api.config.token_cache import BaseTokenCache, TokenData

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TokenCredentials:
    client_id: str
    client_secret: str
    refresh_token: str
    token_url: str = "https://api.amazon.com/auth/o2/token"


class TokenManager:
    __slots__ = ("_credentials", "_cache", "_lock", "_timeout", "_access_token", "_expires_at")

    def __init__(
        self,
        credentials: TokenCredentials,
        cache: BaseTokenCache | None = None,
        timeout: float = 600.0,
    ) -> None:
        self._credentials = credentials
        self._cache = cache
        self._lock = asyncio.Lock()
        self._timeout = timeout
        self._access_token: str | None = None
        self._expires_at: float | None = None

    @property
    def access_token(self) -> str | None:
        return self._access_token

    async def get_access_token(self, force: bool = False) -> str:
        if not force and await self._is_token_valid():
            assert self._access_token is not None and self._expires_at is not None
            logger.info("Using cached access token, expires in %.0f seconds", self._expires_at - time.time())
            return self._access_token
        async with self._lock:
            if not force and await self._is_token_valid():
                assert self._access_token is not None and self._expires_at is not None
                logger.info("Using cached access token, expires in %.0f seconds", self._expires_at - time.time())
                return self._access_token
            if force:
                logger.info("Forcing token refresh")
            return await self._refresh()

    async def _is_token_valid(self) -> bool:
        if self._access_token is not None and self._expires_at is not None and time.time() < self._expires_at:
            return True
        await self._load_from_cache()
        return self._access_token is not None and self._expires_at is not None and time.time() < self._expires_at

    async def _refresh(self) -> str:
        logger.info("Refreshing access token from %s", self._credentials.token_url)
        try:
            async with httpx.AsyncClient(timeout=httpx.Timeout(self._timeout)) as client:
                resp = await client.post(
                    self._credentials.token_url,
                    data={
                        "grant_type": "refresh_token",
                        "refresh_token": self._credentials.refresh_token,
                        "client_id": self._credentials.client_id,
                        "client_secret": self._credentials.client_secret,
                    },
                )
                resp.raise_for_status()
                data = resp.json()
                self._access_token = data["access_token"]
                expires_in = data["expires_in"] if "expires_in" in data else 3600
                self._expires_at = time.time() + expires_in - 600
                logger.info("Token refreshed, expires in %d seconds", expires_in)
        except httpx.HTTPStatusError as e:
            logger.error("Token refresh failed: %s %s", e.response.status_code, e.response.text)
            raise
        except httpx.HTTPError:
            logger.exception("Token refresh request failed")
            raise
        await self._write_to_cache()
        return self._access_token

    async def _load_from_cache(self) -> None:
        if self._cache is None:
            return
        data = await self._cache.read()
        if data is None:
            logger.info("Token cache miss")
            return
        self._access_token = data.access_token
        self._expires_at = data.expires_at
        remaining = data.expires_at - time.time()
        logger.info("Loaded access token from cache, expires in %.0f seconds", remaining)

    async def _write_to_cache(self) -> None:
        if self._cache is None or self._access_token is None or self._expires_at is None:
            return
        await self._cache.write(
            TokenData(
                access_token=self._access_token,
                expires_at=self._expires_at,
            )
        )
        logger.info("Wrote access token to cache")

    async def close(self) -> None:
        """Close token manager resources, including token cache."""
        if self._cache is not None:
            await self._cache.close()
            logger.info("Closed token cache")
