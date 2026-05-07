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

MODULE_IMPORTS = {
    "_enums.py": HEADER,
    "_filters.py": '''"""filter models."""

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
    "_requests.py": '''"""request models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_responses.py": '''"""response models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
    "_shared.py": '''"""shared models."""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict
''',
}

# ── Entity model grouping ───────────────────────────────────────────────────

CAMPAIGN_NAMES = {
    "SPCampaign",
    "SPCampaignCreate",
    "SPCampaignUpdate",
    "SPCampaignMultiStatusSuccess",
    "SPCampaignOptimizations",
}

AD_GROUP_NAMES = {
    "SPAdGroup",
    "SPAdGroupCreate",
    "SPAdGroupUpdate",
    "SPAdGroupMultiStatusSuccess",
    "SPAdGroupBid",
    "SPCreateAdGroupBid",
    "SPUpdateAdGroupBid",
}

AD_NAMES = {
    "SPAd",
    "SPAdCreate",
    "SPAdUpdate",
    "SPAdMultiStatusSuccess",
    "SPAdvertisedProducts",
    "SPCreateAdvertisedProducts",
    "SPProductCreative",
    "SPProductCreativeSettings",
    "SPCreateProductCreative",
    "SPCreateProductCreativeSettings",
    "SPCreateProductValue",
    "SPProductValue",
    "SPVideo",
    "SPCreateVideo",
    "SPCreateSpotlightVideoSettings",
    "SPSpotlightVideoSettings",
    "SPVideoExtension",
    "SPCreateVideoExtension",
    "SPAudienceBidAdjustment",
    "SPCreateAudienceBidAdjustment",
    "SPCreateCreative",
    "SPCreateCreativeBidAdjustment",
    "SPCreativeBidAdjustment",
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
}

AD_EXTENSION_NAMES = {
    "SPAdExtension",
    "SPAdExtensionCreate",
    "SPAdExtensionUpdate",
    "SPAdExtensionMultiStatusSuccess",
    "SPAdExtensionSettings",
    "SPCreateAdExtensionSettings",
    "SPPromptExtension",
    "SPCreatePromptExtension",
}

ENTITY_GROUPS = [
    ("_campaigns.py", CAMPAIGN_NAMES),
    ("_ad_groups.py", AD_GROUP_NAMES),
    ("_ads.py", AD_NAMES),
    ("_targets.py", TARGET_NAMES),
    ("_ad_extensions.py", AD_EXTENSION_NAMES),
]


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


def openapi_to_python_type(schema: dict) -> str:
    t = schema.get("type", "object")
    fmt = schema.get("format", "")
    if t == "array":
        items = schema.get("items", {})
        inner = openapi_to_python_type(items)
        return f"list[{inner}]"
    if t == "object":
        if schema.get("additionalProperties"):
            val = openapi_to_python_type(schema["additionalProperties"])
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


def generate_model(name: str, schema: dict) -> str:
    doc = schema.get("description", "")
    props = schema.get("properties", {})
    required: set[str] = set(schema.get("required", []))
    if not props:
        return f'''class {name}(BaseModel):
    """{doc}"""
    model_config = ConfigDict(extra="forbid")
'''
    fields = []
    for fname, fschema in props.items():
        typ = openapi_to_python_type(fschema)
        is_required = fname in required
        default = "" if is_required else " = None"
        if not is_required and typ not in ("Any",):
            typ = f"{typ} | None"
        desc = _clean_description(fschema.get("description", "")).strip()[:80].rstrip()
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
    return None  # falls through to _shared.py


def _classify(schemas: dict[str, dict]) -> dict[str, list[str]]:
    enums: list[str] = []
    filters: list[str] = []
    campaigns: list[str] = []
    ad_groups: list[str] = []
    ads: list[str] = []
    targets: list[str] = []
    ad_extensions: list[str] = []
    requests: list[str] = []
    responses: list[str] = []
    shared: list[str] = []

    for name in sorted(schemas):
        s = schemas[name]
        if is_enum(s) and s.get("enum"):
            enums.append(name)
        elif "Filter" in name:
            filters.append(name)
        elif "Request" in name:
            requests.append(name)
        elif "Response" in name or "SuccessResponse" in name:
            responses.append(name)
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
        else:
            shared.append(name)

    return {
        "_enums.py": enums,
        "_filters.py": filters,
        "_campaigns.py": campaigns,
        "_ad_groups.py": ad_groups,
        "_ads.py": ads,
        "_targets.py": targets,
        "_ad_extensions.py": ad_extensions,
        "_requests.py": requests,
        "_responses.py": responses,
        "_shared.py": shared,
    }


def emit(schema: dict, name: str) -> str:
    if is_enum(schema) and schema.get("enum"):
        return generate_enum(name, schema)
    return generate_model(name, schema)


def main(*, output_dir: Path | None = None) -> None:
    with open(SCHEMA_PATH) as f:
        data = json.load(f)
    schemas = data["components"]["schemas"]
    groups = _classify(schemas)

    if output_dir is None:
        # Legacy single-file output
        parts = [HEADER]
        done: set[str] = set()

        def emit_one(name: str) -> str:
            if name in done:
                return ""
            done.add(name)
            return emit(schemas[name], name)

        for section, names in [
            ("# ── Enums ──", groups["_enums.py"]),
            ("\n# ── Filters ──", groups["_filters.py"]),
            (
                "\n# ── Entity Models ──",
                groups["_campaigns.py"]
                + groups["_ad_groups.py"]
                + groups["_ads.py"]
                + groups["_targets.py"]
                + groups["_ad_extensions.py"],
            ),
            ("\n# ── Request Bodies ──", groups["_requests.py"]),
            ("\n# ── Response Bodies ──", groups["_responses.py"]),
            ("\n# ── Other Schemas ──", groups["_shared.py"]),
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
    (output_dir / "__init__.py").write_text(HEADER + "\n")

    done: set[str] = set()

    def emit_to_file(buf: list[str], name: str) -> None:
        if name in done:
            return
        done.add(name)
        out = emit(schemas[name], name)
        if out:
            buf.append(out)

    for filename, names in groups.items():
        buf = [MODULE_IMPORTS[filename]]
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
