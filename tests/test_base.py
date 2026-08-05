from __future__ import annotations

import json
from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
from pydantic import BaseModel

from async_amazon_ads_api_v1._base import BaseResource, ClientContext
from async_amazon_ads_api_v1.config.settings import AmazonAdsConfig
from async_amazon_ads_api_v1.errors import BadRequestError, InternalServerError
from async_amazon_ads_api_v1.models.general.brand_store_edition_publish_versions import (
    BrandStoreEditionPublishVersion,
    StorePublishStatus,
)


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


class TestBaseResource:
    @pytest.fixture
    def resource(self, ctx: ClientContext) -> BaseResource:
        return BaseResource(ctx)

    @pytest.mark.asyncio
    async def test_dump_with_model_instances(self, resource: BaseResource) -> None:
        items = [DummyModel(name="a", value=1)]
        result = resource._dump(items)
        assert result == [{"name": "a", "value": 1}]

    @pytest.mark.asyncio
    async def test_dump_uses_json_mode(self, resource: BaseResource) -> None:
        items = [DummyDateModel(startDateTime=datetime(2026, 6, 8, tzinfo=UTC))]
        result = resource._dump(items)
        assert result == [{"startDateTime": "2026-06-08T00:00:00Z"}]

    @pytest.mark.asyncio
    async def test_request_success(
        self, resource: BaseResource, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_request_accept_header_override(
        self, resource: BaseResource, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            await resource._request(
                "POST",
                "/test",
                headers={"Accept": "application/vnd.createasyncrequestresults.v3+json"},
            )
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["headers"]["Accept"] == "application/vnd.createasyncrequestresults.v3+json"

    @pytest.mark.asyncio
    async def test_request_profile_header(
        self, resource: BaseResource, mock_async_client: MagicMock, mock_response: MagicMock
    ) -> None:
        resource._ctx.config.profile_id = "1"
        mock_async_client.request.return_value = mock_response
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            await resource._request("GET", "/test")
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["headers"]["Amazon-Ads-ClientId"] == "test-client-id"
        assert call_kwargs["headers"]["Amazon-Advertising-API-Scope"] == "1"

    @pytest.mark.asyncio
    async def test_request_retry_on_429(self, resource: BaseResource, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 429
        error_resp.is_error = True
        success_resp = MagicMock(spec=httpx.Response)
        success_resp.status_code = 200
        success_resp.is_error = False
        mock_async_client.request.side_effect = [
            error_resp,
            error_resp,
            success_resp,
        ]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200

    @pytest.mark.asyncio
    async def test_request_retry_on_connect_error(self, resource: BaseResource, mock_async_client: MagicMock) -> None:
        success_resp = MagicMock(spec=httpx.Response)
        success_resp.status_code = 200
        success_resp.is_error = False
        mock_async_client.request.side_effect = [
            httpx.ConnectError("conn refused"),
            httpx.ConnectError("conn refused"),
            success_resp,
        ]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200
        assert mock_async_client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_request_exhaust_retries(self, resource: BaseResource, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 503
        error_resp.is_error = True
        mock_async_client.request.side_effect = [error_resp, error_resp, error_resp]
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            with pytest.raises(InternalServerError):
                await resource._request("GET", "/test")
        assert mock_async_client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_request_non_retryable_status(self, resource: BaseResource, mock_async_client: MagicMock) -> None:
        error_resp = MagicMock(spec=httpx.Response)
        error_resp.status_code = 400
        error_resp.is_error = True
        mock_async_client.request.return_value = error_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            with pytest.raises(BadRequestError):
                await resource._request("GET", "/test")
        assert mock_async_client.request.call_count == 1

    @pytest.mark.asyncio
    async def test_response(self, resource: BaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.text = json.dumps({"name": "x", "value": 2})
        result = resource._response(DummyModel, resp)
        assert isinstance(result, DummyModel)
        assert result.name == "x"
        assert result.value == 2

    @pytest.mark.asyncio
    async def test_response_preserves_unknown_enum_values(self, resource: BaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.text = json.dumps(
            {
                "editionId": "edition-1",
                "publishState": "FUTURE_STATE",
                "publishStatus": "DRAFT",
                "storeEditionPublishId": "publish-1",
                "storeId": "store-1",
            }
        )
        result = resource._response(BrandStoreEditionPublishVersion, resp)
        assert result.publishState == "FUTURE_STATE"
        assert result.publishStatus == StorePublishStatus.DRAFT

    @pytest.mark.asyncio
    async def test_raw_resource_proxy(self, resource: BaseResource) -> None:
        raw_res = resource.raw
        assert raw_res is not None

        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.text = json.dumps({"name": "x", "value": 2})

        class DummyResource(BaseResource):
            async def get_dummy(self) -> DummyModel:
                resp = await self._request("GET", "/dummy")
                return self._response(DummyModel, resp)

        dummy_res = DummyResource(resource._ctx)
        with patch.object(dummy_res, "_request", AsyncMock(return_value=mock_resp)):
            # 1. Normal call -> DummyModel
            normal_result = await dummy_res.get_dummy()
            assert isinstance(normal_result, DummyModel)

            # 2. Raw call via .raw proxy -> httpx.Response
            raw_result = await dummy_res.raw.get_dummy()
            assert raw_result is mock_resp

    @pytest.mark.asyncio
    async def test_raw_resource_proxy_list(self, resource: BaseResource) -> None:
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.json.return_value = [{"name": "x", "value": 2}]

        class DummyListResource(BaseResource):
            async def list_dummy(self) -> list[DummyModel]:
                resp = await self._request("GET", "/dummies")
                return self._response_list(DummyModel, resp)

        dummy_res = DummyListResource(resource._ctx)
        with patch.object(dummy_res, "_request", AsyncMock(return_value=mock_resp)):
            raw_result = await dummy_res.raw.list_dummy()
            assert raw_result is mock_resp
