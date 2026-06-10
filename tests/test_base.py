from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
from pydantic import BaseModel

from async_amazon_ads_api_v1._base import ClientContext, _ResourceBase, _ResourceSpec
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig


class DummyModel(BaseModel):
    name: str
    value: int


class DummyResponse(BaseModel):
    ok: bool


class DummyDateModel(BaseModel):
    startDateTime: datetime  # noqa: N815 - Amazon API 字段使用 camelCase
    note: str | None = None


class TestClientContext:
    @pytest.mark.asyncio
    async def test_get_client_lazy_init(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        assert ctx._client is None
        client = await ctx.get_client()
        assert client is not None
        assert client is ctx._client

    @pytest.mark.asyncio
    async def test_get_client_base_url(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        client = await ctx.get_client()
        assert str(client.base_url) == "https://advertising-api.amazon.com"

    @pytest.mark.asyncio
    async def test_get_client_cached(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        c1 = await ctx.get_client()
        c2 = await ctx.get_client()
        assert c1 is c2

    def test_response(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        resp = MagicMock(spec=httpx.Response)
        resp.content = b'{"name": "test", "value": 1}'
        result = ctx._response(DummyModel, resp)
        assert isinstance(result, DummyModel)
        assert result.name == "test"
        assert result.value == 1


class TestResourceSpec:
    def test_minimal(self) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel)
        assert spec.name == "items"
        assert spec.create_model is DummyModel
        assert spec.update_model is None
        assert spec.delete_key is None
        assert spec.path_suffix == ""

    def test_full(self) -> None:
        spec = _ResourceSpec(
            name="campaigns",
            create_model=DummyModel,
            update_model=DummyModel,
            delete_key="campaignIds",
            path_suffix="/v2",
        )
        assert spec.delete_key == "campaignIds"
        assert spec.path_suffix == "/v2"


class TestResourceBase:
    @pytest.fixture
    def resource(self, ctx: ClientContext) -> _ResourceBase:
        return _ResourceBase(ctx)

    @pytest.mark.asyncio
    async def test_validate_with_model_instances(self, resource: _ResourceBase) -> None:
        items = [DummyModel(name="a", value=1)]
        result = resource._validate(items, DummyModel)
        assert result == [{"name": "a", "value": 1}]

    @pytest.mark.asyncio
    async def test_validate_with_dicts(self, resource: _ResourceBase) -> None:
        items = [{"name": "b", "value": 2}]
        result = resource._validate(items, DummyModel)
        assert result == [{"name": "b", "value": 2}]

    @pytest.mark.asyncio
    async def test_validate_uses_json_mode(self, resource: _ResourceBase) -> None:
        items = [DummyDateModel(startDateTime=datetime(2026, 6, 8, tzinfo=UTC))]
        result = resource._validate(items, DummyDateModel)
        assert result == [{"startDateTime": "2026-06-08T00:00:00Z"}]

    @pytest.mark.asyncio
    async def test_request_success(
        self, resource: _ResourceBase, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_request_accept_async(
        self, resource: _ResourceBase, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            await resource._request("POST", "/test", accept_async=True)
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["headers"]["Accept"] == "application/vnd.createasyncrequestresults.v3+json"

    @pytest.mark.asyncio
    async def test_request_profile_header(
        self, resource: _ResourceBase, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        resource._ctx.config.profile_id = "1"
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            await resource._request("GET", "/test")
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["headers"]["Amazon-Ads-ClientId"] == "test-client-id"
        assert call_kwargs["headers"]["Amazon-Advertising-API-Scope"] == "1"

    @pytest.mark.asyncio
    async def test_request_retry_on_429(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 429
        error_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            "too many", request=MagicMock(), response=error_resp
        )
        mock_async_client.request.side_effect = [
            error_resp,
            error_resp,
            MagicMock(status_code=200, content=b"{}"),
        ]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200
        assert mock_async_client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_request_retry_on_connect_error(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        mock_async_client.request.side_effect = [
            httpx.ConnectError("conn refused"),
            httpx.ConnectError("conn refused"),
            MagicMock(status_code=200, content=b"{}"),
        ]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200
        assert mock_async_client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_request_exhaust_retries(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 503
        error_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            "unavailable", request=MagicMock(), response=error_resp
        )
        mock_async_client.request.side_effect = [error_resp, error_resp, error_resp]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            with pytest.raises(httpx.HTTPStatusError):
                await resource._request("GET", "/test")
        assert mock_async_client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_request_non_retryable_status(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 400
        exc = httpx.HTTPStatusError("bad", request=MagicMock(), response=error_resp)
        error_resp.raise_for_status.side_effect = exc
        mock_async_client.request.return_value = error_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            with pytest.raises(httpx.HTTPStatusError):
                await resource._request("GET", "/test")
        assert mock_async_client.request.call_count == 1

    @pytest.mark.asyncio
    async def test_response(self, resource: _ResourceBase) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.content = b'{"name": "x", "value": 2}'
        result = resource._response(DummyModel, resp)
        assert isinstance(result, DummyModel)
        assert result.name == "x"
        assert result.value == 2

    @pytest.mark.asyncio
    async def test_create(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel)
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.content = b'{"ok": true}'
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._create([{"name": "a", "value": 1}], spec, DummyResponse)
        assert isinstance(result, DummyResponse)
        assert result.ok is True
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["method"] == "POST"
        assert "/create/items" in call_kwargs["url"]
        assert call_kwargs["json"] == {"items": [{"name": "a", "value": 1}]}

    @pytest.mark.asyncio
    async def test_update(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel, update_model=DummyModel)
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.content = b'{"ok": true}'
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._update([DummyModel(name="a", value=1)], spec, DummyResponse)
        assert isinstance(result, DummyResponse)
        assert result.ok is True
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["method"] == "POST"
        assert "/update/items" in call_kwargs["url"]

    @pytest.mark.asyncio
    async def test_update_no_model_raises(self, resource: _ResourceBase) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel)
        with pytest.raises(AssertionError, match="has no update model"):
            await resource._update([], spec, DummyResponse)

    @pytest.mark.asyncio
    async def test_delete(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel, delete_key="itemIds")
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.content = b'{"ok": true}'
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._delete(["1", "2"], spec, DummyResponse)
        assert isinstance(result, DummyResponse)
        assert result.ok is True
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["json"] == {"itemIds": ["1", "2"]}

    @pytest.mark.asyncio
    async def test_delete_no_key_raises(self, resource: _ResourceBase) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel)
        with pytest.raises(AssertionError, match="has no delete operation"):
            await resource._delete([], spec, DummyResponse)

    @pytest.mark.asyncio
    async def test_query(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        body = DummyModel(name="test", value=1)
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.content = b'{"ok": true}'
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._query(body, "/test/query", DummyResponse)
        assert isinstance(result, DummyResponse)
        assert result.ok is True
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["method"] == "POST"
        assert call_kwargs["url"] == "/test/query"
        assert call_kwargs["json"] == {"name": "test", "value": 1}
