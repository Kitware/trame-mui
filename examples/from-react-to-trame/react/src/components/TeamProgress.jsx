import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemAvatar from "@mui/material/ListItemAvatar";
import ListItemText from "@mui/material/ListItemText";
import Avatar from "@mui/material/Avatar";
import AvatarGroup from "@mui/material/AvatarGroup";
import LinearProgress from "@mui/material/LinearProgress";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Skeleton from "@mui/material/Skeleton";
import { team } from "../data/mockData";

function progressColor(value) {
  if (value >= 80) return "success";
  if (value >= 50) return "primary";
  return "warning";
}

export default function TeamProgress({ loading }) {
  return (
    <Card>
      <CardHeader
        title="Team workload"
        slotProps={{ title: { variant: "subtitle1", fontWeight: 700 } }}
        subheader={`${team.length} members`}
        action={
          <AvatarGroup max={4} sx={{ mr: 1, mt: 1 }}>
            {team.map((m) => (
              <Avatar key={m.name} sx={{ width: 28, height: 28, fontSize: 12 }}>
                {m.initials}
              </Avatar>
            ))}
          </AvatarGroup>
        }
      />
      <CardContent sx={{ pt: 0 }}>
        <List disablePadding>
          {team.map((member) => (
            <ListItem key={member.name} disableGutters sx={{ py: 1 }}>
              <ListItemAvatar>
                <Avatar sx={{ bgcolor: "primary.main" }}>{member.initials}</Avatar>
              </ListItemAvatar>
              <ListItemText
                primary={loading ? <Skeleton width="50%" /> : member.name}
                secondary={loading ? <Skeleton width="30%" /> : member.role}
              />
              <Box sx={{ width: 120, ml: 2 }}>
                {loading ? (
                  <Skeleton variant="rectangular" height={8} sx={{ borderRadius: 4 }} />
                ) : (
                  <>
                    <LinearProgress
                      variant="determinate"
                      value={member.completion}
                      color={progressColor(member.completion)}
                      sx={{ height: 8, borderRadius: 4 }}
                    />
                    <Typography
                      variant="caption"
                      color="text.secondary"
                      sx={{ display: "block", textAlign: "right", mt: 0.5 }}
                    >
                      {member.completion}%
                    </Typography>
                  </>
                )}
              </Box>
            </ListItem>
          ))}
        </List>
      </CardContent>
    </Card>
  );
}
