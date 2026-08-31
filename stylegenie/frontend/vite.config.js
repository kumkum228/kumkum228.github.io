import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Vite is the build tool / dev server for the React app.
// The dev server runs on http://localhost:5173 by default.
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true, // automatically open the browser when you run `npm run dev`
  },
});
