"""Shared HTTP session and base resource class."""

from __future__ import annotations

import asyncio
import email.utils
import logging
import random
from datetime import UTC, datetime
from typing import Any, Literal, cast, overload

import httpx
from pydantic import BaseModel, TypeAdapter, ValidationError

from ads_api.config.settings import AmazonAdsConfig
from ads_api.errors import raise_for_status

logger = logging.getLogger(__name__)

type ResponseMode = Literal["pydantic", "dict", "raw"]


def _parse_retry_after(resp: httpx.Response | None, fallback_seconds: float, max_wait: float = 60.0) -> float:
    """Parse the Retry-After header as seconds or HTTP-Date with fallback."""
    if resp is None:
        return fallback_seconds
    headers = getattr(resp, "headers", None)
    if headers is None:
        return fallback_seconds
    raw = headers.get("Retry-After")
    if not raw:
        return fallback_seconds
    try:
        seconds = float(raw)
        if seconds >= 0:
            return min(seconds + random.uniform(0, 0.5), max_wait)
    except (ValueError, TypeError):
        pass
    try:
        target_dt = email.utils.parsedate_to_datetime(str(raw))
        now_dt = datetime.now(UTC)
        delta = (target_dt - now_dt).total_seconds()
        if delta > 0:
            return min(delta + random.uniform(0, 0.5), max_wait)
    except Exception:
        pass
    return fallback_seconds


class ClientContext:
    """Shared HTTP state for all resource instances."""

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
        if self.config._token_manager is not None:
            await self.config._token_manager.close()

    async def __aenter__(self) -> ClientContext:
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.close()


class BaseResource:
    """HTTP helpers shared by generated resource classes."""

    __slots__ = ("_ctx", "exclude_unset", "exclude_none")

    def __init__(self, ctx: ClientContext, exclude_unset: bool = True, exclude_none: bool = True) -> None:
        self._ctx: ClientContext = ctx
        self.exclude_unset = exclude_unset
        self.exclude_none = exclude_none

    def dump_json(self, body: BaseModel) -> dict[str, Any]:
        return body.model_dump(mode="json", exclude_unset=self.exclude_unset, exclude_none=self.exclude_none)

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
        if self._ctx.config.account_id is not None:
            headers["Amazon-Ads-AccountId"] = self._ctx.config.account_id
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
                        token = await self._ctx.config.refresh_access_token(force=True)
                        headers["Authorization"] = f"Bearer {token}"
                        continue
                    if resp.status_code in (429, 503, 504) and attempt < self._ctx.config.max_retries - 1:
                        fallback = 2**attempt + random.uniform(0, 1)
                        wait_time = _parse_retry_after(resp, fallback_seconds=fallback)
                        logger.warning("Rate limit exceeded, retrying in %.2f seconds %s", wait_time, resp.status_code)
                        await asyncio.sleep(wait_time)
                        continue
                    logger.error("%s %s", resp.status_code, resp.text)
                    raise_for_status(resp)
                return resp
            except (httpx.ConnectError, httpx.TimeoutException, httpx.RemoteProtocolError):
                if attempt < self._ctx.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    @overload
    def _response[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["pydantic"] = "pydantic"
    ) -> T: ...
    @overload
    def _response[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["dict"]
    ) -> dict[str, Any]: ...
    @overload
    def _response[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def _response[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: ResponseMode = "pydantic"
    ) -> T | dict[str, Any] | httpx.Response:
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
    def _response_list[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["pydantic"] = "pydantic"
    ) -> list[T]: ...
    @overload
    def _response_list[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["dict"]
    ) -> list[dict[str, Any]]: ...
    @overload
    def _response_list[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: Literal["raw"]
    ) -> httpx.Response: ...
    def _response_list[T: BaseModel](
        self, model_cls: type[T], resp: httpx.Response, *, mode: ResponseMode = "pydantic"
    ) -> list[T] | list[dict[str, Any]] | httpx.Response:
        if mode == "raw":
            return resp
        if mode == "dict":
            return cast(list[dict[str, Any]], resp.json())
        try:
            list_type: Any = list[model_cls]  # type: ignore[valid-type]
            return TypeAdapter[list[T]](list_type).validate_json(resp.text)
        except ValidationError:
            logger.error("Failed to parse response list as %s: %s", model_cls.__name__, resp.text)
            raise
