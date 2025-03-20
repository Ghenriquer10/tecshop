import { defineConfig } from "vite";

export default defineConfig({
  build: {
    manifest: true,
    outDir: "../static/", // Gera os arquivos estáticos para o Django
    rollupOptions: {
      input: "./src/main.js", // Arquivo principal de entrada
    },
  },
  server: {
    port: 3000,
    strictPort: true,
    hmr: {
      host: "localhost",
    },
  },
});
