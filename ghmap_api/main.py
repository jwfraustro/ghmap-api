"""This module contains the main application setup for the ghmap_api service."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ghmap_api.config.settings import settings
from ghmap_api.middleware import UppercaseQueryParamsMiddleware
from ghmap_api.router import ghmap_api_router, vosi

app = FastAPI(
    title="ghmap-api",
    description="Project to allow community contributions to GHMap",
    version="0.1.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware
app.add_middleware(UppercaseQueryParamsMiddleware)

# Routers
app.include_router(ghmap_api_router.router)
app.include_router(vosi.vosi_router)


@app.get("/")
async def root():
    return {"message": "Welcome to ghmap-api"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}