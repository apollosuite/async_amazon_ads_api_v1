from __future__ import annotations

from datetime import UTC, datetime
from unittest.mock import AsyncMock, MagicMock, call, patch

import httpx
import pytest
from pydantic import BaseModel

from ads_api.base import BaseResource as UnifiedBaseResource
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
        resp.json.return_value = {"name": "test", "value": 1}
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
        result = resource._validate(items)
        assert result == [{"name": "a", "value": 1}]

    @pytest.mark.asyncio
    async def test_validate_uses_json_mode(self, resource: _ResourceBase) -> None:
        items = [DummyDateModel(startDateTime=datetime(2026, 6, 8, tzinfo=UTC))]
        result = resource._validate(items)
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
    async def test_request_retry_on_401_with_force_refresh(
        self, resource: _ResourceBase, mock_async_client: MagicMock
    ) -> None:
        resource._ctx.config._token_manager = MagicMock()
        auth_error_resp = MagicMock(spec=httpx.Response)
        auth_error_resp.status_code = 401
        auth_error_resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            "unauthorized", request=MagicMock(), response=auth_error_resp
        )
        ok_resp = MagicMock(spec=httpx.Response)
        ok_resp.status_code = 200

        mock_async_client.request.side_effect = [
            auth_error_resp.raise_for_status.side_effect,
            ok_resp,
        ]
        with (
            patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)),
            patch.object(
                AmazonAdsConfig, "refresh_access_token", AsyncMock(return_value="refreshed-token")
            ) as mock_refresh,
        ):
            resp = await resource._request("GET", "/test")
        assert resp.status_code == 200
        assert mock_refresh.await_args_list == [call(), call(force=True)]
        assert mock_async_client.request.call_count == 2

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
        resp.json.return_value = {"name": "x", "value": 2}
        result = resource._response(DummyModel, resp)
        assert isinstance(result, DummyModel)
        assert result.name == "x"
        assert result.value == 2

    @pytest.mark.asyncio
    async def test_create(self, resource: _ResourceBase, mock_async_client: MagicMock) -> None:
        spec = _ResourceSpec(name="items", create_model=DummyModel)
        mock_resp = MagicMock(spec=httpx.Response)
        mock_resp.json.return_value = {"ok": True}
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._create([DummyModel(name="a", value=1)], spec, DummyResponse)
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
        mock_resp.json.return_value = {"ok": True}
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
        mock_resp.json.return_value = {"ok": True}
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
        mock_resp.json.return_value = {"ok": True}
        mock_async_client.request.return_value = mock_resp
        with patch.object(ClientContext, "get_client", AsyncMock(return_value=mock_async_client)):
            result = await resource._query(body, "/test/query", DummyResponse)
        assert isinstance(result, DummyResponse)
        assert result.ok is True
        call_kwargs = mock_async_client.request.call_args[1]
        assert call_kwargs["method"] == "POST"
        assert call_kwargs["url"] == "/test/query"
        assert call_kwargs["json"] == {"name": "test", "value": 1}


class TestUnifiedBaseResource:
    @pytest.fixture
    def unified_resource(self) -> UnifiedBaseResource:
        from ads_api.base import BaseResource, ClientContext
        from ads_api.config.settings import AmazonAdsConfig as NewConfig

        return BaseResource(ClientContext(NewConfig(access_token="test-token", client_id="test-client")))

    def test_response_pydantic_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.text = '{"name": "test", "value": 123}'
        result = unified_resource._response(DummyModel, resp, mode="pydantic")
        assert isinstance(result, DummyModel)
        assert result.name == "test"
        assert result.value == 123

    def test_response_dict_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.json.return_value = {"name": "test", "value": 123}
        result = unified_resource._response(DummyModel, resp, mode="dict")
        assert isinstance(result, dict)
        assert result == {"name": "test", "value": 123}

    def test_response_raw_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        result = unified_resource._response(DummyModel, resp, mode="raw")
        assert result is resp

    def test_response_list_pydantic_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.text = '[{"name": "item1", "value": 1}, {"name": "item2", "value": 2}]'
        result = unified_resource._response_list(DummyModel, resp, mode="pydantic")
        assert isinstance(result, list)
        assert len(result) == 2
        assert isinstance(result[0], DummyModel)
        assert result[0].name == "item1"
        assert result[1].value == 2

    def test_response_list_dict_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        resp.json.return_value = [{"name": "item1", "value": 1}]
        result = unified_resource._response_list(DummyModel, resp, mode="dict")
        assert isinstance(result, list)
        assert result == [{"name": "item1", "value": 1}]

    def test_response_list_raw_mode(self, unified_resource: UnifiedBaseResource) -> None:
        resp = MagicMock(spec=httpx.Response)
        result = unified_resource._response_list(DummyModel, resp, mode="raw")
        assert result is resp

    @pytest.mark.asyncio
    async def test_request_retry_on_401_with_force_refresh(self, unified_resource: UnifiedBaseResource) -> None:
        from ads_api.base import ClientContext as UnifiedClientContext
        from ads_api.config.settings import AmazonAdsConfig as NewConfig

        unified_resource._ctx.config._token_manager = MagicMock()
        auth_error_resp = MagicMock(spec=httpx.Response)
        auth_error_resp.status_code = 401
        auth_error_resp.is_error = True
        auth_error_resp.text = "Unauthorized"

        ok_resp = MagicMock(spec=httpx.Response)
        ok_resp.status_code = 200
        ok_resp.is_error = False

        mock_client = MagicMock(spec=httpx.AsyncClient)
        mock_client.request = AsyncMock(side_effect=[auth_error_resp, ok_resp])

        with (
            patch.object(UnifiedClientContext, "get_client", AsyncMock(return_value=mock_client)),
            patch.object(NewConfig, "refresh_access_token", AsyncMock(return_value="refreshed-token")) as mock_refresh,
        ):
            resp = await unified_resource._request("GET", "/test")

        assert resp.status_code == 200
        assert mock_refresh.await_args_list == [call(), call(force=True)]
        assert mock_client.request.call_count == 2

    @pytest.mark.asyncio
    async def test_request_retry_on_429_with_retry_after(self, unified_resource: UnifiedBaseResource) -> None:
        from ads_api.base import ClientContext as UnifiedClientContext

        rate_limit_resp = MagicMock(spec=httpx.Response)
        rate_limit_resp.status_code = 429
        rate_limit_resp.is_error = True
        rate_limit_resp.headers = {"Retry-After": "3"}

        ok_resp = MagicMock(spec=httpx.Response)
        ok_resp.status_code = 200
        ok_resp.is_error = False

        mock_client = MagicMock(spec=httpx.AsyncClient)
        mock_client.request = AsyncMock(side_effect=[rate_limit_resp, ok_resp])

        with (
            patch.object(UnifiedClientContext, "get_client", AsyncMock(return_value=mock_client)),
            patch("asyncio.sleep", AsyncMock()) as mock_sleep,
        ):
            resp = await unified_resource._request("GET", "/test")

        assert resp.status_code == 200
        assert mock_sleep.await_count == 1
        assert mock_sleep.await_args is not None
        slept = mock_sleep.await_args.args[0]
        assert 3.0 <= slept <= 3.5

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "transient_error",
        [
            httpx.ConnectError("Connection refused"),
            httpx.ReadTimeout("The read operation timed out"),
            httpx.ConnectTimeout("The connection timed out"),
            httpx.RemoteProtocolError("Server disconnected unexpectedly"),
        ],
    )
    async def test_request_retry_on_transient_network_errors(
        self, unified_resource: UnifiedBaseResource, transient_error: Exception
    ) -> None:
        from ads_api.base import ClientContext as UnifiedClientContext

        ok_resp = MagicMock(spec=httpx.Response)
        ok_resp.status_code = 200
        ok_resp.is_error = False

        mock_client = MagicMock(spec=httpx.AsyncClient)
        mock_client.request = AsyncMock(side_effect=[transient_error, ok_resp])

        with (
            patch.object(UnifiedClientContext, "get_client", AsyncMock(return_value=mock_client)),
            patch("asyncio.sleep", AsyncMock()) as mock_sleep,
        ):
            resp = await unified_resource._request("GET", "/test")

        assert resp.status_code == 200
        assert mock_client.request.call_count == 2
        assert mock_sleep.await_count == 1


class TestParseRetryAfter:
    def test_delta_seconds(self) -> None:
        from ads_api.base import _parse_retry_after

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {"Retry-After": "5"}
        result = _parse_retry_after(resp, fallback_seconds=1.0)
        assert 5.0 <= result <= 5.5

    def test_delta_seconds_float(self) -> None:
        from ads_api.base import _parse_retry_after

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {"Retry-After": "2.5"}
        result = _parse_retry_after(resp, fallback_seconds=1.0)
        assert 2.5 <= result <= 3.0

    def test_missing_header_uses_fallback(self) -> None:
        from ads_api.base import _parse_retry_after

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {}
        result = _parse_retry_after(resp, fallback_seconds=3.0)
        assert result == 3.0

    def test_invalid_header_uses_fallback(self) -> None:
        from ads_api.base import _parse_retry_after

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {"Retry-After": "not-a-valid-value"}
        result = _parse_retry_after(resp, fallback_seconds=4.0)
        assert result == 4.0

    def test_max_wait_cap(self) -> None:
        from ads_api.base import _parse_retry_after

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {"Retry-After": "1000"}
        result = _parse_retry_after(resp, fallback_seconds=1.0, max_wait=30.0)
        assert result == 30.0

    def test_http_date_format(self) -> None:
        import email.utils
        from datetime import UTC, datetime, timedelta

        from ads_api.base import _parse_retry_after

        future = datetime.now(UTC) + timedelta(seconds=10)
        date_str = email.utils.format_datetime(future)

        resp = MagicMock(spec=httpx.Response)
        resp.headers = {"Retry-After": date_str}
        result = _parse_retry_after(resp, fallback_seconds=1.0)
        assert 9.0 <= result <= 11.0
