from playwright.sync_api import expect
import pytest


@pytest.mark.parametrize("server_path", ["examples/test/mui_app.py"])
def test_mui_widgets(server, page):
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    # Button click -> server state
    count_value = page.locator(".countValue")
    expect(count_value).to_have_text("count = 0")
    page.locator(".plusButton").click()
    expect(count_value).to_have_text("count = 1")
    assert server.get("count") == 1

    # TextField r_model -> server state
    page.locator("input[type=text]").fill("hello mui")
    page.wait_for_timeout(200)
    assert server.get("message") == "hello mui"

    # Dialog controlled by state (r_model="dialog_open")
    page.locator(".openDialog").click()
    expect(page.locator(".dialogTitle")).to_be_visible()
    assert server.get("dialog_open") is True
    page.locator(".closeDialog").click()
    expect(page.locator(".dialogTitle")).not_to_be_visible()
    page.wait_for_timeout(200)
    assert server.get("dialog_open") is False


@pytest.mark.parametrize("server_path", ["examples/test/mui_slot_app.py"])
def test_mui_select_render_value_slot(server, page):
    """react.Slot as a custom renderer injected into a prop that takes a
    render function - Select's `renderValue(value)` here - rather than
    nested inside the widget's own `with` block (see mui_slot_app.py).

    Regression coverage for two fixes this exercises together:
      - `literal_children` (trame-client's resolveLiteralChildren.js):
        without it, MUI's SelectInput can't read `child.props.value` off
        its MenuItem children, so nothing renders/selects correctly.
      - `react.Slot`: renderValue must be called with the live `value` and
        re-invoked whenever it changes, proving the slot's render prop is
        wired through classifyProps -> makeSlotRenderProp correctly.
    """
    url = f"http://127.0.0.1:{server.port}/"
    page.goto(url)

    console_errors = []
    page.on(
        "console",
        lambda msg: console_errors.append(msg.text) if msg.type == "error" else None,
    )

    select_box = page.locator(".flavorSelect [role='combobox']")
    expect(select_box).to_have_text("🍦 Vanilla")

    select_box.click()
    page.locator(".flavorChocolate").click()

    expect(select_box).to_have_text("🍫 Chocolate")
    assert server.get("flavor") == "chocolate"

    select_box.click()
    page.locator(".flavorPistachio").click()

    expect(select_box).to_have_text("🥜 Pistachio")
    assert server.get("flavor") == "pistachio"

    # trame-client's react bundle always probes a legacy wslink REST
    # endpoint (POST document.baseURI + "paraview/") on startup before
    # falling back to the real websocket connection; unrelated to this
    # widget library, so it's filtered out rather than asserted away.
    unexpected_errors = [
        msg for msg in console_errors if "405 (Method Not Allowed)" not in msg
    ]
    assert unexpected_errors == []
