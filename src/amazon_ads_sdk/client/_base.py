"""Client base — shared HTTP layer."""

from __future__ import annotations

import asyncio
import random
from collections.abc import Awaitable, Callable
from functools import wraps
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

import httpx
from pydantic import BaseModel

if TYPE_CHECKING:
    from amazon_ads_sdk.config import AmazonAdsConfig

_T = TypeVar("_T", bound=BaseModel)

_RequestMethod = Callable[..., Awaitable[httpx.Response]]


def _validate(items: list[Any], model_cls: type[BaseModel]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for item in items:
        if isinstance(item, model_cls):
            result.append(item.model_dump())
        else:
            result.append(model_cls(**item).model_dump())
    return result


def resource[T](
    method: str,
    path: str,
    *,
    response: type[T],
    wrap: str | None = None,
    request_model: type[BaseModel] | None = None,
    accept_async: bool = False,
) -> Callable[
    [Callable[..., Awaitable[Any]]],
    Callable[..., Awaitable[T]],
]:
    """Decorator that handles request validation and response parsing.

    Parameters
    ----------
    method
        HTTP method (e.g. "POST").
    path
        API endpoint path.
    response
        Pydantic response model class.
    wrap
        If set, wraps the method's return value in {wrap: value} before sending.
    request_model
        If set, validates each item in the wrapped list using this model.
    accept_async
        If True, sets Accept header to request polling mode (v3+json).
        Should be True only for create/update/delete operations that may return async.
    """

    def decorator(fn: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[T]]:
        @wraps(fn)
        async def wrapper(self: Any, *args: Any, **kwargs: Any) -> T:
            result = await fn(self, *args, **kwargs)
            if wrap is not None and request_model is not None:
                validated = _validate(result, request_model)
                json_body = {wrap: validated}
            elif wrap is not None:
                json_body = {wrap: result}
            else:
                json_body = result
            resp = await self._request(method, path, json=json_body, accept_async=accept_async)
            return self._response(response, resp)  # type: ignore[no-any-return]

        return wrapper

    return decorator


class _ResponseMethod(Protocol):
    """Protocol for the _response method signature."""

    def __call__(self, model_cls: type[BaseModel], resp: httpx.Response) -> BaseModel: ...


class _AmazonAdsClientBase:
    _client: httpx.AsyncClient | None
    config: AmazonAdsConfig
    _cached_profile_header: dict[str, str] | None

    @property
    def _profile_header(self) -> dict[str, str]:
        if self._cached_profile_header is None:
            if self.config.profile_id is not None:
                self._cached_profile_header = {
                    "Amazon-Advertising-API-ProfileId": str(self.config.profile_id)
                }
            else:
                self._cached_profile_header = {}
        return self._cached_profile_header

    async def _get_client(self, accept_async: bool = False) -> httpx.AsyncClient:
        if self._client is None:
            accept = "vnd.createasyncrequestresults.v3+json" if accept_async else "json"
            self._client = httpx.AsyncClient(
                base_url=self.config.region.value,
                timeout=httpx.Timeout(self.config.timeout),
                headers={
                    "Authorization": f"Bearer {self.config.access_token}",
                    "Content-Type": "application/json",
                    "Accept": f"application/{accept}",
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
        accept_async: bool = False,
    ) -> httpx.Response:
        client = await self._get_client(accept_async)
        headers = self._profile_header
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
                        await asyncio.sleep(2**attempt + random.uniform(0, 1))
                        continue
                raise
            except httpx.ConnectError:
                if attempt < self.config.max_retries - 1:
                    await asyncio.sleep(2**attempt + random.uniform(0, 1))
                    continue
                raise
        raise RuntimeError("Retry loop exited unexpectedly")

    def _response(self, model_cls: type[_T], resp: httpx.Response) -> _T:
        return model_cls.model_validate_json(resp.content)
