from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import react
from trame_client.utils.testing import enable_testing

from trame_mui.widgets import mui

server = get_server(client_type="react")
state = server.state

state.count = 0
state.message = ""
state.dialog_open = False

with DivLayout(server), mui.ThemeProvider():
    with mui.Stack(spacing=2, style={"padding": "20px"}):
        mui.Typography(["count = ", react.Bind("count")], classes="countValue")
        mui.Button(
            "Add",
            classes="plusButton",
            variant="contained",
            on_click=react.Callback("count++"),
        )
        mui.TextField(
            value=react.Bind("message"),
            on_change=react.Callback("message = $event.target.value"),
            label="Message",
        )
        mui.Button(
            "Open dialog",
            classes="openDialog",
            on_click=react.Callback("dialog_open = true"),
        )
    with mui.Dialog(open=react.Bind("dialog_open")):
        mui.DialogTitle("Hello from MUI", classes="dialogTitle")
        with mui.DialogActions():
            mui.Button(
                "Close",
                classes="closeDialog",
                on_click=react.Callback("dialog_open = false"),
            )

enable_testing(server, "count", "message", "dialog_open")
server.start()
