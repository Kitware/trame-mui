import react from "@vitejs/plugin-react";

export default {
  plugins: [react()],
  define: {
    "process.env.NODE_ENV": JSON.stringify("production"),
  },
  build: {
    lib: {
      entry: "src/index.js",
      name: "TrameMui",
      formats: ["umd"],
      fileName: () => "trame-mui.umd.js",
      cssFileName: "trame-mui",
    },
    outDir: "../trame_mui/module/serve",
    rollupOptions: {
      // Use the single React instance exposed by the trame react client
      external: ["react", "react-dom"],
      output: {
        globals: {
          react: "React",
          "react-dom": "ReactDOM",
        },
      },
    },
  },
};
