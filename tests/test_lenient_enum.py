from __future__ import annotations

import json
from enum import StrEnum
from typing import Annotated

import pytest
from pydantic import BaseModel

from async_amazon_ads_api_v1.models._core.lenient_enum import lenient_enum
from async_amazon_ads_api_v1.models.sd.campaigns import (
    SDCampaignNameFilter,
    SDCampaignNameFilterType,
)
from async_amazon_ads_api_v1.models.sd.enums import SDState


class Color(StrEnum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


class Size(StrEnum):
    S = "S"
    M = "M"
    L = "L"


class SampleProductAnnotated(BaseModel):
    name: str
    color: Annotated[Color | str, lenient_enum(Color)]
    size: Annotated[Size | str, lenient_enum(Size)]

    model_config = {"extra": "forbid"}


class TestLenientEnumFunction:
    def test_valid_enum_string_converts_to_enum(self) -> None:
        p = SampleProductAnnotated(name="T恤", color="RED", size="M")
        assert p.color == Color.RED
        assert p.size == Size.M

    def test_valid_enum_instance_passes_through(self) -> None:
        p = SampleProductAnnotated(name="T恤", color=Color.BLUE, size=Size.L)
        assert p.color == Color.BLUE
        assert p.size == Size.L

    def test_invalid_string_raises_in_python_mode(self) -> None:
        with pytest.raises(ValueError, match="必须为有效的枚举值"):
            SampleProductAnnotated(name="T恤", color="YELLOW", size="XXL")

    def test_invalid_json_string_passes_through(self) -> None:
        p = SampleProductAnnotated.model_validate_json(
            json.dumps({"name": "T恤", "color": "YELLOW", "size": "XXL"})
        )
        assert p.color == "YELLOW"
        assert p.size == "XXL"

    def test_valid_json_string_converts_to_enum(self) -> None:
        p = SampleProductAnnotated.model_validate_json(
            json.dumps({"name": "T恤", "color": "RED", "size": "M"})
        )
        assert p.color == Color.RED
        assert p.size == Size.M


class TestGeneratedSDModels:
    def test_valid_enum_field(self) -> None:
        f = SDCampaignNameFilter(include=["abc"], queryTermMatchType="BROAD_MATCH")
        assert f.queryTermMatchType == SDCampaignNameFilterType.BROAD_MATCH

    def test_valid_enum_instance_field(self) -> None:
        f = SDCampaignNameFilter(
            include=["abc"], queryTermMatchType=SDCampaignNameFilterType.EXACT_MATCH
        )
        assert f.queryTermMatchType == SDCampaignNameFilterType.EXACT_MATCH

    def test_invalid_enum_field_raises(self) -> None:
        with pytest.raises(ValueError, match="必须为有效的枚举值"):
            SDCampaignNameFilter(include=["abc"], queryTermMatchType="INVALID")

    def test_invalid_json_enum_field_passes(self) -> None:
        f = SDCampaignNameFilter.model_validate_json(
            '{"include": ["abc"], "queryTermMatchType": "BROAD_MATCH1"}',
            extra="ignore",
        )
        assert f.queryTermMatchType == "BROAD_MATCH1"

    def test_valid_json_enum_field_converts(self) -> None:
        f = SDCampaignNameFilter.model_validate_json(
            '{"include": ["abc"], "queryTermMatchType": "BROAD_MATCH"}',
            extra="ignore",
        )
        assert f.queryTermMatchType == SDCampaignNameFilterType.BROAD_MATCH

    def test_state_field_accepts_valid_enum(self) -> None:
        from async_amazon_ads_api_v1.models.sd.campaigns import SDCampaign

        data = {
            "adProduct": "SPONSORED_DISPLAY",
            "budgets": [],
            "campaignId": "123",
            "costType": "CPC",
            "creationDateTime": "2024-01-01T00:00:00Z",
            "lastUpdatedDateTime": "2024-01-01T00:00:00Z",
            "marketplaceScope": "SINGLE_MARKETPLACE",
            "name": "Test",
            "startDateTime": "2024-01-01T00:00:00Z",
            "state": "ENABLED",
        }
        c = SDCampaign.model_validate(data)
        assert c.state == SDState.ENABLED

    def test_state_field_accepts_invalid_string_via_json(self) -> None:
        from async_amazon_ads_api_v1.models.sd.campaigns import SDCampaign

        data = {
            "adProduct": "SPONSORED_DISPLAY",
            "budgets": [],
            "campaignId": "123",
            "costType": "CPC",
            "creationDateTime": "2024-01-01T00:00:00Z",
            "lastUpdatedDateTime": "2024-01-01T00:00:00Z",
            "marketplaceScope": "SINGLE_MARKETPLACE",
            "name": "Test",
            "startDateTime": "2024-01-01T00:00:00Z",
            "state": "UNKNOWN_STATE",
        }
        c = SDCampaign.model_validate_json(json.dumps(data))
        assert c.state == "UNKNOWN_STATE"

    def test_state_field_raises_for_invalid_string_in_python(self) -> None:
        from async_amazon_ads_api_v1.models.sd.campaigns import SDCampaign

        data = {
            "adProduct": "SPONSORED_DISPLAY",
            "budgets": [],
            "campaignId": "123",
            "costType": "CPC",
            "creationDateTime": "2024-01-01T00:00:00Z",
            "lastUpdatedDateTime": "2024-01-01T00:00:00Z",
            "marketplaceScope": "SINGLE_MARKETPLACE",
            "name": "Test",
            "startDateTime": "2024-01-01T00:00:00Z",
            "state": "UNKNOWN_STATE",
        }
        with pytest.raises(ValueError, match="必须为有效的枚举值"):
            SDCampaign.model_validate(data)
