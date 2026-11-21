# Mavoren: complete project

Everything for the Mavoren agency website in one folder.

## What is here
- `site/`: the finished website (single page). Open `site/index.html` in a browser, or deploy the folder. Keep `site/assets/hero-bg.mp4` next to it.
- `nextjs-kit/`: the Next.js + TypeScript handoff for the advanced build (typed data, SEO, sitemap, Sentry, Lighthouse CI, Playwright config and tests, promo counter API). Start with `CLAUDE_CODE_PROMPT.md`. This kit was written without running npm, so it must be installed, built and tested in Claude Code.
- `assets/`: transparent logos, favicon, your five project screenshots, hero video and poster.
- `docs/REPORT.md`: what is built, what was tested, what is missing, and what you must supply.
- `docs/templates/`: robots.txt and sitemap.xml templates (need your real domain).
- `tests/`: the Playwright (Python) checks used on the site. See `tests/README.md`.
- `previews/`: dark and light screenshots.

## Deploy the site (free)
1. Vercel: install the Vercel CLI, run `vercel` inside `site/`, accept the defaults. Or Netlify: drag the `site/` folder into Netlify Drop.
2. Add your domain in the host's dashboard. Buy nothing without deciding first.
3. After the domain exists, copy `docs/templates/robots.txt` and `sitemap.xml` into `site/`, replace the domain, and submit the sitemap in Google Search Console.

## Things you edit by hand in `site/index.html`
- Promo counter: find `{"limit":10,"used":0}`. Set `used` to the number of confirmed orders that used MAVOREN30. At 10 the code, popup, chips, FAQ and terms row disappear and the Year-End Sale card (50% off on bulk orders) appears.
- Client feedback: find `id=reviews-data>[]`. Paste real feedback as `[{"name":"","business":"","location":"","rating":5,"text":""}]`. The section shows only when the list has real entries.
- Contact details are in the contact and footer sections and in the JSON-LD block.

## Before launch
- Confirm you have the right to use the hero video (it came from a social media download).
- Add refund and cancellation terms and a privacy policy (not written because they need your terms).
- Test mail and phone links on your own phone.
