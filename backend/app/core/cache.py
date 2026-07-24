"""
High-performance Async Caching System using Upstash Redis REST API and In-Memory fallback.
Includes Single-Flight Coalescing (Thundering Herd Protection) for production safety.
"""

import asyncio
import fnmatch
import json
import logging
import time
from functools import wraps
from typing import Any, Callable, Optional

import httpx

from app.core.config import settings

logger = logging.getLogger("app.cache")


class MemoryCacheBackend:
    """Thread-safe, non-blocking in-memory TTL cache storage."""

    def __init__(self):
        self._store: dict[str, tuple[Any, float]] = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str) -> Optional[Any]:
        async with self._lock:
            entry = self._store.get(key)
            if not entry:
                return None
            value, expires_at = entry
            if time.time() > expires_at:
                del self._store[key]
                return None
            return value

    async def set(self, key: str, value: Any, ttl: int) -> None:
        async with self._lock:
            expires_at = time.time() + ttl
            self._store[key] = (value, expires_at)

    async def delete(self, key: str) -> None:
        async with self._lock:
            self._store.pop(key, None)

    async def clear_pattern(self, pattern: str) -> int:
        """Clear all keys matching fnmatch pattern (e.g., 'content:*')."""
        count = 0
        async with self._lock:
            now = time.time()
            keys_to_delete = [
                k for k, (_, exp) in self._store.items()
                if now <= exp and fnmatch.fnmatch(k, pattern)
            ]
            for k in keys_to_delete:
                del self._store[k]
                count += 1
        return count

    async def clear(self) -> None:
        async with self._lock:
            self._store.clear()


class UpstashRestCacheBackend:
    """Upstash Redis HTTP / REST API Backend."""

    def __init__(self, rest_url: str, rest_token: str):
        self.url = rest_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {rest_token}"}
        self.client: Optional[httpx.AsyncClient] = None

    async def init(self) -> None:
        try:
            self.client = httpx.AsyncClient(headers=self.headers, timeout=5.0)
            res = await self.client.get(f"{self.url}/ping")
            if res.status_code == 200:
                logger.info("Successfully connected to Upstash Redis REST API.")
            else:
                logger.warning(f"Upstash REST ping returned status {res.status_code}. Falling back to Memory.")
                self.client = None
        except Exception as e:
            logger.warning(f"Failed to connect to Upstash REST API ({e}). Falling back to Memory Cache.")
            self.client = None

    async def close(self) -> None:
        if self.client:
            await self.client.aclose()
            self.client = None

    async def get(self, key: str) -> Optional[Any]:
        if not self.client:
            return None
        try:
            res = await self.client.get(f"{self.url}/get/{key}")
            if res.status_code == 200:
                data = res.json()
                result = data.get("result")
                if result is None:
                    return None
                return json.loads(result) if isinstance(result, str) else result
            return None
        except Exception as e:
            logger.error(f"Upstash REST GET error for key '{key}': {e}")
            return None

    async def set(self, key: str, value: Any, ttl: int) -> None:
        if not self.client:
            return
        try:
            raw = json.dumps(value)
            await self.client.post(f"{self.url}/set/{key}?EX={ttl}", content=raw)
        except Exception as e:
            logger.error(f"Upstash REST SET error for key '{key}': {e}")

    async def delete(self, key: str) -> None:
        if not self.client:
            return
        try:
            await self.client.get(f"{self.url}/del/{key}")
        except Exception as e:
            logger.error(f"Upstash REST DELETE error for key '{key}': {e}")

    async def clear_pattern(self, pattern: str) -> int:
        if not self.client:
            return 0
        try:
            res = await self.client.get(f"{self.url}/keys/{pattern}")
            if res.status_code == 200:
                keys = res.json().get("result", [])
                if keys:
                    pipeline_cmd = [["DEL", k] for k in keys]
                    await self.client.post(f"{self.url}/pipeline", json=pipeline_cmd)
                    return len(keys)
            return 0
        except Exception as e:
            logger.error(f"Upstash REST CLEAR_PATTERN error for '{pattern}': {e}")
            return 0

    async def clear(self) -> None:
        if self.client:
            try:
                await self.client.get(f"{self.url}/flushdb")
            except Exception as e:
                logger.error(f"Upstash REST FLUSHDB error: {e}")


class CacheManager:
    """
    Central Manager for Caching & Thundering Herd Protection.
    Uses Upstash Redis REST API if configured, otherwise Async In-Memory.
    """

    def __init__(self):
        self.memory_backend = MemoryCacheBackend()
        self.upstash_backend: Optional[UpstashRestCacheBackend] = None
        self._flight_locks: dict[str, asyncio.Lock] = {}
        self._global_flight_lock = asyncio.Lock()

    async def init_cache(self) -> None:
        """Initialize Upstash Redis REST connection if credentials are set."""
        try:
            url = (settings.UPSTASH_REDIS_REST_URL or "").strip()
            token = (settings.UPSTASH_REDIS_REST_TOKEN or "").strip()
            if url and token:
                if not url.startswith("http://") and not url.startswith("https://"):
                    url = f"https://{url}"
                self.upstash_backend = UpstashRestCacheBackend(url, token)
                await self.upstash_backend.init()
        except Exception as e:
            logger.warning(f"Failed to initialize Upstash Redis ({e}). Falling back to In-Memory Cache.")
            self.upstash_backend = None


    async def close(self) -> None:
        if self.upstash_backend:
            await self.upstash_backend.close()

    async def get(self, key: str) -> Optional[Any]:
        if not settings.CACHE_ENABLED:
            return None

        if self.upstash_backend:
            val = await self.upstash_backend.get(key)
            if val is not None:
                return val

        return await self.memory_backend.get(key)

    async def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        if not settings.CACHE_ENABLED:
            return

        ttl = ttl or settings.CACHE_DEFAULT_TTL

        # Store in Memory Backend
        await self.memory_backend.set(key, value, ttl)

        # Store in Upstash REST Backend if available
        if self.upstash_backend:
            await self.upstash_backend.set(key, value, ttl)

    async def delete(self, key: str) -> None:
        await self.memory_backend.delete(key)
        if self.upstash_backend:
            await self.upstash_backend.delete(key)

    async def clear_pattern(self, pattern: str) -> int:
        c1 = await self.memory_backend.clear_pattern(pattern)
        c2 = 0
        if self.upstash_backend:
            c2 = await self.upstash_backend.clear_pattern(pattern)
        logger.info(f"Invalidated cache for pattern '{pattern}' (Memory: {c1}, Upstash: {c2})")
        return max(c1, c2)

    async def get_or_set(
        self,
        key: str,
        fetch_coro: Callable[[], Any],
        ttl: Optional[int] = None,
    ) -> Any:
        """
        Get value from cache. On MISS, use Single-Flight lock so concurrent
        calls wait and execute fetch_coro only once.
        """
        # Fast path: check cache directly
        cached_val = await self.get(key)
        if cached_val is not None:
            return cached_val

        # Get or create lock for this key (Single-Flight Pattern)
        async with self._global_flight_lock:
            if key not in self._flight_locks:
                self._flight_locks[key] = asyncio.Lock()
            lock = self._flight_locks[key]

        async with lock:
            # Double check cache inside lock (another task might have populated it)
            cached_val = await self.get(key)
            if cached_val is not None:
                return cached_val

            # Cache MISS -> execute query once
            result = await fetch_coro()

            # Store in cache
            if result is not None:
                serializable = result.model_dump() if hasattr(result, "model_dump") else result
                await self.set(key, serializable, ttl)

            return result


# Global Singleton Instance
cache_manager = CacheManager()


def cached(
    key_prefix: str,
    ttl: Optional[int] = None,
    key_builder: Optional[Callable[..., str]] = None,
):
    """
    Decorator for caching async functions / API endpoints.
    Protects against thundering herd crashes via Single-Flight locking.
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if not settings.CACHE_ENABLED:
                return await func(*args, **kwargs)

            # Build Cache Key
            if key_builder:
                cache_key = key_builder(*args, **kwargs)
            else:
                arg_str = ":".join(str(a) for a in args)
                kwarg_str = ":".join(f"{k}={v}" for k, v in sorted(kwargs.items()))
                parts = [key_prefix, arg_str, kwarg_str]
                cache_key = ":".join(p for p in parts if p)

            async def _fetch():
                return await func(*args, **kwargs)

            return await cache_manager.get_or_set(cache_key, _fetch, ttl=ttl)

        return wrapper

    return decorator
