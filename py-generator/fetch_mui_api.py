#!/usr/bin/env python3
"""Vendor MUI's API metadata into mui-api.json (trame-vuetify vendors
Vuetify's web-types.json the same way).

MUI does not ship API metadata in its npm package; its docs pipeline
generates one JSON per component (types) plus one translation JSON per
component (descriptions), versioned in the mui/material-ui repository.
This script fetches both for the exact @mui/material version installed in
node_modules and merges them into a single vendored file so that
generate_python.py runs offline and reproducibly.

Usage:
    python3 fetch_mui_api.py
"""

import json
import re
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
MUI_ROOT = BASE_DIR / "react-components" / "node_modules" / "@mui" / "material"
DEST_FILE = BASE_DIR / "py-generator" / "mui-api.json"

RAW = "https://raw.githubusercontent.com/mui/material-ui/v{version}/docs/{path}"


def kebab(name):
    return re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower()


def list_components():
    return sorted(
        p.name
        for p in MUI_ROOT.iterdir()
        if p.is_dir()
        and p.name[0].isupper()
        and "_" not in p.name
        and (p / f"{p.name}.d.ts").exists()
    )


def fetch_json(version, path):
    url = RAW.format(version=version, path=path)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return json.loads(response.read())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def fetch_component(version, name):
    slug = kebab(name)
    api = fetch_json(version, f"pages/material-ui/api/{slug}.json")
    if api is None:
        return name, None
    translations = (
        fetch_json(version, f"translations/api-docs/{slug}/{slug}.json") or {}
    )
    return name, {
        "props": api.get("props", {}),
        "propDescriptions": translations.get("propDescriptions", {}),
        "componentDescription": translations.get("componentDescription", ""),
    }


def main():
    version = json.loads((MUI_ROOT / "package.json").read_text())["version"]
    components = list_components()
    print(f"@mui/material {version}: fetching api for {len(components)} components")

    result = {"$mui-version": version, "components": {}}
    skipped = []
    with ThreadPoolExecutor(max_workers=16) as pool:
        for name, data in pool.map(lambda n: fetch_component(version, n), components):
            if data is None:
                skipped.append(name)
            else:
                result["components"][name] = data

    DEST_FILE.write_text(json.dumps(result, indent=1, sort_keys=True))
    print(f"Wrote {DEST_FILE.name}: {len(result['components'])} components")
    if skipped:
        print(f"No api json (skipped): {', '.join(skipped)}")


if __name__ == "__main__":
    main()
