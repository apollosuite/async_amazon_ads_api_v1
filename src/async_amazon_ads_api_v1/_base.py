"""Shared HTTP session and base resource class for all API resource classes."""

from __future__ import annotations

import asyncio
import logging
import random
from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

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

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return model_cls.model_construct(**resp.json())


@dataclass
class _ResourceSpec:
    """Metadata for a REST resource (campaigns, adGroups, etc)."""

    name: str
    create_model: type[BaseModel]
    update_model: type[BaseModel] | None = None
    delete_key: str | None = None
    path_suffix: str = ""


class _ResourceBase:
    """Base class providing shared HTTP operations for resource classes."""

    __slots__ = ("_ctx",)

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx: ClientContext = ctx

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        accept_async: bool = False,
    ) -> httpx.Response:
        client = await self._ctx.get_client()
        accept = "application/vnd.createasyncrequestresults.v3+json" if accept_async else "application/json"
        if self._ctx.config.access_token is None and self._ctx.config.refresh_token:
            await self._ctx.config.refresh_access_token()
        headers = {
            "Authorization": f"Bearer {self._ctx.config.access_token}",
            "Accept": accept,
            "Amazon-Ads-ClientId": self._ctx.config.client_id,
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
                if exc.response.status_code == 401 and self._ctx.config.refresh_token and attempt == 0:
                    await self._ctx.config.refresh_access_token()
                    headers["Authorization"] = f"Bearer {self._ctx.config.access_token}"
                    continue
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self._ctx.config.max_retries - 1:
                        wait_time = 2**attempt + random.uniform(0, 1)
                        logger.warning("Rate limit exceeded, retrying in %.2f seconds %s", wait_time, exc)
                        await asyncio.sleep(wait_time)
                        continue
                logger.error(f"{exc.response.status_code} {exc.response.text}")
                raise
            except httpx.ConnectError:
                if attempt < self._ctx.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return self._ctx._response(model_cls, resp)

    def _validate(self, items: Sequence[BaseModel]) -> list[dict[str, Any]]:
        return [item.model_dump(mode="json", exclude_none=True) for item in items]

    async def _create(self, items: Sequence[BaseModel], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        validated = self._validate(items)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/create/{spec.name}{spec.path_suffix}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _update(self, items: Sequence[BaseModel], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        assert spec.update_model is not None, f"{spec.name} has no update model"
        validated = self._validate(items)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/update/{spec.name}{spec.path_suffix}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _delete(self, ids: list[str], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        assert spec.delete_key is not None, f"{spec.name} has no delete operation"
        resp = await self._request(
            "POST",
            f"/adsApi/v1/delete/{spec.name}{spec.path_suffix}",
            json={spec.delete_key: ids},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _query(self, body: BaseModel, path: str, response_cls: type[_T]) -> _T:
        resp = await self._request("POST", path, json=body.model_dump(exclude_none=True))
        return self._response(response_cls, resp)
