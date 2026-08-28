"""Base class for MUI widgets.

MUI's API surface is large and evolving; rather than hard-coding every prop,
MuiHtmlElement accepts any keyword argument and declares it on the fly:
``full_width=True`` becomes the ``fullWidth`` prop, ``input_change=...``
becomes the ``inputChange`` event, and so on. The react client forwards the
evaluated props straight to the MUI component.

Structural directives (``r_if``, ``r_for``, ``r_model``, ...) and standard
HTML attributes/DOM events keep their usual trame handling.
"""

from trame_client.widgets.core import (
    SHARED_ATTRIBUTES,
    SHARED_EVENTS,
    AbstractElement,
)

from trame_mui import module

# Kwargs handled natively by AbstractElement (directives, html attrs, DOM events)
_NATIVE_KEYS = set()
for _item in [*SHARED_ATTRIBUTES, *SHARED_EVENTS]:
    _NATIVE_KEYS.add(_item if isinstance(_item, str) else _item[0])

# MUI callback props exposed as trame events (onChange, onClose, ...)
MUI_EVENTS = {
    "change",
    "close",
    "open",
    "delete",
    "toggle",
    "expand",
    "input_change",
    "click_away",
    "page_change",
    "rows_per_page_change",
}


def to_camel(name):
    first, *rest = name.split("_")
    return first + "".join(part.title() for part in rest)


class MuiHtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        properties = []
        events = []
        for key in kwargs:
            if key.startswith(("v_", "r_", "__")) or key in _NATIVE_KEYS:
                continue
            if key in ("trame_server", "ctx_name"):
                continue
            if key in MUI_EVENTS:
                events.append(key)
                continue
            camel = to_camel(key)
            properties.append((key, camel) if camel != key else key)

        kwargs["__properties"] = [*kwargs.get("__properties", []), *properties]
        kwargs["__events"] = [*kwargs.get("__events", []), *events]
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)
