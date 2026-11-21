import { Redis } from '@upstash/redis'
import { PROMO } from '@/data/promo'

const redis = Redis.fromEnv()
const KEY = 'promo:used'

export async function promoStatus() {
  const used = (await redis.get<number>(KEY)) ?? 0
  return { used, limit: PROMO.limit, active: used < PROMO.limit }
}

export const recordOrder = () => redis.incr(KEY)
