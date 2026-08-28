from trame.app import get_server
from trame.ui.html import DivLayout

from trame_mui.widgets import mui

server = get_server(client_type="react")
state, ctrl = server.state, server.controller

state.count = 3
state.message = "hello trame"
state.dark = False
state.dialog_open = False
state.flavor = "vanilla"


@state.change("count")
def on_count(count, **kwargs):
    print(f"count={count}")


def reset():
    state.count = 0
    state.message = ""


with DivLayout(server) as layout:
    with mui.ThemeProvider(mode=("dark ? 'dark' : 'light'",)):
        with mui.Container(max_width="sm", style="padding-top: 40px;"):
            with mui.Card(elevation=4), mui.CardContent():
                with mui.Stack(spacing=3):
                    mui.Typography(
                        "trame-mui: MUI widgets from Python",
                        variant="h5",
                    )
                    mui.Typography(
                        "count = {{ count }} | message = {{ message }} |"
                        " flavor = {{ flavor }}",
                        variant="body2",
                        color="text.secondary",
                    )
                    mui.Slider(
                        r_model_number="count",
                        min=0,
                        max=10,
                        step=1,
                        marks=True,
                        value_label_display="auto",
                    )
                    mui.TextField(
                        r_model="message",
                        label="Message",
                        variant="outlined",
                        full_width=True,
                        helper_text="Synchronized with the trame state",
                    )
                    with mui.Select(r_model="flavor", full_width=True):
                        mui.MenuItem("Vanilla", value="vanilla")
                        mui.MenuItem("Chocolate", value="chocolate")
                        mui.MenuItem("Pistachio", value="pistachio")
                    with mui.Stack(direction="row", spacing=2):
                        mui.Switch(r_model="dark")
                        mui.Typography("Dark mode", variant="body1")
                    with mui.Stack(direction="row", spacing=2):
                        mui.Button(
                            "Reset",
                            variant="contained",
                            color="primary",
                            click=reset,
                        )
                        mui.Button(
                            "About",
                            variant="outlined",
                            click="dialog_open = true",
                        )
            with mui.Dialog(r_model="dialog_open"):
                mui.DialogTitle("trame-mui")
                with mui.DialogContent():
                    mui.DialogContentText(
                        "All 149 MUI components driven from Python "
                        "through the native trame react client."
                    )
                with mui.DialogActions():
                    mui.Button("Close", click="dialog_open = false")

if __name__ == "__main__":
    server.start()
