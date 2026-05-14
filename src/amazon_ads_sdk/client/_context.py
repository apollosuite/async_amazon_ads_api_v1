"""Shared HTTP state passed to all resource instances."""

from __future__ import annotations

from typing import TypeVar

import httpx
from pydantic import BaseModel

from amazon_ads_sdk.config import AmazonAdsConfig

_T = TypeVar("_T", bound=BaseModel)


class ClientContext:
    """Holds all shared HTTP state for resource instances.

    Lazily creates and caches the ``httpx.AsyncClient`` on first use.
    """

    __slots__ = ("config", "_client", "_profile_header")

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config: AmazonAdsConfig = config
        self._client: httpx.AsyncClient | None = None
        self._profile_header: dict[str, str] | None = None

    @property
    def profile_header(self) -> dict[str, str]:
        """Return the cached profile header, building it on first access."""
        if self._profile_header is None:
            if self.config.profile_id is not None:
                self._profile_header = {
                    "Amazon-Advertising-API-ProfileId": str(self.config.profile_id)
                }
            else:
                self._profile_header = {}
        return self._profile_header

    async def get_client(self, accept_async: bool = False) -> httpx.AsyncClient:
        """Lazily create and return the shared httpx.AsyncClient."""
        if self._client is None:
            accept = "vnd.createasyncrequestresults.v3+json" if accept_async else "json"
            self._client = httpx.AsyncClient(
                base_url=self.config.region.value,
                timeout=httpx.Timeout(self.config.timeout),
                headers={
                    "Authorization": f"Bearer {self.config.access_token}",
                    "Content-Type": "application/json",
                    "Accept": f"application/{accept}",
                },
            )
        return self._client

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return model_cls.model_validate_json(resp.content)
