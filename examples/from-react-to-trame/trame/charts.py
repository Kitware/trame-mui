"""
Hand-rolled charts for the dashboard: trame_mui only wraps @mui/material (no
@mui/x-charts yet), so the sparkline/revenue trend are drawn as raw SVG paths
(see `svg.py`) and the donut/gauge/bars are drawn with plain CSS
(conic-gradient / flex heights) on `mui.Box`. Mark specs (2px line, 4px
rounded bar caps, a light area wash, a surface ring behind end-markers) follow
the same dataviz conventions as the react/ sibling example.
"""

from trame.widgets import mui

import svg_elements as svg

# -----------------------------------------------------------------------------
# Line / area geometry
# -----------------------------------------------------------------------------


def _line_points(values, width, height, pad_top=4, pad_bottom=4):
    lo, hi = min(values), max(values)
    span = (hi - lo) or 1
    n = len(values)
    step = width / (n - 1) if n > 1 else 0
    points = []
    for i, v in enumerate(values):
        x = i * step
        y = pad_top + (1 - (v - lo) / span) * (height - pad_top - pad_bottom)
        points.append((x, y))
    return points


def _line_path(points):
    d = f"M {points[0][0]:.1f} {points[0][1]:.1f}"
    for x, y in points[1:]:
        d += f" L {x:.1f} {y:.1f}"
    return d


def _area_path(points, height):
    d = f"M {points[0][0]:.1f} {height:.1f}"
    for x, y in points:
        d += f" L {x:.1f} {y:.1f}"
    d += f" L {points[-1][0]:.1f} {height:.1f} Z"
    return d


def sparkline(values, color, width=96, height=40):
    """A tiny 12-point trend line + wash, sized to fill a stat tile corner."""
    points = _line_points(values, width, height, pad_top=4, pad_bottom=4)
    with svg.Svg(width=str(width), height=str(height)):
        svg.Path(
            d=_area_path(points, height), fill=color, fill_opacity=0.15, stroke="none"
        )
        svg.Path(
            d=_line_path(points),
            fill="none",
            stroke=color,
            stroke_width=2,
            stroke_linecap="round",
            stroke_linejoin="round",
        )


def revenue_chart(values, months, color, surface, width=760, height=220):
    """A single-series area/line trend chart with month ticks below it."""
    pad_top, pad_bottom = 10, 10
    points = _line_points(values, width, height, pad_top=pad_top, pad_bottom=pad_bottom)
    last_x, last_y = points[-1]

    with mui.Box():
        with svg.Svg(
            width="100%",
            height=str(height),
            view_box=f"0 0 {width} {height}",
            preserve_aspect_ratio="none",
        ):
            svg.Path(
                d=_area_path(points, height),
                fill=color,
                fill_opacity=0.12,
                stroke="none",
            )
            svg.Path(
                d=_line_path(points),
                fill="none",
                stroke=color,
                stroke_width=2,
                stroke_linecap="round",
                stroke_linejoin="round",
            )
            # end marker: a surface ring behind the accent dot so it stays
            # legible where it meets the line.
            svg.Circle(cx=f"{last_x:.1f}", cy=f"{last_y:.1f}", r="6", fill=surface)
            svg.Circle(cx=f"{last_x:.1f}", cy=f"{last_y:.1f}", r="4", fill=color)

        with mui.Box(
            style={
                "display": "flex",
                "justifyContent": "space-between",
                "padding": "4px 2px 0",
            }
        ):
            for month in months:
                mui.Typography(month, variant="caption", color="text.secondary")


# -----------------------------------------------------------------------------
# Region bars - pure CSS, sequential single hue (magnitude comparison)
# -----------------------------------------------------------------------------


def bar_chart(data, value_key, label_key, color, height=220, bar_width=40):
    max_value = max(d[value_key] for d in data) or 1
    with mui.Box(style={"display": "flex", "alignItems": "stretch", "gap": "16px"}):
        for d in data:
            pct = round(d[value_key] / max_value * 100)
            with mui.Box(
                style={
                    "flex": "1",
                    "display": "flex",
                    "flexDirection": "column",
                    "alignItems": "center",
                    "gap": "8px",
                }
            ):
                with mui.Box(
                    style={
                        "height": f"{height}px",
                        "width": "100%",
                        "display": "flex",
                        "alignItems": "flex-end",
                        "justifyContent": "center",
                    }
                ):
                    mui.Box(
                        style={
                            "width": f"{bar_width}px",
                            "maxWidth": "100%",
                            "height": f"{pct}%",
                            "background": color,
                            "borderRadius": "4px 4px 0 0",
                        }
                    )
                mui.Typography(
                    d[label_key],
                    variant="caption",
                    color="text.secondary",
                    style={"textAlign": "center"},
                )


# -----------------------------------------------------------------------------
# Donut / gauge - CSS conic-gradient rings
# -----------------------------------------------------------------------------


def _ring(gradient, surface, size, hole_ratio, center_children=None):
    hole = round(size * hole_ratio)
    with mui.Box(
        style={
            "position": "relative",
            "width": f"{size}px",
            "height": f"{size}px",
            "borderRadius": "50%",
            "background": gradient,
            "margin": "0 auto",
        }
    ):
        with mui.Box(
            style={
                "position": "absolute",
                "top": "50%",
                "left": "50%",
                "transform": "translate(-50%, -50%)",
                "width": f"{hole}px",
                "height": f"{hole}px",
                "borderRadius": "50%",
                "background": surface,
                "display": "flex",
                "alignItems": "center",
                "justifyContent": "center",
            }
        ):
            if center_children:
                center_children()


def donut_chart(data, value_key, colors, surface, size=180, hole_ratio=0.62):
    total = sum(d[value_key] for d in data) or 1
    stops = []
    acc = 0
    for d, color in zip(data, colors):
        start = acc / total * 100
        acc += d[value_key]
        end = acc / total * 100
        stops.append(f"{color} {start:.2f}% {end:.2f}%")
    gradient = "conic-gradient(" + ", ".join(stops) + ")"
    _ring(gradient, surface, size, hole_ratio)


def gauge_chart(
    pct, color, track_color, surface, size=180, hole_ratio=0.68, label=None
):
    pct = max(0, min(100, pct))
    gradient = f"conic-gradient({color} 0% {pct}%, {track_color} {pct}% 100%)"

    def _label():
        mui.Typography(label or f"{pct:.0f}%", variant="h5", style={"fontWeight": 700})

    _ring(gradient, surface, size, hole_ratio, center_children=_label)
