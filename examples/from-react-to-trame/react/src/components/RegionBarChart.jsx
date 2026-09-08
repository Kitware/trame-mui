import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import { useTheme } from "@mui/material/styles";
import { BarChart } from "@mui/x-charts/BarChart";
import { salesByRegion } from "../data/mockData";

export default function RegionBarChart({ loading }) {
  const theme = useTheme();

  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Typography variant="subtitle1" sx={{ fontWeight: 700 }}>
          Sales by region
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Units sold, current quarter
        </Typography>

        {loading ? (
          <Skeleton variant="rectangular" height={260} sx={{ mt: 2, borderRadius: 1 }} />
        ) : (
          <BarChart
            height={260}
            dataset={salesByRegion}
            xAxis={[{ scaleType: "band", dataKey: "region" }]}
            series={[{ dataKey: "value", color: theme.palette.primary.main }]}
            borderRadius={4}
            categoryGapRatio={0.4}
            grid={{ horizontal: true }}
            margin={{ left: 45, right: 10, top: 20, bottom: 50 }}
            sx={{
              "& .MuiChartsAxis-line, & .MuiChartsAxis-tick": {
                stroke: theme.palette.divider,
              },
              "& .MuiChartsGrid-line": { stroke: theme.palette.divider },
              "& .MuiChartsAxis-tickLabel": { fontSize: 11 },
            }}
          />
        )}
      </CardContent>
    </Card>
  );
}
