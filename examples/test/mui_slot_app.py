from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import mui, react
from trame_client.utils.testing import enable_testing

server = get_server(client_type="react")
state = server.state
state.flavor = "vanilla"

with DivLayout(server):
    # react.Slot: a custom renderer injected into a prop that takes a
    # render function (here Select's `renderValue(value)`) instead of
    # nesting inside the widget's own `with` block.
    with react.Slot(params=["value"]) as flavor_display:
        mui.Typography(
            react.Bind(
                "value === 'vanilla' ? '🍦 Vanilla'"
                " : value === 'chocolate' ? '🍫 Chocolate'"
                " : '🥜 Pistachio'"
            ),
            classes="flavorDisplay",
        )

    with mui.Select(
        value=react.Bind("flavor"),
        on_change=react.Callback("flavor = $event.target.value"),
        render_value=flavor_display,
        classes="flavorSelect",
    ):
        mui.MenuItem("Vanilla", value="vanilla", classes="flavorVanilla")
        mui.MenuItem("Chocolate", value="chocolate", classes="flavorChocolate")
        mui.MenuItem("Pistachio", value="pistachio", classes="flavorPistachio")

enable_testing(server, "flavor")
server.start()
