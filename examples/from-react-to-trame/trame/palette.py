"""
Chart color tokens, mirroring the fixed categorical order and surfaces from
the react/ sibling example (see its dataviz-skill palette). Every color a
chart draws with its own inline style (donut, gauge, bars) needs a light AND
a dark step, bound to the same `dark` state flag that drives the MUI
ThemeProvider's `mode=`, so hand-rolled SVG/CSS charts stay coherent with the
theme toggle instead of freezing at whichever mode the page happened to
render in first.
"""

from trame.widgets import react

# Fixed categorical order - never cycled, never reordered by filters.
CATEGORICAL_LIGHT = [
    "#2a78d6",
    "#eb6834",
    "#1baf7a",
    "#eda100",
    "#e87ba4",
    "#008300",
    "#4a3aa7",
    "#e34948",
]
CATEGORICAL_DARK = [
    "#3987e5",
    "#d95926",
    "#199e70",
    "#c98500",
    "#d55181",
    "#008300",
    "#9085e9",
    "#e66767",
]

SURFACE_LIGHT = "#fcfcfb"
SURFACE_DARK = "#1a1a19"
OTHER_LIGHT = "#c3c2b7"
OTHER_DARK = "#52514e"

STATUS = {
    "good": "#0ca30c",
    "warning": "#fab219",
    "serious": "#ec835a",
    "critical": "#d03b3b",
}


def mode_bind(light_value, dark_value):
    """A style value that follows the same `dark` flag as the ThemeProvider."""
    expr = f"dark ? '{dark_value}' : '{light_value}'"
    return react.Bind(expr, dark=False)


def series(index):
    """Categorical color at `index`, reactive to light/dark mode."""
    return mode_bind(CATEGORICAL_LIGHT[index], CATEGORICAL_DARK[index])


SURFACE = mode_bind(SURFACE_LIGHT, SURFACE_DARK)
OTHER = mode_bind(OTHER_LIGHT, OTHER_DARK)
