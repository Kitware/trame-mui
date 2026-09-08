import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Chip from "@mui/material/Chip";
import Skeleton from "@mui/material/Skeleton";
import { useTheme } from "@mui/material/styles";
import { LineChart } from "@mui/x-charts/LineChart";
import { months, revenueTrend } from "../data/mockData";

export default function RevenueChart({ loading }) {
  const theme = useTheme();
  const total = revenueTrend.reduce((a, b) => a + b, 0);

  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Stack direction="row" justifyContent="space-between" alignItems="flex-start" sx={{ mb: 1 }}>
          <Box>
            <Typography variant="subtitle1" sx={{ fontWeight: 700 }}>
              Revenue
            </Typography>
            <Typography variant="caption" color="text.secondary">
              Last 12 months
            </Typography>
          </Box>
          <Chip size="small" label={`$${(total / 1000).toFixed(0)}K total`} color="primary" variant="outlined" />
        </Stack>

        {loading ? (
          <Skeleton variant="rectangular" height={300} sx={{ borderRadius: 1 }} />
        ) : (
          <LineChart
            height={300}
            series={[
              {
                data: revenueTrend,
                area: true,
                showMark: false,
                color: theme.palette.primary.main,
                valueFormatter: (v) => `$${(v / 1000).toFixed(0)}K`,
              },
            ]}
            xAxis={[{ scaleType: "point", data: months }]}
            yAxis={[{ valueFormatter: (v) => `$${(v / 1000).toFixed(0)}K` }]}
            grid={{ horizontal: true }}
            margin={{ left: 60, right: 20, top: 20, bottom: 30 }}
            sx={{
              "& .MuiLineChart-area": { fillOpacity: 0.12 },
              "& .MuiLineChart-line": { strokeWidth: 2 },
              "& .MuiChartsAxis-line, & .MuiChartsAxis-tick": {
                stroke: theme.palette.divider,
              },
              "& .MuiChartsGrid-line": { stroke: theme.palette.divider },
            }}
          />
        )}
      </CardContent>
    </Card>
  );
}
