import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import WindiCSS from 'vite-plugin-windicss'
import * as path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        react(),
        WindiCSS({
            preflight: false,
        }),
    ],
    resolve: {
        // eslint-disable-next-line no-undef
        alias: [{ find: '@', replacement: path.resolve(__dirname, 'src') }],
    },
})
