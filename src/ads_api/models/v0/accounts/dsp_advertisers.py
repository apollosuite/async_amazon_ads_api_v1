"""Auto-generated models for Advertiser from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel
from ads_api.models._core.lenient_enum import lenient_enum


class DspCountryV1(StrEnum):
    """
    The country code.
    """

    US = "US"
    CA = "CA"
    MX = "MX"
    JP = "JP"
    AU = "AU"
    IN = "IN"
    UK = "UK"
    GB = "GB"
    DE = "DE"
    FR = "FR"
    IT = "IT"
    ES = "ES"
    AT = "AT"
    AE = "AE"
    SA = "SA"
    BR = "BR"
    NL = "NL"
    SE = "SE"
    SG = "SG"
    TR = "TR"


class DspSupportedCurrencyV1(StrEnum):
    """
    The supported currencies.
    """

    USD = "USD"
    CAD = "CAD"
    JPY = "JPY"
    GBP = "GBP"
    EUR = "EUR"
    INR = "INR"
    MXN = "MXN"
    AED = "AED"
    SAR = "SAR"
    BRL = "BRL"
    AUD = "AUD"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"


class DspAdvertiserV1(LenientModel):
    """The DSP Advertiser object"""

    advertiserId: str | None = Field(default=None, description="The advertiser identifier.")
    name: str | None = Field(default=None, description="The advertiser name.")
    currency: Annotated[DspSupportedCurrencyV1 | str, lenient_enum(DspSupportedCurrencyV1)] | None = Field(default=None)
    url: str | None = Field(default=None, description="The URL of the advertiser’s website.")
    country: Annotated[DspCountryV1 | str, lenient_enum(DspCountryV1)] | None = Field(default=None)
    timezone: DspTimezoneV1 | None = Field(default=None)
    isRegional: bool | None = Field(
        default=None, description="Set to `true` if account is associated with a Global Advertiser Account."
    )


class DspAdvertisersV1(LenientModel):
    """List of advertisers along with total number of advertisers which satisfy the filtering criteria."""

    totalResults: int | None = Field(
        default=None,
        description="Total number of advertisers which satisfy the filtering criteria. This number is given to support pagination and tell the client if there are more advertisers to be fetched.",
    )
    response: list[DspAdvertiserV1] | None = Field(
        default=None, description="List of advertisers with complete information."
    )


type DspTimezoneV1 = str

__all__ = ["DspAdvertiserV1", "DspAdvertisersV1", "DspCountryV1", "DspSupportedCurrencyV1", "DspTimezoneV1"]
