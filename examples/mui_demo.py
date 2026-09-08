from trame.app import TrameApp
from trame.ui.html import DivLayout
from trame.decorators import change

from trame.widgets import mui, react


class MuiDemo(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")
        self._build_ui()

    @change("count")
    def on_count(self, count, **_):
        print(f"count={count}")

    def reset(self):
        self.state.count = 0
        self.state.message = ""

    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            with mui.ThemeProvider(mode=react.Bind("dark ? 'dark' : 'light'", dark=False)):
                with mui.Container(max_width="sm", style={"paddingTop": "40px"}):
                    with mui.Card(elevation=4), mui.CardContent():
                        with mui.Stack(spacing=3):
                            mui.Typography(
                                "trame-mui: MUI widgets from Python",
                                variant="h5",
                            )
                            mui.Typography(
                                [
                                    "count = ",
                                    react.Bind("count", count=3),
                                    " | message = ",
                                    react.Bind("message", message="hello trame"),
                                    " | flavor = ",
                                    react.Bind("flavor", flavor="vanilla"),
                                    " | dark = ",
                                    react.Bind("dark ? 'Dark' : 'Light'", dark=True),
                                ],
                                variant="body2",
                                color="text.secondary",
                            )
                            mui.Slider(
                                value=react.Bind("count"),
                                on_change=react.Callback(
                                    "count = Number($event.target.value)"
                                ),
                                min=0,
                                max=10,
                                step=1,
                                marks=True,
                                value_label_display="auto",
                            )
                            mui.TextField(
                                value=react.Bind("message"),
                                on_change=react.Callback(
                                    "message = $event.target.value"
                                ),
                                label="Message",
                                variant="outlined",
                                full_width=True,
                                helper_text="Synchronized with the trame state",
                            )
                            # react.Slot: a custom renderer injected into a MUI
                            # prop that takes a render function (here Select's
                            # `renderValue(value)`). Must be defined outside the
                            # widget's own `with` block, then passed in like any
                            # other prop - the client calls it with the current
                            # `value` and mounts whatever it renders in place of
                            # the plain text MUI would otherwise show.
                            with react.Slot(params=["value"]) as flavor_display:
                                mui.Typography(
                                    react.Bind(
                                        "value === 'vanilla' ? '🍦 Vanilla'"
                                        " : value === 'chocolate' ? '🍫 Chocolate'"
                                        " : '🥜 Pistachio'"
                                    ),
                                    variant="body1",
                                )

                            with mui.Select(
                                value=react.Bind("flavor", flavor="vanilla"),
                                on_change=react.Callback(
                                    "flavor = $event.target.value"
                                ),
                                render_value=flavor_display,
                                full_width=True,
                            ):
                                mui.MenuItem("Vanilla", value="vanilla")
                                mui.MenuItem("Chocolate", value="chocolate")
                                mui.MenuItem("Pistachio", value="pistachio")

                            with mui.Stack(direction="row", spacing=2):
                                mui.Switch(
                                    checked=react.Bind("dark"),
                                    on_change=react.Callback(
                                        "dark = $event.target.checked"
                                    ),
                                )
                                mui.Typography("Dark mode", variant="body1")
                                with mui.Stack(direction="row", spacing=2):
                                    mui.Button(
                                        "Reset",
                                        variant="contained",
                                        color="primary",
                                        on_click=react.Callback(self.reset),
                                    )
                                    mui.Button(
                                        "About",
                                        variant="outlined",
                                        on_click=react.Callback("dialog_open = true"),
                                    )
                                    with mui.Dialog(
                                        open=react.Bind(
                                            "dialog_open", dialog_open=False
                                        ),
                                    ):
                                        mui.DialogTitle("trame-mui")
                                        with mui.DialogContent():
                                            mui.DialogContentText(
                                                "All 149 MUI components driven from Python "
                                                "through the native trame react client."
                                            )
                                            with mui.DialogActions():
                                                mui.Button(
                                                    "Close",
                                                    on_click=react.Callback(
                                                        "dialog_open = false"
                                                    ),
                                                )


def main():
    app = MuiDemo()
    app.server.start()


if __name__ == "__main__":
    main()
