import { useMemo } from "react";
import { ThemeProvider as MuiThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";

// trame contract: like every other registered tag, children arrive through
// the normal `children` prop. Wraps them with a MUI theme (palette mode
// and/or a full theme override) plus CssBaseline. Place at the layout root.
export default function ThemeProvider({ theme, mode, children }) {
  const muiTheme = useMemo(
    () =>
      createTheme({
        ...(theme || {}),
        // Merged after the spread (rather than merged into it) so a
        // `theme.palette` override (custom primary/secondary/...) doesn't
        // shallow-clobber `mode` and vice versa - both need to survive.
        palette: { ...(theme?.palette || {}), mode: mode || "light" },
      }),
    [theme, mode],
  );

  return (
    <MuiThemeProvider theme={muiTheme}>
      <CssBaseline />
      {children}
    </MuiThemeProvider>
  );
}
