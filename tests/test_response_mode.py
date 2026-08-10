from __future__ import annotations

from typing import Literal

import httpx
import pytest
from pydantic import BaseModel

from async_amazon_ads_api_v1 import AmazonAdsConfig
from async_amazon_ads_api_v1.base import BaseResource, ClientContext

ResponseMode = Literal["pydantic", "dict", "raw"]


class DummyModel(BaseModel):
    id: str
    name: str


class DummyResource(BaseResource):
    async def get_dummy(self, *, mode: ResponseMode = "pydantic") -> DummyModel | dict | httpx.Response:
        resp = await self._request("GET", "/dummy")
        return self._response(DummyModel, resp, mode=mode)

    async def get_dummy_list(
        self, *, mode: ResponseMode = "pydantic"
    ) -> list[DummyModel] | list[dict] | httpx.Response:
        resp = await self._request("GET", "/dummy_list")
        return self._response_list(DummyModel, resp, mode=mode)

    async def post_dummy(
        self, body: DummyModel, *, mode: ResponseMode = "pydantic"
    ) -> DummyModel | dict | httpx.Response:
        resp = await self._request("POST", "/dummy", json=self.dump_json(body))
        return self._response(DummyModel, resp, mode=mode)


@pytest.mark.asyncio
async def test_response_mode_pydantic() -> None:
    config = AmazonAdsConfig(client_id="test", access_token="test")
    ctx = ClientContext(config)
    res = DummyResource(ctx)

    def mock_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"id": "123", "name": "test_item"})

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(mock_handler), base_url="https://advertising-api.amazon.com"
    )
    ctx._client = client

    item = await res.get_dummy(mode="pydantic")
    assert isinstance(item, DummyModel)
    assert item.id == "123"
    assert item.name == "test_item"


@pytest.mark.asyncio
async def test_response_mode_dict() -> None:
    config = AmazonAdsConfig(client_id="test", access_token="test")
    ctx = ClientContext(config)
    res = DummyResource(ctx)

    def mock_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"id": "123", "name": "test_item"})

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(mock_handler), base_url="https://advertising-api.amazon.com"
    )
    ctx._client = client

    # Per-request override to dict
    item_dict = await res.get_dummy(mode="dict")
    assert isinstance(item_dict, dict)
    assert item_dict == {"id": "123", "name": "test_item"}


@pytest.mark.asyncio
async def test_response_mode_raw() -> None:
    config = AmazonAdsConfig(client_id="test", access_token="test")
    ctx = ClientContext(config)
    res = DummyResource(ctx)

    def mock_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"id": "123", "name": "test_item"})

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(mock_handler), base_url="https://advertising-api.amazon.com"
    )
    ctx._client = client

    resp = await res.get_dummy(mode="raw")
    assert isinstance(resp, httpx.Response)
    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_dict_body_input() -> None:
    config = AmazonAdsConfig(client_id="test", access_token="test")
    ctx = ClientContext(config)
    res = DummyResource(ctx)

    captured_request: httpx.Request | None = None

    def mock_handler(request: httpx.Request) -> httpx.Response:
        nonlocal captured_request
        captured_request = request
        return httpx.Response(200, json={"id": "456", "name": "dict_input"})

    client = httpx.AsyncClient(
        transport=httpx.MockTransport(mock_handler), base_url="https://advertising-api.amazon.com"
    )
    ctx._client = client

    # Pass Pydantic model body
    item = await res.post_dummy(DummyModel(id="456", name="dict_input"))
    assert isinstance(item, DummyModel)
    assert item.id == "456"
    assert captured_request is not None
    assert b'"id":"456"' in captured_request.content or b'"id": "456"' in captured_request.content
