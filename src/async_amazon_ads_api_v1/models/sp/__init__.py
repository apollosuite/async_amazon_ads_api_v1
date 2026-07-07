"""Auto-generated Pydantic models for SP from Amazon Ads API schema."""

from __future__ import annotations

import async_amazon_ads_api_v1.errors as _core_errors

from . import ad_extensions, ad_groups, ads, campaigns, enums, shared, targets

_ns: dict = {}
_ns.update(vars(ad_extensions))
_ns.update(vars(ad_groups))
_ns.update(vars(ads))
_ns.update(vars(campaigns))
_ns.update(vars(enums))
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
