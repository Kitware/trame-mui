import { useState } from "react";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import InputAdornment from "@mui/material/InputAdornment";
import Stack from "@mui/material/Stack";
import Badge from "@mui/material/Badge";
import Avatar from "@mui/material/Avatar";
import Menu from "@mui/material/Menu";
import MenuItem from "@mui/material/MenuItem";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import Divider from "@mui/material/Divider";
import Tooltip from "@mui/material/Tooltip";
import Box from "@mui/material/Box";
import MenuIcon from "@mui/icons-material/Menu";
import SearchIcon from "@mui/icons-material/Search";
import Brightness4Icon from "@mui/icons-material/Brightness4";
import Brightness7Icon from "@mui/icons-material/Brightness7";
import NotificationsNoneIcon from "@mui/icons-material/NotificationsNone";
import PersonOutlineIcon from "@mui/icons-material/PersonOutlineOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import LogoutOutlinedIcon from "@mui/icons-material/LogoutOutlined";
import { notifications } from "../data/mockData";

export default function AppHeader({ mode, onToggleMode, onMenuClick }) {
  const [notifAnchor, setNotifAnchor] = useState(null);
  const [profileAnchor, setProfileAnchor] = useState(null);

  return (
    <AppBar position="fixed" elevation={0} sx={{ zIndex: (t) => t.zIndex.drawer + 1 }}>
      <Toolbar sx={{ gap: 1.5 }}>
        <IconButton
          edge="start"
          onClick={onMenuClick}
          sx={{ display: { md: "none" } }}
        >
          <MenuIcon />
        </IconButton>

        <Typography variant="h6" noWrap sx={{ fontWeight: 700, mr: 2 }}>
          Insight
        </Typography>

        <TextField
          size="small"
          placeholder="Search…"
          variant="outlined"
          sx={{
            display: { xs: "none", sm: "block" },
            width: 280,
            "& .MuiOutlinedInput-root": { borderRadius: 999 },
          }}
          slotProps={{
            input: {
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon fontSize="small" />
                </InputAdornment>
              ),
            },
          }}
        />

        <Box sx={{ flexGrow: 1 }} />

        <Stack direction="row" spacing={0.5} alignItems="center">
          <Tooltip title={mode === "light" ? "Switch to dark mode" : "Switch to light mode"}>
            <IconButton onClick={onToggleMode}>
              {mode === "light" ? (
                <Brightness4Icon fontSize="small" />
              ) : (
                <Brightness7Icon fontSize="small" />
              )}
            </IconButton>
          </Tooltip>

          <Tooltip title="Notifications">
            <IconButton onClick={(e) => setNotifAnchor(e.currentTarget)}>
              <Badge badgeContent={notifications.length} color="error">
                <NotificationsNoneIcon fontSize="small" />
              </Badge>
            </IconButton>
          </Tooltip>

          <Menu
            anchorEl={notifAnchor}
            open={Boolean(notifAnchor)}
            onClose={() => setNotifAnchor(null)}
            slotProps={{ paper: { sx: { width: 340, mt: 1 } } }}
          >
            <Typography variant="subtitle2" sx={{ px: 2, py: 1, fontWeight: 700 }}>
              Notifications
            </Typography>
            <Divider />
            {notifications.map((n) => (
              <MenuItem key={n.title} onClick={() => setNotifAnchor(null)} sx={{ whiteSpace: "normal" }}>
                <ListItemText
                  primary={n.title}
                  secondary={`${n.detail} · ${n.time}`}
                  slotProps={{
                    secondary: { variant: "caption", color: "text.secondary" },
                  }}
                />
              </MenuItem>
            ))}
          </Menu>

          <Tooltip title="Account">
            <IconButton onClick={(e) => setProfileAnchor(e.currentTarget)} sx={{ ml: 0.5 }}>
              <Avatar sx={{ width: 32, height: 32, bgcolor: "primary.main", fontSize: 14 }}>
                SJ
              </Avatar>
            </IconButton>
          </Tooltip>

          <Menu
            anchorEl={profileAnchor}
            open={Boolean(profileAnchor)}
            onClose={() => setProfileAnchor(null)}
            slotProps={{ paper: { sx: { width: 240, mt: 1 } } }}
          >
            <ListItemAvatar sx={{ pl: 2, pt: 1, display: "flex", alignItems: "center", gap: 1.5, pb: 1 }}>
              <Avatar sx={{ bgcolor: "primary.main" }}>SJ</Avatar>
              <Box>
                <Typography variant="body2" sx={{ fontWeight: 700 }}>
                  Sebastien Jourdain
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  sebastien.jourdain@kitware.com
                </Typography>
              </Box>
            </ListItemAvatar>
            <Divider />
            <MenuItem onClick={() => setProfileAnchor(null)}>
              <ListItemIcon>
                <PersonOutlineIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText>Profile</ListItemText>
            </MenuItem>
            <MenuItem onClick={() => setProfileAnchor(null)}>
              <ListItemIcon>
                <SettingsOutlinedIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText>Settings</ListItemText>
            </MenuItem>
            <Divider />
            <MenuItem onClick={() => setProfileAnchor(null)}>
              <ListItemIcon>
                <LogoutOutlinedIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText>Sign out</ListItemText>
            </MenuItem>
          </Menu>
        </Stack>
      </Toolbar>
    </AppBar>
  );
}
