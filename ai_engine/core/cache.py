import redis.asyncio as redis
import json
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

async def get_cached(key: str):
    r = await redis.from_url(REDIS_URL)
    val = await r.get(key)
    return json.loads(val) if val else None

async def set_cached(key: str, value, ttl_seconds: int = 3600):
    r = await redis.from_url(REDIS_URL)
    await r.setex(key, ttl_seconds, json.dumps(value))
