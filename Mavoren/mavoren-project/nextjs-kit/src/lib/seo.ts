import type { Metadata } from 'next'
import { site } from '@/data/site'

export const BASE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000'

export function pageMetadata(o: { title: string; description: string; path: string }): Metadata {
  return {
    title: o.title,
    description: o.description,
    alternates: { canonical: o.path },
    openGraph: { title: o.title, description: o.description, url: o.path, siteName: site.name, type: 'website', locale: 'en_IN' },
    twitter: { card: 'summary_large_image', title: o.title, description: o.description },
  }
}

// Never add ratings, reviews or an address that does not exist.
export const organizationJsonLd = () => ({
  '@context': 'https://schema.org',
  '@type': 'Organization',
  name: site.name,
  url: BASE_URL,
  email: site.email,
  telephone: site.phone,
  areaServed: site.areaServed,
  sameAs: [site.instagram, site.facebook],
})
export const serviceJsonLd = (name: string, description: string, path: string) => ({
  '@context': 'https://schema.org', '@type': 'Service', name, description, url: BASE_URL + path,
  provider: { '@type': 'Organization', name: site.name }, areaServed: site.areaServed,
})
export const articleJsonLd = (title: string, path: string, updated: string) => ({
  '@context': 'https://schema.org', '@type': 'Article', headline: title, url: BASE_URL + path, dateModified: updated,
  author: { '@type': 'Organization', name: site.name },
})
export const breadcrumbJsonLd = (items: { name: string; path: string }[]) => ({
  '@context': 'https://schema.org', '@type': 'BreadcrumbList',
  itemListElement: items.map((it, i) => ({ '@type': 'ListItem', position: i + 1, name: it.name, item: BASE_URL + it.path })),
})
