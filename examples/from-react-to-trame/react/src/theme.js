import { createTheme, alpha } from "@mui/material/styles";

// Fixed categorical order — never cycled, never reordered by filters.
// (blue, orange, aqua, yellow, magenta, green, violet, red)
export const categorical = {
  light: [
    "#2a78d6",
    "#eb6834",
    "#1baf7a",
    "#eda100",
    "#e87ba4",
    "#008300",
    "#4a3aa7",
    "#e34948",
  ],
  dark: [
    "#3987e5",
    "#d95926",
    "#199e70",
    "#c98500",
    "#d55181",
    "#008300",
    "#9085e9",
    "#e66767",
  ],
};

// Single-hue sequential ramp (blue), light -> dark, for magnitude comparisons.
export const sequential = {
  light: ["#cde2fb", "#9ec5f4", "#5598e7", "#2a78d6", "#1c5cab", "#0d366b"],
  dark: ["#184f95", "#1c5cab", "#256abf", "#2a78d6", "#3987e5", "#86b6ef"],
};

export const status = {
  good: "#0ca30c",
  warning: "#fab219",
  serious: "#ec835a",
  critical: "#d03b3b",
};

const surfaces = {
  light: { surface1: "#fcfcfb", page: "#f9f9f7" },
  dark: { surface1: "#222221", page: "#0d0d0d" },
};

const ink = {
  light: { primary: "#0b0b0b", secondary: "#52514e", muted: "#898781" },
  dark: { primary: "#ffffff", secondary: "#c3c2b7", muted: "#898781" },
};

export function getTheme(mode) {
  const cat = categorical[mode];
  return createTheme({
    palette: {
      mode,
      primary: { main: cat[0] },
      secondary: { main: cat[1] },
      success: { main: status.good },
      warning: { main: status.warning },
      error: { main: status.critical },
      info: { main: cat[0] },
      background: {
        default: surfaces[mode].page,
        paper: surfaces[mode].surface1,
      },
      text: {
        primary: ink[mode].primary,
        secondary: ink[mode].secondary,
        disabled: ink[mode].muted,
      },
      divider: mode === "light" ? "#e1e0d9" : "rgba(255,255,255,0.10)",
    },
    shape: { borderRadius: 12 },
    typography: {
      fontFamily: [
        "system-ui",
        "-apple-system",
        '"Segoe UI"',
        "Roboto",
        "sans-serif",
      ].join(","),
      h4: { fontWeight: 600 },
      h5: { fontWeight: 600 },
      h6: { fontWeight: 600 },
    },
    components: {
      MuiPaper: {
        styleOverrides: {
          root: { backgroundImage: "none" },
        },
      },
      MuiCard: {
        styleOverrides: {
          root: ({ theme }) => ({
            border: `1px solid ${theme.palette.divider}`,
            boxShadow: "none",
          }),
        },
      },
      MuiAppBar: {
        styleOverrides: {
          root: ({ theme }) => ({
            backgroundColor: alpha(theme.palette.background.paper, 0.85),
            backdropFilter: "blur(8px)",
            color: theme.palette.text.primary,
          }),
        },
      },
      MuiButton: {
        styleOverrides: {
          root: { textTransform: "none", fontWeight: 600 },
        },
      },
      MuiChip: {
        styleOverrides: {
          root: { fontWeight: 600 },
        },
      },
    },
  });
}
