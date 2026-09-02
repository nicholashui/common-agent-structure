import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    port: 15173,
    strictPort: true,
    proxy: {
      "/api": { target: "http://127.0.0.1:18080", changeOrigin: true },
      "/health": { target: "http://127.0.0.1:18080", changeOrigin: true },
      "/debug": { target: "http://127.0.0.1:18080", changeOrigin: true },
    },
  },
  preview: {
    port: 4173,
    proxy: {
      "/api": { target: "http://127.0.0.1:18080", changeOrigin: true },
      "/health": { target: "http://127.0.0.1:18080", changeOrigin: true },
      "/debug": { target: "http://127.0.0.1:18080", changeOrigin: true },
    },
  },
  test: {
    environment: "node",
    include: ["tests/**/*.test.ts"],
  },
});
