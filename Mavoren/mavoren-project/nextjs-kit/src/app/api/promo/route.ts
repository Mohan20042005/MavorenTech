import { NextResponse } from 'next/server'
import { promoStatus } from '@/lib/promo-server'

export const dynamic = 'force-dynamic'

// Public: only says whether the code is still active, never the count.
export async function GET() {
  const { active } = await promoStatus()
  return NextResponse.json({ active }, { headers: { 'Cache-Control': 'no-store' } })
}
