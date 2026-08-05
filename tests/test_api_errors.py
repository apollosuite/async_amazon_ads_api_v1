from __future__ import annotations

import httpx
import pytest

from async_amazon_ads_api_v1.errors import (
    AmazonAdsAPIError,
    AmazonAdsError,
    BadRequestError,
    ForbiddenError,
    InternalServerError,
    NotFoundError,
    RateLimitError,
    UnauthorizedError,
    raise_for_status,
)


def test_exception_hierarchy() -> None:
    err = BadRequestError(httpx.Response(400, text="Bad Request"))
    assert isinstance(err, AmazonAdsAPIError)
    assert isinstance(err, AmazonAdsError)
    assert err.status_code == 400


def test_error_body_parsing_and_request_id() -> None:
    resp = httpx.Response(
        400,
        headers={"x-amz-request-id": "REQ12345"},
        json={"code": "INVALID_ARG", "message": "Invalid adGroupId"},
    )
    err = BadRequestError(resp)
    assert err.status_code == 400
    assert err.request_id == "REQ12345"
    assert err.error_body == {"code": "INVALID_ARG", "message": "Invalid adGroupId"}
    assert "Invalid adGroupId" in str(err)


def test_raise_for_status_mapping() -> None:
    # 400
    with pytest.raises(BadRequestError):
        raise_for_status(httpx.Response(400))

    # 401
    with pytest.raises(UnauthorizedError):
        raise_for_status(httpx.Response(401))

    # 403
    with pytest.raises(ForbiddenError):
        raise_for_status(httpx.Response(403))

    # 404
    with pytest.raises(NotFoundError):
        raise_for_status(httpx.Response(404))

    # 429
    with pytest.raises(RateLimitError):
        raise_for_status(httpx.Response(429))

    # 500
    with pytest.raises(InternalServerError):
        raise_for_status(httpx.Response(500))

    # 418 (unmapped code -> fallback to AmazonAdsAPIError)
    with pytest.raises(AmazonAdsAPIError) as exc_info:
        raise_for_status(httpx.Response(418, text="I'm a teapot"))
    assert type(exc_info.value) is AmazonAdsAPIError
    assert exc_info.value.status_code == 418


def test_raise_for_status_success() -> None:
    # Non-error responses should not raise
    raise_for_status(httpx.Response(200))
    raise_for_status(httpx.Response(201))
    raise_for_status(httpx.Response(207))
