"""
A handful of raw SVG element wrappers, used to hand-draw the sparkline and
revenue charts. trame_mui only wraps @mui/material (no @mui/x-charts), so
these charts are built directly as SVG paths rather than through a charting
widget.

`trame.widgets.html` only generates HTML5 tags (plus the bare `<svg>`
container) - it has no `<path>`/`<circle>` wrappers, so we declare them here
the same way `trame_client.widgets.html.Svg` does: subclass the shared
`HtmlElement` and register the exact prop names we need through
`__properties`, since `client_type="react"` only serializes props it knows
about for a given element.
"""

from trame_client.widgets.core import HtmlElement

_SVG_PROPS = [
    "d",
    "fill",
    "stroke",
    "points",
    "cx",
    "cy",
    "r",
    "x1",
    "y1",
    "x2",
    "y2",
    "transform",
    "opacity",
    ("stroke_width", "strokeWidth"),
    ("stroke_linecap", "strokeLinecap"),
    ("stroke_linejoin", "strokeLinejoin"),
    ("fill_opacity", "fillOpacity"),
    ("stroke_opacity", "strokeOpacity"),
    ("text_anchor", "textAnchor"),
    ("font_size", "fontSize"),
]


def _svg_tag(tag_name):
    class _SvgTag(HtmlElement):
        def __init__(self, children=None, **kwargs):
            kwargs["__properties"] = kwargs.get("__properties", []) + _SVG_PROPS
            super().__init__(tag_name, children, **kwargs)

    _SvgTag.__name__ = tag_name.capitalize()
    _SvgTag.__qualname__ = _SvgTag.__name__
    return _SvgTag


Path = _svg_tag("path")
Circle = _svg_tag("circle")
Line = _svg_tag("line")
Text = _svg_tag("text")


class Svg(HtmlElement):
    """
    Like `trame.widgets.html.Svg`, but also registers `viewBox` /
    `preserveAspectRatio` (not in the generated html.Svg's prop list), so a
    chart can be drawn against fixed pixel coordinates while its `<svg>`
    stretches to its container's width.
    """

    def __init__(self, children=None, **kwargs):
        kwargs["__properties"] = kwargs.get("__properties", []) + [
            "width",
            "height",
            "xmlns",
            ("view_box", "viewBox"),
            ("preserve_aspect_ratio", "preserveAspectRatio"),
        ]
        super().__init__("svg", children, **kwargs)
