"""Client base — shared HTTP layer."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

import httpx
from pydantic import BaseModel

if TYPE_CHECKING:
    from amazon_ads_sdk.config import AmazonAdsConfig

_T = TypeVar("_T", bound=BaseModel)

_RequestMethod = Callable[..., Awaitable[httpx.Response]]


class _ResponseMethod(Protocol):
    """Protocol for the _response method signature."""

    def __call__(self, model_cls: type[BaseModel], resp: httpx.Response) -> BaseModel: ...


class _AmazonAdsClientBase:
    _client: httpx.AsyncClient | None
    config: AmazonAdsConfig

    def _profile_header(self) -> dict[str, str]:
        if self.config.profile_id is not None:
            return {"Amazon-Advertising-API-ProfileId": str(self.config.profile_id)}
        return {}

    async def _get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.config.region.value,
                timeout=httpx.Timeout(self.config.timeout),
                headers={
                    "Authorization": f"Bearer {self.config.access_token}",
                    "Content-Type": "application/json",
                    "Accept": "application/vnd.createasyncrequestresults.v3+json",
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
    ) -> httpx.Response:
        client = await self._get_client()
        headers = self._profile_header()
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
                        await asyncio.sleep(2**attempt)
                        continue
                raise
            except httpx.ConnectError:
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(2**attempt)
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        """Parse JSON response into a Pydantic model.

        Parameters
        ----------
        model_cls
            Target Pydantic model class.
        resp
            httpx response with JSON body.
        """
        return model_cls.model_validate_json(resp.content)
