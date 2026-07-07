"""Token manager — handles token refresh, validation, and caching."""

from __future__ import annotations

import asyncio
import logging
import time
from dataclasses import dataclass

import httpx

from async_amazon_ads_api_v1.config.token_cache import BaseTokenCache, _TokenData

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TokenCredentials:
    """Immutable token credentials required for refresh."""

    client_id: str
    client_secret: str
    refresh_token: str
    token_url: str = "https://api.amazon.com/auth/o2/token"


class TokenManager:
    """Manages OAuth token lifecycle — refresh, validation, and caching.

    Parameters
    ----------
    credentials : TokenCredentials
        Immutable credentials for token refresh.
    cache : BaseTokenCache | None
        Optional token cache backend (file or Redis).
    """

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
        """Current access token, or ``None`` if not yet refreshed."""
        return self._access_token

    async def get_access_token(self) -> str:
        """Return a valid access token, refreshing if necessary.

        Returns
        -------
        str
            A valid access token.

        Raises
        ------
        httpx.HTTPError
            If the token endpoint request fails.
        """
        if await self._is_token_valid():
            return self._access_token  # type: ignore[return-value]
        async with self._lock:
            if await self._is_token_valid():
                return self._access_token  # type: ignore[return-value]
            return await self._refresh()

    async def _is_token_valid(self) -> bool:
        """Return ``True`` if a cached access token is still within its expiry window."""
        if self._access_token is not None and self._expires_at is not None:
            if time.time() < self._expires_at:
                return True
        await self._load_from_cache()
        return self._access_token is not None and self._expires_at is not None and time.time() < self._expires_at

    async def _refresh(self) -> str:
        """Exchange the refresh token for a new access token."""
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
            expires_in = data.get("expires_in", 3600)
            self._expires_at = time.time() + expires_in - 60
            logger.info("Token refreshed, expires in %d seconds", expires_in)
        await self._write_to_cache()
        return self._access_token

    async def _load_from_cache(self) -> None:
        """Load token data from cache if available."""
        if self._cache is None:
            return
        data = await self._cache.read()
        if data is not None:
            self._access_token = data.access_token
            self._expires_at = data.expires_at

    async def _write_to_cache(self) -> None:
        """Write current token data to cache."""
        if self._cache is None or self._access_token is None or self._expires_at is None:
            return
        await self._cache.write(
            _TokenData(
                access_token=self._access_token,
                expires_at=self._expires_at,
                refresh_token=self._credentials.refresh_token,
            )
        )
