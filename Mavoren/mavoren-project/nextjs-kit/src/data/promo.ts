export const PROMO = { code: 'MAVOREN30', percent: 30, limit: 10, label: '30% off your first service' } as const

export const isPromo = (v: string) => v.trim().toUpperCase() === PROMO.code

// `active` comes from GET /api/promo; once the first 10 orders are used the code stops working everywhere.
export const applyPromo = (price: number, code: string, active: boolean) =>
  active && isPromo(code) ? Math.round((price * (100 - PROMO.percent)) / 100) : price
