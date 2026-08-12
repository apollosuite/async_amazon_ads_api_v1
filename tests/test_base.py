from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest
from pydantic import BaseModel

from async_amazon_ads_api_v1.base import BaseResource, ClientContext
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

    @pytest.mark.asyncio
    async def test_client_context_close(self, config: AmazonAdsConfig) -> None:
        ctx = ClientContext(config)
        client = await ctx.get_client()
        assert not client.is_closed
        await ctx.close()
        assert client.is_closed
        assert ctx._client is None

    @pytest.mark.asyncio
    async def test_client_context_async_context_manager(self, config: AmazonAdsConfig) -> None:
        async with ClientContext(config) as ctx:
            client = await ctx.get_client()
            assert not client.is_closed
        assert client.is_closed
        assert ctx._client is None


class TestBaseResource:
    @pytest.fixture
    def resource(self, ctx: ClientContext) -> BaseResource:
        return BaseResource(ctx)

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

    def test_dump_json_excludes_unset_and_none(self, resource: BaseResource) -> None:
        class OptionalBody(BaseModel):
            name: str
            note: str | None = None
            count: int | None = None

        body = OptionalBody(name="x", note=None)
        assert resource.dump_json(body) == {"name": "x"}

    def test_dump_json_respects_flags(self, ctx: ClientContext) -> None:
        class OptionalBody(BaseModel):
            name: str
            note: str | None = None

        resource = BaseResource(ctx, exclude_unset=False, exclude_none=False)
        body = OptionalBody(name="x")
        assert resource.dump_json(body) == {"name": "x", "note": None}

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
