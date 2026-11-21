import { test, expect } from '@playwright/test'

// Components must expose these data-testid values (see CLAUDE_CODE_PROMPT.md).
test('home has the brand headline', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByRole('heading', { level: 1 })).toContainText('Your Vision')
})

test('tier service button pre-fills the enquiry form', async ({ page }) => {
  await page.goto('/#services')
  await page.getByTestId('tier-service-business-website').click()
  await expect(page.getByTestId('chip-selected')).toContainText('Business Website')
})

test('promo code MAVOREN30 applies in the estimator', async ({ page }) => {
  await page.goto('/#plan')
  await page.getByTestId('estimator-package').selectOption('Business Website')
  await page.getByTestId('promo-input').fill('mavoren30')
  await page.getByTestId('promo-apply').click()
  await expect(page.getByTestId('estimator-total')).toContainText('₹4,899')
})

test('invalid promo code is rejected', async ({ page }) => {
  await page.goto('/#plan')
  await page.getByTestId('promo-input').fill('WRONG')
  await page.getByTestId('promo-apply').click()
  await expect(page.getByTestId('promo-message')).toContainText('not valid')
})

test('offer popup appears after scrolling two screens', async ({ page }) => {
  await page.goto('/')
  await expect(page.getByTestId('ad-popup')).toBeHidden()
  await page.evaluate(() => window.scrollTo(0, window.innerHeight * 2.5))
  await expect(page.getByTestId('ad-popup')).toBeVisible()
})

test('enquiry form opens a WhatsApp link, never claims delivery', async ({ page, context }) => {
  await page.goto('/contact')
  await page.getByTestId('enquiry-submit-empty').click()
  await expect(page.getByRole('alert')).toBeVisible()
})

test('sitemap, robots and 404', async ({ request, page }) => {
  expect((await request.get('/sitemap.xml')).ok()).toBeTruthy()
  expect(await (await request.get('/robots.txt')).text()).toContain('Sitemap')
  const res = await page.goto('/this-page-does-not-exist')
  expect(res?.status()).toBe(404)
})
