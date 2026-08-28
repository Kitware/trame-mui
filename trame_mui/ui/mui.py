from trame_client.ui.core import AbstractLayout
from trame_client.widgets import html

from trame_mui.widgets import mui

__all__ = [
    "MuiLayout",
    "SinglePageLayout",
    "SinglePageWithDrawerLayout",
]


def get_trame_versions():
    import importlib.metadata

    from trame_client.utils.version import get_version

    output = []
    for pkg in importlib.metadata.distributions():
        name = pkg.metadata.get("Name", "")
        if name.startswith("trame"):
            version = get_version(name)
            output.append(f"{name.replace('trame-', '')} == {version}")

    return "\n".join(output)


class MuiLayout(AbstractLayout):
    """
    Layout composed of just a MUI theme root (ThemeProvider + CssBaseline)

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param mode: MUI palette mode - light | dark (default: light)
    :param theme: Optional MUI theme configuration (dict)
    """

    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(
            _server,
            mui.ThemeProvider(trame_server=_server, **kwargs),
            template_name=template_name,
            **kwargs,
        )

    def on_server_reload(self):
        self.server.controller.on_server_reload(self.server)


class SinglePageLayout(MuiLayout):
    """
    Layout composed of the following structure:

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param mode: MUI palette mode - light | dark (default: light)
    :param theme: Optional MUI theme configuration (dict)

    .. code-block::

        <mui-theme>
          <Box>                                 # column: 100vh
            <AppBar>
              <Toolbar>                         # layout.toolbar
                <IconButton />                  # layout.icon
                <Typography>                    # layout.title
                  Trame application
                </Typography>
              </Toolbar>
            </AppBar>
            <Box>                               # row wrapper
              <Box component="main" />          # layout.content
            </Box>
            <Toolbar variant="dense" />         # layout.footer
          </Box>
        </mui-theme>

    """

    def __init__(self, _server, template_name="main", **kwargs):
        super().__init__(_server, template_name=template_name, **kwargs)
        with (
            self,
            mui.Box(
                style=(
                    "display: flex; flex-direction: column;"
                    " height: 100vh; overflow: hidden;"
                )
            ),
        ):
            with mui.AppBar(position="static"):
                with mui.Toolbar(variant="dense") as toolbar:
                    self.toolbar = toolbar
                    self.icon = mui.IconButton(
                        "\u2630",
                        edge="start",
                        color="inherit",
                        size="small",
                        style="margin-right: 12px;",
                    )
                    self.title = mui.Typography(
                        "Trame application",
                        variant="h6",
                        component="div",
                    )

            # middle row: SinglePageWithDrawerLayout prepends the drawer
            with mui.Box(style="flex: 1; display: flex; overflow: hidden;") as row:
                self._row = row
                self.content = mui.Box(
                    component="main",
                    style="flex: 1; position: relative; overflow: auto;",
                )

            with mui.Toolbar(
                variant="dense",
                style=(
                    "min-height: 32px; border-top: 1px solid"
                    " rgba(128, 128, 128, 0.35); gap: 8px;"
                ),
            ) as footer:
                self.footer = footer
                mui.CircularProgress(
                    r_show="!!trame__busy",
                    size=16,
                    style="color: #04a94d;",
                )
                html.A(
                    "Powered by trame",
                    href="https://kitware.github.io/trame/",
                    target="_blank",
                    style=(
                        "color: #808080; font-size: 0.75rem; text-decoration: none;"
                    ),
                )
                mui.Box(style="flex: 1;")
                reload = self.server.controller.on_server_reload
                if reload.exists():
                    mui.IconButton(
                        "\u21bb",
                        size="small",
                        click=self.on_server_reload,
                    )
                with mui.Tooltip(
                    placement="top",
                    title=get_trame_versions(),
                ):
                    mui.Typography(
                        "?",
                        variant="caption",
                        style="cursor: default; opacity: 0.6;",
                    )


class SinglePageWithDrawerLayout(SinglePageLayout):
    """
    SinglePageLayout with a drawer on the left of the content
    (layout.drawer); layout.icon toggles it.

    :param _server: Server to bound the layout to
    :param template_name: Name of the template (default: main)
    :param mode: MUI palette mode - light | dark (default: light)
    :param theme: Optional MUI theme configuration (dict)
    :param show_drawer: Start with drawer open (default: True)
    :param width: Drawer width in pixel (default: 300)
    """

    def __init__(
        self, _server, template_name="main", show_drawer=True, width=300, **kwargs
    ):
        super().__init__(_server, template_name=template_name, **kwargs)
        drawer_name = f"{template_name}_drawer"
        with self._row:
            self.drawer = mui.Drawer(
                variant="persistent",
                anchor="left",
                open=(drawer_name, show_drawer),
                slot_props=(
                    "{ paper: { style: { position: 'relative', width: '"
                    + str(width)
                    + "px' } } }",
                ),
            )
        # drawer before the content
        row_children = self._row.children
        row_children.insert(0, row_children.pop())

        self.icon.click = f"{drawer_name} = !{drawer_name}"
