from trame.app import TrameApp
from trame.ui.html import DivLayout
from trame.decorators import change

from trame.widgets import mui, react


class MuiSwitch(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")
        self._build_ui()

    @change("dark")
    def on_count(self, dark, **_):
        print(f"dark={dark}")

    def _build_ui(self):
        with DivLayout(self.server) as self.ui:
            mui.Typography(
                [
                    "trame-mui: switch(",
                    react.Bind("dark ? 'dark' : 'light'", dark=False),
                    ")",

                ],
                variant="h5",
            )
            a = mui.Switch(
                checked=react.Bind("dark", dark=False),
                on_change=react.Callback(
                    "dark = $event.target.checked"
                ),
            )
            print(a.html)


def main():
    app = MuiSwitch()
    app.server.start()


if __name__ == "__main__":
    main()
