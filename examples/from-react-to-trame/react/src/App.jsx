import { useMemo, useState } from "react";
import { ThemeProvider } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Container from "@mui/material/Container";
import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Breadcrumbs from "@mui/material/Breadcrumbs";
import Link from "@mui/material/Link";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import RefreshOutlinedIcon from "@mui/icons-material/RefreshOutlined";

import { getTheme } from "./theme";
import { SnackbarProvider, useSnackbar } from "./SnackbarContext";
import AppHeader from "./components/AppHeader";
import SideNav, { drawerWidth } from "./components/SideNav";
import StatCard from "./components/StatCard";
import RevenueChart from "./components/RevenueChart";
import TrafficDonut from "./components/TrafficDonut";
import RegionBarChart from "./components/RegionBarChart";
import GoalGauge from "./components/GoalGauge";
import RecentOrdersTable from "./components/RecentOrdersTable";
import TeamProgress from "./components/TeamProgress";
import PreferencesPanel from "./components/PreferencesPanel";
import { kpis } from "./data/mockData";

function Dashboard() {
  const notify = useSnackbar();
  const [loading, setLoading] = useState(false);

  const handleRefresh = () => {
    setLoading(true);
    window.setTimeout(() => {
      setLoading(false);
      notify("Dashboard refreshed", "info");
    }, 900);
  };

  return (
    <Container maxWidth="xl" sx={{ py: 3 }}>
      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        sx={{ mb: 3 }}
      >
        <Box>
          <Breadcrumbs sx={{ mb: 0.5 }}>
            <Link underline="hover" color="text.secondary" href="#">
              Home
            </Link>
            <Typography color="text.primary">Dashboard</Typography>
          </Breadcrumbs>
          <Typography variant="h5">Welcome back, Sebastien</Typography>
        </Box>
        <Tooltip title="Refresh data">
          <IconButton onClick={handleRefresh} disabled={loading}>
            <RefreshOutlinedIcon
              sx={{
                animation: loading ? "spin 0.9s linear infinite" : "none",
                "@keyframes spin": {
                  from: { transform: "rotate(0deg)" },
                  to: { transform: "rotate(360deg)" },
                },
              }}
            />
          </IconButton>
        </Tooltip>
      </Stack>

      <Grid container spacing={2.5}>
        {kpis.map((item) => (
          <Grid key={item.id} size={{ xs: 12, sm: 6, lg: 3 }}>
            <StatCard item={item} loading={loading} />
          </Grid>
        ))}

        <Grid size={{ xs: 12, lg: 8 }}>
          <RevenueChart loading={loading} />
        </Grid>
        <Grid size={{ xs: 12, lg: 4 }}>
          <TrafficDonut loading={loading} />
        </Grid>

        <Grid size={{ xs: 12, lg: 8 }}>
          <RegionBarChart loading={loading} />
        </Grid>
        <Grid size={{ xs: 12, lg: 4 }}>
          <GoalGauge loading={loading} />
        </Grid>

        <Grid size={{ xs: 12, lg: 7 }}>
          <RecentOrdersTable loading={loading} />
        </Grid>
        <Grid size={{ xs: 12, lg: 5 }}>
          <TeamProgress loading={loading} />
        </Grid>

        <Grid size={12}>
          <PreferencesPanel />
        </Grid>
      </Grid>
    </Container>
  );
}

export default function App() {
  const [mode, setMode] = useState("light");
  const [mobileOpen, setMobileOpen] = useState(false);
  const theme = useMemo(() => getTheme(mode), [mode]);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <SnackbarProvider>
        <Box sx={{ display: "flex", minHeight: "100vh", bgcolor: "background.default" }}>
          <AppHeader
            mode={mode}
            onToggleMode={() => setMode((m) => (m === "light" ? "dark" : "light"))}
            onMenuClick={() => setMobileOpen(true)}
          />
          <SideNav mobileOpen={mobileOpen} onClose={() => setMobileOpen(false)} />
          <Box
            component="main"
            sx={{ flexGrow: 1, width: { md: `calc(100% - ${drawerWidth}px)` } }}
          >
            <Toolbar />
            <Dashboard />
          </Box>
        </Box>
      </SnackbarProvider>
    </ThemeProvider>
  );
}
