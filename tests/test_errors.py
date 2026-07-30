from __future__ import annotations

import pytest
from pydantic import ValidationError

from async_amazon_ads_api_v1.models.sp.enums import SPErrorCode
from async_amazon_ads_api_v1.models.sp.shared import SPError, SPErrorsIndex


class TestErrorCode:
    def test_values(self) -> None:
        assert SPErrorCode.BAD_REQUEST == "BAD_REQUEST"
        assert SPErrorCode.NOT_FOUND == "NOT_FOUND"
        assert SPErrorCode.TOO_MANY_REQUESTS == "TOO_MANY_REQUESTS"
        assert SPErrorCode.UNAUTHORIZED == "UNAUTHORIZED"
        assert SPErrorCode.FORBIDDEN == "FORBIDDEN"
        assert SPErrorCode.INTERNAL_ERROR == "INTERNAL_ERROR"

    def test_known_codes(self) -> None:
        codes = {m.value for m in SPErrorCode}
        assert "ACTION_NOT_SUPPORTED" in codes
        assert "CONFLICT" in codes
        assert "DUPLICATE_RESOURCE_ID_FOUND" in codes


class TestError:
    def test_minimal(self) -> None:
        err = SPError.model_validate({"code": "BAD_REQUEST", "message": "bad"})
        assert err.code == SPErrorCode.BAD_REQUEST
        assert err.message == "bad"
        assert err.fieldLocation is None

    def test_with_field_location(self) -> None:
        err = SPError.model_validate({"code": "NOT_FOUND", "fieldLocation": "campaignId", "message": "not found"})
        assert err.fieldLocation == "campaignId"

    def test_extra_field_allowed(self) -> None:
        err = SPError.model_validate({"code": "BAD_REQUEST", "message": "bad", "extra": "x"})
        assert err.code == SPErrorCode.BAD_REQUEST

    def test_unknown_code_preserved_as_str(self) -> None:
        err = SPError.model_validate_json('{"code": "UNKNOWN_CODE", "message": "x"}')
        assert err.code == "UNKNOWN_CODE"


class TestErrorsIndex:
    def test_valid(self) -> None:
        ei = SPErrorsIndex.model_validate(
            {"errors": [{"code": "BAD_REQUEST", "message": "e1"}], "index": 0},
        )
        assert len(ei.errors or []) == 1
        assert ei.index == 0

    def test_extra_fields_allowed(self) -> None:
        SPErrorsIndex.model_validate(
            {"errors": [{"code": "BAD_REQUEST", "message": "e"}], "index": 0, "extra": "x"},
        )

    def test_missing_fields_rejected(self) -> None:
        with pytest.raises(ValidationError):
            SPErrorsIndex.model_validate({})
