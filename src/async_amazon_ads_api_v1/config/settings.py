"""Core configuration — :class:`AmazonAdsConfig` as a Pydantic model."""

from __future__ import annotations

from enum import StrEnum
from pathlib import Path

from pydantic import BaseModel, PrivateAttr, model_validator

from async_amazon_ads_api_v1.config.region import ENDPOINT_MAP, Region
from async_amazon_ads_api_v1.config.token_cache import (
    BaseTokenCache,
    FileTokenCache,
    RedisTokenCache,
)
from async_amazon_ads_api_v1.config.token_manager import TokenCredentials, TokenManager


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
    timeout: float = 600.0
    max_retries: int = 3

    # ── Runtime state (excluded from serialisation / schema) ──────────
    _token_manager: TokenManager | None = PrivateAttr(None)

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

        # Create token cache if configured
        token_cache: BaseTokenCache | None = None
        if self.cache_backend == CacheBackend.REDIS:
            if not self.redis_url:
                raise ValueError("redis_url is required when cache_backend is 'redis'")
            if self.refresh_token is not None:
                token_cache = RedisTokenCache(
                    redis_url=self.redis_url,
                    client_id=self.client_id,
                    refresh_token=self.refresh_token,
                )
        elif self.token_cache_dir is not None and self.refresh_token is not None:
            token_cache = FileTokenCache(
                cache_dir=Path(self.token_cache_dir).expanduser(),
                client_id=self.client_id,
                refresh_token=self.refresh_token,
            )

        # Create token manager if we have refresh credentials
        if self.refresh_token and self.client_secret:
            credentials = TokenCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret,
                refresh_token=self.refresh_token,
                token_url=self.token_url,
            )
            self._token_manager = TokenManager(credentials=credentials, cache=token_cache, timeout=self.timeout)
        return self

    @property
    def base_url(self) -> str:
        if self.endpoints:
            return self.endpoints[self.region.value]
        return ENDPOINT_MAP[self.region.value]

    # ── Token refresh ─────────────────────────────────────────────────

    async def refresh_access_token(self) -> str:
        """Exchange the refresh token for a new access token.

        Delegates to :class:`TokenManager` for the actual refresh logic.

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
        if self._token_manager is None:
            raise RuntimeError("refresh_token and client_secret must be set to refresh the access token")
        token = await self._token_manager.get_access_token()
        self.access_token = token
        return token
