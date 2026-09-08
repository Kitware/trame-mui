export const months = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec",
];

export const revenueTrend = [
  32, 41, 38, 47, 52, 49, 58, 63, 60, 71, 76, 82,
].map((v) => v * 1000);

export const kpis = [
  {
    id: "revenue",
    label: "Total revenue",
    value: "$824K",
    delta: 12.4,
    trend: [40, 42, 38, 45, 50, 48, 55, 60, 58, 65, 70, 82],
    icon: "revenue",
  },
  {
    id: "users",
    label: "Active users",
    value: "18.2K",
    delta: 8.1,
    trend: [12, 14, 13, 15, 16, 15, 17, 18, 17, 19, 20, 22],
    icon: "users",
  },
  {
    id: "orders",
    label: "Orders",
    value: "3,482",
    delta: -3.2,
    trend: [30, 32, 34, 33, 31, 30, 29, 28, 27, 26, 25, 24],
    icon: "orders",
  },
  {
    id: "conversion",
    label: "Conversion rate",
    value: "4.6%",
    delta: 1.8,
    trend: [3.2, 3.4, 3.3, 3.6, 3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.6],
    icon: "conversion",
  },
];

// Traffic sources — capped at 3 named categorical slots + "Other" (all-pairs
// forms like a donut cap at three before folding the remainder).
export const trafficSources = [
  { label: "Organic search", value: 4820 },
  { label: "Direct", value: 3140 },
  { label: "Social", value: 1960 },
  { label: "Other", value: 980 },
];

export const salesByRegion = [
  { region: "North America", value: 312 },
  { region: "Europe", value: 268 },
  { region: "Asia Pacific", value: 221 },
  { region: "Latin America", value: 104 },
  { region: "Other", value: 58 },
];

export const recentOrders = [
  {
    id: "ORD-7231",
    customer: "Amara Okafor",
    date: "2026-09-06",
    amount: "$482.00",
    status: "Completed",
  },
  {
    id: "ORD-7230",
    customer: "Liam Chen",
    date: "2026-09-06",
    amount: "$129.50",
    status: "Processing",
  },
  {
    id: "ORD-7229",
    customer: "Sofia Rossi",
    date: "2026-09-05",
    amount: "$998.20",
    status: "Completed",
  },
  {
    id: "ORD-7228",
    customer: "Noah Williams",
    date: "2026-09-05",
    amount: "$64.00",
    status: "Pending",
  },
  {
    id: "ORD-7227",
    customer: "Mei Tanaka",
    date: "2026-09-04",
    amount: "$212.75",
    status: "Cancelled",
  },
  {
    id: "ORD-7226",
    customer: "Diego Fernández",
    date: "2026-09-04",
    amount: "$355.10",
    status: "Completed",
  },
];

export const team = [
  {
    name: "Amara Okafor",
    role: "Product design",
    initials: "AO",
    completion: 82,
  },
  { name: "Liam Chen", role: "Frontend", initials: "LC", completion: 64 },
  { name: "Sofia Rossi", role: "Backend", initials: "SR", completion: 91 },
  { name: "Noah Williams", role: "QA", initials: "NW", completion: 45 },
];

export const notifications = [
  {
    title: "New order received",
    detail: "ORD-7231 from Amara Okafor",
    time: "5m ago",
  },
  {
    title: "Server deployment finished",
    detail: "v2.4.1 shipped to production",
    time: "1h ago",
  },
  {
    title: "Weekly report ready",
    detail: "Analytics summary for last week",
    time: "3h ago",
  },
];
