import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig(({ mode }) => ({
  plugins: [vue()],
  base: mode === 'development' ? '/' : '/static/',
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
    },
    strictPort: false,
    hmr: {
      overlay: true
    }
  },
  publicDir: 'public',
  assetsInclude: ['**/*.json'],
}))