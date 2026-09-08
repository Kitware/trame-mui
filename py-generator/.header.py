##########################################################
# DO NOT EDIT: GENERATED FILE
# => instead run: react-components/generate_python.py
##########################################################

# ruff: noqa: E501

from trame_client.widgets.core import AbstractElement
from trame_mui import module


class MuiHtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)
