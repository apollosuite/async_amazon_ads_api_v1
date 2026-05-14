"""Base class for all API resource classes."""

from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass
from typing import Any, TypeVar

import httpx
from pydantic import BaseModel

from ._context import ClientContext

_T = TypeVar("_T", bound=BaseModel)


@dataclass
class _ResourceSpec:
    """Metadata for a REST resource (campaigns, adGroups, etc)."""

    name: str
    create_model: type[BaseModel]
    update_model: type[BaseModel]
    delete_key: str | None = None


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
        headers = {"Accept": accept, **self._ctx.profile_header}
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
            f"/adsApi/v1/create/{spec.name}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _update(self, items: list[Any], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        validated = self._validate(items, spec.update_model)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/update/{spec.name}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _delete(self, ids: list[str], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        assert spec.delete_key is not None, f"{spec.name} has no delete operation"
        resp = await self._request(
            "POST",
            f"/adsApi/v1/delete/{spec.name}",
            json={spec.delete_key: ids},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _query(self, body: dict[str, Any], spec: _ResourceSpec, response_cls: type[_T]) -> _T:
        resp = await self._request("POST", f"/adsApi/v1/query/{spec.name}", json=body)
        return self._response(response_cls, resp)
