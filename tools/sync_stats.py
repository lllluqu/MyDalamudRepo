#!/usr/bin/env python3
"""Sync DownloadCount in pluginmaster.json from GitHub Release asset download counts.

For every entry, the RepoUrl owner/repo is queried via the Releases API and the
download_count of all release assets is summed into DownloadCount. GitHub counts
unique requesters per asset per 24h window, so the number approximates installs
plus updates rather than raw HTTP requests.

Usage:
    python tools/sync_stats.py [path/to/pluginmaster.json]
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

API = "https://api.github.com"
HEADERS = {
    "User-Agent": "MyDalamudRepo-stats",
    "Accept": "application/vnd.github+json",
}


def total_downloads(repo: str) -> int:
    req = urllib.request.Request(f"{API}/repos/{repo}/releases?per_page=100", headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        releases = json.load(resp)
    return sum(a.get("download_count", 0) for rel in releases for a in rel.get("assets", []))


def main() -> int:
    master = Path(sys.argv[1] if len(sys.argv) > 1 else "pluginmaster.json")
    entries = json.loads(master.read_text(encoding="utf-8-sig"))
    flat = []
    for item in entries:
        if isinstance(item, dict) and isinstance(item.get("value"), list):
            flat.extend(item["value"])
        else:
            flat.append(item)
    entries = flat

    changed = False
    failed = 0
    for e in entries:
        m = re.search(r"github\.com/([^/]+/[^/]+)", e.get("RepoUrl", ""))
        if not m:
            continue
        try:
            count = total_downloads(m.group(1))
        except Exception as ex:  # noqa: BLE001 - keep syncing the other entries
            print(f"{e.get('InternalName')}: fetch failed: {ex}")
            failed += 1
            continue
        print(f"{e.get('InternalName')}: {count}")
        if e.get("DownloadCount") != count:
            e["DownloadCount"] = count
            changed = True

    if changed:
        out = master
        out.write_text(json.dumps(entries, ensure_ascii=False, indent=4) + "\n", encoding="utf-8", newline="\n")
        print(f"updated: {out}")
    else:
        print("no change")
    return 1 if failed and not changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
