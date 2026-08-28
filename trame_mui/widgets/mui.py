"""MUI (Material UI) widgets for trame applications using client_type="react".

All @mui/material components are exposed (see mui_generated.py). Any MUI prop
can be passed as a snake_case keyword argument; two-way binding uses
``r_model=`` / ``r_model_number=`` on stateful components (TextField, Slider,
Checkbox, Select, Dialog, ...).
"""

from .core import MuiHtmlElement
from .mui_generated import *  # noqa: F403
from .mui_generated import __all__ as _generated_all

__all__ = [*_generated_all, "ThemeProvider"]


class ThemeProvider(MuiHtmlElement):
    """MUI theme + CssBaseline wrapper - place at the layout root.

    :param mode: light | dark
    :param theme: Optional MUI theme configuration (dict)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-theme", children, **kwargs)
