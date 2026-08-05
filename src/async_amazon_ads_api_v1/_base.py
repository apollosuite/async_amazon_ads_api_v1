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


_R = TypeVar("_R", bound="BaseResource")


class BaseResource:
    """Base class providing shared HTTP operations for resource classes."""

    __slots__ = ("_ctx", "_raw", "_raw_mode")

    ASYNC_ACCEPT = {"Accept": "application/vnd.createasyncrequestresults.v3+json"}

    def __init__(self, ctx: ClientContext) -> None:
        self._ctx: ClientContext = ctx
        self._raw: Any | None = None
        self._raw_mode: bool = False

    @property
    def raw(self: _R) -> RawResource[_R]:
        """Access raw response version of this resource's methods."""
        if self._raw is None:
            self._raw = RawResource(self)
        return self._raw

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
    def _response(self, model_cls: type[_T], resp: httpx.Response, *, raw_response: Literal[False] = False) -> _T: ...

    @overload
    def _response(
        self, model_cls: type[_T], resp: httpx.Response, *, raw_response: Literal[True]
    ) -> httpx.Response: ...

    @overload
    def _response(self, model_cls: type[_T], resp: httpx.Response, *, raw_response: bool) -> _T | httpx.Response: ...

    def _response(
        self, model_cls: type[_T], resp: httpx.Response, *, raw_response: bool = False
    ) -> _T | httpx.Response:
        if raw_response or self._raw_mode:
            return resp
        try:
            return model_cls.model_validate_json(resp.text)
        except ValidationError:
            logger.error("Failed to parse response as %s: %s", model_cls.__name__, resp.text)
            raise

    def _response_list(self, model_cls: type[_T], resp: httpx.Response) -> list[_T]:
        if self._raw_mode:
            return cast("list[_T]", resp)
        try:
            return [model_cls.model_validate(item) for item in resp.json()]
        except ValidationError:
            logger.error("Failed to parse response list as %s: %s", model_cls.__name__, resp.text)
            raise

    def _dump(self, items: Sequence[BaseModel]) -> list[dict[str, Any]]:
        return [item.model_dump(mode="json", exclude_none=True) for item in items]


class RawResource[R: BaseResource]:
    """Wrapper that bypasses model parsing and returns raw httpx.Response."""

    __slots__ = ("_resource",)

    def __init__(self, resource: _R) -> None:
        self._resource = resource

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self._resource, name)
        if callable(attr) and not name.startswith("_"):

            async def raw_method(*args: Any, **kwargs: Any) -> httpx.Response:
                self._resource._raw_mode = True
                try:
                    res: httpx.Response = await attr(*args, **kwargs)
                    return res
                finally:
                    self._resource._raw_mode = False

            return raw_method
        return attr
