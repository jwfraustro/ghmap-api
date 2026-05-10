"""Configuration settings for ghmap-api"""
import os
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings"""

    PROJECT_NAME: str = "ghmap-api"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # CORS
    CORS_ORIGINS: List[str] = ["*"]

    # Add your settings here
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///./ghmap.db")

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
