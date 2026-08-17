"""下载 Amazon Ads 文档 TOC → script2/data/toc2.json。"""

from __future__ import annotations

from pathlib import Path

import httpx
from _json_io import fetch_json_with_etag

URL = "https://d3a0d0y2hgofx6.cloudfront.net/en-us/toc2.json"
DATA_DIR = Path(__file__).resolve().parent / "data"
OUT_FILE = DATA_DIR / "toc2.json"
META_FILE = DATA_DIR / "toc2.meta.json"


def main() -> None:
    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        fetch_json_with_etag(client, URL, OUT_FILE, META_FILE)


if __name__ == "__main__":
    main()
