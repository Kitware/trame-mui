import { useState } from "react";
import Drawer from "@mui/material/Drawer";
import Toolbar from "@mui/material/Toolbar";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Divider from "@mui/material/Divider";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import DashboardOutlinedIcon from "@mui/icons-material/DashboardOutlined";
import InsightsOutlinedIcon from "@mui/icons-material/InsightsOutlined";
import ReceiptLongOutlinedIcon from "@mui/icons-material/ReceiptLongOutlined";
import PeopleAltOutlinedIcon from "@mui/icons-material/PeopleAltOutlined";
import Inventory2OutlinedIcon from "@mui/icons-material/Inventory2Outlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";

export const drawerWidth = 240;

const primaryItems = [
  { label: "Dashboard", icon: DashboardOutlinedIcon },
  { label: "Analytics", icon: InsightsOutlinedIcon },
  { label: "Orders", icon: ReceiptLongOutlinedIcon },
  { label: "Customers", icon: PeopleAltOutlinedIcon },
  { label: "Products", icon: Inventory2OutlinedIcon },
];

const secondaryItems = [
  { label: "Settings", icon: SettingsOutlinedIcon },
  { label: "Help & support", icon: HelpOutlineOutlinedIcon },
];

function NavList({ selected, onSelect }) {
  return (
    <Box sx={{ display: "flex", flexDirection: "column", height: "100%" }}>
      <List sx={{ px: 1.5, pt: 1 }}>
        {primaryItems.map((item) => (
          <ListItem key={item.label} disablePadding sx={{ mb: 0.5 }}>
            <ListItemButton
              selected={selected === item.label}
              onClick={() => onSelect(item.label)}
              sx={{ borderRadius: 2 }}
            >
              <ListItemIcon sx={{ minWidth: 36 }}>
                <item.icon fontSize="small" />
              </ListItemIcon>
              <ListItemText
                primary={item.label}
                slotProps={{ primary: { fontSize: 14, fontWeight: 600 } }}
              />
            </ListItemButton>
          </ListItem>
        ))}
      </List>

      <Box sx={{ flexGrow: 1 }} />

      <Divider sx={{ mx: 1.5 }} />
      <List sx={{ px: 1.5, py: 1 }}>
        {secondaryItems.map((item) => (
          <ListItem key={item.label} disablePadding sx={{ mb: 0.5 }}>
            <ListItemButton
              selected={selected === item.label}
              onClick={() => onSelect(item.label)}
              sx={{ borderRadius: 2 }}
            >
              <ListItemIcon sx={{ minWidth: 36 }}>
                <item.icon fontSize="small" />
              </ListItemIcon>
              <ListItemText
                primary={item.label}
                slotProps={{ primary: { fontSize: 14, fontWeight: 600 } }}
              />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
      <Box sx={{ px: 2.5, pb: 2 }}>
        <Typography variant="caption" color="text.secondary">
          v2.4.1 · from-react-to-trame
        </Typography>
      </Box>
    </Box>
  );
}

export default function SideNav({ mobileOpen, onClose }) {
  const [selected, setSelected] = useState("Dashboard");

  return (
    <Box component="nav" sx={{ width: { md: drawerWidth }, flexShrink: { md: 0 } }}>
      <Drawer
        variant="temporary"
        open={mobileOpen}
        onClose={onClose}
        ModalProps={{ keepMounted: true }}
        sx={{
          display: { xs: "block", md: "none" },
          "& .MuiDrawer-paper": { width: drawerWidth },
        }}
      >
        <Toolbar />
        <NavList
          selected={selected}
          onSelect={(label) => {
            setSelected(label);
            onClose();
          }}
        />
      </Drawer>

      <Drawer
        variant="permanent"
        sx={{
          display: { xs: "none", md: "block" },
          "& .MuiDrawer-paper": {
            width: drawerWidth,
            boxSizing: "border-box",
            borderRight: "1px solid",
            borderColor: "divider",
          },
        }}
        open
      >
        <Toolbar />
        <NavList selected={selected} onSelect={setSelected} />
      </Drawer>
    </Box>
  );
}
