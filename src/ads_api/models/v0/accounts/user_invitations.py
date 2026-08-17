"""Auto-generated models for user_invitations from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import LenientModel, StrictModel


class Country(StrictModel):
    countryCode: str | None = Field(default=None)


class CountryOut(LenientModel):
    countryCode: str | None = Field(default=None)


class CreateUserInvitationsRequestContent(StrictModel):
    notifyInvitedUsers: bool | None = Field(
        default=None,
        description="""
Indicates if an invitation email will be sent to the invited user. This email will direct users to the Amazon
Ads Console to redeem their invitation. Default value: false
""",
    )
    userInvitationRequests: list[UserInvitationRequest] = Field(
        min_length=1, max_length=50, description="List of invitations to be sent to users."
    )


class CreateUserInvitationsResponseContent(LenientModel):
    errors: list[InvitationError] | None = Field(default=None, min_length=0, max_length=50)
    successes: list[UserInvitation] | None = Field(default=None)


class GetUserInvitationResponseContent(LenientModel):
    invitation: UserInvitation | None = Field(default=None)
    termsTypes: list[str] | None = Field(default=None)


class InvitationError(LenientModel):
    errorCode: str | None = Field(default=None)
    errorDetail: str | None = Field(default=None)
    errorMessage: str | None = Field(default=None)
    identifier: str | None = Field(default=None)


class ListUserInvitationsRequestContent(StrictModel):
    maxResults: float | None = Field(default=None, ge=1, le=50, description="Max results to fetch per page.")
    nextToken: str | None = Field(default=None, description="Identifier of the next pagination token.")


class ListUserInvitationsResponseContent(LenientModel):
    invitations: list[UserInvitation] | None = Field(default=None)
    nextToken: str | None = Field(default=None)


class Permission(StrictModel):
    name: str | None = Field(default=None)


class PermissionOut(LenientModel):
    name: str | None = Field(default=None)


class PermissionSet(StrictModel):
    customPermissionSet: list[Permission] | None = Field(
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
    role: Role | None = Field(default=None)
    type: str | None = Field(
        default=None, description="Type of permission set. Supported values: ROLE, CUSTOM_PERMISSION_SET"
    )


class PermissionSetOut(LenientModel):
    customPermissionSet: list[PermissionOut] | None = Field(
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
    role: RoleOut | None = Field(default=None)
    type: str | None = Field(
        default=None, description="Type of permission set. Supported values: ROLE, CUSTOM_PERMISSION_SET"
    )


class RedeemUserInvitationRequestContent(StrictModel):
    invitationId: str = Field(description="Identifier of the invitation to be redeemed.")


class Role(StrictModel):
    name: str | None = Field(default=None)


class RoleOut(LenientModel):
    name: str | None = Field(default=None)


class Update(StrictModel):
    invitationId: str = Field(description="Identifier of the invitation you want to update.")
    state: str = Field(description="""
State to change your invitation to.
Support states: REVOKED, RESENT.
""")


class UpdateOut(LenientModel):
    invitationId: str = Field(description="Identifier of the invitation you want to update.")
    state: str = Field(description="""
State to change your invitation to.
Support states: REVOKED, RESENT.
""")


class UpdateUserInvitationsRequestContent(StrictModel):
    notifyInvitedUsers: bool | None = Field(
        default=None,
        description="""
Indicates if an invitation email will be sent to the invited user. This email will direct users to the Amazon
Ads Console to redeem their invitation. Default value: false
""",
    )
    updates: list[Update] = Field(
        min_length=1, max_length=50, description="List of updates to perform for a set of invitations."
    )


class UpdateUserInvitationsResponseContent(LenientModel):
    errors: list[InvitationError] | None = Field(default=None, min_length=0, max_length=50)
    successes: list[UpdateOut] | None = Field(default=None, min_length=1, max_length=50)


class User(StrictModel):
    emailAddress: str = Field(description="Email address of the user to be invited")
    userName: str = Field(description="Name of the user to be invited")


class UserInvitation(LenientModel):
    countries: list[CountryOut] | None = Field(default=None, min_length=1, max_length=100)
    createdAt: float | None = Field(default=None)
    createdBy: str | None = Field(default=None)
    expiration: float | None = Field(default=None)
    invitationId: str | None = Field(default=None)
    permissionSet: PermissionSetOut | None = Field(default=None)
    state: str | None = Field(default=None)
    targetId: str | None = Field(default=None)
    user: UserOut | None = Field(default=None)


class UserInvitationRequest(StrictModel):
    countries: list[Country] | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="""
List of two-letter ISO 3166 country codes that the user is invited to. Only valid for invitations
to global accounts.
""",
    )
    permissionSet: PermissionSet | None = Field(default=None)
    user: User | None = Field(default=None)


class UserOut(LenientModel):
    emailAddress: str = Field(description="Email address of the user to be invited")
    userName: str = Field(description="Name of the user to be invited")


__all__ = [
    "Country",
    "CountryOut",
    "CreateUserInvitationsRequestContent",
    "CreateUserInvitationsResponseContent",
    "GetUserInvitationResponseContent",
    "InvitationError",
    "ListUserInvitationsRequestContent",
    "ListUserInvitationsResponseContent",
    "Permission",
    "PermissionOut",
    "PermissionSet",
    "PermissionSetOut",
    "RedeemUserInvitationRequestContent",
    "Role",
    "RoleOut",
    "Update",
    "UpdateOut",
    "UpdateUserInvitationsRequestContent",
    "UpdateUserInvitationsResponseContent",
    "User",
    "UserInvitation",
    "UserInvitationRequest",
    "UserOut",
]
