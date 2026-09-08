// trame-mui: MUI widgets for the trame react client.
//
// Every component exported by @mui/material is auto-registered under its
// kebab-case tag (Button -> "mui-button", CardContent -> "mui-card-content").
//
// The trame react client evaluates the `react_use` module entry and calls
// `install(registry)`.

import * as MUI from "@mui/material";
import ThemeProvider from "./widgets/ThemeProvider.jsx";

const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();

function isComponent(name, value) {
  if (!/^[A-Z]/.test(name)) return false; // hooks, createTheme, colors, ...
  if (name.includes("_")) return false; // Unstable_/Experimental_ exports
  const type = typeof value;
  return type === "function" || (type === "object" && value !== null);
}

// Components hand-registered here take precedence over the auto-registration
// below (mui-theme-provider would otherwise resolve to the raw
// @mui/material ThemeProvider, which has no `mode` shorthand and doesn't
// mount CssBaseline).
const OVERRIDES = {
  "mui-theme-provider": ThemeProvider,
};

export function install(registerTag) {
  Object.entries(MUI)
    .filter((args) => isComponent(...args))
    .forEach(([name, component]) => {
      registerTag(`mui-${kebab(name)}`, component);
    });

  Object.entries(OVERRIDES).forEach(([tag, component]) => {
    registerTag(tag, component);
  });
}
