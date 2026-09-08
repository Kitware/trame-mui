import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import Skeleton from "@mui/material/Skeleton";
import { useTheme, alpha } from "@mui/material/styles";
import { Gauge, gaugeClasses } from "@mui/x-charts/Gauge";

const GOAL = 900;
const CURRENT = 824;

export default function GoalGauge({ loading }) {
  const theme = useTheme();
  const pct = Math.round((CURRENT / GOAL) * 100);

  return (
    <Card sx={{ height: "100%" }}>
      <CardContent>
        <Typography variant="subtitle1" sx={{ fontWeight: 700 }}>
          Monthly goal
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Revenue vs. ${GOAL}K target
        </Typography>

        {loading ? (
          <Skeleton variant="circular" width={180} height={180} sx={{ mx: "auto", my: 2 }} />
        ) : (
          <Box sx={{ display: "flex", justifyContent: "center", mt: 1 }}>
            <Gauge
              width={180}
              height={180}
              value={CURRENT}
              valueMin={0}
              valueMax={GOAL}
              startAngle={-110}
              endAngle={110}
              text={() => `${pct}%`}
              sx={{
                [`& .${gaugeClasses.valueArc}`]: {
                  fill: theme.palette.primary.main,
                },
                [`& .${gaugeClasses.referenceArc}`]: {
                  fill: alpha(theme.palette.primary.main, 0.15),
                },
                [`& .${gaugeClasses.valueText}`]: {
                  fontSize: 28,
                  fontWeight: 700,
                  fill: theme.palette.text.primary,
                },
              }}
            />
          </Box>
        )}
        <Typography variant="body2" color="text.secondary" align="center">
          ${CURRENT}K of ${GOAL}K
        </Typography>
      </CardContent>
    </Card>
  );
}
