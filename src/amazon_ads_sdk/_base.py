"""Shared HTTP session and base resource class for all API resource classes."""

from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from .config import AmazonAdsConfig

_T = TypeVar("_T", bound=BaseModel)


class ClientContext:
    """Shared HTTP state for all resource instances.

    Lazily creates and caches the ``httpx.AsyncClient`` on first use.
    """

    __slots__ = ("config", "_client")

    def __init__(self, config: AmazonAdsConfig) -> None:
        self.config: AmazonAdsConfig = config
        self._client: httpx.AsyncClient | None = None

    @property
    def profile_header(self) -> dict[str, str]:
        if self.config.profile_id is not None:
            return {"Amazon-Advertising-API-Scope": str(self.config.profile_id)}
        return {}

    async def get_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.config.region.value,
                timeout=httpx.Timeout(self.config.timeout),
                headers={
                    "Authorization": f"Bearer {self.config.access_token}",
                    "Amazon-Ads-ClientId": self.config.client_id,
                    "Content-Type": "application/json",
                },
            )
        return self._client

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return model_cls.model_validate_json(resp.content)


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
        accept = (
            "application/vnd.createasyncrequestresults.v3+json"
            if accept_async
            else "application/json"
        )
        headers = {
            "Accept": accept,
            "Amazon-Ads-ClientId": self._ctx.config.client_id,
            **self._ctx.profile_header,
        }
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
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self._ctx.config.max_retries - 1:
                        await asyncio.sleep(2**attempt + random.uniform(0, 1))
                        continue
                raise
            except httpx.ConnectError:
                if attempt < self._ctx.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return self._ctx._response(model_cls, resp)

    def _validate(self, items: list[Any], model_cls: type[_T]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for item in items:
            if isinstance(item, model_cls):
                result.append(item.model_dump())
            else:
                result.append(model_cls(**item).model_dump())
        return result

    async def _create(self, items: list[Any], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        validated = self._validate(items, spec.create_model)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/create/{spec.name}{spec.path_suffix}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _update(self, items: list[Any], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        assert spec.update_model is not None, f"{spec.name} has no update model"
        validated = self._validate(items, spec.update_model)
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

    async def _query(
        self, body: dict[str, Any] | BaseModel, spec: _ResourceSpec, response_cls: type[_T]
    ) -> _T:
        if isinstance(body, BaseModel):
            body = body.model_dump()
        resp = await self._request(
            "POST", f"/adsApi/v1/query/{spec.name}{spec.path_suffix}", json=body
        )
        return self._response(response_cls, resp)
