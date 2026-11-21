import { withSentryConfig } from '@sentry/nextjs'
import bundleAnalyzer from '@next/bundle-analyzer'

const withAnalyzer = bundleAnalyzer({ enabled: process.env.ANALYZE === 'true' })
const config = { reactStrictMode: true, images: { formats: ['image/avif', 'image/webp'] } }

// Sentry wraps the build only when an auth token exists; the runtime DSN is separate.
export default process.env.SENTRY_AUTH_TOKEN
  ? withSentryConfig(withAnalyzer(config), { silent: true })
  : withAnalyzer(config)
