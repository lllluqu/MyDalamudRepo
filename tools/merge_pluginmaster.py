#!/usr/bin/env python3
"""Merge one plugin entry into pluginmaster.json.

The entry is matched by InternalName: an existing entry with the same
InternalName is replaced, otherwise the entry is appended. Entries are written
as a flat JSON array (PowerShell's ConvertTo-Json can nest arrays as
{"value": [...], "Count": n}, which Dalamud cannot read — this script also
repairs that if it happens).

Usage:
    python tools/merge_pluginmaster.py --master pluginmaster.json --entry entry.json
    python tools/merge_pluginmaster.py --master pluginmaster.json --entry entry.json --output out.json
"""
import argparse
import json
from pathlib import Path


def load(path: Path):
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    flat = []
    for item in data:
        if isinstance(item, dict) and isinstance(item.get("value"), list):
            flat.extend(item["value"])
        else:
            flat.append(item)
    return flat


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--master", required=True, help="pluginmaster.json to update")
    parser.add_argument("--entry", required=True, help="JSON file containing one plugin entry object")
    parser.add_argument("--output", help="output path (defaults to --master)")
    args = parser.parse_args()

    master_path = Path(args.master)
    entries = load(master_path)

    entry = json.loads(Path(args.entry).read_text(encoding="utf-8-sig"))
    if isinstance(entry, list):
        if len(entry) != 1:
            raise SystemExit("--entry must contain exactly one plugin object")
        entry = entry[0]

    merged = [e for e in entries if e.get("InternalName") != entry.get("InternalName")]
    merged.append(entry)
    merged.sort(key=lambda e: e.get("InternalName", ""))

    out = Path(args.output) if args.output else master_path
    out.write_text(json.dumps(merged, ensure_ascii=False, indent=4) + "\n", encoding="utf-8", newline="\n")

    for e in merged:
        print(f"{e.get('InternalName')}: {e.get('AssemblyVersion')}")
    print(f"written: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
