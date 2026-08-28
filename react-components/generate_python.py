#!/usr/bin/env python3
"""Generate trame_mui/widgets/mui_generated.py from the vendored
mui-api.json — the direct mirror of trame-vuetify's generate_python.py
(which reads Vuetify's vendored web-types.json).

Run fetch_mui_api.py first to (re)vendor the metadata for the installed
@mui/material version.

Usage:
    python3 generate_python.py
"""

import json
import re
from html import unescape
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DEST_FILE = BASE_DIR / "trame_mui" / "widgets" / "mui_generated.py"
INPUT_JSON = BASE_DIR / "react-components" / "mui-api.json"
HEADER_FILE = Path(__file__).with_name(".header.py")

# Props inherited from the DOM/React side that trame already handles natively
SKIP_PROPS = {
    "children",
    "className",
    "classes",
    "style",
    "sx",
    "ref",
    "key",
    "component",
    "components",
    "componentsProps",
}

# ----------------------------------------
# Helpers
# ----------------------------------------


def to_attr_name(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def to_tag(name):
    return "mui-" + re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name).lower()


def clean_description(text):
    if not text:
        return ""
    text = re.sub(r"<a[^>]*>|</a>", "", text)
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).replace('"""', "'''").strip()


def truncate(text, limit=80):
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + " ..."


def type_of(prop):
    type_info = prop.get("type", {})
    description = type_info.get("description")
    if description:
        return truncate(clean_description(description))
    return type_info.get("name", "any")


# ----------------------------------------
# Generation
# ----------------------------------------


def generate_class(name, definition):
    attrs = []
    events = []
    doc_lines = []
    descriptions = definition.get("propDescriptions", {})

    for prop_name, prop in sorted(definition.get("props", {}).items()):
        if prop_name in SKIP_PROPS or not re.match(r"^[a-zA-Z]\w*$", prop_name):
            continue

        py_name = to_attr_name(prop_name)
        description = clean_description(
            descriptions.get(prop_name, {}).get("description", "")
        )
        if prop.get("deprecated"):
            description = f"(deprecated) {description}"
        default = prop.get("default")
        if default:
            description = f"{description} (default: {default})"

        is_event = re.match(r"^on[A-Z]", prop_name) and prop.get("type", {}).get(
            "name"
        ) in ("func", "function")
        if is_event:
            event_name = prop_name[2].lower() + prop_name[3:]
            py_event = to_attr_name(event_name)
            if py_event == event_name:
                events.append(f'"{event_name}"')
            else:
                events.append(f'("{py_event}", "{event_name}")')
            doc_lines.append(f"    :param {py_event}: {description}")
        else:
            if py_name == prop_name:
                attrs.append(f'"{prop_name}"')
            else:
                attrs.append(f'("{py_name}", "{prop_name}")')
            doc_lines.append(
                f"    :param {py_name}: {description} (``{type_of(prop)}``)"
            )

    component_doc = clean_description(definition.get("componentDescription", ""))
    doc = [
        f'    """MUI {name} - https://mui.com/material-ui/api/{to_tag(name)[4:]}/',
    ]
    if component_doc:
        doc.append("")
        doc.append(f"    {component_doc}")
    if doc_lines:
        doc.append("")
        doc.extend(doc_lines)
    doc.append('    """')

    lines = [
        "",
        "",
        f"class {name}(MuiHtmlElement):",
        *doc,
        "",
        "    def __init__(self, children=None, **kwargs):",
        f'        super().__init__("{to_tag(name)}", children, **kwargs)',
    ]
    if attrs:
        lines.append("        self._attr_names += [")
        lines.extend(f"            {attr}," for attr in attrs)
        lines.append("        ]")
    if events:
        lines.append("        self._event_names += [")
        lines.extend(f"            {event}," for event in events)
        lines.append("        ]")
    return "\n".join(lines)


def main():
    data = json.loads(INPUT_JSON.read_text())
    components = data["components"]

    output = [HEADER_FILE.read_text()]
    output.append(f"\n# Generated from @mui/material {data['$mui-version']}\n")
    output.append("\n__all__ = [\n")
    output.extend(f'    "{name}",\n' for name in sorted(components))
    output.append("]\n")
    output.extend(generate_class(name, components[name]) for name in sorted(components))
    output.append("\n")

    DEST_FILE.write_text("".join(output))
    print(f"Wrote {DEST_FILE}: {len(components)} classes")


if __name__ == "__main__":
    main()
