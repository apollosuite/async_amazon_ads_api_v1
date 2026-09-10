"""Auto-generated models for targetable_entities from Amazon Ads API v0."""

from __future__ import annotations

from typing import Literal

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel

type AdProduct = Literal["SPONSORED_BRANDS", "SPONSORED_DISPLAY", "SPONSORED_PRODUCTS", "SPONSORED_TELEVISION"]


type Locale = Literal[
    "ar_AE",
    "de_DE",
    "en_AE",
    "en_AU",
    "en_CA",
    "en_GB",
    "en_IN",
    "en_SG",
    "en_US",
    "en_ZA",
    "es_ES",
    "es_MX",
    "fr_CA",
    "fr_FR",
    "hi_IN",
    "it_IT",
    "ja_JP",
    "ko_KR",
    "nl_NL",
    "pl_PL",
    "pt_BR",
    "sv_SE",
    "ta_IN",
    "th_TH",
    "tr_TR",
    "vi_VN",
    "zh_CN",
]


type TargetType = Literal["AUDIENCE", "CONTENT_CATEGORY", "PRODUCT_CATEGORY", "PRODUCT_CATEGORY_AUDIENCE"]
"""
A targeting type
"""


class ListTargetableEntitiesRequestContent(StrictModel):
    adProduct: AdProduct
    locale: Locale | None = Field(default=None)
    maxResults: float | None = Field(
        default=None, ge=1, le=250, description="Number of records to include in the paginated response."
    )
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    parentBrowseNodeIdFilter: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Filter by parent browse node IDs. Returns entities whose parent category matches any of the provided IDs.",
    )
    pathsFilter: list[list[str]] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="""
Get direct descendant sub paths that fall under the paths specified in the field value.
The value is a list of paths, where each object is a path hierarchy represented as a list of strings.
For Example: If you would like to get direct descendants under the path "Apps & Games"
then the field value would be [["Apps & Games"]]
""",
    )
    productCategoryIdFilter: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=1000,
        description="Filter by product category IDs (browse node IDs). Returns entities matching any of the provided IDs.",
    )
    searchQueryFilter: str | None = Field(
        default=None,
        description="""
The query string used to filter targetable entities. Search for terms or phrases
that are relevant to your advertising goals. For example, if you sell running shoes,
you might search for "Runners", "Athletic Apparel", or "Fitness Enthusiasts" to find
the best targetable entities for your advertising goals.
""",
    )
    targetTypeFilter: list[TargetType] | None = Field(
        default=None,
        min_length=0,
        max_length=4,
        description="""
A list of targeting types. If an empty list is provided, it is equivalent
to passing all targeting types.
""",
    )


class ListTargetableEntitiesResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    targetableEntities: list[TargetableEntity] | None = Field(
        default=None, min_length=0, max_length=250, description="The list of targetable entities."
    )
    totalResults: float | None = Field(default=None, description="The total number of entities.")


class ListTargetableEntityPathsRequestContent(StrictModel):
    adProduct: AdProduct
    locale: Locale | None = Field(default=None)
    pathsFilter: list[list[str]] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="""
Get direct descendant sub paths that fall under the paths specified in the field value.
The value is a list of paths, where each object is a path hierarchy represented as a list of strings.
For Example: If you would like to get direct descendants under the path "Apps & Games"
then the field value would be [["Apps & Games"]]
""",
    )


class ListTargetableEntityPathsResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )
    paths: list[list[str]] | None = Field(
        default=None,
        min_length=0,
        max_length=10,
        description="""
The direct descendants of the paths specified in the
request's pathsFilter field.
""",
    )
    totalResults: float | None = Field(default=None, description="The total number of entities.")


class TargetableEntity(LenientModel):
    """A targetable entity."""

    audienceId: str | None = Field(default=None, description="The identifier for a target of type AUDIENCE.")
    audienceResolved: str | None = Field(default=None, description="The resolved name of audienceId.")
    audienceTooltip: str | None = Field(
        default=None, description="The tooltip description to describe the amazon audience targetable entity."
    )
    behaviouralTargetingEligibility: str | None = Field(
        default=None,
        description="""
The behavioural targeting eligibility for this browse node category.
Values from Tamber browse-node-targeting-policy-validation dataset:
"All" (eligible for behavioural targeting), "None" (not eligible).
""",
    )
    childCount: float | None = Field(default=None, description="The number of direct child categories.")
    contentCategoryId: str | None = Field(
        default=None, description="The identifier for a target of type CONTENT_CATEGORY."
    )
    contentCategoryResolved: str | None = Field(default=None, description="The resolved name of contentCategoryId.")
    parentBrowseNodeId: str | None = Field(default=None, description="The browse node ID of the parent category.")
    path: list[str] = Field(
        min_length=0, max_length=10, description="The location of the targetable entity in Amazon's taxonomy."
    )
    pathNodeIds: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=50,
        description="The browse node IDs for each segment in the path hierarchy.",
    )
    productCategoryId: str | None = Field(
        default=None,
        description="The identifier for a target of either type PRODUCT_CATEGORY or PRODUCT_CATEGORY_AUDIENCE.",
    )
    productCategoryResolved: str | None = Field(default=None, description="The resolved name of productCategoryId.")
    targetType: TargetType | str


__all__ = [
    "AdProduct",
    "ListTargetableEntitiesRequestContent",
    "ListTargetableEntitiesResponseContent",
    "ListTargetableEntityPathsRequestContent",
    "ListTargetableEntityPathsResponseContent",
    "Locale",
    "TargetType",
    "TargetableEntity",
]
