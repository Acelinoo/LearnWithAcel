"""
FastAPI application factory and lifespan management.
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from app.api.v1.router import api_router
from app.core.cache import cache_manager
from app.core.config import settings
from app.core.database import prisma
from app.core.exceptions import http_exception_handler, unhandled_exception_handler

logger = logging.getLogger("app.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Connect Prisma and Cache Manager on startup, disconnect on shutdown."""
    try:
        if not prisma.is_connected():
            await prisma.connect()
    except Exception as e:
        logger.error(f"Prisma connection error during startup: {e}")

    try:
        await cache_manager.init_cache()
    except Exception as e:
        logger.error(f"Cache init error during startup: {e}")

    yield

    try:
        await cache_manager.close()
    except Exception:
        pass

    try:
        if prisma.is_connected():
            await prisma.disconnect()
    except Exception:
        pass


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    # ── GZip Response Compression ────────────────────────────────────────────
    # Compresses responses larger than 1KB by ~70% for faster mobile loads
    app.add_middleware(GZipMiddleware, minimum_size=1000)

    # ── CORS ─────────────────────────────────────────────────────────────────
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── Exception handlers ────────────────────────────────────────────────────
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)

    # ── Routers ───────────────────────────────────────────────────────────────
    app.include_router(api_router)

    # ── Root & Health check ───────────────────────────────────────────────────
    @app.get("/", tags=["Health"], summary="Root endpoint")
    async def root():
        return {
            "status": "ok",
            "name": settings.APP_NAME,
            "version": settings.APP_VERSION,
        }

    @app.get("/health", tags=["Health"], summary="Health check")
    async def health():
        return {"status": "ok", "version": settings.APP_VERSION}

    return app


app = create_app()
