"""Main application setup for the ghmap_api service."""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from ghmap_api.database import init_db
from ghmap_api.router import content_log_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="ghmap-api",
    description="Project to allow community contributions to GHMap",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(content_log_router.router)
