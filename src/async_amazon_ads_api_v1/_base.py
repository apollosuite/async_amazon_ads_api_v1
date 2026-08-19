"""Shared HTTP session and base resource class for all API resource classes."""

from __future__ import annotations

import asyncio
import email.utils
import logging
import random
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any

import httpx
from pydantic import BaseModel

from .config.settings import AmazonAdsConfig

logger = logging.getLogger(__name__)


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

    def _response[T: BaseModel](self, model_cls: type[T], resp: httpx.Response) -> T:
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
        json: dict[str, Any] | list[Any] | None = None,
        accept_async: bool = False,
        headers: dict[str, Any] | None = None,
    ) -> httpx.Response:
        client = await self._ctx.get_client()
        accept = "application/vnd.createasyncrequestresults.v3+json" if accept_async else "application/json"
        if self._ctx.config._token_manager is not None:
            token: str = await self._ctx.config.refresh_access_token()
        else:
            token = self._ctx.config.access_token or ""
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": accept,
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
                    token = await self._ctx.config.refresh_access_token(force=True)
                    headers["Authorization"] = f"Bearer {token}"
                    continue
                if exc.response.status_code in (429, 503, 504):
                    if attempt < self._ctx.config.max_retries - 1:
                        fallback = 2**attempt + random.uniform(0, 1)
                        wait_time = _parse_retry_after(exc.response, fallback_seconds=fallback)
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

    def _response[T: BaseModel](self, model_cls: type[T], resp: httpx.Response) -> T:
        return self._ctx._response(model_cls, resp)

    def _validate(self, items: Sequence[BaseModel]) -> list[dict[str, Any]]:
        return [item.model_dump(mode="json", exclude_none=True) for item in items]

    async def _create[T: BaseModel](self, items: Sequence[BaseModel], spec: _ResourceSpec, response_cls: type[T]) -> T:
        validated = self._validate(items)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/create/{spec.name}{spec.path_suffix}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _update[T: BaseModel](self, items: Sequence[BaseModel], spec: _ResourceSpec, response_cls: type[T]) -> T:
        assert spec.update_model is not None, f"{spec.name} has no update model"
        validated = self._validate(items)
        resp = await self._request(
            "POST",
            f"/adsApi/v1/update/{spec.name}{spec.path_suffix}",
            json={spec.name: validated},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _delete[T: BaseModel](self, ids: list[str], spec: _ResourceSpec, response_cls: type[T]) -> T:
        assert spec.delete_key is not None, f"{spec.name} has no delete operation"
        resp = await self._request(
            "POST",
            f"/adsApi/v1/delete/{spec.name}{spec.path_suffix}",
            json={spec.delete_key: ids},
            accept_async=True,
        )
        return self._response(response_cls, resp)

    async def _query[T: BaseModel](self, body: BaseModel, path: str, response_cls: type[T]) -> T:
        resp = await self._request("POST", path, json=body.model_dump(exclude_none=True))
        return self._response(response_cls, resp)
