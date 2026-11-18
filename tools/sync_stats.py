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
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

API = "https://api.github.com"


def headers() -> dict:
    h = {
        "User-Agent": "MyDalamudRepo-stats",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    # GITHUB_TOKEN is provided automatically by GitHub Actions (5000 req/h vs 60
    # req/h unauthenticated, and the runner's shared IP exhausts the anon quota).
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def total_downloads(repo: str, retries: int = 3) -> int:
    url = f"{API}/repos/{repo}/releases?per_page=100"
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers())
            with urllib.request.urlopen(req, timeout=30) as resp:
                releases = json.load(resp)
            return sum(a.get("download_count", 0) for rel in releases for a in rel.get("assets", []))
        except Exception as ex:  # noqa: BLE001 - retry on transient/rate-limit errors
            last = ex
            if attempt < retries - 1:
                time.sleep(5 * (attempt + 1))
    raise last


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
            # Keep the previous DownloadCount and let the next scheduled run
            # retry; a transient rate limit should not fail the whole workflow.
            print(f"::warning::{e.get('InternalName')}: fetch failed, keeping previous count: {ex}")
            failed += 1
            continue
        print(f"{e.get('InternalName')}: {count}")
        if e.get("DownloadCount") != count:
            e["DownloadCount"] = count
            changed = True

    if failed == len([e for e in entries if e.get("RepoUrl")]):
        print("::warning::all fetches failed; no counts were refreshed this run")

    if changed:
        out = master
        out.write_text(json.dumps(entries, ensure_ascii=False, indent=4) + "\n", encoding="utf-8", newline="\n")
        print(f"updated: {out}")
    else:
        print("no change")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
