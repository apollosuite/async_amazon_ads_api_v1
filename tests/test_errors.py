from __future__ import annotations

import pytest
from pydantic import ValidationError

from async_amazon_ads_api_v1.errors import (
    BadGatewayResponseContent,
    BadRequestResponseContent,
    ContentTooLargeResponseContent,
    Error,
    ErrorCode,
    ErrorsIndex,
    ForbiddenResponseContent,
    GatewayTimeoutResponseContent,
    InternalServerErrorResponseContent,
    NotFoundResponseContent,
    ServiceUnavailableErrorResponseContent,
    TooManyRequestsResponseContent,
    UnauthorizedResponseContent,
)


class TestErrorCode:
    def test_values(self) -> None:
        assert ErrorCode.BAD_REQUEST == "BAD_REQUEST"
        assert ErrorCode.NOT_FOUND == "NOT_FOUND"
        assert ErrorCode.TOO_MANY_REQUESTS == "TOO_MANY_REQUESTS"
        assert ErrorCode.UNAUTHORIZED == "UNAUTHORIZED"
        assert ErrorCode.FORBIDDEN == "FORBIDDEN"
        assert ErrorCode.INTERNAL_ERROR == "INTERNAL_ERROR"

    def test_known_codes(self) -> None:
        codes = {m.value for m in ErrorCode}
        assert "ACTION_NOT_SUPPORTED" in codes
        assert "CONFLICT" in codes
        assert "DUPLICATE_RESOURCE_ID_FOUND" in codes


class TestError:
    def test_minimal(self) -> None:
        err = Error(code="BAD_REQUEST", message="bad")
        assert err.code == ErrorCode.BAD_REQUEST
        assert err.message == "bad"
        assert err.fieldLocation is None

    def test_with_field_location(self) -> None:
        err = Error(code="NOT_FOUND", fieldLocation="campaignId", message="not found")
        assert err.fieldLocation == "campaignId"

    def test_extra_field_forbidden(self) -> None:
        with pytest.raises(ValidationError):
            Error(code="BAD_REQUEST", message="bad", extra="x")  # type: ignore[call-arg]

    def test_unknown_code(self) -> None:
        with pytest.raises(ValidationError):
            Error(code="UNKNOWN_CODE", message="x")


class TestErrorsIndex:
    def test_valid(self) -> None:
        ei = ErrorsIndex(
            errors=[Error(code="BAD_REQUEST", message="e1")],
            index=0,
        )
        assert len(ei.errors) == 1
        assert ei.index == 0

    def test_extra_fields_forbidden(self) -> None:
        with pytest.raises(ValidationError):
            ErrorsIndex(errors=[], index=0, extra="x")  # type: ignore[call-arg]


class TestResponseModels:
    @pytest.mark.parametrize(
        ("model_cls", "data"),
        [
            (BadRequestResponseContent, {"code": "BAD_REQUEST", "message": "bad"}),
            (ContentTooLargeResponseContent, {"code": "CONTENT_TOO_LARGE", "message": "big"}),
            (ForbiddenResponseContent, {"code": "FORBIDDEN", "message": "forbidden"}),
            (NotFoundResponseContent, {"code": "NOT_FOUND", "message": "missing"}),
            (TooManyRequestsResponseContent, {"code": "TOO_MANY_REQUESTS", "message": "slow"}),
            (UnauthorizedResponseContent, {"code": "UNAUTHORIZED", "message": "no auth"}),
        ],
    )
    def test_valid(self, model_cls: type, data: dict) -> None:
        obj = model_cls(**data)
        assert obj.code == data["code"]
        assert obj.message == data["message"]

    @pytest.mark.parametrize(
        ("model_cls", "data"),
        [
            (BadGatewayResponseContent, {"code": "UPSTREAM_ERR", "message": "up"}),
            (GatewayTimeoutResponseContent, {"code": "TIMEOUT", "message": "gateway"}),
            (InternalServerErrorResponseContent, {"code": "CRASH", "message": "server"}),
            (ServiceUnavailableErrorResponseContent, {"code": "DOWN", "message": "srv"}),
        ],
    )
    def test_string_code(self, model_cls: type, data: dict) -> None:
        obj = model_cls(**data)
        assert isinstance(obj.code, str)
        assert obj.message == data["message"]

    @pytest.mark.parametrize(
        "model_cls",
        [
            BadRequestResponseContent,
            ForbiddenResponseContent,
            NotFoundResponseContent,
            TooManyRequestsResponseContent,
            UnauthorizedResponseContent,
        ],
    )
    def test_extra_forbidden(self, model_cls: type) -> None:
        with pytest.raises(ValidationError):
            model_cls(code="BAD_REQUEST", message="x", extra="y")  # type: ignore[call-arg]

    @pytest.mark.parametrize(
        "model_cls",
        [
            BadGatewayResponseContent,
            GatewayTimeoutResponseContent,
            InternalServerErrorResponseContent,
            ServiceUnavailableErrorResponseContent,
        ],
    )
    def test_extra_forbidden_string_code(self, model_cls: type) -> None:
        with pytest.raises(ValidationError):
            model_cls(code="X", message="x", extra="y")  # type: ignore[call-arg]
