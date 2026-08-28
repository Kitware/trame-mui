// Application-provided React components - no build step required.
// The trame react client exposes the page's React as window.React; this file
// is served by the app through `server.enable_module(...)` and registered
// through `react_use`.
(function () {
  const { createElement: h, useMemo } = window.React;

  // ---------------------------------------------------------------------
  // <my-sparkline points=[...] /> - inline SVG line chart
  // ---------------------------------------------------------------------
  function Sparkline({
    points = [],
    width = 400,
    height = 60,
    color = "#1976d2",
  }) {
    const path = useMemo(() => {
      if (points.length < 2) return "";
      const min = Math.min(...points);
      const max = Math.max(...points);
      const span = max - min || 1;
      const dx = width / (points.length - 1);
      return points
        .map((v, i) => {
          const x = (i * dx).toFixed(1);
          const y = (height - 4 - ((v - min) / span) * (height - 8)).toFixed(1);
          return `${i === 0 ? "M" : "L"}${x},${y}`;
        })
        .join(" ");
    }, [points, width, height]);

    return h(
      "svg",
      { width, height, style: { display: "block" } },
      h("path", {
        d: path,
        fill: "none",
        stroke: color,
        strokeWidth: 2,
        strokeLinejoin: "round",
        strokeLinecap: "round",
      }),
    );
  }

  // ---------------------------------------------------------------------
  // <my-color-swatch r_model="color" colors=[...] /> - two-way bound picker
  // (receives value + onUpdateValue from the trame model contract)
  // ---------------------------------------------------------------------
  function ColorSwatch({ value, onUpdateValue, colors = [] }) {
    return h(
      "div",
      { style: { display: "flex", gap: "8px" } },
      colors.map((color) =>
        h("button", {
          key: color,
          onClick: () => onUpdateValue?.(color),
          title: color,
          style: {
            width: 28,
            height: 28,
            borderRadius: "50%",
            border:
              value === color ? "3px solid black" : "1px solid rgba(0,0,0,.2)",
            background: color,
            cursor: "pointer",
            padding: 0,
          },
        }),
      ),
    );
  }

  window.MyWidgets = {
    install(registry) {
      registry.register("my-sparkline", Sparkline);
      registry.register("my-color-swatch", ColorSwatch);
    },
  };
})();
