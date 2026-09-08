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


# Generated from @mui/material 9.4.0

__all__ = [
    "Accordion",
    "AccordionActions",
    "AccordionDetails",
    "AccordionSummary",
    "Alert",
    "AlertTitle",
    "AppBar",
    "Autocomplete",
    "Avatar",
    "AvatarGroup",
    "Backdrop",
    "Badge",
    "BottomNavigation",
    "BottomNavigationAction",
    "Box",
    "Breadcrumbs",
    "Button",
    "ButtonBase",
    "ButtonGroup",
    "Card",
    "CardActionArea",
    "CardActions",
    "CardContent",
    "CardHeader",
    "CardMedia",
    "Checkbox",
    "Chip",
    "CircularProgress",
    "ClickAwayListener",
    "Collapse",
    "Container",
    "CssBaseline",
    "Dialog",
    "DialogActions",
    "DialogContent",
    "DialogContentText",
    "DialogTitle",
    "Divider",
    "Drawer",
    "Fab",
    "Fade",
    "FilledInput",
    "FormControl",
    "FormControlLabel",
    "FormGroup",
    "FormHelperText",
    "FormLabel",
    "GlobalStyles",
    "Grid",
    "Grow",
    "Icon",
    "IconButton",
    "ImageList",
    "ImageListItem",
    "ImageListItemBar",
    "InitColorSchemeScript",
    "Input",
    "InputAdornment",
    "InputBase",
    "InputLabel",
    "LinearProgress",
    "Link",
    "List",
    "ListItem",
    "ListItemAvatar",
    "ListItemButton",
    "ListItemIcon",
    "ListItemSecondaryAction",
    "ListItemText",
    "ListSubheader",
    "Menu",
    "MenuItem",
    "MenuList",
    "MobileStepper",
    "Modal",
    "NativeSelect",
    "NoSsr",
    "OutlinedInput",
    "Pagination",
    "PaginationItem",
    "Paper",
    "PigmentContainer",
    "PigmentGrid",
    "PigmentStack",
    "Popover",
    "Popper",
    "Portal",
    "Radio",
    "RadioGroup",
    "Rating",
    "ScopedCssBaseline",
    "Select",
    "Skeleton",
    "Slide",
    "Slider",
    "Snackbar",
    "SnackbarContent",
    "SpeedDial",
    "SpeedDialAction",
    "SpeedDialIcon",
    "Stack",
    "Step",
    "StepButton",
    "StepConnector",
    "StepContent",
    "StepIcon",
    "StepLabel",
    "Stepper",
    "SvgIcon",
    "SwipeableDrawer",
    "Switch",
    "Tab",
    "TabScrollButton",
    "Table",
    "TableBody",
    "TableCell",
    "TableContainer",
    "TableFooter",
    "TableHead",
    "TablePagination",
    "TablePaginationActions",
    "TableRow",
    "TableSortLabel",
    "Tabs",
    "TextField",
    "TextareaAutosize",
    "ThemeProvider",
    "ToggleButton",
    "ToggleButtonGroup",
    "Toolbar",
    "Tooltip",
    "Typography",
    "Zoom",
]


class Accordion(MuiHtmlElement):
    """MUI Accordion - https://mui.com/material-ui/api/accordion/

    :param default_expanded: If true, expands the accordion by default. (default: false) (``bool``)
    :param disable_gutters: If true, it removes the margin between two expanded accordion items and prevents the increased height when expanded. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param expanded: If true, expands the accordion, otherwise collapses it. Setting this prop enables control over the accordion. (``bool``)
    :param on_change: Callback fired when the expand/collapse state is changed. (``func``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ heading?: func | object, region?: func | object, root?: func | object, ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ heading?: elementType, region?: elementType, root?: elementType, transition?: ...``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-accordion", children, **kwargs)
        self.props += [
            ("default_expanded", "defaultExpanded"),
            ("disable_gutters", "disableGutters"),
            "disabled",
            "expanded",
            ("on_change", "onChange"),
            ("slot_props", "slotProps"),
            "slots",
        ]


class AccordionActions(MuiHtmlElement):
    """MUI AccordionActions - https://mui.com/material-ui/api/accordion-actions/

    :param disable_spacing: If true, the actions do not have additional margin. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-accordion-actions", children, **kwargs)
        self.props += [
            ("disable_spacing", "disableSpacing"),
        ]


class AccordionDetails(MuiHtmlElement):
    """MUI AccordionDetails - https://mui.com/material-ui/api/accordion-details/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-accordion-details", children, **kwargs)


class AccordionSummary(MuiHtmlElement):
    """MUI AccordionSummary - https://mui.com/material-ui/api/accordion-summary/

    :param expand_icon: The icon to display as the expand indicator. (``node``)
    :param focus_visible_class_name: This prop can help identify which element has keyboard focus. The class name will be applied when the element gains the focus through keyboard interaction. It's a polyfill for the CSS :focus-visible selector. The rationale for using this feature is explained here. A polyfill can be used to apply a focus-visible class to other components if needed. (``string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ content?: func | object, expandIconWrapper?: func | object, root?: func | ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ content?: elementType, expandIconWrapper?: elementType, root?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-accordion-summary", children, **kwargs)
        self.props += [
            ("expand_icon", "expandIcon"),
            ("focus_visible_class_name", "focusVisibleClassName"),
            ("slot_props", "slotProps"),
            "slots",
        ]


class Alert(MuiHtmlElement):
    """MUI Alert - https://mui.com/material-ui/api/alert/

    :param action: The action to display. It renders after the message, at the end of the alert. (``node``)
    :param close_text: Override the default label for the close popup icon button. For localization purposes, you can use the provided translations. (default: 'Close') (``string``)
    :param color: The color of the component. Unless provided, the value is taken from the severity prop. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (``'error' | 'info' | 'success' | 'warning' | string``)
    :param icon: Override the icon displayed before the children. Unless provided, the icon is mapped to the value of the severity prop. Set to false to remove the icon. (``node``)
    :param icon_mapping: The component maps the severity prop to a range of different icons, for instance success to <SuccessOutlined>. If you wish to change this mapping, you can provide your own. Alternatively, you can use the icon prop to override the icon displayed. (``{ error?: node, info?: node, success?: node, warning?: node }``)
    :param on_close: Callback fired when the component requests to be closed. When provided and no action prop is set, a close icon button is displayed that triggers the callback when clicked. (``func``)
    :param role: The ARIA role attribute of the element. (default: 'alert') (``string``)
    :param severity: The severity of the alert. This defines the color and icon used. (default: 'success') (``'error' | 'info' | 'success' | 'warning' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ action?: func | object, closeButton?: func | object, closeIcon?: func | ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ action?: elementType, closeButton?: elementType, closeIcon?: elementType, ...``)
    :param variant: The variant to use. (default: 'standard') (``'filled' | 'outlined' | 'standard' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-alert", children, **kwargs)
        self.props += [
            "action",
            ("close_text", "closeText"),
            "color",
            "icon",
            ("icon_mapping", "iconMapping"),
            ("on_close", "onClose"),
            "role",
            "severity",
            ("slot_props", "slotProps"),
            "slots",
            "variant",
        ]


class AlertTitle(MuiHtmlElement):
    """MUI AlertTitle - https://mui.com/material-ui/api/alert-title/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-alert-title", children, **kwargs)


class AppBar(MuiHtmlElement):
    """MUI AppBar - https://mui.com/material-ui/api/app-bar/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'default' | 'inherit' | 'primary' | 'secondary' | 'transparent' | 'error' | ...``)
    :param elevation: Shadow depth, corresponds to dp in the spec. It accepts values between 0 and 24 inclusive. (default: 4) (``number``)
    :param enable_color_on_dark: If true, the color prop is applied in dark mode. (default: false) (``bool``)
    :param position: The positioning type. The behavior of the different options is described in the MDN web docs. Note: sticky is not universally supported and will fall back to static when unavailable. (default: 'fixed') (``'absolute' | 'fixed' | 'relative' | 'static' | 'sticky'``)
    :param square: If false, rounded corners are enabled. (default: true) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-app-bar", children, **kwargs)
        self.props += [
            "color",
            "elevation",
            ("enable_color_on_dark", "enableColorOnDark"),
            "position",
            "square",
        ]


class Autocomplete(MuiHtmlElement):
    """MUI Autocomplete - https://mui.com/material-ui/api/autocomplete/

    :param auto_complete: If true, the portion of the selected suggestion that the user hasn't typed, known as the completion string, appears inline after the input cursor in the textbox. The inline completion string is visually highlighted and has a selected state. (default: false) (``bool``)
    :param auto_highlight: If true, the first option is automatically highlighted. (default: false) (``bool``)
    :param auto_select: If true, the value is updated when the input loses focus under one of these conditions: - An option highlighted via keyboard navigation or autoHighlight is selected. Hover and touch highlights are ignored. - Otherwise, in freeSolo mode, the typed text becomes the value. (default: false) (``bool``)
    :param blur_on_select: Control if the input should be blurred when an option is selected: false the input is not blurred. true the input is always blurred. touch the input is blurred after a touch event. mouse the input is blurred after a mouse event. (default: false) (``'mouse' | 'touch' | bool``)
    :param clear_icon: The icon to display in place of the default clear icon. (default: <ClearIcon fontSize="small" />) (``node``)
    :param clear_on_blur: If true, the input's text is cleared on blur if no value is selected. Set it to true if you want to help the user enter a new value. Set it to false if you want to help the user resume their search. (default: !props.freeSolo) (``bool``)
    :param clear_on_escape: If true, clear all values when the user presses escape and the popup is closed. (default: false) (``bool``)
    :param clear_text: Override the default text for the clear icon button. For localization purposes, you can use the provided translations. (default: 'Clear') (``string``)
    :param close_text: Override the default text for the close popup icon button. For localization purposes, you can use the provided translations. (default: 'Close') (``string``)
    :param default_value: The default value. Use when the component is not controlled. (default: props.multiple ? [] : null) (``any``)
    :param disable_clearable: If true, the input can't be cleared. (default: false) (``bool``)
    :param disable_close_on_select: If true, the popup won't close when a value is selected. (default: false) (``bool``)
    :param disable_list_wrap: If true, the list box in the popup will not wrap focus. (default: false) (``bool``)
    :param disable_portal: If true, the Popper content will be under the DOM hierarchy of the parent component. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param disabled_items_focusable: If true, will allow focus on disabled items. (default: false) (``bool``)
    :param filter_options: A function that determines the filtered options to be rendered on search. (default: createFilterOptions()) (``func``)
    :param filter_selected_options: If true, hide the selected options from the list box. (default: false) (``bool``)
    :param force_popup_icon: Force the visibility display of the popup icon. (default: 'auto') (``'auto' | bool``)
    :param free_solo: If true, the Autocomplete is free solo, meaning that the user input is not bound to provided options. (default: false) (``bool``)
    :param full_width: If true, the input takes up the full width of its container. Autocomplete treats undefined and false differently. If undefined, the inner input takes up the full width of its container. If false, the inner input is restricted to its intrinsic width. (default: false) (``bool``)
    :param get_limit_tags_text: The label to display when the tags are truncated (limitTags). (default: (more) => `+${more}`) (``func``)
    :param get_option_disabled: Used to determine the disabled state for a given option. (``func``)
    :param get_option_key: Used to determine the key for a given option. This can be useful when the labels of options are not unique (since labels are used as keys by default). (``func``)
    :param get_option_label: Used to determine the string value for a given option. It's used to fill the input (and the list box options if renderOption is not provided). If used in free solo mode, it must accept both the type of the options and a string. (default: (option) => option.label ?? option) (``func``)
    :param group_by: If provided, the options will be grouped under the returned string. The groupBy value is also used as the text for group headings when renderGroup is not provided. (``func``)
    :param handle_home_end_keys: If true, the component handles the "Home" and "End" keys when the popup is open. It should move focus to the first option and last option, respectively. (default: !props.freeSolo) (``bool``)
    :param id: This prop is used to help implement the accessibility logic. If you don't provide an id it will fall back to a randomly generated one. (``string``)
    :param include_input_in_list: If true, the highlight can move to the input. (default: false) (``bool``)
    :param input_value: The input value. (``string``)
    :param is_option_equal_to_value: Used to determine if the option represents the given value. Uses strict equality by default. ⚠️ Both arguments need to be handled, an option can only match with one value. (``func``)
    :param limit_tags: The maximum number of tags that will be visible when not focused. Set -1 to disable the limit. (default: -1) (``integer``)
    :param loading: If true, the component is in a loading state. This shows the loadingText in place of suggestions (only if there are no suggestions to show, for example options are empty). (default: false) (``bool``)
    :param loading_text: Text to display when in a loading state. For localization purposes, you can use the provided translations. (default: 'Loading…') (``node``)
    :param multiple: If true, value must be an array and the menu will support multiple selections. (default: false) (``bool``)
    :param no_options_text: Text to display when there are no options. For localization purposes, you can use the provided translations. (default: 'No options') (``node``)
    :param on_change: Callback fired when the value changes. (``func``)
    :param on_close: Callback fired when the popup requests to be closed. Use in controlled mode (see open). (``func``)
    :param on_highlight_change: Callback fired when the highlight option changes. (``func``)
    :param on_input_change: Callback fired when the input value changes. (``func``)
    :param on_open: Callback fired when the popup requests to be opened. Use in controlled mode (see open). (``func``)
    :param open: If true, the component is shown. (``bool``)
    :param open_on_focus: If true, the popup will open on input focus. (default: false) (``bool``)
    :param open_text: Override the default text for the open popup icon button. For localization purposes, you can use the provided translations. (default: 'Open') (``string``)
    :param options: A list of options that will be shown in the Autocomplete. (``array``)
    :param popup_icon: The icon to display in place of the default popup icon. (default: <ArrowDropDownIcon />) (``node``)
    :param read_only: If true, the component becomes readonly. It is also supported for multiple tags where the tag cannot be deleted. (default: false) (``bool``)
    :param render_group: Render the group. (``func``)
    :param render_input: Render the input. Note: The renderInput prop must return a TextField component or a compatible custom component that correctly forwards InputProps.ref and spreads inputProps. This ensures proper integration with the Autocomplete's internal logic (e.g., focus management and keyboard navigation). Avoid using components like DatePicker or Select directly, as they may not forward the required props, leading to runtime errors or unexpected behavior. (``func``)
    :param render_option: Render the option, use getOptionLabel by default. (``func``)
    :param render_value: Renders the selected value(s) as rich content in the input for both single and multiple selections. (``func``)
    :param reset_highlight_on_mouse_leave: If true, clears an option highlighted by mouse movement when the mouse leaves the listbox. This behavior will be enabled by default in the next major version. (default: false) (``bool``)
    :param select_on_focus: If true, the input's text is selected on focus. It helps the user clear the selected value. (default: !props.freeSolo) (``bool``)
    :param size: The size of the component. (default: 'medium') (``'small' | 'medium' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ chip?: func | object, clearIndicator?: func | object, listbox?: func | ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ clearIndicator?: elementType, listbox?: elementType, paper?: elementType, ...``)
    :param value: The value of the autocomplete. The value must have reference equality with the option in order to be selected. You can customize the equality behavior with the isOptionEqualToValue prop. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-autocomplete", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_highlight", "autoHighlight"),
            ("auto_select", "autoSelect"),
            ("blur_on_select", "blurOnSelect"),
            ("clear_icon", "clearIcon"),
            ("clear_on_blur", "clearOnBlur"),
            ("clear_on_escape", "clearOnEscape"),
            ("clear_text", "clearText"),
            ("close_text", "closeText"),
            ("default_value", "defaultValue"),
            ("disable_clearable", "disableClearable"),
            ("disable_close_on_select", "disableCloseOnSelect"),
            ("disable_list_wrap", "disableListWrap"),
            ("disable_portal", "disablePortal"),
            "disabled",
            ("disabled_items_focusable", "disabledItemsFocusable"),
            ("filter_options", "filterOptions"),
            ("filter_selected_options", "filterSelectedOptions"),
            ("force_popup_icon", "forcePopupIcon"),
            ("free_solo", "freeSolo"),
            ("full_width", "fullWidth"),
            ("get_limit_tags_text", "getLimitTagsText"),
            ("get_option_disabled", "getOptionDisabled"),
            ("get_option_key", "getOptionKey"),
            ("get_option_label", "getOptionLabel"),
            ("group_by", "groupBy"),
            ("handle_home_end_keys", "handleHomeEndKeys"),
            "id",
            ("include_input_in_list", "includeInputInList"),
            ("input_value", "inputValue"),
            ("is_option_equal_to_value", "isOptionEqualToValue"),
            ("limit_tags", "limitTags"),
            "loading",
            ("loading_text", "loadingText"),
            "multiple",
            ("no_options_text", "noOptionsText"),
            ("on_change", "onChange"),
            ("on_close", "onClose"),
            ("on_highlight_change", "onHighlightChange"),
            ("on_input_change", "onInputChange"),
            ("on_open", "onOpen"),
            "open",
            ("open_on_focus", "openOnFocus"),
            ("open_text", "openText"),
            "options",
            ("popup_icon", "popupIcon"),
            ("read_only", "readOnly"),
            ("render_group", "renderGroup"),
            ("render_input", "renderInput"),
            ("render_option", "renderOption"),
            ("render_value", "renderValue"),
            ("reset_highlight_on_mouse_leave", "resetHighlightOnMouseLeave"),
            ("select_on_focus", "selectOnFocus"),
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class Avatar(MuiHtmlElement):
    """MUI Avatar - https://mui.com/material-ui/api/avatar/

    :param alt: Used in combination with src or srcSet to provide an alt attribute for the rendered img element. (``string``)
    :param sizes: The sizes attribute for the img element. (``string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ fallback?: func | object, img?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ fallback?: elementType, img?: elementType, root?: elementType }``)
    :param src: The src attribute for the img element. (``string``)
    :param src_set: The srcSet attribute for the img element. Use this attribute for responsive image display. (``string``)
    :param variant: The shape of the avatar. (default: 'circular') (``'circular' | 'rounded' | 'square' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-avatar", children, **kwargs)
        self.props += [
            "alt",
            "sizes",
            ("slot_props", "slotProps"),
            "slots",
            "src",
            ("src_set", "srcSet"),
            "variant",
        ]


class AvatarGroup(MuiHtmlElement):
    """MUI AvatarGroup - https://mui.com/material-ui/api/avatar-group/

    :param max: Max avatars to show before +x. (default: 5) (``number``)
    :param render_surplus: custom renderer of extraAvatars (``func``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ surplus?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ surplus?: elementType }``)
    :param spacing: Spacing between avatars. (default: 'medium') (``'medium' | 'small' | number``)
    :param total: The total number of avatars. Used for calculating the number of extra avatars. (default: children.length) (``number``)
    :param variant: The variant to use. (default: 'circular') (``'circular' | 'rounded' | 'square' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-avatar-group", children, **kwargs)
        self.props += [
            "max",
            ("render_surplus", "renderSurplus"),
            ("slot_props", "slotProps"),
            "slots",
            "spacing",
            "total",
            "variant",
        ]
        self.literal_children = True


class Backdrop(MuiHtmlElement):
    """MUI Backdrop - https://mui.com/material-ui/api/backdrop/

    :param invisible: If true, the backdrop is invisible. It can be used when rendering a popover or a custom select component. (default: false) (``bool``)
    :param open: If true, the component is shown. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ root?: func | object, transition?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ root?: elementType, transition?: elementType }``)
    :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-backdrop", children, **kwargs)
        self.props += [
            "invisible",
            "open",
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
        ]


class Badge(MuiHtmlElement):
    """MUI Badge - https://mui.com/material-ui/api/badge/

        :param anchor_origin: The anchor of the badge. (default: {
      vertical: 'top',
      horizontal: 'right',
    }) (``{ horizontal?: 'left' | 'right', vertical?: 'bottom' | 'top' }``)
        :param badge_content: The content rendered within the badge. (``node``)
        :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'default') (``'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
        :param invisible: If true, the badge is invisible. (default: false) (``bool``)
        :param max: Max count to show. (default: 99) (``number``)
        :param overlap: Wrapped shape the badge should overlap. (default: 'rectangular') (``'circular' | 'rectangular'``)
        :param show_zero: Controls whether the badge is hidden when badgeContent is zero. (default: false) (``bool``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ badge?: func | object, root?: func | object }``)
        :param slots: The components used for each slot inside. (default: {}) (``{ badge?: elementType, root?: elementType }``)
        :param variant: The variant to use. (default: 'standard') (``'dot' | 'standard' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-badge", children, **kwargs)
        self.props += [
            ("anchor_origin", "anchorOrigin"),
            ("badge_content", "badgeContent"),
            "color",
            "invisible",
            "max",
            "overlap",
            ("show_zero", "showZero"),
            ("slot_props", "slotProps"),
            "slots",
            "variant",
        ]


class BottomNavigation(MuiHtmlElement):
    """MUI BottomNavigation - https://mui.com/material-ui/api/bottom-navigation/

    :param on_change: Callback fired when the value changes. (``func``)
    :param show_labels: If true, all BottomNavigationActions will show their labels. By default, only the selected BottomNavigationAction will show its label. (default: false) (``bool``)
    :param value: The value of the currently selected BottomNavigationAction. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-bottom-navigation", children, **kwargs)
        self.props += [
            ("on_change", "onChange"),
            ("show_labels", "showLabels"),
            "value",
        ]
        self.literal_children = True


class BottomNavigationAction(MuiHtmlElement):
    """MUI BottomNavigationAction - https://mui.com/material-ui/api/bottom-navigation-action/

    :param icon: The icon to display. (``node``)
    :param label: The label element. (``node``)
    :param show_label: If true, the BottomNavigationAction will show its label. By default, only the selected BottomNavigationAction inside BottomNavigation will show its label. The prop defaults to the value (false) inherited from the parent BottomNavigation component. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ label?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ label?: elementType, root?: elementType }``)
    :param value: You can provide your own value. Otherwise, we fallback to the child position index. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-bottom-navigation-action", children, **kwargs)
        self.props += [
            "icon",
            "label",
            ("show_label", "showLabel"),
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class Box(MuiHtmlElement):
    """MUI Box - https://mui.com/material-ui/api/box/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-box", children, **kwargs)


class Breadcrumbs(MuiHtmlElement):
    """MUI Breadcrumbs - https://mui.com/material-ui/api/breadcrumbs/

    :param expand_text: Override the default label for the expand button. For localization purposes, you can use the provided translations. (default: 'Show path') (``string``)
    :param items_after_collapse: If max items is exceeded, the number of items to show after the ellipsis. (default: 1) (``integer``)
    :param items_before_collapse: If max items is exceeded, the number of items to show before the ellipsis. (default: 1) (``integer``)
    :param max_items: Specifies the maximum number of breadcrumbs to display. When there are more than the maximum number, only the first itemsBeforeCollapse and last itemsAfterCollapse will be shown, with an ellipsis in between. (default: 8) (``integer``)
    :param separator: Custom separator node. (default: '/') (``node``)
    :param slot_props: The props used for each slot inside the Breadcumb. (default: {}) (``{ collapsedIcon?: func | object }``)
    :param slots: The components used for each slot inside the Breadcumb. Either a string to use a HTML element or a component. (default: {}) (``{ CollapsedIcon?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-breadcrumbs", children, **kwargs)
        self.props += [
            ("expand_text", "expandText"),
            ("items_after_collapse", "itemsAfterCollapse"),
            ("items_before_collapse", "itemsBeforeCollapse"),
            ("max_items", "maxItems"),
            "separator",
            ("slot_props", "slotProps"),
            "slots",
        ]


class Button(MuiHtmlElement):
    """MUI Button - https://mui.com/material-ui/api/button/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'inherit' | 'primary' | 'secondary' | 'success' | 'error' | 'info' | 'warning' ...``)
    :param disable_elevation: If true, no elevation is used. (default: false) (``bool``)
    :param disable_focus_ripple: If true, the keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. ⚠️ Without a ripple there is no styling for :focus-visible by default. Be sure to highlight the element by applying separate styles with the .Mui-focusVisible class. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param end_icon: Element placed after the children. (``node``)
    :param full_width: If true, the button will take up the full width of its container. (default: false) (``bool``)
    :param href: The URL to link to when the button is clicked. If defined, an a element will be used as the root node. (``string``)
    :param loading: If true, the loading indicator is visible and the button is disabled. If true | false, the loading wrapper is always rendered before the children to prevent Google Translation Crash. (default: null) (``bool``)
    :param loading_indicator: Element placed before the children if the button is in loading state. The node should contain an element with role="progressbar" with an accessible name. By default, it renders a CircularProgress that is labeled by the button itself. (default: <CircularProgress color="inherit" size={16} />) (``node``)
    :param loading_position: The loading indicator can be positioned on the start, end, or the center of the button. (default: 'center') (``'center' | 'end' | 'start'``)
    :param size: The size of the component. small is equivalent to the dense button styling. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param start_icon: Element placed before the children. (``node``)
    :param variant: The variant to use. (default: 'text') (``'contained' | 'outlined' | 'text' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-button", children, **kwargs)
        self.props += [
            "color",
            ("disable_elevation", "disableElevation"),
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            ("end_icon", "endIcon"),
            ("full_width", "fullWidth"),
            "href",
            "loading",
            ("loading_indicator", "loadingIndicator"),
            ("loading_position", "loadingPosition"),
            "size",
            ("start_icon", "startIcon"),
            "variant",
        ]


class ButtonBase(MuiHtmlElement):
    """MUI ButtonBase - https://mui.com/material-ui/api/button-base/

    `ButtonBase` contains as few styles as possible. It aims to be a simple building block for creating a button. It contains a load of style reset and some focus/ripple logic.

    :param link_component: The component used to render a link when the href prop is provided. (default: 'a') (``elementType``)
    :param touch_ripple_props: Props applied to the TouchRipple element. (``object``)
    :param action: A ref for imperative actions. It currently only supports focusVisible() action. (``ref``)
    :param center_ripple: If true, the ripples are centered. They won't start at the cursor interaction position. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. ⚠️ Without a ripple there is no styling for :focus-visible by default. Be sure to highlight the element by applying separate styles with the .Mui-focusVisible class. (default: false) (``bool``)
    :param disable_touch_ripple: If true, the touch ripple effect is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param focus_ripple: If true, the base button will have a keyboard focus ripple. (default: false) (``bool``)
    :param focus_visible_class_name: This prop can help identify which element has keyboard focus. The class name will be applied when the element gains the focus through keyboard interaction. It's a polyfill for the CSS :focus-visible selector. The rationale for using this feature is explained here. A polyfill can be used to apply a focus-visible class to other components if needed. (``string``)
    :param native_button: Whether the custom component is expected to render a native <button> element when passing a React component to the component or slots prop. (``bool``)
    :param on_focus_visible: Callback fired when the component is focused with a keyboard. We trigger a onFocus callback too. (``func``)
    :param touch_ripple_ref: A ref that points to the TouchRipple element. (``func | { current?: { pulsate: func, start: func, stop: func } }``)
    :param type: The HTML type attribute applied to button and a elements. Ignored when rendering non-native buttons. (default: 'button') (``string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-button-base", children, **kwargs)
        self.props += [
            ("link_component", "LinkComponent"),
            ("touch_ripple_props", "TouchRippleProps"),
            "action",
            ("center_ripple", "centerRipple"),
            ("disable_ripple", "disableRipple"),
            ("disable_touch_ripple", "disableTouchRipple"),
            "disabled",
            ("focus_ripple", "focusRipple"),
            ("focus_visible_class_name", "focusVisibleClassName"),
            ("native_button", "nativeButton"),
            ("on_focus_visible", "onFocusVisible"),
            ("touch_ripple_ref", "touchRippleRef"),
            "type",
        ]


class ButtonGroup(MuiHtmlElement):
    """MUI ButtonGroup - https://mui.com/material-ui/api/button-group/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'inherit' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param disable_elevation: If true, no elevation is used. (default: false) (``bool``)
    :param disable_focus_ripple: If true, the button keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the button ripple effect is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param full_width: If true, the buttons will take up the full width of its container. (default: false) (``bool``)
    :param orientation: The component orientation (layout flow direction). (default: 'horizontal') (``'horizontal' | 'vertical'``)
    :param size: The size of the component. small is equivalent to the dense button styling. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param variant: The variant to use. (default: 'outlined') (``'contained' | 'outlined' | 'text' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-button-group", children, **kwargs)
        self.props += [
            "color",
            ("disable_elevation", "disableElevation"),
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            ("full_width", "fullWidth"),
            "orientation",
            "size",
            "variant",
        ]


class Card(MuiHtmlElement):
    """MUI Card - https://mui.com/material-ui/api/card/

    :param raised: If true, the card will use raised styling. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card", children, **kwargs)
        self.props += [
            "raised",
        ]


class CardActionArea(MuiHtmlElement):
    """MUI CardActionArea - https://mui.com/material-ui/api/card-action-area/

    :param slot_props: The props used for each slot inside. (default: {}) (``{ focusHighlight?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ focusHighlight?: elementType, root?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card-action-area", children, **kwargs)
        self.props += [
            ("slot_props", "slotProps"),
            "slots",
        ]


class CardActions(MuiHtmlElement):
    """MUI CardActions - https://mui.com/material-ui/api/card-actions/

    :param disable_spacing: If true, the actions do not have additional margin. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card-actions", children, **kwargs)
        self.props += [
            ("disable_spacing", "disableSpacing"),
        ]


class CardContent(MuiHtmlElement):
    """MUI CardContent - https://mui.com/material-ui/api/card-content/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card-content", children, **kwargs)


class CardHeader(MuiHtmlElement):
    """MUI CardHeader - https://mui.com/material-ui/api/card-header/

    :param action: The action to display in the card header. (``node``)
    :param avatar: The Avatar element to display. (``node``)
    :param disable_typography: If true, subheader and title won't be wrapped by a Typography component. This can be useful to render an alternative Typography variant by wrapping the title text, and optional subheader text with the Typography component. (default: false) (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ action?: func | object, avatar?: func | object, content?: func | object, ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ action?: elementType, avatar?: elementType, content?: elementType, root?: ...``)
    :param subheader: The content of the component. (``node``)
    :param title: The content of the component. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card-header", children, **kwargs)
        self.props += [
            "action",
            "avatar",
            ("disable_typography", "disableTypography"),
            ("slot_props", "slotProps"),
            "slots",
            "subheader",
            "title",
        ]


class CardMedia(MuiHtmlElement):
    """MUI CardMedia - https://mui.com/material-ui/api/card-media/

    :param image: Image to be displayed as a background image. Either image or src prop must be specified. Note that caller must specify height otherwise the image will not be visible. (``string``)
    :param src: An alias for image property. Available only with media components. Media components: video, audio, picture, iframe, img. (``string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-card-media", children, **kwargs)
        self.props += [
            "image",
            "src",
        ]


class Checkbox(MuiHtmlElement):
    """MUI Checkbox - https://mui.com/material-ui/api/checkbox/

    :param checked: If true, the component is checked. (``bool``)
    :param checked_icon: The icon to display when the component is checked. (default: <CheckBoxIcon />) (``node``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param default_checked: The default checked state. Use when the component is not controlled. (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param icon: The icon to display when the component is unchecked. (default: <CheckBoxOutlineBlankIcon />) (``node``)
    :param id: The id of the input element. (``string``)
    :param indeterminate: If true, the component appears indeterminate. This does not set the native input element to indeterminate due to inconsistent behavior across browsers. However, we set a data-indeterminate attribute on the input. (default: false) (``bool``)
    :param indeterminate_icon: The icon to display when the component is indeterminate. (default: <IndeterminateCheckBoxIcon />) (``node``)
    :param on_change: Callback fired when the state is changed. (``func``)
    :param required: If true, the input element is required. (default: false) (``bool``)
    :param size: The size of the component. small is equivalent to the dense checkbox styling. (default: 'medium') (``'medium' | 'small' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ input?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType }``)
    :param value: The value of the component. The DOM API casts this to a string. The browser uses "on" as the default value. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-checkbox", children, **kwargs)
        self.props += [
            "checked",
            ("checked_icon", "checkedIcon"),
            "color",
            ("default_checked", "defaultChecked"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            "icon",
            "id",
            "indeterminate",
            ("indeterminate_icon", "indeterminateIcon"),
            ("on_change", "onChange"),
            "required",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class Chip(MuiHtmlElement):
    """MUI Chip - https://mui.com/material-ui/api/chip/

    Chips represent complex entities in small blocks, such as a contact.

    :param avatar: The Avatar element to display. (``element``)
    :param clickable: If true, the chip will appear clickable, and will raise when pressed, even if the onClick prop is not defined. If false, the chip will not appear clickable, even if onClick prop is defined. This can be used, for example, along with the component prop to indicate an anchor Chip is clickable. Note: this controls the UI and does not affect the onClick event. (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'default') (``'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param delete_icon: Override the default delete icon element. Shown only if onDelete is set. (``element``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param icon: Icon element. (``element``)
    :param label: The content of the component. (``node``)
    :param native_button: If true, the component is expected to resolve to a native <button> element. When omitted, custom components inherit the default button semantics of the current wrapper. Set to true when a custom component resolves to a native <button>, or false when it resolves to a non-button host. (``bool``)
    :param on_delete: Callback fired when the delete icon is clicked. If set, the delete icon will be shown. (``func``)
    :param size: The size of the component. (default: 'medium') (``'medium' | 'small' | string``)
    :param skip_focus_when_disabled: If true, allows the disabled chip to escape focus. If false, allows the disabled chip to receive focus. (default: false) (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ label?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ label?: elementType, root?: elementType }``)
    :param variant: The variant to use. (default: 'filled') (``'filled' | 'outlined' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-chip", children, **kwargs)
        self.props += [
            "avatar",
            "clickable",
            "color",
            ("delete_icon", "deleteIcon"),
            "disabled",
            "icon",
            "label",
            ("native_button", "nativeButton"),
            ("on_delete", "onDelete"),
            "size",
            ("skip_focus_when_disabled", "skipFocusWhenDisabled"),
            ("slot_props", "slotProps"),
            "slots",
            "variant",
        ]


class CircularProgress(MuiHtmlElement):
    """MUI CircularProgress - https://mui.com/material-ui/api/circular-progress/

    ## ARIA If the progress bar is describing the loading progress of a particular region of a page, you should use `aria-describedby` to point to the progress bar, and set the `aria-busy` attribute to `true` on that region until it has finished loading.

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'inherit' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param disable_shrink: If true, the shrink animation is disabled. This only works if variant is indeterminate. (default: false) (``bool``)
    :param enable_track_slot: If true, a track circle slot is mounted to show a subtle background for the progress. The size and thickness apply to the track slot to be consistent with the progress circle. (default: false) (``bool``)
    :param max: The maximum value for the progress indicator for the determinate variant. (default: 100) (``number``)
    :param min: The minimum value for the progress indicator for the determinate variant. (default: 0) (``number``)
    :param size: The size of the component. If using a number, the pixel unit is assumed. If using a string, you need to provide the CSS unit, for example '3rem'. (default: 40) (``number | string``)
    :param thickness: The thickness of the circle. (default: 3.6) (``number``)
    :param value: The value of the progress indicator for the determinate variant. Value between min and max. (default: props.min ?? 0) (``number``)
    :param variant: The variant to use. Use indeterminate when there is no progress value. (default: 'indeterminate') (``'determinate' | 'indeterminate'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-circular-progress", children, **kwargs)
        self.props += [
            "color",
            ("disable_shrink", "disableShrink"),
            ("enable_track_slot", "enableTrackSlot"),
            "max",
            "min",
            "size",
            "thickness",
            "value",
            "variant",
        ]


class ClickAwayListener(MuiHtmlElement):
    """MUI ClickAwayListener - https://mui.com/material-ui/api/click-away-listener/

    Listen for click events that occur somewhere in the document, outside of the element itself. For instance, if you need to hide a menu when people click anywhere else on your page.

    :param disable_react_tree: If true, the React tree is ignored and only the DOM tree is considered. This prop changes how portaled elements are handled. (default: false) (``bool``)
    :param mouse_event: The mouse event to listen to. You can disable the listener by providing false. (default: 'onClick') (``'onClick' | 'onMouseDown' | 'onMouseUp' | 'onPointerDown' | 'onPointerUp' | ...``)
    :param on_click_away: Callback fired when a "click away" event is detected. (``func``)
    :param touch_event: The touch event to listen to. You can disable the listener by providing false. (default: 'onTouchEnd') (``'onTouchEnd' | 'onTouchStart' | false``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-click-away-listener", children, **kwargs)
        self.props += [
            ("disable_react_tree", "disableReactTree"),
            ("mouse_event", "mouseEvent"),
            ("on_click_away", "onClickAway"),
            ("touch_event", "touchEvent"),
        ]


class Collapse(MuiHtmlElement):
    """MUI Collapse - https://mui.com/material-ui/api/collapse/

    The Collapse transition is used by the [Vertical Stepper](/material-ui/react-stepper/#vertical-stepper) StepContent component.

    :param add_end_listener: Add a custom transition end trigger. Use it when you need custom logic to decide when the transition has ended. Note: Timeouts are still used as a fallback if provided. (``func``)
    :param collapsed_size: The width (horizontal) or height (vertical) of the container when collapsed. (default: '0px') (``number | string``)
    :param disable_prefers_reduced_motion: If true, the transition ignores theme.motion.reducedMotion and keeps its normal timing. (default: false) (``bool``)
    :param easing: The transition timing function. You may specify a single easing or a object containing enter and exit values. (``{ enter?: string, exit?: string } | string``)
    :param in: If true, the component will transition in. (``bool``)
    :param orientation: The transition orientation. (default: 'vertical') (``'horizontal' | 'vertical'``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ root?: func | object, wrapper?: func | object, wrapperInner?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ root?: elementType, wrapper?: elementType, wrapperInner?: elementType }``)
    :param timeout: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. Set to 'auto' to automatically calculate transition time based on height. (default: duration.standard) (``'auto' | number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-collapse", children, **kwargs)
        self.props += [
            ("add_end_listener", "addEndListener"),
            ("collapsed_size", "collapsedSize"),
            ("disable_prefers_reduced_motion", "disablePrefersReducedMotion"),
            "easing",
            "in",
            "orientation",
            ("slot_props", "slotProps"),
            "slots",
            "timeout",
        ]


class Container(MuiHtmlElement):
    """MUI Container - https://mui.com/material-ui/api/container/

    :param disable_gutters: If true, the left and right padding is removed. (default: false) (``bool``)
    :param fixed: Set the max-width to match the min-width of the current breakpoint. This is useful if you'd prefer to design for a fixed set of sizes instead of trying to accommodate a fully fluid viewport. It's fluid by default. (default: false) (``bool``)
    :param max_width: Determine the max-width of the container. The container width grows with the size of the screen. Set to false to disable maxWidth. (default: 'lg') (``'xs' | 'sm' | 'md' | 'lg' | 'xl' | false | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-container", children, **kwargs)
        self.props += [
            ("disable_gutters", "disableGutters"),
            "fixed",
            ("max_width", "maxWidth"),
        ]


class CssBaseline(MuiHtmlElement):
    """MUI CssBaseline - https://mui.com/material-ui/api/css-baseline/

    Kickstart an elegant, consistent, and simple baseline to build upon.

    :param enable_color_scheme: Enable color-scheme CSS property to use theme.palette.mode. For more details, check out https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme For browser support, check out https://caniuse.com/?search=color-scheme (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-css-baseline", children, **kwargs)
        self.props += [
            ("enable_color_scheme", "enableColorScheme"),
        ]


class Dialog(MuiHtmlElement):
    """MUI Dialog - https://mui.com/material-ui/api/dialog/

        Dialogs are overlaid modal paper based components with a backdrop.

        :param paper_component: The component used to render the body of the dialog. (default: Paper) (``elementType``)
        :param full_screen: If true, the dialog is full-screen. (default: false) (``bool``)
        :param full_width: If true, the dialog stretches to maxWidth. Notice that the dialog width grow is limited by the default margin. (default: false) (``bool``)
        :param max_width: Determine the max-width of the dialog. The dialog width grows with the size of the screen. Set to false to disable maxWidth. (default: 'sm') (``'xs' | 'sm' | 'md' | 'lg' | 'xl' | false | string``)
        :param on_close: Callback fired when the component requests to be closed. (``func``)
        :param open: If true, the component is shown. (``bool``)
        :param role: The ARIA role for the dialog element. The main dialog role is dialog, but alertdialog can be used if the content of the dialog requires immediate attention. See https://www.w3.org/TR/wai-aria-1.2/#dialog and https://www.w3.org/TR/wai-aria-1.2/#alertdialog for more details. (default: 'dialog') (``'alertdialog' | 'dialog'``)
        :param scroll: Determine the container for scrolling the dialog. (default: 'paper') (``'body' | 'paper'``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ backdrop?: func | object, container?: func | object, paper?: func | object, ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ backdrop?: elementType, container?: elementType, paper?: elementType, root?: ...``)
        :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-dialog", children, **kwargs)
        self.props += [
            ("paper_component", "PaperComponent"),
            ("full_screen", "fullScreen"),
            ("full_width", "fullWidth"),
            ("max_width", "maxWidth"),
            ("on_close", "onClose"),
            "open",
            "role",
            "scroll",
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
        ]


class DialogActions(MuiHtmlElement):
    """MUI DialogActions - https://mui.com/material-ui/api/dialog-actions/

    :param disable_spacing: If true, the actions do not have additional margin. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-dialog-actions", children, **kwargs)
        self.props += [
            ("disable_spacing", "disableSpacing"),
        ]


class DialogContent(MuiHtmlElement):
    """MUI DialogContent - https://mui.com/material-ui/api/dialog-content/

    :param dividers: Display the top and bottom dividers. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-dialog-content", children, **kwargs)
        self.props += [
            "dividers",
        ]


class DialogContentText(MuiHtmlElement):
    """MUI DialogContentText - https://mui.com/material-ui/api/dialog-content-text/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-dialog-content-text", children, **kwargs)


class DialogTitle(MuiHtmlElement):
    """MUI DialogTitle - https://mui.com/material-ui/api/dialog-title/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-dialog-title", children, **kwargs)


class Divider(MuiHtmlElement):
    """MUI Divider - https://mui.com/material-ui/api/divider/

    :param absolute: Absolutely position the element. (default: false) (``bool``)
    :param flex_item: If true, a vertical divider will have the correct height when used in flex container. (By default, a vertical divider will have a calculated height of 0px if it is the child of a flex container.) (default: false) (``bool``)
    :param orientation: The component orientation. (default: 'horizontal') (``'horizontal' | 'vertical'``)
    :param text_align: The text alignment. (default: 'center') (``'center' | 'left' | 'right'``)
    :param variant: The variant to use. (default: 'fullWidth') (``'fullWidth' | 'inset' | 'middle' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-divider", children, **kwargs)
        self.props += [
            "absolute",
            ("flex_item", "flexItem"),
            "orientation",
            ("text_align", "textAlign"),
            "variant",
        ]


class Drawer(MuiHtmlElement):
    """MUI Drawer - https://mui.com/material-ui/api/drawer/

        The props of the [Modal](/material-ui/api/modal/) component are available when `variant="temporary"` is set.

        :param modal_props: Props applied to the Modal element. (default: {}) (``object``)
        :param anchor: Side from which the drawer will appear. (default: 'left') (``'bottom' | 'left' | 'right' | 'top'``)
        :param elevation: The elevation of the drawer. (default: 16) (``integer``)
        :param hide_backdrop: If true, the backdrop is not rendered. (default: false) (``bool``)
        :param on_close: Callback fired when the component requests to be closed. The reason parameter can optionally be used to control the response to onClose. (``func``)
        :param open: If true, the component is shown. (default: false) (``bool``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ backdrop?: func | object, docked?: func | object, paper?: func | object, ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ backdrop?: elementType, docked?: elementType, paper?: elementType, root?: ...``)
        :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
        :param variant: The variant to use. (default: 'temporary') (``'permanent' | 'persistent' | 'temporary'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-drawer", children, **kwargs)
        self.props += [
            ("modal_props", "ModalProps"),
            "anchor",
            "elevation",
            ("hide_backdrop", "hideBackdrop"),
            ("on_close", "onClose"),
            "open",
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
            "variant",
        ]


class Fab(MuiHtmlElement):
    """MUI Fab - https://mui.com/material-ui/api/fab/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'default') (``'default' | 'error' | 'info' | 'inherit' | 'primary' | 'secondary' | 'success' ...``)
    :param disable_focus_ripple: If true, the keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param href: The URL to link to when the button is clicked. If defined, an a element will be used as the root node. (``string``)
    :param size: The size of the component. small is equivalent to the dense button styling. (default: 'large') (``'small' | 'medium' | 'large' | string``)
    :param variant: The variant to use. (default: 'circular') (``'circular' | 'extended' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-fab", children, **kwargs)
        self.props += [
            "color",
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            "href",
            "size",
            "variant",
        ]


class Fade(MuiHtmlElement):
    """MUI Fade - https://mui.com/material-ui/api/fade/

        The Fade transition is used by the [Modal](/material-ui/react-modal/) component.

        :param add_end_listener: Add a custom transition end trigger. Use it when you need custom logic to decide when the transition has ended. Note: Timeouts are still used as a fallback if provided. (``func``)
        :param appear: Perform the enter transition when it first mounts if in is also true. Set this to false to disable this behavior. (default: true) (``bool``)
        :param disable_prefers_reduced_motion: If true, the transition ignores theme.motion.reducedMotion and keeps its normal timing. (default: false) (``bool``)
        :param easing: The transition timing function. You may specify a single easing or a object containing enter and exit values. (``{ enter?: string, exit?: string } | string``)
        :param in: If true, the component will transition in. (``bool``)
        :param timeout: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-fade", children, **kwargs)
        self.props += [
            ("add_end_listener", "addEndListener"),
            "appear",
            ("disable_prefers_reduced_motion", "disablePrefersReducedMotion"),
            "easing",
            "in",
            "timeout",
        ]


class FilledInput(MuiHtmlElement):
    """MUI FilledInput - https://mui.com/material-ui/api/filled-input/

    :param auto_complete: This prop helps users to fill forms faster, especially on mobile devices. The name can be confusing, as it's more like an autofill. You can learn more about it following the specification. (``string``)
    :param auto_focus: If true, the input element is focused during the first mount. (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. The prop defaults to the value ('primary') inherited from the parent FormControl component. (``'primary' | 'secondary' | string``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param disable_underline: If true, the input will not have an underline. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param end_adornment: End InputAdornment for this component. (``node``)
    :param error: If true, the input will indicate an error. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param full_width: If true, the input will take up the full width of its container. (default: false) (``bool``)
    :param hidden_label: If true, the label is hidden. This is used to increase density for a FilledInput. Be sure to add aria-label to the input element. (default: false) (``bool``)
    :param id: The id of the input element. (``string``)
    :param input_component: The component used for the input element. Either a string to use a HTML element or a component. (default: 'input') (``elementType``)
    :param input_props: Attributes applied to the input element. (default: {}) (``object``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. The prop defaults to the value ('none') inherited from the parent FormControl component. (``'dense' | 'none'``)
    :param max_rows: Maximum number of rows to display when multiline option is set to true. (``number | string``)
    :param min_rows: Minimum number of rows to display when multiline option is set to true. (``number | string``)
    :param multiline: If true, a TextareaAutosize element is rendered. (default: false) (``bool``)
    :param name: Name attribute of the input element. (``string``)
    :param on_change: Callback fired when the value is changed. (``func``)
    :param placeholder: The short hint displayed in the input before the user enters a value. (``string``)
    :param read_only: It prevents the user from changing the value of the field (not from interacting with the field). (``bool``)
    :param required: If true, the input element is required. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param rows: Number of rows to display when multiline option is set to true. (``number | string``)
    :param slot_props: The extra props for the slot components. You can override the existing props or add new ones. (default: {}) (``{ input?: object, root?: object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType }``)
    :param start_adornment: Start InputAdornment for this component. (``node``)
    :param type: Type of the input element. It should be a valid HTML5 input type. (default: 'text') (``string``)
    :param value: The value of the input element, required for a controlled component. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-filled-input", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_focus", "autoFocus"),
            "color",
            ("default_value", "defaultValue"),
            ("disable_underline", "disableUnderline"),
            "disabled",
            ("end_adornment", "endAdornment"),
            "error",
            ("full_width", "fullWidth"),
            ("hidden_label", "hiddenLabel"),
            "id",
            ("input_component", "inputComponent"),
            ("input_props", "inputProps"),
            ("input_ref", "inputRef"),
            "margin",
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
            "multiline",
            "name",
            ("on_change", "onChange"),
            "placeholder",
            ("read_only", "readOnly"),
            "required",
            "rows",
            ("slot_props", "slotProps"),
            "slots",
            ("start_adornment", "startAdornment"),
            "type",
            "value",
        ]


class FormControl(MuiHtmlElement):
    """MUI FormControl - https://mui.com/material-ui/api/form-control/

    Provides context such as filled/focused/error/required for form inputs. Relying on the context provides high flexibility and ensures that the state always stays consistent across the children of the `FormControl`. This context is used by the following components: - FormLabel - FormHelperText - Input - InputLabel You can find one composition example below and more going to [the demos](/material-ui/react-text-field/#components). ```jsx Email address We'll never share your email. ``` ⚠️ Only one `InputBase` can be used within a FormControl because it creates visual inconsistencies. For instance, only one input can be focused at the same time, the state shouldn't be shared.

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' | string``)
    :param disabled: If true, the label, input and helper text should be displayed in a disabled state. (default: false) (``bool``)
    :param error: If true, the label is displayed in an error state. (default: false) (``bool``)
    :param focused: If true, the component is displayed in focused state. (``bool``)
    :param full_width: If true, the component will take up the full width of its container. (default: false) (``bool``)
    :param hidden_label: If true, the label is hidden. This is used to increase density for a FilledInput. Be sure to add aria-label to the input element. (default: false) (``bool``)
    :param margin: If dense or normal, will adjust vertical spacing of this and contained components. (default: 'none') (``'dense' | 'none' | 'normal'``)
    :param required: If true, the label will indicate that the input is required. (default: false) (``bool``)
    :param size: The size of the component. (default: 'medium') (``'medium' | 'small' | string``)
    :param variant: The variant to use. (default: 'outlined') (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-form-control", children, **kwargs)
        self.props += [
            "color",
            "disabled",
            "error",
            "focused",
            ("full_width", "fullWidth"),
            ("hidden_label", "hiddenLabel"),
            "margin",
            "required",
            "size",
            "variant",
        ]
        self.literal_children = True


class FormControlLabel(MuiHtmlElement):
    """MUI FormControlLabel - https://mui.com/material-ui/api/form-control-label/

    Drop-in replacement of the `Radio`, `Switch` and `Checkbox` component. Use this component if you want to display an extra label.

    :param checked: If true, the component appears selected. (``bool``)
    :param control: A control element. For instance, it can be a Radio, a Switch or a Checkbox. (``element``)
    :param disable_typography: If true, the label is rendered as it is passed without an additional typography node. (``bool``)
    :param disabled: If true, the control is disabled. (``bool``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param label: A text or an element to be used in an enclosing label element. (``node``)
    :param label_placement: The position of the label. (default: 'end') (``'bottom' | 'end' | 'start' | 'top'``)
    :param on_change: Callback fired when the state is changed. (``func``)
    :param required: If true, the label will indicate that the input is required. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ typography?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ typography?: elementType }``)
    :param value: The value of the component. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-form-control-label", children, **kwargs)
        self.props += [
            "checked",
            "control",
            ("disable_typography", "disableTypography"),
            "disabled",
            ("input_ref", "inputRef"),
            "label",
            ("label_placement", "labelPlacement"),
            ("on_change", "onChange"),
            "required",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class FormGroup(MuiHtmlElement):
    """MUI FormGroup - https://mui.com/material-ui/api/form-group/

    `FormGroup` wraps controls such as `Checkbox` and `Switch`. It provides compact row layout. For the `Radio`, you should be using the `RadioGroup` component instead of this one.

    :param row: Display group of elements in a compact row. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-form-group", children, **kwargs)
        self.props += [
            "row",
        ]


class FormHelperText(MuiHtmlElement):
    """MUI FormHelperText - https://mui.com/material-ui/api/form-helper-text/

    :param disabled: If true, the helper text should be displayed in a disabled state. (``bool``)
    :param error: If true, helper text should be displayed in an error state. (``bool``)
    :param filled: If true, the helper text should use filled classes key. (``bool``)
    :param focused: If true, the helper text should use focused classes key. (``bool``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. (``'dense'``)
    :param required: If true, the helper text should use required classes key. (``bool``)
    :param variant: The variant to use. (``'filled' | 'outlined' | 'standard' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-form-helper-text", children, **kwargs)
        self.props += [
            "disabled",
            "error",
            "filled",
            "focused",
            "margin",
            "required",
            "variant",
        ]


class FormLabel(MuiHtmlElement):
    """MUI FormLabel - https://mui.com/material-ui/api/form-label/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (``'error' | 'info' | 'primary' | 'secondary' | 'success' | 'warning' | string``)
    :param disabled: If true, the label should be displayed in a disabled state. (``bool``)
    :param error: If true, the label is displayed in an error state. (``bool``)
    :param filled: If true, the label should use filled classes key. (``bool``)
    :param focused: If true, the input of this label is focused (used by FormGroup components). (``bool``)
    :param required: If true, the label will indicate that the input is required. (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-form-label", children, **kwargs)
        self.props += [
            "color",
            "disabled",
            "error",
            "filled",
            "focused",
            "required",
        ]


class GlobalStyles(MuiHtmlElement):
    """MUI GlobalStyles - https://mui.com/material-ui/api/global-styles/

    :param styles: The styles you want to apply globally. (``array | func | number | object | string | bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-global-styles", children, **kwargs)
        self.props += [
            "styles",
        ]


class Grid(MuiHtmlElement):
    """MUI Grid - https://mui.com/material-ui/api/grid/

    :param column_spacing: Defines the horizontal space between the type item components. It overrides the value of the spacing prop. (``Array<number | string> | number | object | string``)
    :param columns: The number of columns. (default: 12) (``Array<number> | number | object``)
    :param container: If true, the component will have the flex container behavior. You should be wrapping items with a container. (default: false) (``bool``)
    :param direction: Defines the flex-direction style property for the container. ⚠️ Only row and row-reverse are supported. column and column-reverse are not supported, because the Grid component is designed to subdivide layouts into columns, not rows. For vertical layouts, use Stack instead. (default: 'row') (``'row-reverse' | 'row' | Array<'row-reverse' | 'row'> | object``)
    :param offset: Defines the offset value for the type item components. (``string | number | Array<string | number> | object``)
    :param row_spacing: Defines the vertical space between the type item components. It overrides the value of the spacing prop. (``Array<number | string> | number | object | string``)
    :param size: Defines the size of the the type item components. (``string | bool | number | Array<string | bool | number> | object``)
    :param spacing: Defines the space between the type item components. It can only be used on a type container component. (default: 0) (``Array<number | string> | number | object | string``)
    :param wrap: Defines the flex-wrap style property. It's applied for all screen sizes. (default: 'wrap') (``'nowrap' | 'wrap-reverse' | 'wrap'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-grid", children, **kwargs)
        self.props += [
            ("column_spacing", "columnSpacing"),
            "columns",
            "container",
            "direction",
            "offset",
            ("row_spacing", "rowSpacing"),
            "size",
            "spacing",
            "wrap",
        ]


class Grow(MuiHtmlElement):
    """MUI Grow - https://mui.com/material-ui/api/grow/

    The Grow transition is used by the [Tooltip](/material-ui/react-tooltip/) and [Popover](/material-ui/react-popover/) components.

    :param add_end_listener: Add a custom transition end trigger. Use it when you need custom logic to decide when the transition has ended. Note: Timeouts are still used as a fallback if provided. (``func``)
    :param appear: Perform the enter transition when it first mounts if in is also true. Set this to false to disable this behavior. (default: true) (``bool``)
    :param disable_prefers_reduced_motion: If true, the transition ignores theme.motion.reducedMotion and keeps its normal timing. (default: false) (``bool``)
    :param easing: The transition timing function. You may specify a single easing or a object containing enter and exit values. (``{ enter?: string, exit?: string } | string``)
    :param in: If true, the component will transition in. (``bool``)
    :param timeout: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. Set to 'auto' to automatically calculate transition time based on height. (default: 'auto') (``'auto' | number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-grow", children, **kwargs)
        self.props += [
            ("add_end_listener", "addEndListener"),
            "appear",
            ("disable_prefers_reduced_motion", "disablePrefersReducedMotion"),
            "easing",
            "in",
            "timeout",
        ]


class Icon(MuiHtmlElement):
    """MUI Icon - https://mui.com/material-ui/api/icon/

    :param base_class_name: The base class applied to the icon. Defaults to 'material-icons', but can be changed to any other base class that suits the icon font you're using (for example material-icons-rounded, fas, etc). (default: 'material-icons') (``string``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'inherit') (``'inherit' | 'action' | 'disabled' | 'primary' | 'secondary' | 'error' | 'info' ...``)
    :param font_size: The fontSize applied to the icon. Defaults to 24px, but can be configure to inherit font size. (default: 'medium') (``'inherit' | 'large' | 'medium' | 'small' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-icon", children, **kwargs)
        self.props += [
            ("base_class_name", "baseClassName"),
            "color",
            ("font_size", "fontSize"),
        ]


class IconButton(MuiHtmlElement):
    """MUI IconButton - https://mui.com/material-ui/api/icon-button/

    Refer to the [Icons](/material-ui/icons/) section of the documentation regarding the available icon options.

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'default') (``'inherit' | 'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' ...``)
    :param disable_focus_ripple: If true, the keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. ⚠️ Without a ripple there is no styling for :focus-visible by default. Be sure to highlight the element by applying separate styles with the .Mui-focusVisible class. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param edge: If given, uses a negative margin to counteract the padding on one side (this is often helpful for aligning the left or right side of the icon with content above or below, without ruining the border size and shape). (default: false) (``'end' | 'start' | false``)
    :param loading: If true, the loading indicator is visible and the button is disabled. If true | false, the loading wrapper is always rendered before the children to prevent Google Translation Crash. (default: null) (``bool``)
    :param loading_indicator: Element placed before the children if the button is in loading state. The node should contain an element with role="progressbar" with an accessible name. By default, it renders a CircularProgress that is labeled by the button itself. (default: <CircularProgress color="inherit" size={16} />) (``node``)
    :param size: The size of the component. small is equivalent to the dense button styling. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-icon-button", children, **kwargs)
        self.props += [
            "color",
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            "edge",
            "loading",
            ("loading_indicator", "loadingIndicator"),
            "size",
        ]


class ImageList(MuiHtmlElement):
    """MUI ImageList - https://mui.com/material-ui/api/image-list/

    :param cols: Number of columns. (default: 2) (``integer``)
    :param gap: The gap between items in px. (default: 4) (``number``)
    :param row_height: The height of one row in px. (default: 'auto') (``'auto' | number``)
    :param variant: The variant to use. (default: 'standard') (``'masonry' | 'quilted' | 'standard' | 'woven' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-image-list", children, **kwargs)
        self.props += [
            "cols",
            "gap",
            ("row_height", "rowHeight"),
            "variant",
        ]


class ImageListItem(MuiHtmlElement):
    """MUI ImageListItem - https://mui.com/material-ui/api/image-list-item/

    :param cols: Width of the item in number of grid columns. (default: 1) (``integer``)
    :param rows: Height of the item in number of grid rows. (default: 1) (``integer``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-image-list-item", children, **kwargs)
        self.props += [
            "cols",
            "rows",
        ]
        self.literal_children = True


class ImageListItemBar(MuiHtmlElement):
    """MUI ImageListItemBar - https://mui.com/material-ui/api/image-list-item-bar/

    :param action_icon: An IconButton element to be used as secondary action target (primary action target is the item itself). (``node``)
    :param action_position: Position of secondary action IconButton. (default: 'right') (``'left' | 'right'``)
    :param position: Position of the title bar. (default: 'bottom') (``'below' | 'bottom' | 'top'``)
    :param subtitle: String or element serving as subtitle (support text). (``node``)
    :param title: Title to be displayed. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-image-list-item-bar", children, **kwargs)
        self.props += [
            ("action_icon", "actionIcon"),
            ("action_position", "actionPosition"),
            "position",
            "subtitle",
            "title",
        ]


class InitColorSchemeScript(MuiHtmlElement):
    """MUI InitColorSchemeScript - https://mui.com/material-ui/api/init-color-scheme-script/

    :param attribute: DOM attribute for applying a color scheme. (default: 'data-mui-color-scheme') (``string``)
    :param color_scheme_node: The node (provided as string) used to attach the color-scheme attribute. (default: 'document.documentElement') (``string``)
    :param color_scheme_storage_key: localStorage key used to store colorScheme. (default: 'mui-color-scheme') (``string``)
    :param default_dark_color_scheme: The default color scheme to be used in dark mode. (default: 'dark') (``string``)
    :param default_light_color_scheme: The default color scheme to be used in light mode. (default: 'light') (``string``)
    :param default_mode: The default mode when the storage is empty (user's first visit). (default: 'system') (``'dark' | 'light' | 'system'``)
    :param mode_storage_key: localStorage key used to store mode. (default: 'mui-mode') (``string``)
    :param nonce: Nonce string to pass to the inline script for CSP headers. (``string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-init-color-scheme-script", children, **kwargs)
        self.props += [
            "attribute",
            ("color_scheme_node", "colorSchemeNode"),
            ("color_scheme_storage_key", "colorSchemeStorageKey"),
            ("default_dark_color_scheme", "defaultDarkColorScheme"),
            ("default_light_color_scheme", "defaultLightColorScheme"),
            ("default_mode", "defaultMode"),
            ("mode_storage_key", "modeStorageKey"),
            "nonce",
        ]


class Input(MuiHtmlElement):
    """MUI Input - https://mui.com/material-ui/api/input/

    :param auto_complete: This prop helps users to fill forms faster, especially on mobile devices. The name can be confusing, as it's more like an autofill. You can learn more about it following the specification. (``string``)
    :param auto_focus: If true, the input element is focused during the first mount. (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. The prop defaults to the value ('primary') inherited from the parent FormControl component. (``'primary' | 'secondary' | string``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param disable_underline: If true, the input will not have an underline. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param end_adornment: End InputAdornment for this component. (``node``)
    :param error: If true, the input will indicate an error. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param full_width: If true, the input will take up the full width of its container. (default: false) (``bool``)
    :param id: The id of the input element. (``string``)
    :param input_component: The component used for the input element. Either a string to use a HTML element or a component. (default: 'input') (``elementType``)
    :param input_props: Attributes applied to the input element. (default: {}) (``object``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. The prop defaults to the value ('none') inherited from the parent FormControl component. (``'dense' | 'none'``)
    :param max_rows: Maximum number of rows to display when multiline option is set to true. (``number | string``)
    :param min_rows: Minimum number of rows to display when multiline option is set to true. (``number | string``)
    :param multiline: If true, a TextareaAutosize element is rendered. (default: false) (``bool``)
    :param name: Name attribute of the input element. (``string``)
    :param on_change: Callback fired when the value is changed. (``func``)
    :param placeholder: The short hint displayed in the input before the user enters a value. (``string``)
    :param read_only: It prevents the user from changing the value of the field (not from interacting with the field). (``bool``)
    :param required: If true, the input element is required. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param rows: Number of rows to display when multiline option is set to true. (``number | string``)
    :param slot_props: The extra props for the slot components. You can override the existing props or add new ones. (default: {}) (``{ input?: object, root?: object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType }``)
    :param start_adornment: Start InputAdornment for this component. (``node``)
    :param type: Type of the input element. It should be a valid HTML5 input type. (default: 'text') (``string``)
    :param value: The value of the input element, required for a controlled component. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-input", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_focus", "autoFocus"),
            "color",
            ("default_value", "defaultValue"),
            ("disable_underline", "disableUnderline"),
            "disabled",
            ("end_adornment", "endAdornment"),
            "error",
            ("full_width", "fullWidth"),
            "id",
            ("input_component", "inputComponent"),
            ("input_props", "inputProps"),
            ("input_ref", "inputRef"),
            "margin",
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
            "multiline",
            "name",
            ("on_change", "onChange"),
            "placeholder",
            ("read_only", "readOnly"),
            "required",
            "rows",
            ("slot_props", "slotProps"),
            "slots",
            ("start_adornment", "startAdornment"),
            "type",
            "value",
        ]


class InputAdornment(MuiHtmlElement):
    """MUI InputAdornment - https://mui.com/material-ui/api/input-adornment/

    :param disable_pointer_events: Disable pointer events on the root. This allows for the content of the adornment to focus the input on click. (default: false) (``bool``)
    :param disable_typography: If children is a string then disable wrapping in a Typography component. (default: false) (``bool``)
    :param position: The position this adornment should appear relative to the Input. (``'end' | 'start'``)
    :param variant: The variant to use. Note: If you are using the TextField component or the FormControl component you do not have to set this manually. (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-input-adornment", children, **kwargs)
        self.props += [
            ("disable_pointer_events", "disablePointerEvents"),
            ("disable_typography", "disableTypography"),
            "position",
            "variant",
        ]


class InputBase(MuiHtmlElement):
    """MUI InputBase - https://mui.com/material-ui/api/input-base/

    `InputBase` contains as few styles as possible. It aims to be a simple building block for creating an input. It contains a load of style reset and some state logic.

    :param auto_complete: This prop helps users to fill forms faster, especially on mobile devices. The name can be confusing, as it's more like an autofill. You can learn more about it following the specification. (``string``)
    :param auto_focus: If true, the input element is focused during the first mount. (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. The prop defaults to the value ('primary') inherited from the parent FormControl component. (``'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' | string``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param disable_injecting_global_styles: If true, GlobalStyles for the auto-fill keyframes will not be injected/removed on mount/unmount. Make sure to inject them at the top of your application. This option is intended to help with boosting the initial rendering performance if you are loading a big amount of Input components at once. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param end_adornment: End InputAdornment for this component. (``node``)
    :param error: If true, the input will indicate an error. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param full_width: If true, the input will take up the full width of its container. (default: false) (``bool``)
    :param id: The id of the input element. (``string``)
    :param input_component: The component used for the input element. Either a string to use a HTML element or a component. (default: 'input') (``element type``)
    :param input_props: Attributes applied to the input element. (default: {}) (``object``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. The prop defaults to the value ('none') inherited from the parent FormControl component. (``'dense' | 'none'``)
    :param max_rows: Maximum number of rows to display when multiline option is set to true. (``number | string``)
    :param min_rows: Minimum number of rows to display when multiline option is set to true. (``number | string``)
    :param multiline: If true, a TextareaAutosize element is rendered. (default: false) (``bool``)
    :param name: Name attribute of the input element. (``string``)
    :param on_blur: Callback fired when the input is blurred. Notice that the first argument (event) might be undefined. (``func``)
    :param on_change: Callback fired when the value is changed. (``func``)
    :param on_invalid: Callback fired when the input doesn't satisfy its constraints. (``func``)
    :param placeholder: The short hint displayed in the input before the user enters a value. (``string``)
    :param read_only: It prevents the user from changing the value of the field (not from interacting with the field). (``bool``)
    :param required: If true, the input element is required. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param rows: Number of rows to display when multiline option is set to true. (``number | string``)
    :param size: The size of the component. (``'medium' | 'small' | string``)
    :param slot_props: The extra props for the slot components. You can override the existing props or add new ones. (default: {}) (``{ input?: object, root?: object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType }``)
    :param start_adornment: Start InputAdornment for this component. (``node``)
    :param type: Type of the input element. It should be a valid HTML5 input type. (default: 'text') (``string``)
    :param value: The value of the input element, required for a controlled component. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-input-base", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_focus", "autoFocus"),
            "color",
            ("default_value", "defaultValue"),
            ("disable_injecting_global_styles", "disableInjectingGlobalStyles"),
            "disabled",
            ("end_adornment", "endAdornment"),
            "error",
            ("full_width", "fullWidth"),
            "id",
            ("input_component", "inputComponent"),
            ("input_props", "inputProps"),
            ("input_ref", "inputRef"),
            "margin",
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
            "multiline",
            "name",
            ("on_blur", "onBlur"),
            ("on_change", "onChange"),
            ("on_invalid", "onInvalid"),
            "placeholder",
            ("read_only", "readOnly"),
            "required",
            "rows",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            ("start_adornment", "startAdornment"),
            "type",
            "value",
        ]


class InputLabel(MuiHtmlElement):
    """MUI InputLabel - https://mui.com/material-ui/api/input-label/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (``'error' | 'info' | 'primary' | 'secondary' | 'success' | 'warning' | string``)
    :param disable_animation: If true, the transition animation is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (``bool``)
    :param error: If true, the label is displayed in an error state. (``bool``)
    :param focused: If true, the input of this label is focused. (``bool``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. (``'dense'``)
    :param required: if true, the label will indicate that the input is required. (``bool``)
    :param shrink: If true, the label is shrunk. (``bool``)
    :param size: The size of the component. (default: 'medium') (``'medium' | 'small' | string``)
    :param variant: The variant to use. (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-input-label", children, **kwargs)
        self.props += [
            "color",
            ("disable_animation", "disableAnimation"),
            "disabled",
            "error",
            "focused",
            "margin",
            "required",
            "shrink",
            "size",
            "variant",
        ]


class LinearProgress(MuiHtmlElement):
    """MUI LinearProgress - https://mui.com/material-ui/api/linear-progress/

    ## ARIA If the progress bar is describing the loading progress of a particular region of a page, you should use `aria-describedby` to point to the progress bar, and set the `aria-busy` attribute to `true` on that region until it has finished loading.

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'inherit' | 'primary' | 'secondary' | string``)
    :param max: The maximum value for the progress indicator for the determinate and buffer variants. (default: 100) (``number``)
    :param min: The minimum value for the progress indicator for the determinate and buffer variants. (default: 0) (``number``)
    :param value: The value of the progress indicator for the determinate and buffer variants. Value between min and max. (``number``)
    :param value_buffer: The value for the buffer variant. Value between min and max. (``number``)
    :param variant: The variant to use. Use indeterminate or query when there is no progress value. (default: 'indeterminate') (``'buffer' | 'determinate' | 'indeterminate' | 'query'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-linear-progress", children, **kwargs)
        self.props += [
            "color",
            "max",
            "min",
            "value",
            ("value_buffer", "valueBuffer"),
            "variant",
        ]


class Link(MuiHtmlElement):
    """MUI Link - https://mui.com/material-ui/api/link/

    :param typography_classes: classes prop applied to the Typography element. (``object``)
    :param color: The color of the link. (default: 'primary') (``'primary' | 'secondary' | 'success' | 'error' | 'info' | 'warning' | ...``)
    :param underline: Controls when the link should have an underline. (default: 'always') (``'always' | 'hover' | 'none'``)
    :param variant: Applies the theme typography styles. (default: 'inherit') (``'body1' | 'body2' | 'button' | 'caption' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | ...``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-link", children, **kwargs)
        self.props += [
            ("typography_classes", "TypographyClasses"),
            "color",
            "underline",
            "variant",
        ]


class List(MuiHtmlElement):
    """MUI List - https://mui.com/material-ui/api/list/

    :param dense: If true, compact vertical padding designed for keyboard and mouse input is used for the list and list items. The prop is available to descendant components as the dense context. (default: false) (``bool``)
    :param disable_padding: If true, vertical padding is removed from the list. (default: false) (``bool``)
    :param subheader: The content of the subheader, normally ListSubheader. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list", children, **kwargs)
        self.props += [
            "dense",
            ("disable_padding", "disablePadding"),
            "subheader",
        ]


class ListItem(MuiHtmlElement):
    """MUI ListItem - https://mui.com/material-ui/api/list-item/

    :param align_items: Defines the align-items style property. (default: 'center') (``'center' | 'flex-start'``)
    :param dense: If true, compact vertical padding designed for keyboard and mouse input is used. The prop defaults to the value inherited from the parent List component. (default: false) (``bool``)
    :param disable_gutters: If true, the left and right padding is removed. (default: false) (``bool``)
    :param disable_padding: If true, all padding is removed. (default: false) (``bool``)
    :param divider: If true, a 1px light border is added to the bottom of the list item. (default: false) (``bool``)
    :param secondary_action: The element to display at the end of ListItem. (``node``)
    :param slot_props: The extra props for the slot components. You can override the existing props or add new ones. (default: {}) (``{ root?: func | object, secondaryAction?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ root?: elementType, secondaryAction?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item", children, **kwargs)
        self.props += [
            ("align_items", "alignItems"),
            "dense",
            ("disable_gutters", "disableGutters"),
            ("disable_padding", "disablePadding"),
            "divider",
            ("secondary_action", "secondaryAction"),
            ("slot_props", "slotProps"),
            "slots",
        ]


class ListItemAvatar(MuiHtmlElement):
    """MUI ListItemAvatar - https://mui.com/material-ui/api/list-item-avatar/

    A simple wrapper to apply `List` styles to an `Avatar`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item-avatar", children, **kwargs)


class ListItemButton(MuiHtmlElement):
    """MUI ListItemButton - https://mui.com/material-ui/api/list-item-button/

    :param align_items: Defines the align-items style property. (default: 'center') (``'center' | 'flex-start'``)
    :param auto_focus: If true, the list item is focused during the first mount. Focus will also be triggered if the value changes from false to true. (default: false) (``bool``)
    :param dense: If true, compact vertical padding designed for keyboard and mouse input is used. The prop defaults to the value inherited from the parent List component. (default: false) (``bool``)
    :param disable_gutters: If true, the left and right padding is removed. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param divider: If true, a 1px light border is added to the bottom of the list item. (default: false) (``bool``)
    :param focus_visible_class_name: This prop can help identify which element has keyboard focus. The class name will be applied when the element gains the focus through keyboard interaction. It's a polyfill for the CSS :focus-visible selector. The rationale for using this feature is explained here. A polyfill can be used to apply a focus-visible class to other components if needed. (``string``)
    :param selected: Use to apply selected styling. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item-button", children, **kwargs)
        self.props += [
            ("align_items", "alignItems"),
            ("auto_focus", "autoFocus"),
            "dense",
            ("disable_gutters", "disableGutters"),
            "disabled",
            "divider",
            ("focus_visible_class_name", "focusVisibleClassName"),
            "selected",
        ]


class ListItemIcon(MuiHtmlElement):
    """MUI ListItemIcon - https://mui.com/material-ui/api/list-item-icon/

    A simple wrapper to apply `List` styles to an `Icon` or `SvgIcon`.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item-icon", children, **kwargs)


class ListItemSecondaryAction(MuiHtmlElement):
    """MUI ListItemSecondaryAction - https://mui.com/material-ui/api/list-item-secondary-action/

    Must be used as the last child of ListItem to function properly.
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item-secondary-action", children, **kwargs)


class ListItemText(MuiHtmlElement):
    """MUI ListItemText - https://mui.com/material-ui/api/list-item-text/

    :param disable_typography: If true, the children won't be wrapped by a Typography component. This can be useful to render an alternative Typography variant by wrapping the children (or primary) text, and optional secondary text with the Typography component. (default: false) (``bool``)
    :param inset: If true, the children are indented. This should be used if there is no left avatar or left icon. (default: false) (``bool``)
    :param primary: The main content element. (``node``)
    :param secondary: The secondary content element. (``node``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ primary?: func | object, root?: func | object, secondary?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ primary?: elementType, root?: elementType, secondary?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-item-text", children, **kwargs)
        self.props += [
            ("disable_typography", "disableTypography"),
            "inset",
            "primary",
            "secondary",
            ("slot_props", "slotProps"),
            "slots",
        ]


class ListSubheader(MuiHtmlElement):
    """MUI ListSubheader - https://mui.com/material-ui/api/list-subheader/

    :param color: The color of the component. It supports those theme colors that make sense for this component. (default: 'default') (``'default' | 'inherit' | 'primary'``)
    :param disable_gutters: If true, the List Subheader will not have gutters. (default: false) (``bool``)
    :param disable_sticky: If true, the List Subheader will not stick to the top during scroll. (default: false) (``bool``)
    :param inset: If true, the List Subheader is indented. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-list-subheader", children, **kwargs)
        self.props += [
            "color",
            ("disable_gutters", "disableGutters"),
            ("disable_sticky", "disableSticky"),
            "inset",
        ]


class Menu(MuiHtmlElement):
    """MUI Menu - https://mui.com/material-ui/api/menu/

    :param popover_classes: classes prop applied to the Popover element. (``object``)
    :param anchor_el: An HTML element, or a function that returns one. It's used to set the position of the menu. (``HTML element | func``)
    :param auto_focus: If true (Default) will focus the [role="menu"] if no focusable child is found. Disabled children are not focusable. If you set this prop to false focus will be placed on the parent modal container. This has severe accessibility implications and should only be considered if you manage focus otherwise. (default: true) (``bool``)
    :param disable_auto_focus_item: When opening the menu will not focus the active item but the [role="menu"] unless autoFocus is also set to false. Not using the default means not following WAI-ARIA authoring practices. Please be considerate about possible accessibility implications. (default: false) (``bool``)
    :param on_close: Callback fired when the component requests to be closed. (``func``)
    :param open: If true, the component is shown. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ backdrop?: func | object, list?: func | object, paper?: func | object, root?: ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ backdrop?: elementType, list?: elementType, paper?: elementType, root?: ...``)
    :param transition_duration: The length of the transition in ms, or 'auto' (default: 'auto') (``'auto' | number | { appear?: number, enter?: number, exit?: number }``)
    :param variant: The variant to use. Use menu to prevent selected items from impacting the initial focus. (default: 'selectedMenu') (``'menu' | 'selectedMenu'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-menu", children, **kwargs)
        self.props += [
            ("popover_classes", "PopoverClasses"),
            ("anchor_el", "anchorEl"),
            ("auto_focus", "autoFocus"),
            ("disable_auto_focus_item", "disableAutoFocusItem"),
            ("on_close", "onClose"),
            "open",
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
            "variant",
        ]


class MenuItem(MuiHtmlElement):
    """MUI MenuItem - https://mui.com/material-ui/api/menu-item/

    :param auto_focus: If true, the list item is focused during the first mount. Focus will also be triggered if the value changes from false to true. (default: false) (``bool``)
    :param dense: If true, compact vertical padding designed for keyboard and mouse input is used. The prop defaults to the value inherited from the parent Menu component. (default: false) (``bool``)
    :param disable_gutters: If true, the left and right padding is removed. (default: false) (``bool``)
    :param divider: If true, a 1px light border is added to the bottom of the menu item. (default: false) (``bool``)
    :param focus_visible_class_name: This prop can help identify which element has keyboard focus. The class name will be applied when the element gains the focus through keyboard interaction. It's a polyfill for the CSS :focus-visible selector. The rationale for using this feature is explained here. A polyfill can be used to apply a focus-visible class to other components if needed. (``string``)
    :param selected: If true, the component is selected. For menuitemcheckbox and menuitemradio roles, this also drives aria-checked. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-menu-item", children, **kwargs)
        self.props += [
            ("auto_focus", "autoFocus"),
            "dense",
            ("disable_gutters", "disableGutters"),
            "divider",
            ("focus_visible_class_name", "focusVisibleClassName"),
            "selected",
        ]


class MenuList(MuiHtmlElement):
    """MUI MenuList - https://mui.com/material-ui/api/menu-list/

    A permanently displayed menu following https://www.w3.org/WAI/ARIA/apg/patterns/menu-button/. It's exposed to help customization of the [`Menu`](/material-ui/api/menu/) component if you use it separately you need to move focus into the component manually. Once the focus is placed inside the component it is fully keyboard accessible.

    :param auto_focus: If true, will focus the [role="menu"] container and move into tab order. (default: false) (``bool``)
    :param auto_focus_item: If true, will focus the first menuitem if variant="menu" or selected item if variant="selectedMenu". (default: false) (``bool``)
    :param disable_list_wrap: If true, the menu items will not wrap focus. (default: false) (``bool``)
    :param disabled_items_focusable: If true, will allow focus on disabled items. (default: false) (``bool``)
    :param variant: The variant to use. Use menu to prevent selected items from impacting the initial focus and the vertical alignment relative to the anchor element. (default: 'selectedMenu') (``'menu' | 'selectedMenu'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-menu-list", children, **kwargs)
        self.props += [
            ("auto_focus", "autoFocus"),
            ("auto_focus_item", "autoFocusItem"),
            ("disable_list_wrap", "disableListWrap"),
            ("disabled_items_focusable", "disabledItemsFocusable"),
            "variant",
        ]


class MobileStepper(MuiHtmlElement):
    """MUI MobileStepper - https://mui.com/material-ui/api/mobile-stepper/

    :param active_step: Set the active step (zero based index). Defines which dot is highlighted when the variant is 'dots'. (default: 0) (``integer``)
    :param back_button: A back button element. For instance, it can be a Button or an IconButton. (``node``)
    :param next_button: A next button element. For instance, it can be a Button or an IconButton. (``node``)
    :param position: Set the positioning type. (default: 'bottom') (``'bottom' | 'static' | 'top'``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ dot?: func | object, dots?: func | object, progress?: func | object, root?: ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ dot?: elementType, dots?: elementType, progress?: elementType, root?: ...``)
    :param steps: The total steps. (``integer``)
    :param variant: The variant to use. (default: 'dots') (``'dots' | 'progress' | 'text'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-mobile-stepper", children, **kwargs)
        self.props += [
            ("active_step", "activeStep"),
            ("back_button", "backButton"),
            ("next_button", "nextButton"),
            "position",
            ("slot_props", "slotProps"),
            "slots",
            "steps",
            "variant",
        ]


class Modal(MuiHtmlElement):
    """MUI Modal - https://mui.com/material-ui/api/modal/

    Modal is a lower-level construct that is leveraged by the following components: - [Dialog](/material-ui/api/dialog/) - [Drawer](/material-ui/api/drawer/) - [Menu](/material-ui/api/menu/) - [Popover](/material-ui/api/popover/) If you are creating a modal dialog, you probably want to use the [Dialog](/material-ui/api/dialog/) component rather than directly using Modal. This component shares many concepts with [react-overlays](https://react-bootstrap.github.io/react-overlays/#modals).

    :param close_after_transition: When set to true the Modal waits until a nested Transition is completed before closing. (default: false) (``bool``)
    :param container: An HTML element or function that returns one. The container will have the portal children appended to it. You can also provide a callback, which is called in a React layout effect. This lets you set the container from a ref, and also makes server-side rendering possible. By default, it uses the body of the top-level document object, so it's simply document.body most of the time. (``HTML element | func``)
    :param disable_auto_focus: If true, the modal will not automatically shift focus to itself when it opens, and replace it to the last focused element when it closes. This also works correctly with any modal children that have the disableAutoFocus prop. Generally this should never be set to true as it makes the modal less accessible to assistive technologies, like screen readers. (default: false) (``bool``)
    :param disable_enforce_focus: If true, the modal will not prevent focus from leaving the modal while open. Generally this should never be set to true as it makes the modal less accessible to assistive technologies, like screen readers. (default: false) (``bool``)
    :param disable_portal: The children will be under the DOM hierarchy of the parent component. (default: false) (``bool``)
    :param disable_restore_focus: If true, the modal will not restore focus to previously focused element once modal is hidden or unmounted. (default: false) (``bool``)
    :param disable_scroll_lock: Disable the scroll lock behavior. (default: false) (``bool``)
    :param hide_backdrop: If true, the backdrop is not rendered. (default: false) (``bool``)
    :param keep_mounted: Always keep the children in the DOM. This prop can be useful in SEO situation or when you want to maximize the responsiveness of the Modal. (default: false) (``bool``)
    :param on_close: Callback fired when the component requests to be closed. The reason parameter can optionally be used to control the response to onClose. (``func``)
    :param on_transition_enter: A function called when a transition enters. (``func``)
    :param on_transition_exited: A function called when a transition has exited. (``func``)
    :param open: If true, the component is shown. (``bool``)
    :param slot_props: The props used for each slot inside the Modal. (default: {}) (``{ backdrop?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside the Modal. Either a string to use a HTML element or a component. (default: {}) (``{ backdrop?: elementType, root?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-modal", children, **kwargs)
        self.props += [
            ("close_after_transition", "closeAfterTransition"),
            "container",
            ("disable_auto_focus", "disableAutoFocus"),
            ("disable_enforce_focus", "disableEnforceFocus"),
            ("disable_portal", "disablePortal"),
            ("disable_restore_focus", "disableRestoreFocus"),
            ("disable_scroll_lock", "disableScrollLock"),
            ("hide_backdrop", "hideBackdrop"),
            ("keep_mounted", "keepMounted"),
            ("on_close", "onClose"),
            ("on_transition_enter", "onTransitionEnter"),
            ("on_transition_exited", "onTransitionExited"),
            "open",
            ("slot_props", "slotProps"),
            "slots",
        ]


class NativeSelect(MuiHtmlElement):
    """MUI NativeSelect - https://mui.com/material-ui/api/native-select/

    An alternative to `` with a much smaller bundle size footprint.

    :param icon_component: The icon that displays the arrow. (default: ArrowDropDownIcon) (``elementType``)
    :param input: An Input element; does not have to be a material-ui specific Input. (default: <Input />) (``element``)
    :param input_props: Attributes applied to the select element. (``object``)
    :param on_change: Callback fired when a menu item is selected. (``func``)
    :param value: The input value. The DOM API casts this to a string. (``any``)
    :param variant: The variant to use. (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-native-select", children, **kwargs)
        self.props += [
            ("icon_component", "IconComponent"),
            "input",
            ("input_props", "inputProps"),
            ("on_change", "onChange"),
            "value",
            "variant",
        ]


class NoSsr(MuiHtmlElement):
    """MUI NoSsr - https://mui.com/material-ui/api/no-ssr/

    NoSsr purposely removes components from the subject of Server Side Rendering (SSR). This component can be useful in a variety of situations: * Escape hatch for broken dependencies not supporting SSR. * Improve the time-to-first paint on the client by only rendering above the fold. * Reduce the rendering time on the server. * Under too heavy server load, you can turn on service degradation.

    :param defer: If true, the component will not only prevent server-side rendering. It will also defer the rendering of the children into a different screen frame. (default: false) (``bool``)
    :param fallback: The fallback content to display. (default: null) (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-no-ssr", children, **kwargs)
        self.props += [
            "defer",
            "fallback",
        ]


class OutlinedInput(MuiHtmlElement):
    """MUI OutlinedInput - https://mui.com/material-ui/api/outlined-input/

    :param auto_complete: This prop helps users to fill forms faster, especially on mobile devices. The name can be confusing, as it's more like an autofill. You can learn more about it following the specification. (``string``)
    :param auto_focus: If true, the input element is focused during the first mount. (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. The prop defaults to the value ('primary') inherited from the parent FormControl component. (``'primary' | 'secondary' | string``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param disabled: If true, the component is disabled. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param end_adornment: End InputAdornment for this component. (``node``)
    :param error: If true, the input will indicate an error. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param full_width: If true, the input will take up the full width of its container. (default: false) (``bool``)
    :param id: The id of the input element. (``string``)
    :param input_component: The component used for the input element. Either a string to use a HTML element or a component. (default: 'input') (``elementType``)
    :param input_props: Attributes applied to the input element. (default: {}) (``object``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param label: The label of the input. It is only used for layout. The actual labelling is handled by InputLabel. (``node``)
    :param margin: If dense, will adjust vertical spacing. This is normally obtained via context from FormControl. The prop defaults to the value ('none') inherited from the parent FormControl component. (``'dense' | 'none'``)
    :param max_rows: Maximum number of rows to display when multiline option is set to true. (``number | string``)
    :param min_rows: Minimum number of rows to display when multiline option is set to true. (``number | string``)
    :param multiline: If true, a TextareaAutosize element is rendered. (default: false) (``bool``)
    :param name: Name attribute of the input element. (``string``)
    :param notched: If true, the outline is notched to accommodate the label. (``bool``)
    :param on_change: Callback fired when the value is changed. (``func``)
    :param placeholder: The short hint displayed in the input before the user enters a value. (``string``)
    :param read_only: It prevents the user from changing the value of the field (not from interacting with the field). (``bool``)
    :param required: If true, the input element is required. The prop defaults to the value (false) inherited from the parent FormControl component. (``bool``)
    :param rows: Number of rows to display when multiline option is set to true. (``number | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ input?: object, notchedOutline?: func | object, root?: object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, notchedOutline?: elementType, root?: elementType }``)
    :param start_adornment: Start InputAdornment for this component. (``node``)
    :param type: Type of the input element. It should be a valid HTML5 input type. (default: 'text') (``string``)
    :param value: The value of the input element, required for a controlled component. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-outlined-input", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_focus", "autoFocus"),
            "color",
            ("default_value", "defaultValue"),
            "disabled",
            ("end_adornment", "endAdornment"),
            "error",
            ("full_width", "fullWidth"),
            "id",
            ("input_component", "inputComponent"),
            ("input_props", "inputProps"),
            ("input_ref", "inputRef"),
            "label",
            "margin",
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
            "multiline",
            "name",
            "notched",
            ("on_change", "onChange"),
            "placeholder",
            ("read_only", "readOnly"),
            "required",
            "rows",
            ("slot_props", "slotProps"),
            "slots",
            ("start_adornment", "startAdornment"),
            "type",
            "value",
        ]


class Pagination(MuiHtmlElement):
    """MUI Pagination - https://mui.com/material-ui/api/pagination/

    :param boundary_count: Number of always visible pages at the beginning and end. (default: 1) (``integer``)
    :param color: The active color. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'standard') (``'primary' | 'secondary' | 'standard' | string``)
    :param count: The total number of pages. (default: 1) (``integer``)
    :param default_page: The page selected by default when the component is uncontrolled. (default: 1) (``integer``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param get_item_aria_label: Accepts a function which returns a string value that provides a user-friendly name for the current page. This is important for screen reader users. For localization purposes, you can use the provided translations. (``func``)
    :param hide_next_button: If true, hide the next-page button. (default: false) (``bool``)
    :param hide_prev_button: If true, hide the previous-page button. (default: false) (``bool``)
    :param on_change: Callback fired when the page is changed. (``func``)
    :param page: The current page. Unlike TablePagination, which starts numbering from 0, this pagination starts from 1. (``integer``)
    :param render_item: Render the item. (default: (item) => <PaginationItem {...item} />) (``func``)
    :param shape: The shape of the pagination items. (default: 'circular') (``'circular' | 'rounded'``)
    :param show_first_button: If true, show the first-page button. (default: false) (``bool``)
    :param show_last_button: If true, show the last-page button. (default: false) (``bool``)
    :param sibling_count: Number of always visible pages before and after the current page. (default: 1) (``integer``)
    :param size: The size of the component. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param variant: The variant to use. (default: 'text') (``'outlined' | 'text' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-pagination", children, **kwargs)
        self.props += [
            ("boundary_count", "boundaryCount"),
            "color",
            "count",
            ("default_page", "defaultPage"),
            "disabled",
            ("get_item_aria_label", "getItemAriaLabel"),
            ("hide_next_button", "hideNextButton"),
            ("hide_prev_button", "hidePrevButton"),
            ("on_change", "onChange"),
            "page",
            ("render_item", "renderItem"),
            "shape",
            ("show_first_button", "showFirstButton"),
            ("show_last_button", "showLastButton"),
            ("sibling_count", "siblingCount"),
            "size",
            "variant",
        ]


class PaginationItem(MuiHtmlElement):
    """MUI PaginationItem - https://mui.com/material-ui/api/pagination-item/

    :param color: The active color. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'standard') (``'primary' | 'secondary' | 'standard' | string``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param native_button: Whether the custom component should render a native <button> element when rendering a React component with the component or slots prop. (``bool``)
    :param page: The current page number. (``node``)
    :param selected: If true the pagination item is selected. (default: false) (``bool``)
    :param shape: The shape of the pagination item. (default: 'circular') (``'circular' | 'rounded'``)
    :param size: The size of the component. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ first?: func | object, last?: func | object, next?: func | object, previous?: ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ first?: elementType, last?: elementType, next?: elementType, previous?: ...``)
    :param type: The type of pagination item. (default: 'page') (``'end-ellipsis' | 'first' | 'last' | 'next' | 'page' | 'previous' | ...``)
    :param variant: The variant to use. (default: 'text') (``'outlined' | 'text' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-pagination-item", children, **kwargs)
        self.props += [
            "color",
            "disabled",
            ("native_button", "nativeButton"),
            "page",
            "selected",
            "shape",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "type",
            "variant",
        ]


class Paper(MuiHtmlElement):
    """MUI Paper - https://mui.com/material-ui/api/paper/

    :param elevation: Shadow depth, corresponds to dp in the spec. It accepts values between 0 and 24 inclusive. (default: 1) (``integer``)
    :param square: If true, rounded corners are disabled. (default: false) (``bool``)
    :param variant: The variant to use. (default: 'elevation') (``'elevation' | 'outlined' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-paper", children, **kwargs)
        self.props += [
            "elevation",
            "square",
            "variant",
        ]


class PigmentContainer(MuiHtmlElement):
    """MUI PigmentContainer - https://mui.com/material-ui/api/pigment-container/

    :param disable_gutters: If true, the left and right padding is removed. (default: false) (``bool``)
    :param fixed: Set the max-width to match the min-width of the current breakpoint. This is useful if you'd prefer to design for a fixed set of sizes instead of trying to accommodate a fully fluid viewport. It's fluid by default. (default: false) (``bool``)
    :param max_width: Determine the max-width of the container. The container width grows with the size of the screen. Set to false to disable maxWidth. (default: 'lg') (``'lg' | 'md' | 'sm' | 'xl' | 'xs' | false``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-pigment-container", children, **kwargs)
        self.props += [
            ("disable_gutters", "disableGutters"),
            "fixed",
            ("max_width", "maxWidth"),
        ]


class PigmentGrid(MuiHtmlElement):
    """MUI PigmentGrid - https://mui.com/material-ui/api/pigment-grid/

    :param column_spacing: Defines the horizontal space between the type item components. It overrides the value of the spacing prop. (``Array<number | string> | number | object | string``)
    :param columns: The number of columns. (default: 12) (``Array<number> | number | object``)
    :param container: If true, the component will have the flex container behavior. You should be wrapping items with a container. (default: false) (``bool``)
    :param direction: Defines the flex-direction style property. It is applied for all screen sizes. (default: 'row') (``'row' | 'row-reverse' | Array<'row' | 'row-reverse'> | object``)
    :param offset: Defines the offset of the grid. (``Array<number> | number | object``)
    :param row_spacing: Defines the vertical space between the type item components. It overrides the value of the spacing prop. (``Array<number | string> | number | object | string``)
    :param size: Defines the column size of the grid. (``Array<number> | number | object``)
    :param spacing: Defines the space between the type item components. It can only be used on a type container component. (default: 0) (``Array<number | string> | number | object | string``)
    :param wrap: Defines the flex-wrap style property. It's applied for all screen sizes. (default: 'wrap') (``'nowrap' | 'wrap-reverse' | 'wrap'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-pigment-grid", children, **kwargs)
        self.props += [
            ("column_spacing", "columnSpacing"),
            "columns",
            "container",
            "direction",
            "offset",
            ("row_spacing", "rowSpacing"),
            "size",
            "spacing",
            "wrap",
        ]


class PigmentStack(MuiHtmlElement):
    """MUI PigmentStack - https://mui.com/material-ui/api/pigment-stack/

    :param direction: Defines the flex-direction style property. It is applied for all screen sizes. (default: 'column') (``'column-reverse' | 'column' | 'row-reverse' | 'row' | Array<'column-reverse' | ...``)
    :param divider: Add an element between each child. (``node``)
    :param spacing: Defines the space between immediate children. (default: 0) (``Array<number | string> | number | { lg?: number | string, md?: number | string, ...``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-pigment-stack", children, **kwargs)
        self.props += [
            "direction",
            "divider",
            "spacing",
        ]


class Popover(MuiHtmlElement):
    """MUI Popover - https://mui.com/material-ui/api/popover/

        :param action: A ref for imperative actions. It currently only supports updatePosition() action. (``ref``)
        :param anchor_el: An HTML element, PopoverVirtualElement, or a function that returns either. It's used to set the position of the popover. (``HTML element | func``)
        :param anchor_origin: This is the point on the anchor where the popover's anchorEl will attach to. This is not used when the anchorReference is 'anchorPosition'. Options: vertical: [top, center, bottom]; horizontal: [left, center, right]. (default: {
      vertical: 'top',
      horizontal: 'left',
    }) (``{ horizontal: 'center' | 'left' | 'right' | number, vertical: 'bottom' | ...``)
        :param anchor_position: This is the position that may be used to set the position of the popover. The coordinates are relative to the application's client area. (``{ left: number, top: number }``)
        :param anchor_reference: This determines which anchor prop to refer to when setting the position of the popover. (default: 'anchorEl') (``'anchorEl' | 'anchorPosition' | 'none'``)
        :param container: An HTML element, component instance, or function that returns either. The container will passed to the Modal component. By default, it uses the body of the anchorEl's top-level document object, so it's simply document.body most of the time. (``HTML element | func``)
        :param disable_auto_focus: If true, the modal will not automatically shift focus to itself when it opens, and replace it to the last focused element when it closes. This also works correctly with any modal children that have the disableAutoFocus prop. Generally this should never be set to true as it makes the modal less accessible to assistive technologies, like screen readers. (default: false) (``bool``)
        :param disable_scroll_lock: Disable the scroll lock behavior. (default: false) (``bool``)
        :param elevation: The elevation of the popover. (default: 8) (``integer``)
        :param margin_threshold: Specifies how close to the edge of the window the popover can appear. If null, the popover will not be constrained by the window. (default: 16) (``number``)
        :param on_close: Callback fired when the component requests to be closed. The reason parameter can optionally be used to control the response to onClose. (``func``)
        :param open: If true, the component is shown. (``bool``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ backdrop?: func | object, paper?: func | object, root?: func | object, ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ backdrop?: elementType, paper?: elementType, root?: elementType, transition?: ...``)
        :param transform_origin: This is the point on the popover which will attach to the anchor's origin. Options: vertical: [top, center, bottom, x(px)]; horizontal: [left, center, right, x(px)]. (default: {
      vertical: 'top',
      horizontal: 'left',
    }) (``{ horizontal: 'center' | 'left' | 'right' | number, vertical: 'bottom' | ...``)
        :param transition_duration: Set to 'auto' to automatically calculate transition time based on height. (default: 'auto') (``'auto' | number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-popover", children, **kwargs)
        self.props += [
            "action",
            ("anchor_el", "anchorEl"),
            ("anchor_origin", "anchorOrigin"),
            ("anchor_position", "anchorPosition"),
            ("anchor_reference", "anchorReference"),
            "container",
            ("disable_auto_focus", "disableAutoFocus"),
            ("disable_scroll_lock", "disableScrollLock"),
            "elevation",
            ("margin_threshold", "marginThreshold"),
            ("on_close", "onClose"),
            "open",
            ("slot_props", "slotProps"),
            "slots",
            ("transform_origin", "transformOrigin"),
            ("transition_duration", "transitionDuration"),
        ]


class Popper(MuiHtmlElement):
    """MUI Popper - https://mui.com/material-ui/api/popper/

    :param anchor_el: An HTML element, virtualElement, or a function that returns either. It's used to set the position of the popper. The return value will passed as the reference object of the Popper instance. (``HTML element | object | func``)
    :param container: An HTML element or function that returns one. The container will have the portal children appended to it. You can also provide a callback, which is called in a React layout effect. This lets you set the container from a ref, and also makes server-side rendering possible. By default, it uses the body of the top-level document object, so it's simply document.body most of the time. (``HTML element | func``)
    :param disable_portal: The children will be under the DOM hierarchy of the parent component. (default: false) (``bool``)
    :param keep_mounted: Always keep the children in the DOM. This prop can be useful in SEO situation or when you want to maximize the responsiveness of the Popper. (default: false) (``bool``)
    :param modifiers: Popper.js is based on a "plugin-like" architecture, most of its features are fully encapsulated "modifiers". A modifier is a function that is called each time Popper.js needs to compute the position of the popper. For this reason, modifiers should be very performant to avoid bottlenecks. To learn how to create a modifier, read the modifiers documentation. (``Array<{ data?: object, effect?: func, enabled?: bool, fn?: func, name?: any, ...``)
    :param open: If true, the component is shown. (``bool``)
    :param placement: Popper placement. (default: 'bottom') (``'auto-end' | 'auto-start' | 'auto' | 'bottom-end' | 'bottom-start' | 'bottom' | ...``)
    :param popper_options: Options provided to the Popper.js instance. (default: {}) (``{ modifiers?: array, onFirstUpdate?: func, placement?: 'auto-end' | ...``)
    :param popper_ref: A ref that points to the used popper instance. (``ref``)
    :param slot_props: The props used for each slot inside the Popper. (default: {}) (``{ root?: func | object }``)
    :param slots: The components used for each slot inside the Popper. Either a string to use a HTML element or a component. (default: {}) (``{ root?: elementType }``)
    :param transition: Help supporting a react-transition-group/Transition component. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-popper", children, **kwargs)
        self.props += [
            ("anchor_el", "anchorEl"),
            "container",
            ("disable_portal", "disablePortal"),
            ("keep_mounted", "keepMounted"),
            "modifiers",
            "open",
            "placement",
            ("popper_options", "popperOptions"),
            ("popper_ref", "popperRef"),
            ("slot_props", "slotProps"),
            "slots",
            "transition",
        ]


class Portal(MuiHtmlElement):
    """MUI Portal - https://mui.com/material-ui/api/portal/

    Portals provide a first-class way to render children into a DOM node that exists outside the DOM hierarchy of the parent component.

    :param container: An HTML element or function that returns one. The container will have the portal children appended to it. You can also provide a callback, which is called in a React layout effect. This lets you set the container from a ref, and also makes server-side rendering possible. By default, it uses the body of the top-level document object, so it's simply document.body most of the time. (``HTML element | func``)
    :param disable_portal: The children will be under the DOM hierarchy of the parent component. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-portal", children, **kwargs)
        self.props += [
            "container",
            ("disable_portal", "disablePortal"),
        ]


class Radio(MuiHtmlElement):
    """MUI Radio - https://mui.com/material-ui/api/radio/

    :param checked: If true, the component is checked. (``bool``)
    :param checked_icon: The icon to display when the component is checked. (default: <RadioButtonIcon checked />) (``node``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param disable_ripple: If true, the ripple effect is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (``bool``)
    :param icon: The icon to display when the component is unchecked. (default: <RadioButtonIcon />) (``node``)
    :param id: The id of the input element. (``string``)
    :param name: Name attribute of the input element. (``string``)
    :param on_change: Callback fired when the state is changed. (``func``)
    :param required: If true, the input element is required. (default: false) (``bool``)
    :param size: The size of the component. small is equivalent to the dense radio styling. (default: 'medium') (``'medium' | 'small' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ input?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType }``)
    :param value: The value of the component. The DOM API casts this to a string. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-radio", children, **kwargs)
        self.props += [
            "checked",
            ("checked_icon", "checkedIcon"),
            "color",
            ("disable_ripple", "disableRipple"),
            "disabled",
            "icon",
            "id",
            "name",
            ("on_change", "onChange"),
            "required",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class RadioGroup(MuiHtmlElement):
    """MUI RadioGroup - https://mui.com/material-ui/api/radio-group/

    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param name: The name used to reference the value of the control. If you don't provide this prop, it falls back to a randomly generated name. (``string``)
    :param on_change: Callback fired when a radio button is selected. (``func``)
    :param value: Value of the selected radio button. The DOM API casts this to a string. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-radio-group", children, **kwargs)
        self.props += [
            ("default_value", "defaultValue"),
            "name",
            ("on_change", "onChange"),
            "value",
        ]


class Rating(MuiHtmlElement):
    """MUI Rating - https://mui.com/material-ui/api/rating/

        :param default_value: The default value. Use when the component is not controlled. (default: null) (``number``)
        :param disabled: If true, the component is disabled. (default: false) (``bool``)
        :param empty_icon: The icon to display when empty. (default: <StarBorder fontSize="inherit" />) (``node``)
        :param empty_label_text: The label read when the rating input is empty. (default: 'Empty') (``node``)
        :param get_label_text: Accepts a function which returns a string value that provides a user-friendly name for the current value of the rating. This is important for screen reader users. For localization purposes, you can use the provided translations. (default: function defaultLabelText(value) {
      return `${value || '0'} Star${value !== 1 ? 's' : ''}`;
    }) (``func``)
        :param highlight_selected_only: If true, only the selected icon will be highlighted. (default: false) (``bool``)
        :param icon: The icon to display. (default: <Star fontSize="inherit" />) (``node``)
        :param max: Maximum rating. (default: 5) (``number``)
        :param name: The name attribute of the radio input elements. This input name should be unique within the page. Being unique within a form is insufficient since the name is used to generate IDs. (``string``)
        :param on_change: Callback fired when the value changes. (``func``)
        :param on_change_active: Callback function that is fired when the hover state changes. (``func``)
        :param precision: The minimum increment value change allowed. (default: 1) (``number``)
        :param read_only: Removes all hover effects and pointer events. (default: false) (``bool``)
        :param size: The size of the component. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ decimal?: func | object, icon?: func | object, label?: func | object, root?: ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ decimal?: elementType, icon?: elementType, label?: elementType, root?: ...``)
        :param value: The rating value. (``number``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-rating", children, **kwargs)
        self.props += [
            ("default_value", "defaultValue"),
            "disabled",
            ("empty_icon", "emptyIcon"),
            ("empty_label_text", "emptyLabelText"),
            ("get_label_text", "getLabelText"),
            ("highlight_selected_only", "highlightSelectedOnly"),
            "icon",
            "max",
            "name",
            ("on_change", "onChange"),
            ("on_change_active", "onChangeActive"),
            "precision",
            ("read_only", "readOnly"),
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class ScopedCssBaseline(MuiHtmlElement):
    """MUI ScopedCssBaseline - https://mui.com/material-ui/api/scoped-css-baseline/

    :param enable_color_scheme: Enable color-scheme CSS property to use theme.palette.mode. For more details, check out https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme For browser support, check out https://caniuse.com/?search=color-scheme (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-scoped-css-baseline", children, **kwargs)
        self.props += [
            ("enable_color_scheme", "enableColorScheme"),
        ]


class Select(MuiHtmlElement):
    """MUI Select - https://mui.com/material-ui/api/select/

    :param icon_component: The icon that displays the arrow. (default: ArrowDropDownIcon) (``elementType``)
    :param menu_props: Props applied to the Menu element. (``object``)
    :param select_display_props: Props applied to the clickable div element. (``object``)
    :param auto_width: If true, the width of the popover will automatically be set according to the items inside the menu, otherwise it will be at least the width of the select input. (default: false) (``bool``)
    :param default_open: If true, the component is initially open. Use when the component open state is not controlled (i.e. the open prop is not defined). You can only use it when the native prop is false (default). (default: false) (``bool``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param display_empty: If true, a value is displayed even if no items are selected. In order to display a meaningful value, a function can be passed to the renderValue prop which returns the value to be displayed when no items are selected. ⚠️ When using this prop, make sure the label doesn't overlap with the empty displayed value. The label should either be hidden or forced to a shrunk state. (default: false) (``bool``)
    :param id: The id of the wrapper element or the select element when native. (``string``)
    :param input: An Input element; does not have to be a material-ui specific Input. (``element``)
    :param input_props: Attributes applied to the input element. When native is true, the attributes are applied on the select element. (``object``)
    :param label: See OutlinedInput#label (``node``)
    :param label_id: The ID of an element that acts as an additional label. The Select will be labelled by the additional label and the selected value. (``string``)
    :param multiple: If true, value must be an array and the menu will support multiple selections. (default: false) (``bool``)
    :param native: If true, the component uses a native select element. (default: false) (``bool``)
    :param on_change: Callback fired when a menu item is selected. (``func``)
    :param on_close: Callback fired when the component requests to be closed. Use it in either controlled (see the open prop), or uncontrolled mode (to detect when the Select collapses). (``func``)
    :param on_open: Callback fired when the component requests to be opened. Use it in either controlled (see the open prop), or uncontrolled mode (to detect when the Select expands). (``func``)
    :param open: If true, the component is shown. You can only use it when the native prop is false (default). (``bool``)
    :param render_value: Render the selected value. You can only use it when the native prop is false (default). (``func``)
    :param value: The input value. Providing an empty string will select no options. Set to an empty string '' if you don't want any of the available options to be selected. If the value is an object it must have reference equality with the option in order to be selected. If the value is not an object, the string representation must match with the string representation of the option in order to be selected. (``'' | any``)
    :param variant: The variant to use. (default: 'outlined') (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-select", children, **kwargs)
        self.props += [
            ("icon_component", "IconComponent"),
            ("menu_props", "MenuProps"),
            ("select_display_props", "SelectDisplayProps"),
            ("auto_width", "autoWidth"),
            ("default_open", "defaultOpen"),
            ("default_value", "defaultValue"),
            ("display_empty", "displayEmpty"),
            "id",
            "input",
            ("input_props", "inputProps"),
            "label",
            ("label_id", "labelId"),
            "multiple",
            "native",
            ("on_change", "onChange"),
            ("on_close", "onClose"),
            ("on_open", "onOpen"),
            "open",
            ("render_value", "renderValue"),
            "value",
            "variant",
        ]
        self.literal_children = True


class Skeleton(MuiHtmlElement):
    """MUI Skeleton - https://mui.com/material-ui/api/skeleton/

    :param animation: The animation. If false the animation effect is disabled. (default: 'pulse') (``'pulse' | 'wave' | false``)
    :param height: Height of the skeleton. Useful when you don't want to adapt the skeleton to a text element but for instance a card. (``number | string``)
    :param variant: The type of content that will be rendered. (default: 'text') (``'circular' | 'rectangular' | 'rounded' | 'text' | string``)
    :param width: Width of the skeleton. Useful when the skeleton is inside an inline element with no width of its own. (``number | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-skeleton", children, **kwargs)
        self.props += [
            "animation",
            "height",
            "variant",
            "width",
        ]


class Slide(MuiHtmlElement):
    """MUI Slide - https://mui.com/material-ui/api/slide/

        The Slide transition is used by the [Drawer](/material-ui/react-drawer/) component.

        :param add_end_listener: Add a custom transition end trigger. Use it when you need custom logic to decide when the transition has ended. Note: Timeouts are still used as a fallback if provided. (``func``)
        :param appear: Perform the enter transition when it first mounts if in is also true. Set this to false to disable this behavior. (default: true) (``bool``)
        :param container: An HTML element, or a function that returns one. It's used to set the container the Slide is transitioning from. (``HTML element | func``)
        :param direction: Direction the child node will enter from. (default: 'down') (``'down' | 'left' | 'right' | 'up'``)
        :param disable_prefers_reduced_motion: If true, the transition ignores theme.motion.reducedMotion and keeps its normal timing. (default: false) (``bool``)
        :param easing: The transition timing function. You may specify a single easing or a object containing enter and exit values. (default: {
      enter: theme.transitions.easing.easeOut,
      exit: theme.transitions.easing.sharp,
    }) (``{ enter?: string, exit?: string } | string``)
        :param in: If true, the component will transition in. (``bool``)
        :param timeout: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-slide", children, **kwargs)
        self.props += [
            ("add_end_listener", "addEndListener"),
            "appear",
            "container",
            "direction",
            ("disable_prefers_reduced_motion", "disablePrefersReducedMotion"),
            "easing",
            "in",
            "timeout",
        ]


class Slider(MuiHtmlElement):
    """MUI Slider - https://mui.com/material-ui/api/slider/

        :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' | string``)
        :param default_value: The default value. Use when the component is not controlled. (``Array<number> | number``)
        :param disable_swap: If true, the active thumb doesn't swap when moving pointer over a thumb while dragging another thumb. (default: false) (``bool``)
        :param disabled: If true, the component is disabled. (default: false) (``bool``)
        :param get_aria_label: Accepts a function which returns a string value that provides a user-friendly name for the thumb labels of the slider. This is important for screen reader users. (``func``)
        :param get_aria_value_text: Accepts a function which returns a string value that provides a user-friendly name for the current value of the slider. This is important for screen reader users. (``func``)
        :param marks: Marks indicate predetermined values to which the user can move the slider. If true the marks are spaced according the value of the step prop. If an array, it should contain objects with value and an optional label keys. (default: false) (``Array<{ label?: node, value: number }> | bool``)
        :param max: The maximum allowed value of the slider. Should not be equal to min. (default: 100) (``number``)
        :param min: The minimum allowed value of the slider. Should not be equal to max. (default: 0) (``number``)
        :param name: Name attribute of the hidden input element. (``string``)
        :param on_change: Callback function that is fired when the slider's value changed. (``func``)
        :param on_change_committed: Callback function that is fired when the pointer or touch interaction ends. (``func``)
        :param orientation: The component orientation. (default: 'horizontal') (``'horizontal' | 'vertical'``)
        :param scale: A transformation function, to change the scale of the slider. (default: function Identity(x) {
      return x;
    }) (``func``)
        :param shift_step: The granularity with which the slider can step through values when using Page Up/Page Down or Shift + Arrow Up/Arrow Down. (default: 10) (``number``)
        :param size: The size of the slider. (default: 'medium') (``'small' | 'medium' | string``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ input?: func | object, mark?: func | object, markLabel?: func | object, ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, mark?: elementType, markLabel?: elementType, rail?: ...``)
        :param step: The granularity with which the slider can step through values. (A "discrete" slider.) The min prop serves as the origin for the valid values. We recommend (max - min) to be evenly divisible by the step. When step is null, the thumb can only be slid onto marks provided with the marks prop. (default: 1) (``number``)
        :param tab_index: Tab index attribute of the hidden input element. (``number``)
        :param track: The track presentation: normal the track will render a bar representing the slider value. inverted the track will render a bar representing the remaining slider value. false the track will render without a bar. (default: 'normal') (``'inverted' | 'normal' | false``)
        :param value: The value of the slider. For ranged sliders, provide an array with two values. (``Array<number> | number``)
        :param value_label_display: Controls when the value label is displayed: auto the value label will display when the thumb is hovered or focused. on will display persistently. off will never display. (default: 'off') (``'auto' | 'off' | 'on'``)
        :param value_label_format: The format function the value label's value. When a function is provided, it should have the following signature: - {number} value The value label's value to format - {number} index The value label's index to format (default: function Identity(x) {
      return x;
    }) (``func | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-slider", children, **kwargs)
        self.props += [
            "color",
            ("default_value", "defaultValue"),
            ("disable_swap", "disableSwap"),
            "disabled",
            ("get_aria_label", "getAriaLabel"),
            ("get_aria_value_text", "getAriaValueText"),
            "marks",
            "max",
            "min",
            "name",
            ("on_change", "onChange"),
            ("on_change_committed", "onChangeCommitted"),
            "orientation",
            "scale",
            ("shift_step", "shiftStep"),
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "step",
            ("tab_index", "tabIndex"),
            "track",
            "value",
            ("value_label_display", "valueLabelDisplay"),
            ("value_label_format", "valueLabelFormat"),
        ]


class Snackbar(MuiHtmlElement):
    """MUI Snackbar - https://mui.com/material-ui/api/snackbar/

        :param action: The action to display. It renders after the message, at the end of the snackbar. (``node``)
        :param anchor_origin: The anchor of the Snackbar. On smaller screens, the component grows to occupy all the available width, the horizontal alignment is ignored. (default: { vertical: 'bottom', horizontal: 'left' }) (``{ horizontal: 'center' | 'left' | 'right', vertical: 'bottom' | 'top' }``)
        :param auto_hide_duration: The number of milliseconds to wait before automatically calling the onClose function. onClose should then set the state of the open prop to hide the Snackbar. This behavior is disabled by default with the null value. (default: null) (``number``)
        :param disable_window_blur_listener: If true, the autoHideDuration timer will expire even if the window is not focused. (default: false) (``bool``)
        :param message: The message to display. (``node``)
        :param on_close: Callback fired when the component requests to be closed. Typically onClose is used to set state in the parent component, which is used to control the Snackbar open prop. The reason parameter can optionally be used to control the response to onClose, for example ignoring clickaway. (``func``)
        :param open: If true, the component is shown. (``bool``)
        :param resume_hide_duration: The number of milliseconds to wait before dismissing after user interaction. If autoHideDuration prop isn't specified, it does nothing. If autoHideDuration prop is specified but resumeHideDuration isn't, we default to autoHideDuration / 2 ms. (``number``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ clickAwayListener?: func | object, content?: func | object, root?: func | ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ clickAwayListener?: elementType, content?: elementType, root?: elementType, ...``)
        :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-snackbar", children, **kwargs)
        self.props += [
            "action",
            ("anchor_origin", "anchorOrigin"),
            ("auto_hide_duration", "autoHideDuration"),
            ("disable_window_blur_listener", "disableWindowBlurListener"),
            "message",
            ("on_close", "onClose"),
            "open",
            ("resume_hide_duration", "resumeHideDuration"),
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
        ]


class SnackbarContent(MuiHtmlElement):
    """MUI SnackbarContent - https://mui.com/material-ui/api/snackbar-content/

    :param action: The action to display. It renders after the message, at the end of the snackbar. (``node``)
    :param message: The message to display. (``node``)
    :param role: The ARIA role attribute of the element. (default: 'alert') (``string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-snackbar-content", children, **kwargs)
        self.props += [
            "action",
            "message",
            "role",
        ]


class SpeedDial(MuiHtmlElement):
    """MUI SpeedDial - https://mui.com/material-ui/api/speed-dial/

        :param fab_props: Props applied to the Fab element. (default: {}) (``object``)
        :param aria_label: The aria-label of the button element. Also used to provide the id for the SpeedDial element and its children. (``string``)
        :param direction: The direction the actions open relative to the floating action button. (default: 'up') (``'down' | 'left' | 'right' | 'up'``)
        :param hidden: If true, the SpeedDial is hidden. (default: false) (``bool``)
        :param icon: The icon to display in the SpeedDial Fab. The SpeedDialIcon component provides a default Icon with animation. (``node``)
        :param on_close: Callback fired when the component requests to be closed. (``func``)
        :param on_open: Callback fired when the component requests to be open. (``func``)
        :param open: If true, the component is shown. (``bool``)
        :param open_icon: The icon to display in the SpeedDial Fab when the SpeedDial is open. (``node``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ root?: func | object, transition?: func | object }``)
        :param slots: The components used for each slot inside. (default: {}) (``{ root?: elementType, transition?: elementType }``)
        :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-speed-dial", children, **kwargs)
        self.props += [
            ("fab_props", "FabProps"),
            ("aria_label", "ariaLabel"),
            "direction",
            "hidden",
            "icon",
            ("on_close", "onClose"),
            ("on_open", "onOpen"),
            "open",
            ("open_icon", "openIcon"),
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
        ]
        self.literal_children = True


class SpeedDialAction(MuiHtmlElement):
    """MUI SpeedDialAction - https://mui.com/material-ui/api/speed-dial-action/

    :param delay: Adds a transition delay, to allow a series of SpeedDialActions to be animated. (default: 0) (``number``)
    :param icon: The icon to display in the SpeedDial Fab. (``node``)
    :param id: This prop is used to help implement the accessibility logic. If you don't provide this prop. It falls back to a randomly generated id. (``string``)
    :param open: If true, the component is shown. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ fab?: func | object, staticTooltip?: func | object, staticTooltipLabel?: func ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ fab?: elementType, staticTooltip?: elementType, staticTooltipLabel?: ...``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-speed-dial-action", children, **kwargs)
        self.props += [
            "delay",
            "icon",
            "id",
            "open",
            ("slot_props", "slotProps"),
            "slots",
        ]


class SpeedDialIcon(MuiHtmlElement):
    """MUI SpeedDialIcon - https://mui.com/material-ui/api/speed-dial-icon/

    :param icon: The icon to display. (``node``)
    :param open_icon: The icon to display in the SpeedDial Floating Action Button when the SpeedDial is open. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-speed-dial-icon", children, **kwargs)
        self.props += [
            "icon",
            ("open_icon", "openIcon"),
        ]


class Stack(MuiHtmlElement):
    """MUI Stack - https://mui.com/material-ui/api/stack/

    :param direction: Defines the flex-direction style property. It is applied for all screen sizes. (default: 'column') (``'column-reverse' | 'column' | 'row-reverse' | 'row' | Array<'column-reverse' | ...``)
    :param divider: Add an element between each child. (``node``)
    :param spacing: Defines the space between immediate children. (default: 0) (``Array<number | string> | number | object | string``)
    :param use_flex_gap: If true, the CSS flexbox gap is used instead of applying margin to children. While CSS gap removes the known limitations, it is not fully supported in some browsers. We recommend checking https://caniuse.com/?search=flex%20gap before using this flag. To enable this flag globally, follow the theme's default props configuration. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-stack", children, **kwargs)
        self.props += [
            "direction",
            "divider",
            "spacing",
            ("use_flex_gap", "useFlexGap"),
        ]


class Step(MuiHtmlElement):
    """MUI Step - https://mui.com/material-ui/api/step/

    :param active: Sets the step as active. Is passed to child components. (``bool``)
    :param completed: Mark the step as completed. Is passed to child components. (``bool``)
    :param disabled: If true, the step is disabled, will also disable the button if StepButton is a child of Step. Is passed to child components. (``bool``)
    :param expanded: Expand the step. (default: false) (``bool``)
    :param index: The position of the step. The prop defaults to the value inherited from the parent Stepper component. (``integer``)
    :param last: If true, the Step is displayed as rendered last. The prop defaults to the value inherited from the parent Stepper component. (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step", children, **kwargs)
        self.props += [
            "active",
            "completed",
            "disabled",
            "expanded",
            "index",
            "last",
        ]


class StepButton(MuiHtmlElement):
    """MUI StepButton - https://mui.com/material-ui/api/step-button/

    :param icon: The icon displayed by the step label. (``node``)
    :param optional: The optional node to display. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step-button", children, **kwargs)
        self.props += [
            "icon",
            "optional",
        ]


class StepConnector(MuiHtmlElement):
    """MUI StepConnector - https://mui.com/material-ui/api/step-connector/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step-connector", children, **kwargs)


class StepContent(MuiHtmlElement):
    """MUI StepContent - https://mui.com/material-ui/api/step-content/

    :param slot_props: The props used for each slot inside. (default: {}) (``{ transition?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ transition?: elementType }``)
    :param transition_duration: Adjust the duration of the content expand transition. Passed as a prop to the transition component. Set to 'auto' to automatically calculate transition time based on height. (default: 'auto') (``'auto' | number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step-content", children, **kwargs)
        self.props += [
            ("slot_props", "slotProps"),
            "slots",
            ("transition_duration", "transitionDuration"),
        ]


class StepIcon(MuiHtmlElement):
    """MUI StepIcon - https://mui.com/material-ui/api/step-icon/

    :param active: Whether this step is active. (default: false) (``bool``)
    :param completed: Mark the step as completed. Is passed to child components. (default: false) (``bool``)
    :param error: If true, the step is marked as failed. (default: false) (``bool``)
    :param icon: The label displayed in the step icon. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step-icon", children, **kwargs)
        self.props += [
            "active",
            "completed",
            "error",
            "icon",
        ]


class StepLabel(MuiHtmlElement):
    """MUI StepLabel - https://mui.com/material-ui/api/step-label/

    :param error: If true, the step is marked as failed. (default: false) (``bool``)
    :param icon: Override the default label of the step icon. (``node``)
    :param optional: The optional node to display. (``node``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ label?: func | object, root?: func | object, stepIcon?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ label?: elementType, root?: elementType, stepIcon?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-step-label", children, **kwargs)
        self.props += [
            "error",
            "icon",
            "optional",
            ("slot_props", "slotProps"),
            "slots",
        ]


class Stepper(MuiHtmlElement):
    """MUI Stepper - https://mui.com/material-ui/api/stepper/

    :param active_step: Set the active step (zero based index). Set to -1 to disable all the steps. (default: 0) (``integer``)
    :param alternative_label: If set to 'true' and orientation is horizontal, then the step label will be positioned under the icon. If set to 'true' and orientation is vertical, it reverses the position of the label and content. (default: false) (``bool``)
    :param connector: An element to be placed between each step. (default: <StepConnector />) (``element``)
    :param non_linear: If set the Stepper will not assist in controlling steps for linear flow. (default: false) (``bool``)
    :param orientation: The component orientation (layout flow direction). (default: 'horizontal') (``'horizontal' | 'vertical'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-stepper", children, **kwargs)
        self.props += [
            ("active_step", "activeStep"),
            ("alternative_label", "alternativeLabel"),
            "connector",
            ("non_linear", "nonLinear"),
            "orientation",
        ]
        self.literal_children = True


class SvgIcon(MuiHtmlElement):
    """MUI SvgIcon - https://mui.com/material-ui/api/svg-icon/

    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. You can use the htmlColor prop to apply a color attribute to the SVG element. (default: 'inherit') (``'inherit' | 'action' | 'disabled' | 'primary' | 'secondary' | 'error' | 'info' ...``)
    :param font_size: The fontSize applied to the icon. Defaults to 24px, but can be configure to inherit font size. (default: 'medium') (``'inherit' | 'large' | 'medium' | 'small' | string``)
    :param html_color: Applies a color attribute to the SVG element. (``string``)
    :param inherit_view_box: If true, the root node will inherit the custom component's viewBox and the viewBox prop will be ignored. Useful when you want to reference a custom component and have SvgIcon pass that component's viewBox to the root node. (default: false) (``bool``)
    :param shape_rendering: The shape-rendering attribute. The behavior of the different options is described on the MDN Web Docs. If you are having issues with blurry icons you should investigate this prop. (``string``)
    :param title_access: Provides a human-readable title for the element that contains it. https://www.w3.org/TR/SVG-access/#Equivalent (``string``)
    :param view_box: Allows you to redefine what the coordinates without units mean inside an SVG element. For example, if the SVG element is 500 (width) by 200 (height), and you pass viewBox="0 0 50 20", this means that the coordinates inside the SVG will go from the top left corner (0,0) to bottom right (50,20) and each unit will be worth 10px. (default: '0 0 24 24') (``string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-svg-icon", children, **kwargs)
        self.props += [
            "color",
            ("font_size", "fontSize"),
            ("html_color", "htmlColor"),
            ("inherit_view_box", "inheritViewBox"),
            ("shape_rendering", "shapeRendering"),
            ("title_access", "titleAccess"),
            ("view_box", "viewBox"),
        ]


class SwipeableDrawer(MuiHtmlElement):
    """MUI SwipeableDrawer - https://mui.com/material-ui/api/swipeable-drawer/

        :param allow_swipe_in_children: If set to true, the swipe event will open the drawer even if the user begins the swipe on one of the drawer's children. This can be useful in scenarios where the drawer is partially visible. You can customize it further with a callback that determines which children the user can drag over to open the drawer (for example, to ignore other elements that handle touch move events, like sliders). (default: false) (``func | bool``)
        :param disable_backdrop_transition: Disable the backdrop transition. This can improve the FPS on low-end devices. (default: false) (``bool``)
        :param disable_discovery: If true, touching the screen near the edge of the drawer will not slide in the drawer a bit to promote accidental discovery of the swipe gesture. (default: false) (``bool``)
        :param disable_swipe_to_open: If true, swipe to open is disabled. This is useful in browsers where swiping triggers navigation actions. Swipe to open is disabled on iOS browsers by default. (default: typeof navigator !== 'undefined' && /iPad|iPhone|iPod/.test(navigator.userAgent)) (``bool``)
        :param hysteresis: Affects how far the drawer must be opened/closed to change its state. Specified as percent (0-1) of the width of the drawer (default: 0.52) (``number``)
        :param min_fling_velocity: Defines, from which (average) velocity on, the swipe is defined as complete although hysteresis isn't reached. Good threshold is between 250 - 1000 px/s (default: 450) (``number``)
        :param on_close: Callback fired when the component requests to be closed. (``func``)
        :param on_open: Callback fired when the component requests to be opened. (``func``)
        :param open: If true, the component is shown. (default: false) (``bool``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ backdrop?: func | object, docked?: func | object, paper?: func | object, ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ backdrop?: elementType, docked?: elementType, paper?: elementType, root?: ...``)
        :param swipe_area_width: The width of the left most (or right most) area in px that the drawer can be swiped open from. (default: 20) (``number``)
        :param transition_duration: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-swipeable-drawer", children, **kwargs)
        self.props += [
            ("allow_swipe_in_children", "allowSwipeInChildren"),
            ("disable_backdrop_transition", "disableBackdropTransition"),
            ("disable_discovery", "disableDiscovery"),
            ("disable_swipe_to_open", "disableSwipeToOpen"),
            "hysteresis",
            ("min_fling_velocity", "minFlingVelocity"),
            ("on_close", "onClose"),
            ("on_open", "onOpen"),
            "open",
            ("slot_props", "slotProps"),
            "slots",
            ("swipe_area_width", "swipeAreaWidth"),
            ("transition_duration", "transitionDuration"),
        ]


class Switch(MuiHtmlElement):
    """MUI Switch - https://mui.com/material-ui/api/switch/

    :param checked: If true, the component is checked. (``bool``)
    :param checked_icon: The icon to display when the component is checked. (``node``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'default' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param default_checked: The default checked state. Use when the component is not controlled. (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (``bool``)
    :param edge: If given, uses a negative margin to counteract the padding on one side (this is often helpful for aligning the left or right side of the icon with content above or below, without ruining the border size and shape). (default: false) (``'end' | 'start' | false``)
    :param icon: The icon to display when the component is unchecked. (``node``)
    :param id: The id of the input element. (``string``)
    :param on_change: Callback fired when the state is changed. (``func``)
    :param required: If true, the input element is required. (default: false) (``bool``)
    :param size: The size of the component. small is equivalent to the dense switch styling. (default: 'medium') (``'medium' | 'small' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ input?: func | object, root?: func | object, switchBase?: func | object, ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ input?: elementType, root?: elementType, switchBase?: elementType, thumb?: ...``)
    :param value: The value of the component. The DOM API casts this to a string. The browser uses "on" as the default value. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-switch", children, **kwargs)
        self.props += [
            "checked",
            ("checked_icon", "checkedIcon"),
            "color",
            ("default_checked", "defaultChecked"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            "edge",
            "icon",
            "id",
            ("on_change", "onChange"),
            "required",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "value",
        ]


class Tab(MuiHtmlElement):
    """MUI Tab - https://mui.com/material-ui/api/tab/

    :param disable_focus_ripple: If true, the keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. ⚠️ Without a ripple there is no styling for :focus-visible by default. Be sure to highlight the element by applying separate styles with the .Mui-focusVisible class. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param icon: The icon to display. (``element | string``)
    :param icon_position: The position of the icon relative to the label. (default: 'top') (``'bottom' | 'end' | 'start' | 'top'``)
    :param label: The label element. (``node``)
    :param value: You can provide your own value. Otherwise, we fallback to the child position index. (``any``)
    :param wrapped: Tab labels appear in a single row. They can use a second line if needed. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-tab", children, **kwargs)
        self.props += [
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            "icon",
            ("icon_position", "iconPosition"),
            "label",
            "value",
            "wrapped",
        ]


class TabScrollButton(MuiHtmlElement):
    """MUI TabScrollButton - https://mui.com/material-ui/api/tab-scroll-button/

    :param direction: The direction the button should indicate. (``'left' | 'right'``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param orientation: The component orientation (layout flow direction). (``'horizontal' | 'vertical'``)
    :param slot_props: The extra props for the slot components. You can override the existing props or add new ones. (default: {}) (``{ endScrollButtonIcon?: func | object, startScrollButtonIcon?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ EndScrollButtonIcon?: elementType, StartScrollButtonIcon?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-tab-scroll-button", children, **kwargs)
        self.props += [
            "direction",
            "disabled",
            "orientation",
            ("slot_props", "slotProps"),
            "slots",
        ]


class Table(MuiHtmlElement):
    """MUI Table - https://mui.com/material-ui/api/table/

    :param padding: Allows TableCells to inherit padding of the Table. (default: 'normal') (``'checkbox' | 'none' | 'normal'``)
    :param size: Allows TableCells to inherit size of the Table. (default: 'medium') (``'medium' | 'small' | string``)
    :param sticky_header: Set the header sticky. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table", children, **kwargs)
        self.props += [
            "padding",
            "size",
            ("sticky_header", "stickyHeader"),
        ]


class TableBody(MuiHtmlElement):
    """MUI TableBody - https://mui.com/material-ui/api/table-body/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-body", children, **kwargs)


class TableCell(MuiHtmlElement):
    """MUI TableCell - https://mui.com/material-ui/api/table-cell/

    The component renders a `` element when the parent context is a header or otherwise a `` element.

    :param align: Set the text-align on the table cell content. Monetary or generally number fields should be right aligned as that allows you to add them up quickly in your head without having to worry about decimals. (default: 'inherit') (``'center' | 'inherit' | 'justify' | 'left' | 'right'``)
    :param padding: Sets the padding applied to the cell. The prop defaults to the value ('default') inherited from the parent Table component. (``'checkbox' | 'none' | 'normal'``)
    :param scope: Set scope attribute. (``string``)
    :param size: Specify the size of the cell. The prop defaults to the value ('medium') inherited from the parent Table component. (``'medium' | 'small' | string``)
    :param sort_direction: Set aria-sort direction. (``'asc' | 'desc' | false``)
    :param variant: Specify the cell type. The prop defaults to the value inherited from the parent TableHead, TableBody, or TableFooter components. (``'body' | 'footer' | 'head' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-cell", children, **kwargs)
        self.props += [
            "align",
            "padding",
            "scope",
            "size",
            ("sort_direction", "sortDirection"),
            "variant",
        ]


class TableContainer(MuiHtmlElement):
    """MUI TableContainer - https://mui.com/material-ui/api/table-container/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-container", children, **kwargs)


class TableFooter(MuiHtmlElement):
    """MUI TableFooter - https://mui.com/material-ui/api/table-footer/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-footer", children, **kwargs)


class TableHead(MuiHtmlElement):
    """MUI TableHead - https://mui.com/material-ui/api/table-head/"""

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-head", children, **kwargs)


class TablePagination(MuiHtmlElement):
    """MUI TablePagination - https://mui.com/material-ui/api/table-pagination/

        A `TableCell` based component for placing inside `TableFooter` for pagination.

        :param actions_component: The component used for displaying the actions. Either a string to use a HTML element or a component. (default: TablePaginationActions) (``elementType``)
        :param count: The total number of rows. To enable server side pagination for an unknown number of items, provide -1. (``integer``)
        :param disabled: If true, the component is disabled. (default: false) (``bool``)
        :param get_item_aria_label: Accepts a function which returns a string value that provides a user-friendly name for the current page. This is important for screen reader users. For localization purposes, you can use the provided translations. (default: function defaultGetAriaLabel(type) {
      return `Go to ${type} page`;
    }) (``func``)
        :param label_displayed_rows: Customize the displayed rows label. Invoked with a { from, to, count, page } object. For localization purposes, you can use the provided translations. (default: function defaultLabelDisplayedRows({ from, to, count }) {
      return `${formatNumber(from)}–${formatNumber(to)} of ${count !== -1 ? formatNumber(count) : `more than ${formatNumber(to)}`}`;
    }) (``func``)
        :param label_rows_per_page: Customize the rows per page label. For localization purposes, you can use the provided translations. (default: 'Rows per page:') (``node``)
        :param on_page_change: Callback fired when the page is changed. (``func``)
        :param on_rows_per_page_change: Callback fired when the number of rows per page is changed. (``func``)
        :param page: The zero-based index of the current page. (``integer``)
        :param rows_per_page: The number of rows per page. Set -1 to display all the rows. (``integer``)
        :param rows_per_page_options: Customizes the options of the rows per page select field. If less than two options are available, no select field will be displayed. Use -1 for the value with a custom label to show all the rows. (default: [10, 25, 50, 100]) (``Array<number | { label: string, value: number }>``)
        :param show_first_button: If true, show the first-page button. (default: false) (``bool``)
        :param show_last_button: If true, show the last-page button. (default: false) (``bool``)
        :param slot_props: The props used for each slot inside. (default: {}) (``{ actions?: { firstButton?: object, firstButtonIcon?: object, lastButton?: ...``)
        :param slots: The components used for each slot inside. (default: {}) (``{ actions?: { firstButton?: elementType, firstButtonIcon?: elementType, ...``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-pagination", children, **kwargs)
        self.props += [
            ("actions_component", "ActionsComponent"),
            "count",
            "disabled",
            ("get_item_aria_label", "getItemAriaLabel"),
            ("label_displayed_rows", "labelDisplayedRows"),
            ("label_rows_per_page", "labelRowsPerPage"),
            ("on_page_change", "onPageChange"),
            ("on_rows_per_page_change", "onRowsPerPageChange"),
            "page",
            ("rows_per_page", "rowsPerPage"),
            ("rows_per_page_options", "rowsPerPageOptions"),
            ("show_first_button", "showFirstButton"),
            ("show_last_button", "showLastButton"),
            ("slot_props", "slotProps"),
            "slots",
        ]


class TablePaginationActions(MuiHtmlElement):
    """MUI TablePaginationActions - https://mui.com/material-ui/api/table-pagination-actions/

    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param get_item_aria_label: Accepts a function which returns a string value that provides a user-friendly name for the current page. This is important for screen reader users. For localization purposes, you can use the provided translations. (``func``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-pagination-actions", children, **kwargs)
        self.props += [
            "disabled",
            ("get_item_aria_label", "getItemAriaLabel"),
        ]


class TableRow(MuiHtmlElement):
    """MUI TableRow - https://mui.com/material-ui/api/table-row/

    Will automatically set dynamic row height based on the material table element parent (head, body, etc).

    :param hover: If true, the table row will shade on hover. (default: false) (``bool``)
    :param selected: If true, the table row will have the selected shading. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-row", children, **kwargs)
        self.props += [
            "hover",
            "selected",
        ]


class TableSortLabel(MuiHtmlElement):
    """MUI TableSortLabel - https://mui.com/material-ui/api/table-sort-label/

    A button based label for placing inside `TableCell` for column sorting.

    :param icon_component: Sort icon to use. (default: ArrowDownwardIcon) (``elementType``)
    :param active: If true, the label will have the active styling (should be true for the sorted column). (default: false) (``bool``)
    :param direction: The current sort direction. (default: 'asc') (``'asc' | 'desc'``)
    :param hide_sort_icon: Hide sort icon when active is false. (default: false) (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ icon?: func | object, root?: func | object }``)
    :param slots: The components used for each slot inside. (default: {}) (``{ icon?: elementType, root?: elementType }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-table-sort-label", children, **kwargs)
        self.props += [
            ("icon_component", "IconComponent"),
            "active",
            "direction",
            ("hide_sort_icon", "hideSortIcon"),
            ("slot_props", "slotProps"),
            "slots",
        ]


class Tabs(MuiHtmlElement):
    """MUI Tabs - https://mui.com/material-ui/api/tabs/

    :param action: Callback fired when the component mounts. This is useful when you want to trigger an action programmatically. It supports two actions: updateIndicator() and updateScrollButtons() (``ref``)
    :param allow_scroll_buttons_mobile: If true, the scroll buttons aren't forced hidden on mobile. By default the scroll buttons are hidden on mobile and takes precedence over scrollButtons. (default: false) (``bool``)
    :param centered: If true, the tabs are centered. This prop is intended for large views. (default: false) (``bool``)
    :param indicator_color: Determines the color of the indicator. (default: 'primary') (``'primary' | 'secondary' | string``)
    :param on_change: Callback fired when the value changes. (``func``)
    :param orientation: The component orientation (layout flow direction). (default: 'horizontal') (``'horizontal' | 'vertical'``)
    :param scroll_buttons: Determine behavior of scroll buttons when tabs are set to scroll: auto will only present them when not all the items are visible. true will always present them. false will never present them. By default the scroll buttons are hidden on mobile. This behavior can be disabled with allowScrollButtonsMobile. (default: 'auto') (``'auto' | false | true``)
    :param selection_follows_focus: If true the selected tab changes on focus. Otherwise it only changes on activation. (``bool``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ endScrollButtonIcon?: func | object, indicator?: func | object, list?: func | ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ endScrollButtonIcon?: elementType, indicator?: elementType, list?: ...``)
    :param text_color: Determines the color of the Tab. (default: 'primary') (``'inherit' | 'primary' | 'secondary'``)
    :param value: The value of the currently selected Tab. If you don't want any selected Tab, you can set this prop to false. (``any``)
    :param variant: Determines additional display behavior of the tabs: scrollable will invoke scrolling properties and allow for horizontally scrolling (or swiping) of the tab bar. fullWidth will make the tabs grow to use all the available space, which should be used for small views, like on mobile. standard will render the default state. (default: 'standard') (``'fullWidth' | 'scrollable' | 'standard'``)
    :param visible_scrollbar: If true, the scrollbar is visible. It can be useful when displaying a long vertical list of tabs. (default: false) (``bool``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-tabs", children, **kwargs)
        self.props += [
            "action",
            ("allow_scroll_buttons_mobile", "allowScrollButtonsMobile"),
            "centered",
            ("indicator_color", "indicatorColor"),
            ("on_change", "onChange"),
            "orientation",
            ("scroll_buttons", "scrollButtons"),
            ("selection_follows_focus", "selectionFollowsFocus"),
            ("slot_props", "slotProps"),
            "slots",
            ("text_color", "textColor"),
            "value",
            "variant",
            ("visible_scrollbar", "visibleScrollbar"),
        ]
        self.literal_children = True


class TextField(MuiHtmlElement):
    """MUI TextField - https://mui.com/material-ui/api/text-field/

    The `TextField` is a convenience wrapper for the most common cases (80%). It cannot be all things to all people, otherwise the API would grow out of control. ## Advanced Configuration It's important to understand that the text field is a simple abstraction on top of the following components: - [FormControl](/material-ui/api/form-control/) - [InputLabel](/material-ui/api/input-label/) - [FilledInput](/material-ui/api/filled-input/) - [OutlinedInput](/material-ui/api/outlined-input/) - [Input](/material-ui/api/input/) - [FormHelperText](/material-ui/api/form-helper-text/) If you wish to alter the props applied to the `input` element, you can do so as follows: ```jsx const slotProps = { htmlInput: { step: 300 } }; return ; ``` For advanced cases, please look at the source of TextField by clicking on the "Edit this page" button above. Consider either: - using the `slotProps` prop for passing values directly to the components - using the underlying components directly as shown in the demos

    :param auto_complete: This prop helps users to fill forms faster, especially on mobile devices. The name can be confusing, as it's more like an autofill. You can learn more about it following the specification. (``string``)
    :param auto_focus: If true, the input element is focused during the first mount. (default: false) (``bool``)
    :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'primary') (``'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' | string``)
    :param default_value: The default value. Use when the component is not controlled. (``any``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param error: If true, the label is displayed in an error state. (default: false) (``bool``)
    :param full_width: If true, the input will take up the full width of its container. (default: false) (``bool``)
    :param helper_text: The helper text content. (``node``)
    :param id: The id of the input element. Use this prop to make label and helperText accessible for screen readers. (``string``)
    :param input_ref: Pass a ref to the input element. (``ref``)
    :param label: The label content. (``node``)
    :param margin: If dense or normal, will adjust vertical spacing of this and contained components. (default: 'none') (``'dense' | 'none' | 'normal'``)
    :param max_rows: Maximum number of rows to display when multiline option is set to true. (``number | string``)
    :param min_rows: Minimum number of rows to display when multiline option is set to true. (``number | string``)
    :param multiline: If true, a textarea element is rendered instead of an input. (default: false) (``bool``)
    :param name: Name attribute of the input element. (``string``)
    :param on_change: Callback fired when the value is changed. (``func``)
    :param placeholder: The short hint displayed in the input before the user enters a value. (``string``)
    :param required: If true, the label is displayed as required and the input element is required. (default: false) (``bool``)
    :param rows: Number of rows to display when multiline option is set to true. (``number | string``)
    :param select: Render a Select element while passing the Input element to Select as input parameter. If this option is set you must pass the options of the select as children. (default: false) (``bool``)
    :param size: The size of the component. (default: 'medium') (``'medium' | 'small' | string``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ formHelperText?: func | object, htmlInput?: func | object, input?: func | ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ formHelperText?: elementType, htmlInput?: elementType, input?: elementType, ...``)
    :param type: Type of the input element. It should be a valid HTML5 input type. (``string``)
    :param value: The value of the input element, required for a controlled component. (``any``)
    :param variant: The variant to use. (default: 'outlined') (``'filled' | 'outlined' | 'standard'``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-text-field", children, **kwargs)
        self.props += [
            ("auto_complete", "autoComplete"),
            ("auto_focus", "autoFocus"),
            "color",
            ("default_value", "defaultValue"),
            "disabled",
            "error",
            ("full_width", "fullWidth"),
            ("helper_text", "helperText"),
            "id",
            ("input_ref", "inputRef"),
            "label",
            "margin",
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
            "multiline",
            "name",
            ("on_change", "onChange"),
            "placeholder",
            "required",
            "rows",
            "select",
            "size",
            ("slot_props", "slotProps"),
            "slots",
            "type",
            "value",
            "variant",
        ]


class TextareaAutosize(MuiHtmlElement):
    """MUI TextareaAutosize - https://mui.com/material-ui/api/textarea-autosize/

    :param max_rows: Maximum number of rows to display. (``number | string``)
    :param min_rows: Minimum number of rows to display. (default: 1) (``number | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-textarea-autosize", children, **kwargs)
        self.props += [
            ("max_rows", "maxRows"),
            ("min_rows", "minRows"),
        ]


class ThemeProvider(MuiHtmlElement):
    """MUI ThemeProvider - https://mui.com/material-ui/customization/theming/

    Wraps its children with a MUI theme and mounts CssBaseline for consistent baseline styles. Place at the root of the UI.

    :param mode: MUI palette mode. (default: 'light') (``'light' | 'dark'``)
    :param theme: Theme options merged on top of the palette mode (forwarded to MUI's createTheme). (``object``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-theme-provider", children, **kwargs)
        self.props += [
            "mode",
            "theme",
        ]


class ToggleButton(MuiHtmlElement):
    """MUI ToggleButton - https://mui.com/material-ui/api/toggle-button/

    :param color: The color of the button when it is in an active state. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'standard') (``'standard' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param disable_focus_ripple: If true, the keyboard focus ripple is disabled. (default: false) (``bool``)
    :param disable_ripple: If true, the ripple effect is disabled. ⚠️ Without a ripple there is no styling for :focus-visible by default. Be sure to highlight the element by applying separate styles with the .Mui-focusVisible class. (default: false) (``bool``)
    :param disabled: If true, the component is disabled. (default: false) (``bool``)
    :param full_width: If true, the button will take up the full width of its container. (default: false) (``bool``)
    :param on_change: Callback fired when the state changes. (``func``)
    :param on_click: Callback fired when the button is clicked. (``func``)
    :param selected: If true, the button is rendered in an active state. (``bool``)
    :param size: The size of the component. The prop defaults to the value inherited from the parent ToggleButtonGroup component. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param value: The value to associate with the button when selected in a ToggleButtonGroup. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-toggle-button", children, **kwargs)
        self.props += [
            "color",
            ("disable_focus_ripple", "disableFocusRipple"),
            ("disable_ripple", "disableRipple"),
            "disabled",
            ("full_width", "fullWidth"),
            ("on_change", "onChange"),
            ("on_click", "onClick"),
            "selected",
            "size",
            "value",
        ]


class ToggleButtonGroup(MuiHtmlElement):
    """MUI ToggleButtonGroup - https://mui.com/material-ui/api/toggle-button-group/

    :param color: The color of the button when it is selected. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (default: 'standard') (``'standard' | 'primary' | 'secondary' | 'error' | 'info' | 'success' | 'warning' ...``)
    :param disabled: If true, the component is disabled. This implies that all ToggleButton children will be disabled. (default: false) (``bool``)
    :param exclusive: If true, only allow one of the child ToggleButton values to be selected. (default: false) (``bool``)
    :param full_width: If true, the button group will take up the full width of its container. (default: false) (``bool``)
    :param on_change: Callback fired when the value changes. (``func``)
    :param orientation: The component orientation (layout flow direction). (default: 'horizontal') (``'horizontal' | 'vertical'``)
    :param size: The size of the component. (default: 'medium') (``'small' | 'medium' | 'large' | string``)
    :param value: The currently selected value within the group or an array of selected values when exclusive is false. The value must have reference equality with the option in order to be selected. (``any``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-toggle-button-group", children, **kwargs)
        self.props += [
            "color",
            "disabled",
            "exclusive",
            ("full_width", "fullWidth"),
            ("on_change", "onChange"),
            "orientation",
            "size",
            "value",
        ]


class Toolbar(MuiHtmlElement):
    """MUI Toolbar - https://mui.com/material-ui/api/toolbar/

    :param disable_gutters: If true, disables gutter padding. (default: false) (``bool``)
    :param variant: The variant to use. (default: 'regular') (``'dense' | 'regular' | string``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-toolbar", children, **kwargs)
        self.props += [
            ("disable_gutters", "disableGutters"),
            "variant",
        ]


class Tooltip(MuiHtmlElement):
    """MUI Tooltip - https://mui.com/material-ui/api/tooltip/

    :param arrow: If true, adds an arrow to the tooltip. (default: false) (``bool``)
    :param describe_child: Set to true if the title acts as an accessible description. By default the title acts as an accessible label for the child. (default: false) (``bool``)
    :param disable_focus_listener: Do not respond to focus-visible events. (default: false) (``bool``)
    :param disable_hover_listener: Do not respond to hover events. (default: false) (``bool``)
    :param disable_interactive: Makes a tooltip not interactive, i.e. it will close when the user hovers over the tooltip before the leaveDelay is expired. (default: false) (``bool``)
    :param disable_touch_listener: Do not respond to long press touch events. (default: false) (``bool``)
    :param enter_delay: The number of milliseconds to wait before showing the tooltip. This prop won't impact the enter touch delay (enterTouchDelay). (default: 100) (``number``)
    :param enter_next_delay: The number of milliseconds to wait before showing the tooltip when one was already recently opened. (default: 0) (``number``)
    :param enter_touch_delay: The number of milliseconds a user must touch the element before showing the tooltip. (default: 700) (``number``)
    :param follow_cursor: If true, the tooltip follow the cursor over the wrapped element. (default: false) (``bool``)
    :param id: This prop is used to help implement the accessibility logic. If you don't provide this prop. It falls back to a randomly generated id. (``string``)
    :param leave_delay: The number of milliseconds to wait before hiding the tooltip. This prop won't impact the leave touch delay (leaveTouchDelay). (default: 0) (``number``)
    :param leave_touch_delay: The number of milliseconds after the user stops touching an element before hiding the tooltip. (default: 1500) (``number``)
    :param on_close: Callback fired when the component requests to be closed. (``func``)
    :param on_open: Callback fired when the component requests to be open. (``func``)
    :param open: If true, the component is shown. (``bool``)
    :param placement: Tooltip placement. (default: 'bottom') (``'auto-end' | 'auto-start' | 'auto' | 'bottom-end' | 'bottom-start' | 'bottom' | ...``)
    :param slot_props: The props used for each slot inside. (default: {}) (``{ arrow?: func | object, popper?: func | object, tooltip?: func | object, ...``)
    :param slots: The components used for each slot inside. (default: {}) (``{ arrow?: elementType, popper?: elementType, tooltip?: elementType, ...``)
    :param title: Tooltip title. Zero-length titles string, undefined, null and false are never displayed. (``node``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-tooltip", children, **kwargs)
        self.props += [
            "arrow",
            ("describe_child", "describeChild"),
            ("disable_focus_listener", "disableFocusListener"),
            ("disable_hover_listener", "disableHoverListener"),
            ("disable_interactive", "disableInteractive"),
            ("disable_touch_listener", "disableTouchListener"),
            ("enter_delay", "enterDelay"),
            ("enter_next_delay", "enterNextDelay"),
            ("enter_touch_delay", "enterTouchDelay"),
            ("follow_cursor", "followCursor"),
            "id",
            ("leave_delay", "leaveDelay"),
            ("leave_touch_delay", "leaveTouchDelay"),
            ("on_close", "onClose"),
            ("on_open", "onOpen"),
            "open",
            "placement",
            ("slot_props", "slotProps"),
            "slots",
            "title",
        ]


class Typography(MuiHtmlElement):
    """MUI Typography - https://mui.com/material-ui/api/typography/

        :param align: Set the text-align on the component. (default: 'inherit') (``'center' | 'inherit' | 'justify' | 'left' | 'right'``)
        :param color: The color of the component. It supports both default and custom theme colors, which can be added as shown in the palette customization guide. (``'primary' | 'secondary' | 'success' | 'error' | 'info' | 'warning' | ...``)
        :param gutter_bottom: If true, the text will have a bottom margin. (default: false) (``bool``)
        :param no_wrap: If true, the text will not wrap, but instead will truncate with a text overflow ellipsis. Note that text overflow can only happen with block or inline-block level elements (the element needs to have a width in order to overflow). (default: false) (``bool``)
        :param variant: Applies the theme typography styles. (default: 'body1') (``'body1' | 'body2' | 'button' | 'caption' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | ...``)
        :param variant_mapping: The component maps the variant prop to a range of different HTML element types. For instance, subtitle1 to <h6>. If you wish to change that mapping, you can provide your own. Alternatively, you can use the component prop. (default: {
      h1: 'h1',
      h2: 'h2',
      h3: 'h3',
      h4: 'h4',
      h5: 'h5',
      h6: 'h6',
      subtitle1: 'h6',
      subtitle2: 'h6',
      body1: 'p',
      body2: 'p',
      inherit: 'p',
    }) (``object``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-typography", children, **kwargs)
        self.props += [
            "align",
            "color",
            ("gutter_bottom", "gutterBottom"),
            ("no_wrap", "noWrap"),
            "variant",
            ("variant_mapping", "variantMapping"),
        ]


class Zoom(MuiHtmlElement):
    """MUI Zoom - https://mui.com/material-ui/api/zoom/

        The Zoom transition can be used for the floating variant of the [Button](/material-ui/react-floating-action-button/#animation) component.

        :param add_end_listener: Add a custom transition end trigger. Use it when you need custom logic to decide when the transition has ended. Note: Timeouts are still used as a fallback if provided. (``func``)
        :param appear: Perform the enter transition when it first mounts if in is also true. Set this to false to disable this behavior. (default: true) (``bool``)
        :param disable_prefers_reduced_motion: If true, the transition ignores theme.motion.reducedMotion and keeps its normal timing. (default: false) (``bool``)
        :param easing: The transition timing function. You may specify a single easing or a object containing enter and exit values. (``{ enter?: string, exit?: string } | string``)
        :param in: If true, the component will transition in. (``bool``)
        :param timeout: The duration for the transition, in milliseconds. You may specify a single timeout for all transitions, or individually with an object. (default: {
      enter: theme.transitions.duration.enteringScreen,
      exit: theme.transitions.duration.leavingScreen,
    }) (``number | { appear?: number, enter?: number, exit?: number }``)
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("mui-zoom", children, **kwargs)
        self.props += [
            ("add_end_listener", "addEndListener"),
            "appear",
            ("disable_prefers_reduced_motion", "disablePrefersReducedMotion"),
            "easing",
            "in",
            "timeout",
        ]
