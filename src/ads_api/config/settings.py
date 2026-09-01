"""Client configuration."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from pydantic import BaseModel, PrivateAttr, model_validator

from ads_api.config.region import ENDPOINT_MAP, Region
from ads_api.config.token_cache import BaseTokenCache, FileTokenCache, RedisTokenCache
from ads_api.config.token_manager import TokenCredentials, TokenManager


class AmazonAdsConfig(BaseModel):
    """Authentication and client-level settings."""

    model_config = {"arbitrary_types_allowed": True}

    client_id: str
    access_token: str | None = None
    refresh_token: str | None = None
    client_secret: str | None = None
    profile_id: str | None = None
    account_id: str | None = None

    region: Region = Region.NA
    endpoints: dict[str, str] | None = None

    token_url: str = "https://api.amazon.com/auth/o2/token"
    token_cache_dir: str | None = None
    redis_url: str | None = None
    redis_client: Any | None = None
    token_cache: BaseTokenCache | None = None

    timeout: float = 600.0
    max_retries: int = 3

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

        if self.refresh_token and self.client_secret:
            credentials = TokenCredentials(
                client_id=self.client_id,
                client_secret=self.client_secret,
                refresh_token=self.refresh_token,
                token_url=self.token_url,
            )
            self._token_manager = TokenManager(
                credentials=credentials, cache=self._resolve_token_cache(), timeout=self.timeout
            )
        return self

    def _resolve_token_cache(self) -> BaseTokenCache | None:
        if self.token_cache is not None:
            return self.token_cache
        if self.refresh_token is None:
            return None
        if self.redis_client is not None or self.redis_url:
            return RedisTokenCache(
                redis_url=self.redis_url,
                redis_client=self.redis_client,
                client_id=self.client_id,
                refresh_token=self.refresh_token,
            )
        if self.token_cache_dir:
            return FileTokenCache(
                cache_dir=Path(self.token_cache_dir).expanduser(),
                client_id=self.client_id,
                refresh_token=self.refresh_token,
            )
        return None

    @property
    def base_url(self) -> str:
        if self.endpoints:
            return self.endpoints[self.region.value]
        return ENDPOINT_MAP[self.region.value]

    async def refresh_access_token(self, force: bool = False) -> str:
        if self._token_manager is None:
            raise RuntimeError("refresh_token and client_secret must be set to refresh the access token")
        token = await self._token_manager.get_access_token(force=force)
        self.access_token = token
        return token
