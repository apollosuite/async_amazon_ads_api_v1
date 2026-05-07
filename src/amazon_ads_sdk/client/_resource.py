"""Base class for all API resource classes."""

from __future__ import annotations

import asyncio
import random
from typing import TYPE_CHECKING, Any, TypeVar

import httpx
from pydantic import BaseModel

if TYPE_CHECKING:
    from ._context import ClientContext

_T = TypeVar("_T", bound=BaseModel)


class _ResourceBase:
    """Base class providing shared HTTP operations for resource classes."""

    __slots__ = ("_ctx",)

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx: ClientContext = ctx

    async def _get_client(self, accept_async: bool = False) -> httpx.AsyncClient:
        if self._ctx._client is None:
            accept = "vnd.createasyncrequestresults.v3+json" if accept_async else "json"
            self._ctx._client = httpx.AsyncClient(
                base_url=self._ctx.config.region.value,
                timeout=httpx.Timeout(self._ctx.config.timeout),
                headers={
                    "Authorization": f"Bearer {self._ctx.config.access_token}",
                    "Content-Type": "application/json",
                    "Accept": f"application/{accept}",
                },
            )
        return self._ctx._client

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
        headers = self._ctx.profile_header
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

    def _validate(self, items: list[Any], model_cls: type[BaseModel]) -> list[dict[str, Any]]:
        result: list[dict[str, Any]] = []
        for item in items:
            if isinstance(item, model_cls):
                result.append(item.model_dump())
            else:
                result.append(model_cls(**item).model_dump())
        return result
