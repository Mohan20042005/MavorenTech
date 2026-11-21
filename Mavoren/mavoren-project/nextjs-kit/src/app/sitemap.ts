import type { MetadataRoute } from 'next'
import { BASE_URL } from '@/lib/seo'
import { services } from '@/data/services'
import { projects } from '@/data/projects'
import { posts } from '@/data/blog'

export default function sitemap(): MetadataRoute.Sitemap {
  const fixed = ['', '/services', '/portfolio', '/pricing', '/offers', '/plan', '/process', '/blog', '/faq', '/contact', '/terms', '/privacy']
  const paths = [...fixed, ...services.map((s) => `/services/${s.slug}`), ...projects.map((p) => `/portfolio/${p.slug}`), ...posts.map((p) => `/blog/${p.slug}`)]
  return paths.map((p) => ({ url: BASE_URL + p, lastModified: new Date() }))
}
