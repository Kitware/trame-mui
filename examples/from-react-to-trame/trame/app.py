"""
A trame + trame-mui port of the standalone React dashboard in ../react.

trame_mui only wraps @mui/material (no @mui/x-charts), so the charts are
hand-rolled: sparkline/revenue trend as raw SVG paths (svg_elements.py,
charts.py), donut/gauge/bars as plain CSS (conic-gradient / flex heights).
Everything else is a direct port onto the equivalent mui.* widget.

Requires trame-server>=3.15 and a trame-client build with client_type="react"
support (not released yet at the time this was written - see ../README.md).
"""

from trame.app import TrameApp
from trame.ui.mui import SinglePageWithDrawerLayout
from trame.widgets import mui, react

import charts
import data
from palette import CATEGORICAL_LIGHT, OTHER_LIGHT, STATUS, SURFACE, series

DRAWER_WIDTH = 260

NAV_ITEMS = [
    ("Dashboard", "📊"),
    ("Analytics", "📈"),
    ("Orders", "🧾"),
    ("Customers", "👥"),
    ("Products", "📦"),
]
SECONDARY_NAV_ITEMS = [
    ("Settings", "⚙️"),
    ("Help & support", "❓"),
]

STATUS_CHIP = {
    "Completed": ("success", "✓ Completed"),
    "Processing": ("info", "↻ Processing"),
    "Pending": ("warning", "◔ Pending"),
    "Cancelled": ("error", "✕ Cancelled"),
}

THEME = {
    "palette": {
        "primary": {"main": CATEGORICAL_LIGHT[0]},
        "secondary": {"main": CATEGORICAL_LIGHT[1]},
        "success": {"main": STATUS["good"]},
        "warning": {"main": STATUS["warning"]},
        "error": {"main": STATUS["critical"]},
    },
    "shape": {"borderRadius": 12},
    "components": {
        "MuiCard": {
            "styleOverrides": {
                "root": {
                    "border": "1px solid rgba(128, 128, 128, 0.2)",
                    "boxShadow": "none",
                }
            }
        },
        "MuiButton": {
            "styleOverrides": {"root": {"textTransform": "none", "fontWeight": 600}}
        },
        "MuiChip": {"styleOverrides": {"root": {"fontWeight": 600}}},
    },
}


def initials_of(name):
    parts = name.split(" ")
    return (parts[0][0] + parts[-1][0]).upper() if len(parts) > 1 else name[:2].upper()


class Dashboard(TrameApp):
    def __init__(self, server=None):
        super().__init__(server, client_type="react")

        self.state.update(
            {
                "nav": "Dashboard",
                "tab": 0,
                "appearance": "system",
                "density": "comfortable",
                "freq": 30,
                "channel_email": True,
                "channel_push": True,
                "channel_sms": False,
                "notif_open": False,
                "account_open": False,
                "confirm_open": False,
                "snack_open": False,
                "snack_message": "",
                "snack_severity": "success",
            }
        )

        self._build_ui()

    # -------------------------------------------------------------------
    # Actions
    # -------------------------------------------------------------------

    def notify(self, message, severity="success"):
        self.state.snack_message = message
        self.state.snack_severity = severity
        self.state.snack_open = True

    def on_refresh(self):
        self.notify("Dashboard refreshed", "info")

    def on_save_preferences(self):
        self.notify("Preferences saved successfully", "success")

    def on_delete_confirm(self):
        self.state.confirm_open = False
        self.notify("Account deletion cancelled — this was just a demo", "info")

    # -------------------------------------------------------------------
    # UI
    # -------------------------------------------------------------------

    def _build_ui(self):
        with SinglePageWithDrawerLayout(
            self.server,
            width=DRAWER_WIDTH,
            theme=THEME,
            mode=react.Bind("dark ? 'dark' : 'light'", dark=False),
        ) as self.ui:
            self.ui.title.set_text("Insight")
            self._build_header()
            self._build_drawer()
            self._build_content()
            self._build_global_snackbar()

    def _build_header(self):
        with self.ui.toolbar:
            mui.Box(style={"flexGrow": "1"})
            mui.TextField(
                placeholder="Search…",
                size="small",
                variant="outlined",
                style={"width": "220px", "marginRight": "8px"},
            )
            mui.IconButton(
                react.Bind("dark ? '🌙' : '☀️'", dark=False),
                color="inherit",
                on_click=react.Callback("dark = !dark"),
            )
            with mui.IconButton(color="inherit", on_click=react.Callback("notif_open = true")):
                with mui.Badge(
                    badge_content=len(data.NOTIFICATIONS),
                    color="error",
                ):
                    mui.Typography("🔔"),
            with mui.IconButton(
                on_click=react.Callback("account_open = true"),
                color="inherit",
            ):
                mui.Avatar("SJ", style={"width": "30px", "height": "30px", "fontSize": "14px"})


        with mui.Dialog(
            open=react.Bind("notif_open", notif_open=False),
            on_close=react.Callback("notif_open = false"),
            max_width="xs",
            full_width=True,
        ):
            mui.DialogTitle("Notifications")
            with mui.DialogContent():
                with mui.List(disable_padding=True):
                    for n in data.NOTIFICATIONS:
                        with mui.ListItem(divider=True):
                            mui.ListItemText(
                                primary=n["title"],
                                secondary=f"{n['detail']} · {n['time']}",
                            )
            with mui.DialogActions():
                mui.Button("Close", on_click=react.Callback("notif_open = false"))

        with mui.Dialog(
            open=react.Bind("account_open", account_open=False),
            on_close=react.Callback("account_open = false"),
            max_width="xs",
            full_width=True,
        ):
            mui.DialogTitle("Account")
            with mui.DialogContent():
                with mui.Stack(direction="row", spacing=2, style={"alignItems": "center", "marginBottom": "12px"}):
                    mui.Avatar("SJ", style={"backgroundColor": series(0)})
                    with mui.Box():
                        mui.Typography("Sebastien Jourdain", style={"fontWeight": 700})
                        mui.Typography(
                            "sebastien.jourdain@kitware.com",
                            variant="body2",
                            color="text.secondary",
                        )
            with mui.DialogActions():
                mui.Button("Sign out", on_click=react.Callback("account_open = false"))
                mui.Button(
                    "Close",
                    variant="contained",
                    on_click=react.Callback("account_open = false"),
                )

    def _build_drawer(self):
        with self.ui.drawer:
            with mui.List():
                for label, icon in NAV_ITEMS:
                    with mui.ListItemButton(
                        selected=react.Bind(f"nav === '{label}'", nav="Dashboard"),
                        on_click=react.Callback(f"nav = '{label}'"),
                    ):
                        mui.ListItemIcon(icon)
                        mui.ListItemText(primary=label)
            mui.Divider()
            with mui.List():
                for label, icon in SECONDARY_NAV_ITEMS:
                    with mui.ListItemButton(
                        selected=react.Bind(f"nav === '{label}'", nav="Dashboard"),
                        on_click=react.Callback(f"nav = '{label}'"),
                    ):
                        mui.ListItemIcon(icon)
                        mui.ListItemText(primary=label)

    def _build_global_snackbar(self):
        with mui.Snackbar(
            open=react.Bind("snack_open", snack_open=False),
            on_close=react.Callback("snack_open = false"),
            auto_hide_duration=3500,
            anchor_origin={"vertical": "bottom", "horizontal": "right"},
        ):
            mui.Alert(
                react.Bind("snack_message"),
                severity=react.Bind("snack_severity", snack_severity="success"),
                variant="filled",
                on_close=react.Callback("snack_open = false"),
            )

    # -------------------------------------------------------------------
    # Dashboard body
    # -------------------------------------------------------------------

    def _build_content(self):
        with self.ui.content:
            with mui.Box(style={"padding": "24px", "maxWidth": "1400px", "margin": "0 auto"}):
                with mui.Stack(
                    direction="row",
                    style={"justifyContent": "space-between", "alignItems": "center", "marginBottom": "24px"},
                ):
                    with mui.Box():
                        with mui.Stack(direction="row", spacing=0.5, style={"alignItems": "center", "marginBottom": "4px"}):
                            mui.Link("Home", underline="hover", color="text.secondary", variant="body2")
                            mui.Typography("/", variant="body2", color="text.secondary")
                            mui.Typography("Dashboard", variant="body2", color="text.primary")
                        mui.Typography("Welcome back, Sebastien", variant="h5")
                    # Plain IconButton, no Tooltip wrapper: MUI's Tooltip
                    # clones its one child via React.Children to attach hover
                    # handlers, which doesn't play well with our lazily
                    # rendered widget tree (it ends up rendering the button
                    # twice - once in place, once cloned).
                    mui.IconButton("↻", on_click=react.Callback(self.on_refresh))

                with mui.Grid(container=True, spacing=2.5):
                    for i, item in enumerate(data.KPIS):
                        with mui.Grid(size={"xs": 12, "sm": 6, "lg": 3}):
                            self._stat_card(item, series(i))

                    with mui.Grid(size={"xs": 12, "lg": 8}):
                        self._revenue_card()
                    with mui.Grid(size={"xs": 12, "lg": 4}):
                        self._traffic_card()

                    with mui.Grid(size={"xs": 12, "lg": 8}):
                        self._region_card()
                    with mui.Grid(size={"xs": 12, "lg": 4}):
                        self._goal_card()

                    with mui.Grid(size={"xs": 12, "lg": 7}):
                        self._orders_card()
                    with mui.Grid(size={"xs": 12, "lg": 5}):
                        self._team_card()

                    with mui.Grid(size=12):
                        self._preferences_card()

    def _stat_card(self, item, color):
        positive = item["delta"] >= 0
        with mui.Card(style={"height": "100%"}):
            with mui.CardContent():
                with mui.Stack(direction="row", spacing=1.5, style={"alignItems": "center"}):
                    mui.Avatar(
                        item["icon"],
                        variant="rounded",
                        style={
                            "backgroundColor": "rgba(128, 128, 128, 0.12)",
                            "width": "40px",
                            "height": "40px",
                            "fontSize": "18px",
                        },
                    )
                    mui.Typography(item["label"], variant="body2", color="text.secondary", style={"fontWeight": 600})

                with mui.Stack(
                    direction="row",
                    style={"alignItems": "flex-end", "justifyContent": "space-between", "marginTop": "16px"},
                ):
                    with mui.Box():
                        mui.Typography(item["value"], variant="h4")
                        mui.Chip(
                            label=f"{'▲' if positive else '▼'} {'+' if positive else ''}{item['delta']}%",
                            size="small",
                            color="success" if positive else "error",
                            variant="outlined",
                            style={"marginTop": "8px"},
                        )
                    with mui.Box(style={"width": "96px", "height": "40px"}):
                        charts.sparkline(item["trend"], color)

    def _revenue_card(self):
        total = sum(data.REVENUE_TREND)
        with mui.Card(style={"height": "100%"}):
            with mui.CardContent():
                with mui.Stack(
                    direction="row",
                    style={"justifyContent": "space-between", "alignItems": "flex-start", "marginBottom": "8px"},
                ):
                    with mui.Box():
                        mui.Typography("Revenue", variant="subtitle1", style={"fontWeight": 700})
                        mui.Typography("Last 12 months", variant="caption", color="text.secondary")
                    mui.Chip(
                        label=f"${total / 1000:.0f}K total",
                        size="small",
                        color="primary",
                        variant="outlined",
                    )
                charts.revenue_chart(data.REVENUE_TREND, data.MONTHS, series(0), SURFACE)

    def _traffic_card(self):
        with mui.Card(style={"height": "100%"}):
            with mui.CardContent():
                mui.Typography("Traffic sources", variant="subtitle1", style={"fontWeight": 700})
                mui.Typography("Sessions by channel, last 30 days", variant="caption", color="text.secondary")

                total = sum(d["value"] for d in data.TRAFFIC_SOURCES)
                # Static (not mode-reactive): these colors feed a single
                # conic-gradient CSS string built in Python, and a `Bind`
                # marker can only stand in for a *whole* prop value, not a
                # fragment spliced into a larger string.
                colors = [
                    CATEGORICAL_LIGHT[0],
                    CATEGORICAL_LIGHT[2],
                    CATEGORICAL_LIGHT[4],
                    OTHER_LIGHT,
                ]
                with mui.Box(style={"margin": "16px 0"}):
                    charts.donut_chart(data.TRAFFIC_SOURCES, "value", colors, SURFACE)

                with mui.Stack(spacing=1, style={"marginTop": "8px"}):
                    for d, color in zip(data.TRAFFIC_SOURCES, colors):
                        with mui.Stack(
                            direction="row",
                            style={"alignItems": "center", "justifyContent": "space-between"},
                        ):
                            with mui.Stack(direction="row", spacing=1, style={"alignItems": "center"}):
                                mui.Box(style={"width": "10px", "height": "10px", "borderRadius": "2px", "background": color})
                                mui.Typography(d["label"], variant="body2")
                            mui.Typography(
                                f"{round(d['value'] / total * 100)}%",
                                variant="body2",
                                color="text.secondary",
                            )

    def _region_card(self):
        with mui.Card(style={"height": "100%"}):
            with mui.CardContent():
                mui.Typography("Sales by region", variant="subtitle1", style={"fontWeight": 700})
                mui.Typography("Units sold, current quarter", variant="caption", color="text.secondary")
                with mui.Box(style={"marginTop": "16px"}):
                    charts.bar_chart(data.SALES_BY_REGION, "value", "region", series(0))

    def _goal_card(self):
        current = sum(v for v in data.REVENUE_TREND[-1:]) // 1000
        goal_k = 900
        current_k = 824
        pct = round(current_k / goal_k * 100)
        with mui.Card(style={"height": "100%"}):
            with mui.CardContent():
                mui.Typography("Monthly goal", variant="subtitle1", style={"fontWeight": 700})
                mui.Typography(f"Revenue vs. ${goal_k}K target", variant="caption", color="text.secondary")
                with mui.Box(style={"marginTop": "12px"}):
                    charts.gauge_chart(
                        pct,
                        CATEGORICAL_LIGHT[0],  # static: see the donut's comment above
                        "rgba(42, 120, 214, 0.15)",
                        SURFACE,
                    )
                mui.Typography(
                    f"${current_k}K of ${goal_k}K",
                    variant="body2",
                    color="text.secondary",
                    style={"textAlign": "center", "marginTop": "8px"},
                )

    def _orders_card(self):
        with mui.Card():
            with mui.CardContent():
                with mui.Stack(
                    direction="row",
                    style={"justifyContent": "space-between", "alignItems": "center"},
                ):
                    mui.Typography("Recent orders", variant="subtitle1", style={"fontWeight": 700})
                    mui.Button("View all", size="small")

                with mui.TableContainer(style={"marginTop": "8px"}):
                    with mui.Table(size="small"):
                        with mui.TableHead():
                            with mui.TableRow():
                                mui.TableCell("Order")
                                mui.TableCell("Customer")
                                mui.TableCell("Date")
                                mui.TableCell("Amount", align="right")
                                mui.TableCell("Status", align="right")
                        with mui.TableBody():
                            for row in data.RECENT_ORDERS:
                                color, label = STATUS_CHIP[row["status"]]
                                with mui.TableRow(hover=True):
                                    mui.TableCell(row["id"], style={"fontWeight": 600})
                                    with mui.TableCell():
                                        with mui.Stack(direction="row", spacing=1, style={"alignItems": "center"}):
                                            mui.Avatar(
                                                initials_of(row["customer"]),
                                                style={"width": "26px", "height": "26px", "fontSize": "12px"},
                                            )
                                            mui.Typography(row["customer"], variant="body2")
                                    mui.TableCell(row["date"])
                                    mui.TableCell(row["amount"], align="right")
                                    with mui.TableCell(align="right"):
                                        mui.Chip(
                                            label=label,
                                            size="small",
                                            color=color,
                                            variant="outlined",
                                        )

    def _team_card(self):
        with mui.Card():
            with mui.CardContent():
                with mui.Stack(
                    direction="row",
                    style={"justifyContent": "space-between", "alignItems": "center", "marginBottom": "8px"},
                ):
                    with mui.Box():
                        mui.Typography("Team workload", variant="subtitle1", style={"fontWeight": 700})
                        mui.Typography(f"{len(data.TEAM)} members", variant="caption", color="text.secondary")
                    with mui.AvatarGroup(max=4):
                        for m in data.TEAM:
                            mui.Avatar(m["initials"], style={"width": "28px", "height": "28px", "fontSize": "12px"})

                with mui.List(disable_padding=True):
                    for m in data.TEAM:
                        color = "success" if m["completion"] >= 80 else ("warning" if m["completion"] < 50 else "primary")
                        with mui.ListItem(disable_gutters=True):
                            with mui.ListItemAvatar():
                                mui.Avatar(m["initials"], style={"backgroundColor": series(0)})
                            mui.ListItemText(primary=m["name"], secondary=m["role"])
                            with mui.Box(style={"width": "120px", "marginLeft": "16px"}):
                                mui.LinearProgress(
                                    variant="determinate",
                                    value=m["completion"],
                                    color=color,
                                    style={"height": "8px", "borderRadius": "4px"},
                                )
                                mui.Typography(
                                    f"{m['completion']}%",
                                    variant="caption",
                                    color="text.secondary",
                                    style={"display": "block", "textAlign": "right", "marginTop": "4px"},
                                )

    def _preferences_card(self):
        with mui.Card():
            with mui.CardContent():
                mui.Typography("Preferences", variant="subtitle1", style={"fontWeight": 700})
                mui.Typography(
                    "Account, notification and appearance settings",
                    variant="caption",
                    color="text.secondary",
                )

                with mui.Tabs(value=react.Bind("tab", tab=0), style={"marginTop": "8px", "borderBottom": "1px solid rgba(128,128,128,0.2)"}):
                    mui.Tab(label="General", value=0, on_click=react.Callback("tab = 0"))
                    mui.Tab(label="Notifications", value=1, on_click=react.Callback("tab = 1"))
                    mui.Tab(label="Appearance", value=2, on_click=react.Callback("tab = 2"))

                with react.If("tab === 0"):
                    self._general_tab()
                with react.If("tab === 1"):
                    self._notifications_tab()
                with react.If("tab === 2"):
                    self._appearance_tab()

                mui.Divider(style={"margin": "24px 0"})

                with mui.Accordion(default_expanded=False):
                    with mui.AccordionSummary():
                        mui.Typography("How is my data used?", variant="body2", style={"fontWeight": 600})
                    with mui.AccordionDetails():
                        mui.Typography(
                            "This demo dashboard uses only local mock data — nothing is"
                            " sent to a server.",
                            variant="body2",
                            color="text.secondary",
                        )
                with mui.Accordion(default_expanded=False):
                    with mui.AccordionSummary():
                        mui.Typography("Can I export my preferences?", variant="body2", style={"fontWeight": 600})

                    with mui.AccordionDetails():
                        mui.Typography(
                            "Not yet — this is a widget showcase ported from the"
                            " react/ sibling example.",
                            variant="body2",
                            color="text.secondary",
                        )


                with mui.Stack(direction="row", spacing=1.5, style={"justifyContent": "flex-end", "marginTop": "24px"}):
                    mui.Button(
                        "Delete account",
                        color="error",
                        variant="outlined",
                        on_click=react.Callback("confirm_open = true"),
                    )
                    mui.Button(
                        "Save changes",
                        variant="contained",
                        on_click=react.Callback(self.on_save_preferences),
                    )

        with mui.Dialog(open=react.Bind("confirm_open", confirm_open=False)):
            mui.DialogTitle("Delete account?")
            with mui.DialogContent():
                mui.Typography(
                    "This action cannot be undone. All of your data will be"
                    " permanently removed. (This is a demo — nothing will"
                    " actually be deleted.)",
                    variant="body2",
                )
            with mui.DialogActions():
                mui.Button("Cancel", on_click=react.Callback("confirm_open = false"))
                mui.Button(
                    "Delete",
                    color="error",
                    variant="contained",
                    on_click=react.Callback(self.on_delete_confirm),
                )

    def _general_tab(self):
        with mui.Grid(container=True, spacing=2, style={"marginTop": "8px"}):
            with mui.Grid(size={"xs": 12, "sm": 6}):
                mui.TextField(
                    label="Display name",
                    default_value="Sebastien Jourdain",
                    full_width=True,
                    size="small",
                )
            with mui.Grid(size={"xs": 12, "sm": 6}):
                with mui.TextField(
                    select=True,
                    label="Timezone",
                    value=react.Bind("timezone", timezone="Pacific Time (US)"),
                    on_change=react.Callback("timezone = $event.target.value"),
                    full_width=True,
                    size="small",
                    literal_children=True,
                ):
                    for tz in [
                        "Pacific Time (US)",
                        "Eastern Time (US)",
                        "Central European Time",
                        "Tokyo Standard Time",
                    ]:
                        mui.MenuItem(tz, value=tz)
            with mui.Grid(size={"xs": 12, "sm": 6}):
                with mui.TextField(
                    select=True,
                    label="Language",
                    value=react.Bind("language", language="English"),
                    on_change=react.Callback("language = $event.target.value"),
                    full_width=True,
                    size="small",
                    literal_children=True,
                ):
                    for lang in ["English", "Français", "Español", "Deutsch", "日本語"]:
                        mui.MenuItem(lang, value=lang)
            with mui.Grid(size={"xs": 12, "sm": 6}):
                mui.Typography("Rate your experience", variant="body2")
                mui.Rating(default_value=4)

    def _notifications_tab(self):
        channels = [
            ("email", "Email notifications", "Order updates and weekly summaries"),
            ("push", "Push notifications", "Real-time alerts on this device"),
            ("sms", "SMS notifications", "Critical alerts only"),
        ]
        with mui.Stack(spacing=1.5, style={"marginTop": "8px"}):
            for i, (name, label, detail) in enumerate(channels):
                if i > 0:
                    mui.Divider()
                with mui.Stack(
                    direction="row",
                    style={"justifyContent": "space-between", "alignItems": "center"},
                ):
                    with mui.Box():
                        mui.Typography(label, variant="body2")
                        mui.Typography(detail, variant="caption", color="text.secondary")
                    mui.Switch(
                        checked=react.Bind(f"channel_{name}"),
                        on_change=react.Callback(f"channel_{name} = $event.target.checked"),
                    )

        with mui.Box(style={"marginTop": "24px"}):
            mui.Typography(
                react.Bind("'Digest frequency: every ' + freq + ' minutes'"),
                variant="body2",
                gutter_bottom=True,
            )
            mui.Slider(
                value=react.Bind("freq", freq=30),
                on_change=react.Callback("freq = Number($event.target.value)"),
                min=5,
                max=60,
                step=5,
                marks=True,
                value_label_display="auto",
                style={"maxWidth": "360px"},
            )

    def _appearance_tab(self):
        with mui.Box(style={"marginTop": "8px"}):
            mui.Typography("Theme", variant="body2", gutter_bottom=True)
            with mui.ToggleButtonGroup(exclusive=True, size="small"):
                for value, label in [("light", "☀️ Light"), ("dark", "🌙 Dark"), ("system", "🖥️ System")]:
                    mui.ToggleButton(
                        label,
                        value=value,
                        selected=react.Bind(f"appearance === '{value}'", appearance="system"),
                        on_click=react.Callback(f"appearance = '{value}'"),
                    )

        with mui.Box(style={"marginTop": "24px"}):
            mui.Typography("Layout density", variant="body2", gutter_bottom=True)
            with mui.RadioGroup(
                row=True,
                value=react.Bind("density", density="comfortable"),
                on_change=react.Callback("density = $event.target.value"),
            ):
                for value, label in [("comfortable", "Comfortable"), ("compact", "Compact")]:
                    with mui.Stack(
                        direction="row",
                        style={"alignItems": "center", "marginRight": "16px"},
                    ):
                        mui.Radio(value=value)
                        mui.Typography(label, variant="body2")


def main():
    app = Dashboard()
    app.server.start()


if __name__ == "__main__":
    main()
