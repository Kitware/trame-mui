import { useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import MenuItem from "@mui/material/MenuItem";
import Autocomplete from "@mui/material/Autocomplete";
import Switch from "@mui/material/Switch";
import Slider from "@mui/material/Slider";
import Rating from "@mui/material/Rating";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import RadioGroup from "@mui/material/RadioGroup";
import Radio from "@mui/material/Radio";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Divider from "@mui/material/Divider";
import Typography from "@mui/material/Typography";
import Button from "@mui/material/Button";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogActions from "@mui/material/DialogActions";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import SettingsBrightnessOutlinedIcon from "@mui/icons-material/SettingsBrightnessOutlined";
import { useSnackbar } from "../SnackbarContext";

const timezones = ["Pacific Time (US)", "Eastern Time (US)", "Central European Time", "Tokyo Standard Time"];
const languages = ["English", "Français", "Español", "Deutsch", "日本語"];

function TabPanel({ value, index, children }) {
  if (value !== index) return null;
  return <Box sx={{ pt: 3 }}>{children}</Box>;
}

export default function PreferencesPanel() {
  const notify = useSnackbar();
  const [tab, setTab] = useState(0);
  const [appearance, setAppearance] = useState("system");
  const [density, setDensity] = useState("comfortable");
  const [frequency, setFrequency] = useState(30);
  const [channels, setChannels] = useState({ email: true, push: true, sms: false });
  const [confirmOpen, setConfirmOpen] = useState(false);

  const handleSave = () => {
    notify("Preferences saved successfully", "success");
  };

  const handleDeleteConfirm = () => {
    setConfirmOpen(false);
    notify("Account deletion cancelled — this was just a demo", "info");
  };

  return (
    <Card>
      <CardContent>
        <Typography variant="subtitle1" sx={{ fontWeight: 700, mb: 0.5 }}>
          Preferences
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Account, notification and appearance settings
        </Typography>

        <Tabs
          value={tab}
          onChange={(_e, v) => setTab(v)}
          sx={{ mt: 1, borderBottom: 1, borderColor: "divider" }}
        >
          <Tab label="General" />
          <Tab label="Notifications" />
          <Tab label="Appearance" />
        </Tabs>

        <TabPanel value={tab} index={0}>
          <Grid container spacing={2}>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                label="Display name"
                defaultValue="Sebastien Jourdain"
                fullWidth
                size="small"
              />
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                select
                label="Timezone"
                defaultValue={timezones[0]}
                fullWidth
                size="small"
              >
                {timezones.map((tz) => (
                  <MenuItem key={tz} value={tz}>
                    {tz}
                  </MenuItem>
                ))}
              </TextField>
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <Autocomplete
                options={languages}
                defaultValue={languages[0]}
                size="small"
                renderInput={(params) => <TextField {...params} label="Language" />}
              />
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <Stack spacing={0.5}>
                <Typography variant="body2">Rate your experience</Typography>
                <Rating defaultValue={4} />
              </Stack>
            </Grid>
          </Grid>
        </TabPanel>

        <TabPanel value={tab} index={1}>
          <Stack spacing={1.5} divider={<Divider flexItem />}>
            <Stack direction="row" justifyContent="space-between" alignItems="center">
              <Box>
                <Typography variant="body2">Email notifications</Typography>
                <Typography variant="caption" color="text.secondary">
                  Order updates and weekly summaries
                </Typography>
              </Box>
              <Switch
                checked={channels.email}
                onChange={(e) => setChannels({ ...channels, email: e.target.checked })}
              />
            </Stack>
            <Stack direction="row" justifyContent="space-between" alignItems="center">
              <Box>
                <Typography variant="body2">Push notifications</Typography>
                <Typography variant="caption" color="text.secondary">
                  Real-time alerts on this device
                </Typography>
              </Box>
              <Switch
                checked={channels.push}
                onChange={(e) => setChannels({ ...channels, push: e.target.checked })}
              />
            </Stack>
            <Stack direction="row" justifyContent="space-between" alignItems="center">
              <Box>
                <Typography variant="body2">SMS notifications</Typography>
                <Typography variant="caption" color="text.secondary">
                  Critical alerts only
                </Typography>
              </Box>
              <Switch
                checked={channels.sms}
                onChange={(e) => setChannels({ ...channels, sms: e.target.checked })}
              />
            </Stack>
          </Stack>

          <Box sx={{ mt: 3 }}>
            <Typography variant="body2" gutterBottom>
              Digest frequency: every {frequency} minutes
            </Typography>
            <Slider
              value={frequency}
              onChange={(_e, v) => setFrequency(v)}
              min={5}
              max={60}
              step={5}
              marks={[{ value: 5, label: "5m" }, { value: 60, label: "60m" }]}
              valueLabelDisplay="auto"
              sx={{ maxWidth: 360 }}
            />
          </Box>
        </TabPanel>

        <TabPanel value={tab} index={2}>
          <Stack spacing={3}>
            <Box>
              <Typography variant="body2" gutterBottom>
                Theme
              </Typography>
              <ToggleButtonGroup
                value={appearance}
                exclusive
                size="small"
                onChange={(_e, v) => v && setAppearance(v)}
              >
                <ToggleButton value="light">
                  <LightModeOutlinedIcon fontSize="small" sx={{ mr: 1 }} />
                  Light
                </ToggleButton>
                <ToggleButton value="dark">
                  <DarkModeOutlinedIcon fontSize="small" sx={{ mr: 1 }} />
                  Dark
                </ToggleButton>
                <ToggleButton value="system">
                  <SettingsBrightnessOutlinedIcon fontSize="small" sx={{ mr: 1 }} />
                  System
                </ToggleButton>
              </ToggleButtonGroup>
            </Box>

            <Box>
              <Typography variant="body2" gutterBottom>
                Layout density
              </Typography>
              <RadioGroup
                row
                value={density}
                onChange={(e) => setDensity(e.target.value)}
              >
                <FormControlLabel value="comfortable" control={<Radio />} label="Comfortable" />
                <FormControlLabel value="compact" control={<Radio />} label="Compact" />
              </RadioGroup>
            </Box>

            <FormControlLabel control={<Checkbox defaultChecked />} label="Reduce motion" />
          </Stack>
        </TabPanel>

        <Divider sx={{ my: 3 }} />

        <Box sx={{ mb: 2 }}>
          <Accordion disableGutters>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography variant="body2" sx={{ fontWeight: 600 }}>
                How is my data used?
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography variant="body2" color="text.secondary">
                This demo dashboard uses only local mock data — nothing is sent to a
                server.
              </Typography>
            </AccordionDetails>
          </Accordion>
          <Accordion disableGutters>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography variant="body2" sx={{ fontWeight: 600 }}>
                Can I export my preferences?
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography variant="body2" color="text.secondary">
                Not yet — this is a UI showcase intended to be ported into a trame
                application.
              </Typography>
            </AccordionDetails>
          </Accordion>
        </Box>

        <Stack direction="row" spacing={1.5} justifyContent="flex-end">
          <Button color="error" variant="outlined" onClick={() => setConfirmOpen(true)}>
            Delete account
          </Button>
          <Button variant="contained" onClick={handleSave}>
            Save changes
          </Button>
        </Stack>
      </CardContent>

      <Dialog open={confirmOpen} onClose={() => setConfirmOpen(false)}>
        <DialogTitle>Delete account?</DialogTitle>
        <DialogContent>
          <DialogContentText>
            This action cannot be undone. All of your data will be permanently
            removed. (This is a demo — nothing will actually be deleted.)
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setConfirmOpen(false)}>Cancel</Button>
          <Button color="error" variant="contained" onClick={handleDeleteConfirm}>
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </Card>
  );
}
