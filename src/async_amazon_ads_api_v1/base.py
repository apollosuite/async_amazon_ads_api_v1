"""Shared HTTP session and base resource class for all API resource classes."""

from __future__ import annotations

import asyncio
import logging
import random
from collections.abc import Sequence
from typing import Any, Literal, TypeVar, cast, overload

import httpx
from pydantic import BaseModel, ValidationError

from .config.settings import AmazonAdsConfig
from .errors import raise_for_status

logger = logging.getLogger(__name__)

_T = TypeVar("_T", bound=BaseModel)
ResponseMode = Literal["pydantic", "dict", "raw"]


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
            self._client = httpx.AsyncClient(base_url=self.config.base_url, timeout=httpx.Timeout(self.config.timeout))
        return self._client

    async def close(self) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None


_R = TypeVar("_R", bound="BaseResource")


class BaseResource:
    """Base class providing shared HTTP operations for resource classes."""

    __slots__ = ("_ctx",)

    ASYNC_ACCEPT = {"Accept": "application/vnd.createasyncrequestresults.v3+json"}

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx: ClientContext = ctx

    async def __aenter__(self: _R) -> _R:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()

    async def close(self) -> None:
        await self._ctx.close()

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
            "Amazon-Advertising-API-ClientId": self._ctx.config.client_id,
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
                if resp.is_error:
                    if resp.status_code == 401 and self._ctx.config._token_manager is not None and attempt == 0:
                        token = await self._ctx.config.refresh_access_token()
                        headers["Authorization"] = f"Bearer {token}"
                        continue
                    if resp.status_code in (429, 503, 504):
                        if attempt < self._ctx.config.max_retries - 1:
                            wait_time = 2**attempt + random.uniform(0, 1)
                            logger.warning(
                                "Rate limit exceeded, retrying in %.2f seconds %s", wait_time, resp.status_code
                            )
                            await asyncio.sleep(wait_time)
                            continue
                    logger.error("%s %s", resp.status_code, resp.text)
                    raise_for_status(resp)
                return resp
            except httpx.ConnectError:
                if attempt < self._ctx.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    @overload
    def _response(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> _T: ...

    @overload
    def _response(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["dict"],
    ) -> dict[str, Any]: ...

    @overload
    def _response(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...

    @overload
    def _response(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: ResponseMode = "pydantic",
    ) -> _T | dict[str, Any] | httpx.Response: ...

    def _response(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: ResponseMode = "pydantic",
    ) -> _T | dict[str, Any] | httpx.Response:
        if mode == "raw":
            return resp

        if mode == "dict":
            return cast(dict[str, Any], resp.json())

        try:
            return model_cls.model_validate_json(resp.text)
        except ValidationError:
            logger.error("Failed to parse response as %s: %s", model_cls.__name__, resp.text)
            raise

    @overload
    def _response_list(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["pydantic"] = "pydantic",
    ) -> list[_T]: ...

    @overload
    def _response_list(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["dict"],
    ) -> list[dict[str, Any]]: ...

    @overload
    def _response_list(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: Literal["raw"],
    ) -> httpx.Response: ...

    @overload
    def _response_list(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: ResponseMode = "pydantic",
    ) -> list[_T] | list[dict[str, Any]] | httpx.Response: ...

    def _response_list(
        self,
        model_cls: type[_T],
        resp: httpx.Response,
        *,
        mode: ResponseMode = "pydantic",
    ) -> list[_T] | list[dict[str, Any]] | httpx.Response:
        if mode == "raw":
            return resp

        if mode == "dict":
            return cast(list[dict[str, Any]], resp.json())

        try:
            return [model_cls.model_validate(item) for item in resp.json()]
        except ValidationError:
            logger.error("Failed to parse response list as %s: %s", model_cls.__name__, resp.text)
            raise

    def _dump(self, items: Sequence[BaseModel]) -> list[dict[str, Any]]:
        return [item.model_dump(mode="json", exclude_unset=True) for item in items]
