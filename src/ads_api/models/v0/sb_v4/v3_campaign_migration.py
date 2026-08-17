"""Auto-generated models for V3 Campaign Migration from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class CampaignMigrationFinalStatus(LenientModel):
    legacyCampaignId: str | None = Field(default=None, description="Entity object identifier.")
    newCampaignId: str | None = Field(default=None)
    migrationStatus: str | None = Field(default=None, description="Enumerated status code for migration job status")
    migrationStatusReason: str | None = Field(default=None, description="Status reason for the given migration status")


class MigrationJobResultsRequestContent(StrictModel):
    jobId: str
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class MigrationJobResultsResponseContent(LenientModel):
    jobId: str | None = Field(default=None)
    migrationJobStatus: str | None = Field(default=None, description="Enumerated status code for migration job status")
    campaigns: list[CampaignMigrationFinalStatus] | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class MigrationJobStatusRequestContent(StrictModel):
    jobId: str


class MigrationJobStatusResponseContent(LenientModel):
    jobId: str | None = Field(default=None)
    migrationJobStatus: str | None = Field(default=None, description="Enumerated status code for migration job status")
    migrationJobStatusReason: str | None = Field(default=None, description="Status reason for the migration job status")


class MigrationResultsRequestContent(StrictModel):
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class MigrationResultsResponseContent(LenientModel):
    campaigns: list[CampaignMigrationFinalStatus] | None = Field(default=None)
    nextToken: str | None = Field(
        default=None, description="Token value allowing to navigate to the next response page."
    )


class StartMigrationJobRequestContent(StrictModel):
    campaignIds: list[str] = Field(
        min_length=0, max_length=1000, description="Provide list of campaign ids that needs to be migrated"
    )
    isStagedMigration: bool | None = Field(
        default=None,
        description="""
Set this flag to true if you want generate new campaign ID based on V3 campaign ID. These campaigns will not be visible through V4 campaign list call. If set to true not all campaign entities such as ad group, targeting, ad, or creatives are created. Use this flag for staging purpose only.
By default it will always be false
""",
    )
    newCampaignState: str | None = Field(
        default=None,
        description="""
This is optional parameter. By default, the new migrated campaigns will have the original status of V3 campaigns. If this parameter is set, then all newly migrated campaigns will have this state.
 Supported campaign states
""",
    )
    enableThemeTargeting: bool = Field(
        description="By default, theme targeting is set true if no value is provide. To disable theme targeting, set this flag to false."
    )
    brandEntityId: str | None = Field(
        default=None,
        description="Please note that brandEntityId is only required for sellers. You can get the brandEntityId by calling the <a href = https://advertising.amazon.com/API/docs/en-us/sponsored-brands/3-0/openapi#tag/Brands/operation/getBrands>GET /brands</a> endpoint.",
    )


class StartMigrationJobResponseContent(LenientModel):
    jobId: str | None = Field(
        default=None,
        description="""
This jobId can be used to track migration status through /sb/v4/legacyCampaigns/migrationJob/status
and results of each campaign through /sb/v4/legacyCampaigns/migrationJob/results API
""",
    )


__all__ = [
    "CampaignMigrationFinalStatus",
    "MigrationJobResultsRequestContent",
    "MigrationJobResultsResponseContent",
    "MigrationJobStatusRequestContent",
    "MigrationJobStatusResponseContent",
    "MigrationResultsRequestContent",
    "MigrationResultsResponseContent",
    "StartMigrationJobRequestContent",
    "StartMigrationJobResponseContent",
]
