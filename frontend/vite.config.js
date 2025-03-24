import { defineConfig } from "vite";

export default defineConfig({
  base: "/static/",
  build: {
    outDir: "../static/",  // Define que os arquivos serão salvos na pasta static/
    emptyOutDir: true,
    rollupOptions: {
      input: "index.html",
    },
  },
  server: {
    port: 5173,
    strictPort: true,
  },
});
