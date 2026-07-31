"""Shared HTTP session and base resource class for all API resource classes."""

from __future__ import annotations

import asyncio
import logging
import random
from collections.abc import Sequence
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel, ValidationError

from .config.settings import AmazonAdsConfig

logger = logging.getLogger(__name__)

_T = TypeVar("_T", bound=BaseModel)


class ClientContext:
    """Shared HTTP state for all resource instances.

    Lazily creates and caches the ``httpx.AsyncClient`` on first use.
    """

    __slots__ = ("config", "_client")

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config: AmazonAdsConfig = config
        self._client: httpx.AsyncClient | None = None

    async def get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.config.base_url,
                timeout=httpx.Timeout(self.config.timeout),
            )
        return self._client


class BaseResource:
    """Base class providing shared HTTP operations for resource classes."""

    __slots__ = ("_ctx",)

    ASYNC_ACCEPT = {"Accept": "application/vnd.createasyncrequestresults.v3+json"}

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx: ClientContext = ctx

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | list[Any] | None = None,
        headers: dict[str, Any] | None = None,
    ) -> httpx.Response:
        client = await self._ctx.get_client()
        if self._ctx.config._token_manager is not None:
            token: str = await self._ctx.config.refresh_access_token()
        else:
            token = self._ctx.config.access_token or ""
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Amazon-Ads-ClientId": self._ctx.config.client_id,
            **(headers or {}),
        }
        if self._ctx.config.profile_id is not None:
            headers["Amazon-Advertising-API-Scope"] = self._ctx.config.profile_id
        for attempt in range(self._ctx.config.max_retries):
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
                if exc.response.status_code == 401 and self._ctx.config._token_manager is not None and attempt == 0:
                    token = await self._ctx.config.refresh_access_token()
                    headers["Authorization"] = f"Bearer {token}"
                    continue
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self._ctx.config.max_retries - 1:
                        wait_time = 2**attempt + random.uniform(0, 1)
                        logger.warning("Rate limit exceeded, retrying in %.2f seconds %s", wait_time, exc)
                        await asyncio.sleep(wait_time)
                        continue
                logger.error("%s %s", exc.response.status_code, exc.response.text)
                raise
            except httpx.ConnectError:
                if attempt < self._ctx.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        try:
            return model_cls.model_validate_json(resp.text)
        except ValidationError:
            logger.error("Failed to parse response as %s: %s", model_cls.__name__, resp.text)
            raise

    def _response_list(self, model_cls: type[_T], resp: httpx.Response) -> list[_T]:
        try:
            return [model_cls.model_validate(item) for item in resp.json()]
        except ValidationError:
            logger.error("Failed to parse response list as %s: %s", model_cls.__name__, resp.text)
            raise

    def _dump(self, items: Sequence[BaseModel]) -> list[dict[str, Any]]:
        return [item.model_dump(mode="json", exclude_none=True) for item in items]
