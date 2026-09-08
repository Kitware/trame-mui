import { useState } from "react";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import TablePagination from "@mui/material/TablePagination";
import Stack from "@mui/material/Stack";
import Avatar from "@mui/material/Avatar";
import Chip from "@mui/material/Chip";
import Skeleton from "@mui/material/Skeleton";
import Typography from "@mui/material/Typography";
import CheckCircleOutlineIcon from "@mui/icons-material/CheckCircleOutlineOutlined";
import ScheduleOutlinedIcon from "@mui/icons-material/ScheduleOutlined";
import AutorenewOutlinedIcon from "@mui/icons-material/AutorenewOutlined";
import CancelOutlinedIcon from "@mui/icons-material/CancelOutlined";
import { recentOrders } from "../data/mockData";

const statusConfig = {
  Completed: { color: "success", icon: CheckCircleOutlineIcon },
  Processing: { color: "info", icon: AutorenewOutlinedIcon },
  Pending: { color: "warning", icon: ScheduleOutlinedIcon },
  Cancelled: { color: "error", icon: CancelOutlinedIcon },
};

function initialsOf(name) {
  return name
    .split(" ")
    .map((p) => p[0])
    .join("")
    .slice(0, 2)
    .toUpperCase();
}

export default function RecentOrdersTable({ loading }) {
  const [page, setPage] = useState(0);
  const rowsPerPage = 4;
  const rows = recentOrders.slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage);

  return (
    <Card>
      <CardHeader
        title="Recent orders"
        slotProps={{ title: { variant: "subtitle1", fontWeight: 700 } }}
        action={
          <Button size="small" sx={{ mt: 0.5 }}>
            View all
          </Button>
        }
      />
      <CardContent sx={{ pt: 0 }}>
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Order</TableCell>
                <TableCell>Customer</TableCell>
                <TableCell>Date</TableCell>
                <TableCell align="right">Amount</TableCell>
                <TableCell align="right">Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {loading
                ? Array.from({ length: rowsPerPage }).map((_, i) => (
                    <TableRow key={i}>
                      <TableCell colSpan={5}>
                        <Skeleton variant="text" />
                      </TableCell>
                    </TableRow>
                  ))
                : rows.map((row) => {
                    const cfg = statusConfig[row.status];
                    const StatusIcon = cfg.icon;
                    return (
                      <TableRow key={row.id} hover>
                        <TableCell>
                          <Typography variant="body2" sx={{ fontWeight: 600 }}>
                            {row.id}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Stack direction="row" spacing={1} alignItems="center">
                            <Avatar sx={{ width: 26, height: 26, fontSize: 12 }}>
                              {initialsOf(row.customer)}
                            </Avatar>
                            <Typography variant="body2">{row.customer}</Typography>
                          </Stack>
                        </TableCell>
                        <TableCell>
                          <Typography variant="body2" color="text.secondary">
                            {row.date}
                          </Typography>
                        </TableCell>
                        <TableCell align="right">
                          <Typography
                            variant="body2"
                            sx={{ fontVariantNumeric: "tabular-nums" }}
                          >
                            {row.amount}
                          </Typography>
                        </TableCell>
                        <TableCell align="right">
                          <Chip
                            size="small"
                            icon={<StatusIcon sx={{ fontSize: 14 }} />}
                            label={row.status}
                            color={cfg.color}
                            variant="outlined"
                          />
                        </TableCell>
                      </TableRow>
                    );
                  })}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          component="div"
          count={recentOrders.length}
          page={page}
          onPageChange={(_e, newPage) => setPage(newPage)}
          rowsPerPage={rowsPerPage}
          rowsPerPageOptions={[rowsPerPage]}
        />
      </CardContent>
    </Card>
  );
}
