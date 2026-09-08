import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Stack from "@mui/material/Stack";
import Box from "@mui/material/Box";
import Skeleton from "@mui/material/Skeleton";
import { useTheme } from "@mui/material/styles";
import { PieChart } from "@mui/x-charts/PieChart";
import { categorical } from "../theme";
import { trafficSources } from "../data/mockData";

export default function TrafficDonut({ loading }) {
  const theme = useTheme();
  const cat = categorical[theme.palette.mode];
  const otherColor = theme.palette.mode === "light" ? "#c3c2b7" : "#52514e";

  const total = trafficSources.reduce((a, b) => a + b.value, 0);
  const data = trafficSources.map((d, i) => ({
    id: d.label,
    label: d.label,
    value: d.value,
    color: d.label === "Other" ? otherColor : cat[i],
  }));

  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Typography variant="subtitle1" sx={{ fontWeight: 700 }}>
          Traffic sources
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Sessions by channel, last 30 days
        </Typography>

        {loading ? (
          <Skeleton variant="circular" width={180} height={180} sx={{ mx: "auto", my: 2 }} />
        ) : (
          <>
            <Box sx={{ display: "flex", justifyContent: "center" }}>
              <PieChart
                series={[
                  {
                    data,
                    innerRadius: 55,
                    outerRadius: 90,
                    paddingAngle: 2,
                    cornerRadius: 4,
                  },
                ]}
                height={220}
                width={220}
                hideLegend
                slotProps={{ tooltip: { trigger: "item" } }}
              />
            </Box>
            <Stack spacing={1} sx={{ mt: 1 }}>
              {data.map((d) => (
                <Stack
                  key={d.id}
                  direction="row"
                  alignItems="center"
                  justifyContent="space-between"
                >
                  <Stack direction="row" alignItems="center" spacing={1}>
                    <Box
                      sx={{
                        width: 10,
                        height: 10,
                        borderRadius: "2px",
                        bgcolor: d.color,
                        flexShrink: 0,
                      }}
                    />
                    <Typography variant="body2">{d.label}</Typography>
                  </Stack>
                  <Typography variant="body2" color="text.secondary">
                    {Math.round((d.value / total) * 100)}%
                  </Typography>
                </Stack>
              ))}
            </Stack>
          </>
        )}
      </CardContent>
    </Card>
  );
}
