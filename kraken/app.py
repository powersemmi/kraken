from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from kraken.settings import settings

from .routes import build, health

API_VERSION = "0.0.1"

origins = ["*"]


def create_app():
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.SERVICE_NAME.title(),
        version=API_VERSION,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    v1 = "/api/v1"
    app.include_router(health.router)
    app.include_router(build.router, prefix=v1)
    return app
