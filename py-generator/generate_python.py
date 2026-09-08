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
DEST_FILE = BASE_DIR / "src" / "trame_mui" / "widgets" / "mui.py"
INPUT_JSON = BASE_DIR / "py-generator" / "mui-api.json"
HEADER_FILE = Path(__file__).with_name(".header.py")

# Components that read their `children` directly via React.Children
# (React.Children.toArray/cloneElement) before rendering, to find the
# selected/active item(s) and inject props (onClick, selected, ...) into
# them - trame's react client normally hands every widget's children through
# a lazy per-node wrapper (see trame-client's
# react-app/src/runtime/resolveLiteralChildren.js), which defeats that
# inspection since the props such a component reads (`child.props.value`,
# `child.props.children`, ...) end up on the wrapper instead of on the real
# child element. `literal_children = True` opts a widget's Python class into
# the eager, non-wrapped children resolution that mechanism provides.
# Verified against @mui/material's source (react-components/node_modules):
# each of these reads `child.props.*` (value/selected/index/inputProps/...)
# straight off its `children` array - most (Select, Tabs, Stepper,
# BottomNavigation, SpeedDial, AvatarGroup) then `React.cloneElement(child,
# {...})` to inject props back in; FormControl/ImageListItem only READ
# `child.props.*` to derive their own state (label-shrink, image className)
# without cloning, but still need real values there for that to be correct.
# RadioGroup and ToggleButtonGroup were deliberately left out despite also
# matching a `React.Children`/`cloneElement` grep - both actually coordinate
# with their children via React Context (RadioGroupContext,
# ToggleButtonGroupContext/RovingTabIndexContext) instead, so the lazy
# per-node wrapper doesn't break them.
LITERAL_CHILDREN_COMPONENTS = {
    "Select",
    "Tabs",
    "Stepper",
    "BottomNavigation",
    "SpeedDial",
    "AvatarGroup",
    "FormControl",
    "ImageListItem",
}

# Components with no MUI docs API page (they live under @mui/material/styles
# rather than as a top-level documented component, so fetch_mui_api.py never
# sees them) but that we still want generated with hand-written prop
# metadata, matching the shape of a fetched component definition.
MANUAL_COMPONENTS = {
    "ThemeProvider": {
        "docUrl": "https://mui.com/material-ui/customization/theming/",
        "componentDescription": (
            "Wraps its children with a MUI theme and mounts CssBaseline for "
            "consistent baseline styles. Place at the root of the UI."
        ),
        "props": {
            "mode": {"type": {"name": "'light' | 'dark'"}, "default": "'light'"},
            "theme": {"type": {"name": "object"}},
        },
        "propDescriptions": {
            "mode": {"description": "MUI palette mode."},
            "theme": {
                "description": (
                    "Theme options merged on top of the palette mode "
                    "(forwarded to MUI's createTheme)."
                )
            },
        },
    },
}

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

        if py_name == prop_name:
            attrs.append(f'"{prop_name}"')
        else:
            attrs.append(f'("{py_name}", "{prop_name}")')
        doc_lines.append(f"    :param {py_name}: {description} (``{type_of(prop)}``)")

    component_doc = clean_description(definition.get("componentDescription", ""))
    doc_url = definition.get(
        "docUrl", f"https://mui.com/material-ui/api/{to_tag(name)[4:]}/"
    )
    doc = [
        f'    """MUI {name} - {doc_url}',
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
        lines.append("        self.props += [")
        lines.extend(f"            {attr}," for attr in attrs)
        lines.append("        ]")
    if name in LITERAL_CHILDREN_COMPONENTS:
        lines.append("        self.literal_children = True")
    return "\n".join(lines)


def main():
    data = json.loads(INPUT_JSON.read_text())
    components = {**data["components"], **MANUAL_COMPONENTS}

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
