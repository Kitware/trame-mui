"""Sample trame application mixing trame-mui (MUI) widgets with
application-defined React components (see www/components.js - no build step).
"""

from pathlib import Path

from trame.app import get_server
from trame.ui.html import DivLayout
from trame_client.widgets.core import AbstractElement

from trame_mui.widgets import mui

server = get_server(client_type="react")
state, ctrl = server.state, server.controller

# -----------------------------------------------------------------------------
# Application-provided React components
# -----------------------------------------------------------------------------

server.enable_module(
    {
        "serve": {"my_app": str(Path(__file__).with_name("www").resolve())},
        "scripts": ["my_app/components.js"],
        "react_use": ["MyWidgets"],
    }
)


class Sparkline(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("my-sparkline", children, **kwargs)
        self._attr_names += ["points", "width", "height", "color"]


class ColorSwatch(AbstractElement):
    def __init__(self, children=None, **kwargs):
        super().__init__("my-color-swatch", children, **kwargs)
        self._attr_names += ["colors"]


# -----------------------------------------------------------------------------
# State
# -----------------------------------------------------------------------------

state.value = 5
state.history = [5]
state.color = "#1976d2"

COLORS = ["#1976d2", "#9c27b0", "#2e7d32", "#ed6c02", "#d32f2f"]


@state.change("value")
def on_value(value, **kwargs):
    state.history = [*state.history[-49:], value]


def clear_history():
    state.history = [state.value]


# -----------------------------------------------------------------------------
# UI
# -----------------------------------------------------------------------------

with (
    DivLayout(server) as layout,
    mui.ThemeProvider(
        theme=("{ palette: { primary: { main: color } } }",),
    ),
    mui.Container(max_width="sm", style="padding-top: 40px;"),
):
    with mui.Card(elevation=4):
        with mui.CardContent():
            with mui.Stack(spacing=3):
                mui.Typography(
                    "MUI widgets + custom React components",
                    variant="h5",
                )

                # --- MUI widgets (trame-mui)
                mui.Slider(
                    r_model_number="value",
                    min=0,
                    max=10,
                    step=1,
                    value_label_display="auto",
                )

                # --- custom React components (www/components.js)
                mui.Typography(
                    "Sparkline ({{ history.length }} samples)",
                    variant="subtitle2",
                    color="text.secondary",
                )
                Sparkline(points=("history",), color=("color",))
                mui.Typography(
                    "Theme color", variant="subtitle2", color="text.secondary"
                )
                ColorSwatch(r_model="color", colors=("colors", COLORS))

                mui.Button(
                    "Clear history",
                    variant="contained",
                    click=clear_history,
                )

if __name__ == "__main__":
    server.start()
