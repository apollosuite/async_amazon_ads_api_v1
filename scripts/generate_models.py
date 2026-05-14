"""Code generator: generates Pydantic models from the OpenAPI schema JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent.parent / "AmazonAdsAPISPMerged_prod_3p.json"

HEADER = '''"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict
'''

ENUMS_IMPORT = '''"""Auto-generated Pydantic models from Amazon Ads API schema."""

from __future__ import annotations

from enum import StrEnum
'''

MODULE_IMPORTS = {
    "_enums.py": ENUMS_IMPORT,
    "_errors.py": '''"""error and HTTP response models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_shared.py": '''"""shared models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_bids.py": '''"""bid adjustment models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_creatives.py": '''"""creative models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_budgets.py": '''"""budget models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_campaigns.py": '''"""campaign models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_ad_groups.py": '''"""ad_group models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_ads.py": '''"""ad models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_targets.py": '''"""target models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_ad_extensions.py": '''"""ad_extension models."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict
''',
}

# ── Entity model grouping ───────────────────────────────────────────────────

CAMPAIGN_NAMES = {
    "SPCampaign",
    "SPCampaignAdProductFilter",
    "SPCampaignCampaignIdFilter",
    "SPCampaignCreate",
    "SPCampaignMultiStatusResponse",
    "SPCampaignMultiStatusSuccess",
    "SPCampaignNameFilter",
    "SPCampaignOptimizations",
    "SPCampaignPortfolioIdFilter",
    "SPCampaignStateFilter",
    "SPCampaignSuccessResponse",
    "SPCampaignUpdate",
    "SPCreateCampaignOptimizations",
    "SPUpdateCampaignOptimizations",
    "SPCreateCampaignRequest",
    "SPDeleteCampaignRequest",
    "SPQueryCampaignRequest",
    "SPUpdateCampaignRequest",
    # cross-resource filter models
    "SPAdCampaignIdFilter",
    "SPTargetCampaignIdFilter",
}

AD_GROUP_NAMES = {
    "SPAdGroup",
    "SPAdGroupAdGroupIdFilter",
    "SPAdGroupAdProductFilter",
    "SPAdGroupBid",
    "SPAdGroupCampaignIdFilter",
    "SPAdGroupCreate",
    "SPAdGroupMultiStatusResponse",
    "SPAdGroupMultiStatusSuccess",
    "SPAdGroupNameFilter",
    "SPAdGroupStateFilter",
    "SPAdGroupSuccessResponse",
    "SPAdGroupUpdate",
    "SPCreateAdGroupBid",
    "SPUpdateAdGroupBid",
    "SPCreateAdGroupRequest",
    "SPDeleteAdGroupRequest",
    "SPQueryAdGroupRequest",
    "SPUpdateAdGroupRequest",
    # cross-resource filter models
    "SPAdAdGroupIdFilter",
    "SPTargetAdGroupIdFilter",
}

AD_NAMES = {
    "SPAd",
    "SPAdAdIdFilter",
    "SPAdAdProductFilter",
    "SPAdCreate",
    "SPAdMultiStatusResponse",
    "SPAdMultiStatusSuccess",
    "SPAdStateFilter",
    "SPAdSuccessResponse",
    "SPAdUpdate",
    "SPCreateAdRequest",
    "SPDeleteAdRequest",
    "SPQueryAdRequest",
    "SPUpdateAdRequest",
}

TARGET_NAMES = {
    "SPTarget",
    "SPTargetCreate",
    "SPTargetUpdate",
    "SPTargetMultiStatusSuccess",
    "SPTargetBid",
    "SPCreateTargetBid",
    "SPUpdateTargetBid",
    "SPTargetDetails",
    "SPCreateTargetDetails",
    "SPKeywordTarget",
    "SPCreateKeywordTarget",
    "SPLocationTarget",
    "SPCreateLocationTarget",
    "SPProductCategoryTarget",
    "SPCreateProductCategoryTarget",
    "SPProductCategoryRefinement",
    "SPCreateProductCategoryRefinement",
    "SPProductCategoryRefinementValue",
    "SPCreateProductCategoryRefinementValue",
    "SPThemeTarget",
    "SPCreateThemeTarget",
    "SPProductTarget",
    "SPCreateProductTarget",
    "SPProductValue",
    "SPCreateProductValue",
    "SPTargetAdProductFilter",
    "SPTargetKeywordFilter",
    "SPTargetMatchTypeFilter",
    "SPTargetMultiStatusResponse",
    "SPTargetNegativeFilter",
    "SPTargetProductIdFilter",
    "SPTargetStateFilter",
    "SPTargetSuccessResponse",
    "SPTargetTargetIdFilter",
    "SPTargetTargetTypeFilter",
    "SPCreateTargetRequest",
    "SPDeleteTargetRequest",
    "SPQueryTargetRequest",
    "SPUpdateTargetRequest",
}

AD_EXTENSION_NAMES = {
    "SPAdExtension",
    "SPAdExtensionAdExtensionIdFilter",
    "SPAdExtensionAdExtensionStatusFilter",
    "SPAdExtensionAdExtensionTypeFilter",
    "SPAdExtensionAdGroupIdFilter",
    "SPAdExtensionAdIdFilter",
    "SPAdExtensionAdProductFilter",
    "SPAdExtensionCreate",
    "SPAdExtensionMultiStatusResponse",
    "SPAdExtensionMultiStatusSuccess",
    "SPAdExtensionSettings",
    "SPAdExtensionStateFilter",
    "SPAdExtensionSuccessResponse",
    "SPAdExtensionUpdate",
    "SPCreateAdExtensionRequest",
    "SPCreateAdExtensionSettings",
    "SPCreatePromptExtension",
    "SPCreateVideoExtension",
    "SPPromptExtension",
    "SPQueryAdExtensionRequest",
    "SPUpdateAdExtensionRequest",
    "SPVideoExtension",
}

ERROR_NAMES = {
    "BadGatewayResponseContent",
    "BadRequestResponseContent",
    "ContentTooLargeResponseContent",
    "Error",
    "ErrorsIndex",
    "ForbiddenResponseContent",
    "GatewayTimeoutResponseContent",
    "InternalServerErrorResponseContent",
    "NotFoundResponseContent",
    "ServiceUnavailableErrorResponseContent",
    "TooManyRequestsResponseContent",
    "UnauthorizedResponseContent",
}

BID_NAMES = {
    "SPAudienceBidAdjustment",
    "SPBidAdjustments",
    "SPBidSettings",
    "SPCreateAudienceBidAdjustment",
    "SPCreateBidAdjustments",
    "SPCreateBidSettings",
    "SPCreateCreativeBidAdjustment",
    "SPCreatePlacementBidAdjustment",
    "SPCreativeBidAdjustment",
    "SPPlacementBidAdjustment",
    "SPUpdateBidAdjustments",
    "SPUpdateBidSettings",
}

CREATIVE_NAMES = {
    "SPAdvertisedProducts",
    "SPCreateAdvertisedProducts",
    "SPCreateCreative",
    "SPCreateGlobalStoreSettings",
    "SPCreateProductCreative",
    "SPCreateProductCreativeSettings",
    "SPCreateSpotlightVideoSettings",
    "SPCreateVideo",
    "SPCreative",
    "SPGlobalStoreSettings",
    "SPProductCreative",
    "SPProductCreativeSettings",
    "SPSpotlightVideoSettings",
    "SPUpdateCreative",
    "SPUpdateProductCreative",
    "SPUpdateProductCreativeSettings",
    "SPUpdateSpotlightVideoSettings",
    "SPVideo",
}

BUDGET_NAMES = {
    "SPBudget",
    "SPBudgetSettings",
    "SPBudgetValue",
    "SPCreateBudget",
    "SPCreateBudgetSettings",
    "SPCreateBudgetValue",
    "SPCreateMonetaryBudget",
    "SPCreateMonetaryBudgetValue",
    "SPMonetaryBudget",
    "SPMonetaryBudgetValue",
    "SPUpdateBudgetSettings",
}

SHARED_NAMES = {
    "SPAutoCreationSettings",
    "SPCreateAutoCreationSettings",
    "SPStatus",
    "SPTag",
    "SPCreateTag",
}

ENTITY_GROUPS = [
    ("_campaigns.py", CAMPAIGN_NAMES),
    ("_ad_groups.py", AD_GROUP_NAMES),
    ("_ads.py", AD_NAMES),
    ("_targets.py", TARGET_NAMES),
    ("_ad_extensions.py", AD_EXTENSION_NAMES),
    ("_errors.py", ERROR_NAMES),
    ("_bids.py", BID_NAMES),
    ("_creatives.py", CREATIVE_NAMES),
    ("_budgets.py", BUDGET_NAMES),
    ("_shared.py", SHARED_NAMES),
]

_ENTITY_KEYWORDS: list[tuple[str, str]] = [
    ("AdExtension", "_ad_extensions.py"),
    ("AdGroup", "_ad_groups.py"),
    ("Campaign", "_campaigns.py"),
    ("Target", "_targets.py"),
    ("Ad", "_ads.py"),
]


def _match_entity_keyword(name: str) -> str | None:
    """Match entity keyword in schema name, accounting for false positives."""
    for kw, mod in _ENTITY_KEYWORDS:
        if kw not in name:
            continue
        if kw == "Ad" and "Adjust" in name:
            continue
        return mod
    return None


def _clean_description(desc: str) -> str:
    """Strip markdown table syntax from descriptions."""
    lines = desc.splitlines()
    result_lines = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            content = stripped[1:-1]
            if all(cell.strip() in ("", "---") for cell in content.split("|")):
                continue
            cells = [c.strip() for c in content.split("|")]
            if cells:
                result_lines.append(" ".join(cells))
        else:
            result_lines.append(line)
    return " ".join(result_lines).strip()


def openapi_to_python_type(schema: dict, schemas: dict | None = None) -> str:
    # Resolve $ref to the referenced schema name
    if "$ref" in schema:
        ref_name = schema["$ref"].split("/")[-1]
        return ref_name

    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        items = schema.get("items", {})
        inner = openapi_to_python_type(items, schemas)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = openapi_to_python_type(schema["additionalProperties"], schemas)
            return f"dict[str, {val}]"
        return "dict[str, Any]"
    if t == "string":
        if fmt == "date-time":
            return "datetime"
        if fmt == "date":
            return "date"
        return "str"
    return {"integer": "int", "number": "float", "boolean": "bool"}.get(t, "Any")


def is_enum(schema: dict) -> bool:
    return bool(schema.get("enum")) or (not schema.get("properties") and not schema.get("type"))


def generate_enum(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    values = schema.get("enum", [])
    members = "\n    ".join(f'{v} = "{v}"' for v in values)
    return f'''class {name}(StrEnum):
    """{doc}"""
    {members}
'''


def generate_model(name: str, schema: dict, schemas: dict | None = None) -> str:
    doc = schema.get("description", "")
    required: set[str] = set(schema.get("required", []))

    # Handle oneOf — extract variant properties as optional fields
    if not schema.get("properties") and schema.get("oneOf"):
        fields = []
        for variant in schema["oneOf"]:
            if variant.get("type") == "object" and variant.get("properties"):
                for fname, fschema in variant["properties"].items():
                    typ = openapi_to_python_type(fschema, schemas)
                    desc = _clean_description(fschema.get("description", "")).strip().rstrip()
                    comment = f"  # {desc}" if desc else ""
                    fields.append(f"    {fname}: {typ} | None = None{comment}")
        field_block = "\n".join(fields) if fields else "    pass"
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")

{field_block}
'''

    props = schema.get("properties", {})
    if not props:
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")
'''
    fields = []
    for fname, fschema in props.items():
        typ = openapi_to_python_type(fschema, schemas)
        is_required = fname in required
        default = "" if is_required else " = None"
        if not is_required and typ not in ("Any",):
            typ = f"{typ} | None"
        desc = _clean_description(fschema.get("description", "")).strip().rstrip()
        comment = f"  # {desc}" if desc else ""
        fields.append(f"    {fname}: {typ}{default}{comment}")
    field_block = "\n".join(fields)
    return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")

{field_block}
'''


def _group_entity(name: str) -> str | None:
    for filename, names in ENTITY_GROUPS:
        if name in names:
            return filename
    return None


def _classify(schemas: dict[str, dict]) -> dict[str, list[str]]:
    enums: list[str] = []
    campaigns: list[str] = []
    ad_groups: list[str] = []
    ads: list[str] = []
    targets: list[str] = []
    ad_extensions: list[str] = []
    errors: list[str] = []
    shared: list[str] = []
    bids: list[str] = []
    creatives: list[str] = []
    budgets: list[str] = []

    for name in sorted(schemas):
        s = schemas[name]
        if is_enum(s) and s.get("enum"):
            enums.append(name)
        elif g := _group_entity(name):
            if g == "_campaigns.py":
                campaigns.append(name)
            elif g == "_ad_groups.py":
                ad_groups.append(name)
            elif g == "_ads.py":
                ads.append(name)
            elif g == "_targets.py":
                targets.append(name)
            elif g == "_ad_extensions.py":
                ad_extensions.append(name)
            elif g == "_errors.py":
                errors.append(name)
            elif g == "_shared.py":
                shared.append(name)
            elif g == "_bids.py":
                bids.append(name)
            elif g == "_creatives.py":
                creatives.append(name)
            elif g == "_budgets.py":
                budgets.append(name)
        elif g := _match_entity_keyword(name):
            if g == "_campaigns.py":
                campaigns.append(name)
            elif g == "_ad_groups.py":
                ad_groups.append(name)
            elif g == "_ads.py":
                ads.append(name)
            elif g == "_targets.py":
                targets.append(name)
            elif g == "_ad_extensions.py":
                ad_extensions.append(name)
        else:
            shared.append(name)

    return {
        "_enums.py": enums,
        "_campaigns.py": campaigns,
        "_ad_groups.py": ad_groups,
        "_ads.py": ads,
        "_targets.py": targets,
        "_ad_extensions.py": ad_extensions,
        "_errors.py": errors,
        "_bids.py": bids,
        "_creatives.py": creatives,
        "_budgets.py": budgets,
        "_shared.py": shared,
    }


def emit(schema: dict, name: str, schemas: dict | None = None) -> str:
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema, schemas)


def _ext_refs_from_schema(name: str, schema: dict, schemas: dict, schema_module: dict) -> set[str]:
    """Return set of type names referenced by this schema that belong to other modules."""
    refs: set[str] = set()
    seen: set[str] = set()

    def walk(s: dict) -> None:
        if "$ref" in s:
            rname = s["$ref"].split("/")[-1]
            if (
                rname not in seen
                and schema_module.get(rname)
                and schema_module[rname] != schema_module[name]
            ):
                refs.add(rname)
            seen.add(rname)
        elif s.get("type") == "array":
            walk(s.get("items", {}))
        elif s.get("type") == "object" and s.get("additionalProperties"):
            walk(s["additionalProperties"])

    for fname, fschema in schema.get("properties", {}).items():
        walk(fschema)
    for variant in schema.get("oneOf", []):
        if variant.get("type") == "object" and variant.get("properties"):
            for fname, fschema in variant["properties"].items():
                walk(fschema)
    return refs


def _build_import_block(module_filename: str, refs: set[str], schema_module: dict) -> str:
    """Build a TYPE_CHECKING import block for types coming from other modules."""
    grouped: dict[str, list[str]] = {}
    for ref in sorted(refs):
        src = schema_module[ref]
        grouped.setdefault(src, []).append(ref)
    if not grouped:
        return ""
    lines: list[str] = ["if TYPE_CHECKING:"]
    for src in sorted(grouped):
        names = sorted(grouped[src])
        lines.append(f"    from .{src.removesuffix('.py')} import {', '.join(names)}")
    return "\n".join(lines) + "\n\n"


def main(*, output_dir: Path | None = None) -> None:
    with open(SCHEMA_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]
    groups = _classify(schemas)

    # Build reverse map: schema_name -> module_filename
    schema_module: dict[str, str] = {}
    for mod, names in groups.items():
        for n in names:
            schema_module[n] = mod

    # First pass: collect external type refs per module
    ext_refs: dict[str, set[str]] = {}
    for mod, names in groups.items():
        mod_refs: set[str] = set()
        for n in names:
            refs = _ext_refs_from_schema(n, schemas[n], schemas, schema_module)
            mod_refs.update(refs)
        mod_refs = {r for r in mod_refs if schema_module.get(r) != mod}
        ext_refs[mod] = mod_refs

    if output_dir is None:
        # Legacy single-file output
        parts = [HEADER]
        done: set[str] = set()

        def emit_one(name: str) -> str:
            if name in done:
                return ""
            done.add(name)
            return emit(schemas[name], name, schemas)

        for section, names in [
            ("# ── Enums ──", groups["_enums.py"]),
            ("\n# ── Campaigns ──", groups["_campaigns.py"]),
            ("\n# ── Ad Groups ──", groups["_ad_groups.py"]),
            ("\n# ── Ads ──", groups["_ads.py"]),
            ("\n# ── Targets ──", groups["_targets.py"]),
            ("\n# ── Ad Extensions ──", groups["_ad_extensions.py"]),
            ("\n# ── Errors ──", groups["_errors.py"]),
            ("\n# ── Bids ──", groups["_bids.py"]),
            ("\n# ── Creatives ──", groups["_creatives.py"]),
            ("\n# ── Budgets ──", groups["_budgets.py"]),
            ("\n# ── Shared ──", groups["_shared.py"]),
        ]:
            parts.append(section)
            for n in names:
                out = emit_one(n)
                if out:
                    parts.append(out)

        legacy_out = SCHEMA_PATH.parent / "src" / "amazon_ads_sdk" / "models.py"
        legacy_out.write_text("\n".join(parts) + "\n")
        print(f"Wrote {legacy_out}")
        return

    # Multi-file output
    output_dir.mkdir(parents=True, exist_ok=True)

    # __init__.py — re-export all generated modules + rebuild models
    init_parts = [
        '"""Auto-generated Pydantic models from Amazon Ads API schema."""',
        "",
        "from __future__ import annotations",
        "",
        "import sys",
        "import typing",
        "",
    ]
    for module_file in sorted(groups):
        mod = module_file.removesuffix(".py")
        init_parts.append(f"from .{mod} import *")
    init_parts.extend(
        [
            "",
            "# Resolve cross-module forward references",
            "_ns: dict[str, typing.Any] = dict(sys.modules[__name__].__dict__)",
            "for _name, _obj in list(_ns.items()):",
            "    if (",
            "        isinstance(_obj, type)",
            "        and hasattr(_obj, 'model_rebuild')",
            "        and getattr(_obj, '__module__', '').startswith('amazon_ads_sdk.models')",
            "    ):",
            "        _obj.model_rebuild(_types_namespace=_ns)",
        ]
    )
    (output_dir / "__init__.py").write_text("\n".join(init_parts) + "\n")

    done: set[str] = set()

    def emit_to_file(buf: list[str], name: str) -> None:
        if name in done:
            return
        done.add(name)
        out = emit(schemas[name], name, schemas)
        if out:
            buf.append(out)

    for filename, names in groups.items():
        header = MODULE_IMPORTS[filename]
        refs = ext_refs.get(filename, set())
        imports = _build_import_block(filename, refs, schema_module)
        if refs:
            if "TYPE_CHECKING" not in header:
                header = header.replace(
                    "from typing import Any", "from typing import TYPE_CHECKING, Any"
                )
                header = header.replace(
                    "from typing import Any\n", "from typing import TYPE_CHECKING, Any\n"
                )
        buf = [header, imports] if imports else [header]
        for n in names:
            emit_to_file(buf, n)
        (output_dir / filename).write_text("".join(buf) + "\n")
        print(f"Wrote {output_dir / filename}  ({len(names)} models)")

    print(f"\nAll models written to {output_dir}/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Pydantic models from OpenAPI schema.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for multi-file mode. Omit for legacy single-file output.",
    )
    args = parser.parse_args()
    main(output_dir=args.output_dir)
