// Two-way binding (r_model) semantics per MUI component.
// The trame react client hands registered components `value` +
// `onUpdateValue(newValue)`; these configs map that contract onto each
// component's controlled prop/event pair.

const targetValue = (event) => event.target.value;
const targetChecked = (event) => event.target.checked;
const secondArg = (event, value) => value;

export default {
  // value + onChange(event) -> event.target.value
  TextField: { prop: "value", event: "onChange", extract: targetValue },
  Select: { prop: "value", event: "onChange", extract: targetValue },
  NativeSelect: { prop: "value", event: "onChange", extract: targetValue },
  InputBase: { prop: "value", event: "onChange", extract: targetValue },
  Input: { prop: "value", event: "onChange", extract: targetValue },
  OutlinedInput: { prop: "value", event: "onChange", extract: targetValue },
  FilledInput: { prop: "value", event: "onChange", extract: targetValue },

  // value + onChange(event, value)
  Slider: { prop: "value", event: "onChange", extract: secondArg },
  Rating: { prop: "value", event: "onChange", extract: secondArg },
  RadioGroup: { prop: "value", event: "onChange", extract: secondArg },
  ToggleButtonGroup: { prop: "value", event: "onChange", extract: secondArg },
  Tabs: { prop: "value", event: "onChange", extract: secondArg },
  BottomNavigation: { prop: "value", event: "onChange", extract: secondArg },
  Pagination: { prop: "page", event: "onChange", extract: secondArg },
  Autocomplete: { prop: "value", event: "onChange", extract: secondArg },

  // checked + onChange(event) -> event.target.checked
  Checkbox: { prop: "checked", event: "onChange", extract: targetChecked },
  Switch: { prop: "checked", event: "onChange", extract: targetChecked },

  // open/close components: model drives `open`, closing writes false
  Dialog: { prop: "open", event: "onClose", extract: () => false },
  Drawer: { prop: "open", event: "onClose", extract: () => false },
  Menu: { prop: "open", event: "onClose", extract: () => false },
  Modal: { prop: "open", event: "onClose", extract: () => false },
  Popover: { prop: "open", event: "onClose", extract: () => false },
  Snackbar: { prop: "open", event: "onClose", extract: () => false },
};
