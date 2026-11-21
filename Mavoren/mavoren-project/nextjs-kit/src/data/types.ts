export type Tier = 'starter' | 'business' | 'pro' | 'commerce' | 'care'
export interface Pkg { name: string; price: string; tagline: string; serviceType: string; features: string[]; note: string | null; tier: Tier }
export interface TierService { label: string; serviceType: string; price: string; description: string }
export interface TierCard { name: string; tagline: string; from: string; popular: boolean; services: TierService[] }
export interface Project { name: string; slug: string; kind: string; description: string; features: string[]; tags: string[]; liveUrl: string | null; githubUrl: string | null }
export interface Service { name: string; slug: string; description: string }
export interface Faq { question: string; answer: string }
export interface Post { slug: string; title: string; updated: string; paragraphs: string[] }
