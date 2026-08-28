from trame.app import get_server
from trame.ui.html import DivLayout
from trame_client.utils.testing import enable_testing

from trame_mui.widgets import mui

server = get_server(client_type="react")
state = server.state

state.count = 0
state.message = ""
state.dialog_open = False

with DivLayout(server), mui.ThemeProvider():
    with mui.Stack(spacing=2, style="padding: 20px;"):
        mui.Typography("count = {{ count }}", classes="countValue")
        mui.Button(
            "Add",
            classes="plusButton",
            variant="contained",
            click="count++",
        )
        mui.TextField(r_model="message", label="Message")
        mui.Button(
            "Open dialog",
            classes="openDialog",
            click="dialog_open = true",
        )
    with mui.Dialog(r_model="dialog_open"):
        mui.DialogTitle("Hello from MUI", classes="dialogTitle")
        with mui.DialogActions():
            mui.Button(
                "Close",
                classes="closeDialog",
                click="dialog_open = false",
            )

enable_testing(server, "count", "message", "dialog_open")
server.start()
