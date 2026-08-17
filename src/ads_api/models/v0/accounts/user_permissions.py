"""Auto-generated models for user_permissions from Amazon Ads API v0."""

from __future__ import annotations

from enum import StrEnum
from typing import Annotated

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel
from ads_api.models._core.lenient_enum import lenient_enum


class AccessScope(StrEnum):
    ALL = "ALL"
    DIRECT = "DIRECT"
    EFFECTIVE = "EFFECTIVE"
    INDIRECT = "INDIRECT"


class CountryCode(StrEnum):
    AE = "AE"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CL = "CL"
    CO = "CO"
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
    NG = "NG"
    NL = "NL"
    PL = "PL"
    SA = "SA"
    SE = "SE"
    SG = "SG"
    TR = "TR"
    US = "US"
    ZA = "ZA"


class Role(StrEnum):
    ADMIN = "ADMIN"
    EDITOR = "EDITOR"
    VIEWER = "VIEWER"


class Type(StrEnum):
    CUSTOM_PERMISSION_SET = "CUSTOM_PERMISSION_SET"
    ROLE = "ROLE"


class AccessScopeFilter(StrictModel):
    include: list[Annotated[AccessScope, lenient_enum(AccessScope)]] | None = Field(
        default=None, min_length=1, max_length=1
    )


class CountryCodesFilter(StrictModel):
    include: list[Annotated[CountryCode, lenient_enum(CountryCode)]] | None = Field(
        default=None, min_length=0, max_length=100
    )


class DeleteUserPermissionsError(LenientModel):
    code: str | None = Field(default=None)
    countries: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None, min_length=0, max_length=100
    )
    message: str | None = Field(default=None)
    userId: str | None = Field(
        default=None, description="User ID of the user that had an error when their permissions were deleted"
    )


class DeleteUserPermissionsRequestContent(StrictModel):
    users: list[UserId] | None = Field(default=None, min_length=1, max_length=200)


class DeleteUserPermissionsResponseContent(LenientModel):
    errors: list[DeleteUserPermissionsError] | None = Field(default=None)
    successes: list[DeleteUserPermissionsSuccess] | None = Field(default=None)


class DeleteUserPermissionsSuccess(LenientModel):
    userId: str | None = Field(default=None, description="User ID of the user having their permissions deleted")


class ListUsersRequestContent(StrictModel):
    accessScopeFilter: AccessScopeFilter | None = Field(default=None)
    countryCodesFilter: CountryCodesFilter | None = Field(default=None)
    maxResults: float | None = Field(default=None, ge=1, le=100, description="Max results for pagination")
    nextToken: str | None = Field(
        default=None, description="The pagination token that is required to go to the next page"
    )


class ListUsersResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    users: list[User] | None = Field(default=None, min_length=0, max_length=100)


class Permission(LenientModel):
    accessLevel: str | None = Field(default=None)
    countryCodes: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None, min_length=0, max_length=100
    )
    id: str | None = Field(default=None)
    resourceType: str | None = Field(default=None)


class PermissionId(StrictModel):
    name: str | None = Field(default=None)


class PermissionSet(StrictModel):
    customPermissionSet: list[PermissionId] | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="""
If type = CUSTOM_PERMISSION_SET, indicates the permissions of the invitation.
Different permissions are supported for different account types.
  - Amazon DSP Advertising Accounts: campaign_edit, creatives_edit, reports_edit, reports_limited
  - Sponsored Ads Accounts: campaign_edit, campaign_view, reports_view, brand_posts_edit, store_edit,
  payment_method_edit, payment_method_view billing_edit, billing_view, user_edit
  - Manager accounts do not support custom permissions
  - Marketing Cloud Accounts do not support custom permissions
""",
    )
    role: Annotated[Role, lenient_enum(Role)] | None = Field(default=None)
    type: Annotated[Type, lenient_enum(Type)]


class QueryUserPermissionsRequestContent(StrictModel):
    accessScopeFilter: AccessScopeFilter | None = Field(default=None)
    countryCodesFilter: CountryCodesFilter | None = Field(default=None)
    maxResults: float | None = Field(default=None, ge=1, le=100, description="Max results for pagination")
    nextToken: str | None = Field(
        default=None, description="The pagination token that is required to go to the next page"
    )
    userId: str = Field(max_length=150, pattern="\\S*", description="User ID for the request")


class QueryUserPermissionsResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    permissions: list[Permission] | None = Field(default=None, min_length=0, max_length=100)


class QueryUserRolesRequestContent(StrictModel):
    countryCodesFilter: CountryCodesFilter | None = Field(default=None)
    maxResults: float | None = Field(default=None, ge=1, le=100, description="Max results for pagination")
    nextToken: str | None = Field(
        default=None, description="The pagination token that is required to go to the next page"
    )
    userId: str = Field(
        max_length=150,
        pattern="\\S*",
        description="This represents the userId of the target of the QueryUserRoles call",
    )


class QueryUserRolesResponseContent(LenientModel):
    nextToken: str | None = Field(
        default=None, description="token value allowing to navigate to the next response page"
    )
    roles: list[RoleForCountries] | None = Field(default=None, min_length=0, max_length=5)


class RoleForCountries(LenientModel):
    countryCodes: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="""
The roles for an account are associated to a specific country/countries
These roles may differ per countries
""",
    )
    permissions: list[str] | None = Field(
        default=None,
        min_length=0,
        max_length=200,
        description="""
List of granular permission strings populated when type is CUSTOM_PERMISSION_SET
and accessType is EXTERNAL.
""",
    )
    role: Annotated[Role | str, lenient_enum(Role)] | None = Field(default=None)
    type: Annotated[Type | str, lenient_enum(Type)] | None = Field(default=None)


class UpdateUserPermissionsError(LenientModel):
    code: str | None = Field(default=None)
    message: str | None = Field(default=None)
    userId: str | None = Field(default=None, description="User ID of the user having their permissions updated")


class UpdateUserPermissionsRequestContent(StrictModel):
    userPermissions: list[UserPermission] | None = Field(default=None)


class UpdateUserPermissionsResponseContent(LenientModel):
    errors: list[UpdateUserPermissionsError] | None = Field(default=None)
    successes: list[UpdateUserPermissionsSuccess] | None = Field(default=None)


class UpdateUserPermissionsSuccess(LenientModel):
    userId: str | None = Field(default=None, description="User ID of the user having their permissions updated")


class User(LenientModel):
    countryCodes: list[Annotated[CountryCode | str, lenient_enum(CountryCode)]] | None = Field(
        default=None, min_length=0, max_length=100
    )
    emailAddress: str
    userId: str


class UserId(StrictModel):
    userId: str | None = Field(default=None)


class UserPermission(StrictModel):
    countryCodes: list[Annotated[CountryCode, lenient_enum(CountryCode)]] | None = Field(
        default=None,
        min_length=0,
        max_length=100,
        description="""
List of two-letter ISO 3166 country codes that the user is having permissions edited for. Only valid for updates
to global accounts.
""",
    )
    permissionSet: PermissionSet | None = Field(default=None)
    userId: str | None = Field(default=None, description="User ID of the user having their permissions updated")


__all__ = [
    "AccessScope",
    "AccessScopeFilter",
    "CountryCode",
    "CountryCodesFilter",
    "DeleteUserPermissionsError",
    "DeleteUserPermissionsRequestContent",
    "DeleteUserPermissionsResponseContent",
    "DeleteUserPermissionsSuccess",
    "ListUsersRequestContent",
    "ListUsersResponseContent",
    "Permission",
    "PermissionId",
    "PermissionSet",
    "QueryUserPermissionsRequestContent",
    "QueryUserPermissionsResponseContent",
    "QueryUserRolesRequestContent",
    "QueryUserRolesResponseContent",
    "Role",
    "RoleForCountries",
    "Type",
    "UpdateUserPermissionsError",
    "UpdateUserPermissionsRequestContent",
    "UpdateUserPermissionsResponseContent",
    "UpdateUserPermissionsSuccess",
    "User",
    "UserId",
    "UserPermission",
]
