import { NextResponse } from 'next/server'
import { timingSafeEqual } from 'node:crypto'
import { promoStatus, recordOrder } from '@/lib/promo-server'

function authorised(req: Request) {
  const token = req.headers.get('x-admin-token') ?? ''
  const expected = process.env.ADMIN_TOKEN ?? ''
  if (!expected || token.length !== expected.length) return false
  return timingSafeEqual(Buffer.from(token), Buffer.from(expected))
}

// Call once per confirmed order. The 11th order onwards the promo code and its popup disappear on their own.
export async function POST(req: Request) {
  if (!authorised(req)) return NextResponse.json({ error: 'unauthorised' }, { status: 401 })
  await recordOrder()
  return NextResponse.json(await promoStatus())
}
