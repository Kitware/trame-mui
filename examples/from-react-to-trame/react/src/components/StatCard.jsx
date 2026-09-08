import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Avatar from "@mui/material/Avatar";
import Chip from "@mui/material/Chip";
import Skeleton from "@mui/material/Skeleton";
import { alpha, useTheme } from "@mui/material/styles";
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
import AttachMoneyOutlinedIcon from "@mui/icons-material/AttachMoneyOutlined";
import GroupsOutlinedIcon from "@mui/icons-material/GroupsOutlined";
import ReceiptLongOutlinedIcon from "@mui/icons-material/ReceiptLongOutlined";
import PercentOutlinedIcon from "@mui/icons-material/PercentOutlined";
import { SparkLineChart } from "@mui/x-charts/SparkLineChart";

const icons = {
  revenue: AttachMoneyOutlinedIcon,
  users: GroupsOutlinedIcon,
  orders: ReceiptLongOutlinedIcon,
  conversion: PercentOutlinedIcon,
};

export default function StatCard({ item, loading }) {
  const theme = useTheme();
  const Icon = icons[item.icon];
  const positive = item.delta >= 0;

  if (loading) {
    return (
      <Card sx={{ height: "100%" }}>
        <CardContent>
          <Stack direction="row" spacing={2} alignItems="center" sx={{ mb: 2 }}>
            <Skeleton variant="circular" width={40} height={40} />
            <Skeleton variant="text" width="60%" />
          </Stack>
          <Skeleton variant="text" width="40%" height={40} />
          <Skeleton variant="rectangular" width="100%" height={36} sx={{ mt: 1, borderRadius: 1 }} />
        </CardContent>
      </Card>
    );
  }

  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Stack direction="row" spacing={1.5} alignItems="center">
          <Avatar
            variant="rounded"
            sx={{
              bgcolor: (t) => alpha(t.palette.primary.main, 0.12),
              color: "primary.main",
              width: 40,
              height: 40,
            }}
          >
            <Icon fontSize="small" />
          </Avatar>
          <Typography variant="body2" color="text.secondary" sx={{ fontWeight: 600 }}>
            {item.label}
          </Typography>
        </Stack>

        <Stack direction="row" alignItems="flex-end" justifyContent="space-between" sx={{ mt: 2 }}>
          <Box>
            <Typography variant="h4" sx={{ lineHeight: 1.1 }}>
              {item.value}
            </Typography>
            <Chip
              size="small"
              icon={positive ? <ArrowUpwardIcon /> : <ArrowDownwardIcon />}
              label={`${positive ? "+" : ""}${item.delta}%`}
              color={positive ? "success" : "error"}
              variant="outlined"
              sx={{ mt: 1, "& .MuiChip-icon": { fontSize: 14 } }}
            />
          </Box>
          <Box sx={{ width: 96, height: 40 }}>
            <SparkLineChart
              data={item.trend}
              height={40}
              width={96}
              color={theme.palette.primary.main}
              showTooltip
              area
              curve="monotoneX"
            />
          </Box>
        </Stack>
      </CardContent>
    </Card>
  );
}
