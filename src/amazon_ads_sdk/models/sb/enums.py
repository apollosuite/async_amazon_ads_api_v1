"""Auto-generated Pydantic models for sb from Amazon Ads API schema."""

from __future__ import annotations

from amazon_ads_sdk.models.base import SafeStrEnum


class SBAdProduct(SafeStrEnum):
    """| AdProduct | Description |
    |------|------|
    | `SPONSORED_BRANDS` | Sponsored Brands ad product. |
    """

    SPONSORED_BRANDS = "SPONSORED_BRANDS"


class SBAdvertisingDealPriceType(SafeStrEnum):
    """| AdvertisingDealPriceType | Description |
    |------|------|
    | `FIXED_PRICE` | Sale price for a specific ad placement regardless of auction performance. |
    """

    FIXED_PRICE = "FIXED_PRICE"


class SBCreateState(SafeStrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

    | CreateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class SBCurrencyCode(SafeStrEnum):
    """| CurrencyCode | Description |
    |------|------|
    | `AED` | United Arab Emirates Dirham |
    | `AUD` | Australian Dollar |
    | `BRL` | Brazilian Real |
    | `CAD` | Canadian Dollar |
    | `CHF` | Swiss Franc |
    | `CNY` | Chinese Yuan |
    | `DKK` | Danish Krone |
    | `EGP` | Egyptian Pound |
    | `EUR` | Euro |
    | `GBP` | British Pound Sterling |
    | `INR` | Indian Rupee |
    | `JPY` | Japanese Yen |
    | `MXN` | Mexican Peso |
    | `MXP` | Mexican Peso |
    | `NGN` | Nigerian Naira |
    | `NOK` | Norwegian Krone |
    | `NZD` | New Zealand Dollar |
    | `PLN` | Polish Złoty |
    | `SAR` | Saudi Riyal |
    | `SEK` | Swedish Krona |
    | `SGD` | Singapore Dollar |
    | `TRY` | Turkish Lira |
    | `USD` | United States Dollar |
    | `ZAR` | South African Rand |
    """

    AED = "AED"
    AUD = "AUD"
    BRL = "BRL"
    CAD = "CAD"
    CHF = "CHF"
    CNY = "CNY"
    DKK = "DKK"
    EGP = "EGP"
    EUR = "EUR"
    GBP = "GBP"
    INR = "INR"
    JPY = "JPY"
    MXN = "MXN"
    MXP = "MXP"
    NGN = "NGN"
    NOK = "NOK"
    NZD = "NZD"
    PLN = "PLN"
    SAR = "SAR"
    SEK = "SEK"
    SGD = "SGD"
    TRY = "TRY"
    USD = "USD"
    ZAR = "ZAR"


class SBMarketplace(SafeStrEnum):
    """A list of country codes representing Amazon marketplaces

    | Marketplace | Description |
    |------|------|
    | `AE` |  |
    | `AU` |  |
    | `BE` |  |
    | `BR` |  |
    | `CA` |  |
    | `DE` |  |
    | `EG` |  |
    | `ES` |  |
    | `FR` |  |
    | `GB` |  |
    | `IE` |  |
    | `IN` |  |
    | `IT` |  |
    | `JP` |  |
    | `MX` |  |
    | `NL` |  |
    | `PL` |  |
    | `SA` |  |
    | `SE` |  |
    | `SG` |  |
    | `TR` |  |
    | `US` |  |
    | `ZA` |  |
    """

    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    DE = "DE"
    EG = "EG"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IE = "IE"
    IN = "IN"
    IT = "IT"
    JP = "JP"
    MX = "MX"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class SBMarketplaceScope(SafeStrEnum):
    """| MarketplaceScope | Description |
    |------|------|
    | `SINGLE_MARKETPLACE` |  |
    """

    SINGLE_MARKETPLACE = "SINGLE_MARKETPLACE"


class SBProductIdType(SafeStrEnum):
    """| ProductIdType | Description |
    |------|------|
    | `ASIN` | ASIN identifier type. |
    """

    ASIN = "ASIN"


class SBState(SafeStrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

    | State | Description |
    |------|------|
    | `ARCHIVED` | The object is permanently stopped and cannot be reactivated. Terminal end state. |
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ARCHIVED = "ARCHIVED"
    ENABLED = "ENABLED"
    PAUSED = "PAUSED"


class SBUpdateState(SafeStrEnum):
    """The user defined state for the resource. For ADSP, campaign and ad group resources can only be created in the PAUSED state and must be updated to ENABLED to activate for delivery

    | UpdateState | Description |
    |------|------|
    | `ENABLED` | The object is set active by user and eligible for delivery. |
    | `PAUSED` | The object is stopped by user and not eligible for delivery. |
    """

    ENABLED = "ENABLED"
    PAUSED = "PAUSED"
