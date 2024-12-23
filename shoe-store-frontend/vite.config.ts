import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import dotenv from 'dotenv';

dotenv.config();

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  define: {
    'process.env': {
      API_URL: process.env.VITE_API_URL,
    },
  },
})
