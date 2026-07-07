"""Auto-generated Pydantic models for SB from Amazon Ads API schema."""

from __future__ import annotations

import async_amazon_ads_api_v1.errors as _core_errors

from . import (
    ad_extensions,
    ad_groups,
    ads,
    advertising_deal_targets,
    advertising_deals,
    branded_keywords_pricings,
    campaigns,
    enums,
    keyword_reservation_validations,
    recommendation_types,
    recommendations,
    reserved_target_pricings,
    shared,
    targets,
)

_ns: dict = {}
_ns.update(vars(ad_extensions))
_ns.update(vars(ad_groups))
_ns.update(vars(ads))
_ns.update(vars(advertising_deal_targets))
_ns.update(vars(advertising_deals))
_ns.update(vars(branded_keywords_pricings))
_ns.update(vars(campaigns))
_ns.update(vars(enums))
_ns.update(vars(keyword_reservation_validations))
_ns.update(vars(recommendation_types))
_ns.update(vars(recommendations))
_ns.update(vars(reserved_target_pricings))
_ns.update(vars(shared))
_ns.update(vars(targets))
_ns.update(vars(_core_errors))
for _name, _obj in list(_ns.items()):
    if (
        isinstance(_obj, type)
        and hasattr(_obj, "model_rebuild")
        and getattr(_obj, "__module__", "").startswith("async_amazon_ads_api_v1.models")
    ):
        _obj.model_rebuild(_types_namespace=_ns)
