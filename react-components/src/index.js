// trame-mui: MUI widgets for the trame react client.
//
// Every component exported by @mui/material is auto-registered under its
// kebab-case tag (Button -> "mui-button", CardContent -> "mui-card-content").
// Stateful components get their r_model semantics from modelConfigs.js.
//
// The trame react client evaluates the `react_use` module entry and calls
// `install(registry)`.

import * as MUI from "@mui/material";
import wrap from "./wrap";
import MODEL_CONFIGS from "./modelConfigs";
import MuiThemeProvider from "./widgets/ThemeProvider";

const kebab = (s) => s.replace(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();

function isComponent(name, value) {
  if (!/^[A-Z]/.test(name)) return false; // hooks, createTheme, colors, ...
  if (name.includes("_")) return false; // Unstable_/Experimental_ exports
  const type = typeof value;
  return type === "function" || (type === "object" && value !== null);
}

export function install(registry) {
  Object.entries(MUI).forEach(([name, component]) => {
    if (!isComponent(name, component)) return;
    registry.register(
      `mui-${kebab(name)}`,
      wrap(component, name, MODEL_CONFIGS[name]),
    );
  });

  // Theme + CssBaseline wrapper (place at the layout root)
  registry.register("mui-theme", MuiThemeProvider);
}
