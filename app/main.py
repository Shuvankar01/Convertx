"""FastAPI application factory."""
from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import get_settings
from app.db.session import init_db
from app.routers import converter, favorites, history, pages, settings as settings_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


def create_app() -> FastAPI:
    cfg = get_settings()
    app = FastAPI(
        title=cfg.app_name,
        description=cfg.tagline,
        version="1.0.0",
        lifespan=lifespan,
    )
    app.mount(
        "/static",
        StaticFiles(directory=str(cfg.static_dir)),
        name="static",
    )
    app.include_router(pages.router)
    app.include_router(converter.router)
    app.include_router(history.router)
    app.include_router(favorites.router)
    app.include_router(settings_router.router)
    return app


app = create_app()
