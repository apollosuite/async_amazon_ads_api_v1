"""Auto-generated models for Identity Deletion from Amazon Ads API v0."""

from __future__ import annotations

from pydantic import Field

from ads_api.models._core.base import StrictModel
from ads_api.models.v0._shared import (
    ExternalIdentity,
    HashedPii,
    Identity,
)


class DeleteIdentityRequestContent(StrictModel):
    """The DeleteIdentityRequest represents a request to delete one or more user identities.
    It includes a list of target identities to be deleted, along with common headers."""

    targetIdentities: list[TargetIdentity] = Field(
        min_length=1,
        max_length=1000,
        description="""
A list of identities to be deleted from manager account id.
Each identity is either a single supported ExternalUserId or a collection of externalIdentities , maid or Hashed PII values representing a single user.
""",
    )


class TargetIdentityExternalUserId(StrictModel):
    externalUserId: str


class TargetIdentityIdentity(StrictModel):
    identity: Identity


type TargetIdentity = TargetIdentityExternalUserId | TargetIdentityIdentity

__all__ = ["DeleteIdentityRequestContent", "ExternalIdentity", "HashedPii", "Identity", "TargetIdentity"]
