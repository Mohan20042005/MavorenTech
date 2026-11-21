# Mavoren: status report (final build)

## Built and tested (automated, in a headless browser)
- 85 links on the page: none empty, none "#", every anchor exists; 23 external links open in a new tab with noopener; 3 mailto and 3 tel links with correct format.
- 24 buttons plus all links were clicked. 26 flow checks pass: pricing "Get a quote" (11), "What's included", tier filters, 11 service rows, package finder, estimator and promo, 3-step form with back/next, confirmation dialog, Open WhatsApp link, copy buttons, search, background video pause/play, offer popup (appears after two screens) and its copy/close, back-to-top, FAQ and blog accordions, mobile menu (every item, Escape), light/dark following the device setting live.
- No horizontal scroll at 375, 768 and 1280 px. No console errors.
- Contrast (WCAG): dark text 16:1, muted 7:1, gold links 11:1; light text 15.8:1, muted 6:1, gold links 6:1.
- Promo lifecycle tested in both states (used 0 and used 10).

## Features
Hero with looping video, scroll depth and pointer parallax; 10 text animations; hover, tilt and spotlight effects; lightning cursor (mouse devices only); loader; scroll progress; scrollspy nav; auto light/dark; toasts; 3 price tiers; 11 packages with inclusions; package finder; price estimator; promo MAVOREN30 (first 10 orders, applied when quoted); free domain offer (eligible bulk orders worth Rs 15,000 or above); 10% social media offer; Year-End Sale card after the promo ends; 6 projects (5 live links, 4 GitHub links, your screenshots); 3 blog posts; terms; FAQ; enquiry form that opens WhatsApp (never claims delivery); contact rows for mail, phone, WhatsApp, Instagram, Facebook. Reduced-motion and data-saver respected.

## Not built, and why
- Fake testimonials: not added. The client-feedback section is ready but stays hidden until you add real feedback.
- Cookie banner: the page sets no cookies and loads no analytics. GA4 behind consent is specified in the kit.
- Password toggle: there are no password fields.
- Separate pages (service pages, case studies, blog pages, 404), sitemap, canonical URLs: need the Next.js build and a domain.
- Refund/cancellation and privacy pages: need your terms.
- Sentry, Lighthouse CI, Playwright (TypeScript) tests, Watermelon UI, React Three Fiber: in the kit only, never run.
- Before/after slider and Tamil toggle: you asked to leave them out.

## Not tested
- Real iPhone behaviour (mail/phone apps, clipboard, video autoplay inside the Claude app viewer).
- Whether your five live project sites are online right now.
- Any of the Next.js kit (never installed or built).

## You must supply
Domain, GA4 id, Sentry DSN, Upstash Redis keys and ADMIN_TOKEN (promo counter in the Next.js build), 21st.dev API key (Watermelon UI), refund terms, real testimonials, video licence confirmation.
