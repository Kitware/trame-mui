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
