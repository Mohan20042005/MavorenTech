# Mavoren: build the production Next.js site

Source of truth: `reference/mavoren.html` (design, copy, behaviour) and `src/data/*` (typed content). The config, SEO, Sentry, Lighthouse CI and Playwright files here were written without running npm, so run `npm install`, fix any version or type errors, and make `npm run build`, `npm run typecheck`, `npx playwright test` and `npx lhci autorun` pass before reporting done.

## Stack
Next.js App Router, TypeScript strict, Tailwind CSS, Framer Motion, Lucide React, Zod + React Hook Form, `@sentry/nextjs` (DSN from env, never invented), Lighthouse CI, Playwright, bundle analyzer (`npm run analyze`), Vercel free tier. `next/image`, `next/font` (Bricolage Grotesque, Hanken Grotesk). First run `npx skills add https://github.com/pbakaus/impeccable --skill impeccable`. Use Watermelon UI (https://ui.watermelon.sh/): follow https://ui.watermelon.sh/installation (shadcn CLI), read https://ui.watermelon.sh/llms.txt and the MCP docs at https://ui.watermelon.sh/developers/mcp, and pick blocks and animated components that fit the lightning theme (hero, pricing, FAQ, text effects). Check each component's licence before shipping.
Watermelon components are installed through the 21st.dev registry: `npx shadcn@latest add "https://21st.dev/r/quantvansh/watermelon-<component-name>?api_key=$API_KEY_21ST"`. The owner puts their key in `.env.local` as `API_KEY_21ST` (never in chat, never committed). Candidates seen in the catalog: Reversed Icon Accordion (FAQ), Primary Action Button (CTAs). Browse https://ui.watermelon.sh/blocks and /animated-components for pricing, hero and testimonial blocks; list in the final report exactly which components were installed and their licences.

## Design
Thor-inspired lightning theme: white page, electric blue #0A66FF, cyan #38BDF8, storm navy #070F20, crimson #D7263D. Dot grid, storm hero blended into the light page, dark footer fade, light default with dark toggle. Logos in `public/brand/` are transparent: never redraw or recolour. Project screenshots are in `public/projects/` (owner-supplied).

## Pages (each with unique metadata, canonical, JSON-LD, breadcrumbs)
Home, Services (3 tier cards), 12 service pages, Pricing (packages with inclusions and tier filter), Offers, Plan (package finder + price estimator), Portfolio + 6 case studies, Process, Blog + posts (`src/data/blog.ts`, more topics only after owner confirms), FAQ, Contact, Terms, Privacy, 404. Refund page needs owner terms. No fake testimonials, reviews or statistics: add a testimonials section only when real quotes are supplied.

## Behaviour
- Contact rows are full-width tappable links; copy buttons separate.
- Package, tier and service buttons pre-fill the 3-step enquiry form (Zod validated; opens WhatsApp; never claims delivery; honeypot; UTM added).
- Promo code MAVOREN30 (`src/data/promo.ts`): 30% off first service. Validate in the enquiry form and estimator; include in the WhatsApp message.
- Offer popup: after the visitor scrolls about two screens, a bottom card shows "Get your first service with 30% off", code MAVOREN30, copy button, claim button (fills the promo field), close button and Escape; once per session.
- Package finder (3 questions) and price estimator (starting price, promo, optional maintenance; extras quoted separately). No before/after slider. No Tamil/Tanglish toggle: English only.
- Lightning cursor effect in the hero only for `(hover:hover) and (pointer:fine)`, off for reduced motion.
- Search, theme toggle, mobile menu, back-to-top, progress bar, floating WhatsApp, loader, 10 text animations (mask rise, scramble decode, word stagger, blur in, letter bounce, count up, tracking expand, outline to fill, strike and replace, split halves).
- Free domain: eligible bulk orders worth ₹15,000 or above. 10% social media offer. Payments are arranged manually over WhatsApp.

## Test ids required by `tests/e2e/site.spec.ts`
`tier-service-business-website`, `chip-selected`, `estimator-package`, `promo-input`, `promo-apply`, `promo-message`, `estimator-total`, `ad-popup`, `enquiry-submit-empty`.

## 3D hero (reference video: `public/media/hero-bg.mp4`)
Full-bleed looping globe video behind the hero (muted, playsinline, poster, no autoplay for reduced motion or save-data, pause button, pause when off-screen). Scroll acts as a camera push-in (video scale and content fade by scroll progress), pointer parallax in layers (video, bolts, logo plate tilt), card tilt on hover. In the Next.js build use React Three Fiber only if it keeps Lighthouse performance above the thresholds; otherwise keep CSS 3D. Confirm the video's licence with the owner before launch (it came from a social media download).

## Promo lifecycle and sale
- MAVOREN30 is for the first 10 orders only. State lives in Upstash Redis (`promo:used`). `GET /api/promo` returns `{ active }`; the UI hides the code everywhere (popup, hero chip, FAQ item, terms row, estimator and form fields) and rejects it when `active` is false.
- After each confirmed order the owner calls `POST /api/admin/orders` with header `x-admin-token` (env `ADMIN_TOKEN`). The 11th order onward the code is gone automatically.
- When the code ends, the popup switches to the Year-End Sale card ("50% off on bulk orders", `src/data/sale.ts`) with a WhatsApp enquiry button, plus a sale banner in Offers and a terms row. Do not invent an end date or a code.
- Testimonials: `src/data/testimonials.ts` is empty on purpose. Never add invented testimonials; render the section only when real, permitted quotes exist.

## Measurement
GA4 via `NEXT_PUBLIC_GA4_ID`, loaded only after consent. Events: whatsapp_click, promo_applied, enquiry_opened, package_selected. Search Console + sitemap. Sentry for errors. Lighthouse thresholds in `lighthouserc.json`.

## Done means
Build, typecheck, Playwright and Lighthouse pass; no horizontal scroll at 375/768/1280; final report lists what was tested and what needs owner input (domain, DSN, GA4 id, refund terms, real testimonials, Watermelon UI link).

## Current design decisions (these override anything above)
- Theme: "Antique Parian" style. Dark: espresso black #0D0B09, cream text #F1E8D8, gold #C9A96B. Light: marble ivory #F5EFE4, brown ink #1B1510, gold #B8935A. Thin gold hairlines, faint gold rings behind the hero logo, gold lightning bolts. Fonts: Outfit (headings, light weight, slightly wide tracking) and Jost (body).
- Light and dark follow the device setting (`prefers-color-scheme`, live). No manual toggle.
- The Mavoren logo has no plate: transparent logo directly on the background with a soft gold glow and thin edge light. The hero stays dark in both modes; the footer stays dark.
- The hero video is tinted gold with a CSS filter. Confirm the video licence before launch.
- Content is final. Do not rewrite copy while porting.
