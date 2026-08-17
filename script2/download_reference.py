"""从 toc2.json 解析并下载 Amazon Ads API v1 的 reference_prod.json。"""

from __future__ import annotations

from pathlib import Path

import httpx
from _json_io import fetch_json_with_etag, read_json

DATA_DIR = Path(__file__).resolve().parent / "data"
TOC2_PATH = DATA_DIR / "toc2.json"
OUT_FILE = DATA_DIR / "api-spec-v1" / "reference_prod.json"
META_FILE = DATA_DIR / "api-spec-v1" / "reference_prod.meta.json"


def resolve_reference_prod_url(toc2: dict) -> str:
    for toc in toc2["tocs"]:
        if toc["id"] != "toc-reference":
            continue
        for section in toc["items"]:
            if section["name"] != "Amazon Ads API v1":
                continue
            for item in section["items"]:
                if item["name"] != "API Specifications":
                    continue
                return item["items"].strip("$")
    raise LookupError("未在 toc2.json 中找到 API Specifications 链接")


def main() -> None:
    toc2 = read_json(TOC2_PATH)
    url = resolve_reference_prod_url(toc2)
    print(f"url: {url}")

    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        fetch_json_with_etag(client, url, OUT_FILE, META_FILE)


if __name__ == "__main__":
    main()
