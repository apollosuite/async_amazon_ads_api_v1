"""Client base — shared HTTP layer."""

from __future__ import annotations

import asyncio
import random
from typing import TYPE_CHECKING, Any, TypeVar

import httpx
from pydantic import BaseModel

if TYPE_CHECKING:
    from amazon_ads_sdk.config import AmazonAdsConfig

_T = TypeVar("_T", bound=BaseModel)


class _AmazonAdsClientBase:
    _client: httpx.AsyncClient | None
    config: AmazonAdsConfig
    _cached_profile_header: dict[str, str] | None

    @property
    def _profile_header(self) -> dict[str, str]:
        if self._cached_profile_header is None:
            if self.config.profile_id is not None:
                self._cached_profile_header = {
                    "Amazon-Advertising-API-ProfileId": str(self.config.profile_id)
                }
            else:
                self._cached_profile_header = {}
        return self._cached_profile_header

    async def _get_client(self, accept_async: bool = False) -> httpx.AsyncClient:
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

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        accept_async: bool = False,
    ) -> httpx.Response:
        client = await self._get_client(accept_async)
        headers = self._profile_header
        for attempt in range(self.config.max_retries):
            try:
                resp = await client.request(
                    method=method,
                    url=path,
                    params=params,
                    json=json,
                    headers=headers,
                )
                resp.raise_for_status()
                return resp
            except httpx.HTTPStatusError as exc:
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self.config.max_retries - 1:
                        await asyncio.sleep(2**attempt + random.uniform(0, 1))
                        continue
                raise
            except httpx.ConnectError:
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return model_cls.model_validate_json(resp.content)
