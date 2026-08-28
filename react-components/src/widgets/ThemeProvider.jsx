import { useMemo } from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// trame contract: reads an optional theme config from props; wraps children
// with the MUI theme + CssBaseline. Place at the layout root.
export default function MuiThemeProvider({ theme, mode, slot }) {
  const muiTheme = useMemo(
    () =>
      createTheme({
        palette: { mode: mode || "light" },
        ...(theme || {}),
      }),
    [theme, mode],
  );

  return (
    <ThemeProvider theme={muiTheme}>
      <CssBaseline />
      {slot ? slot() : null}
    </ThemeProvider>
  );
}
