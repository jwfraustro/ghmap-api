"""This module contains the API endpoints for the ghmap_api service."""

from typing import Annotated, Optional

from fastapi import APIRouter, Query
from fastapi_restful.cbv import cbv

from ghmap_api import schemas

router = APIRouter()


@cbv(router)
class MainRouter:
    """Router for ghmap_api API endpoints."""

    @router.get("/hello", summary="Example endpoint")
    def objobssap_request(
        self,
        name: Annotated[
            str,
            Query(
                ...,
                description="Your name",
                example="John Doe",
                alias="NAME",
            ),
        ],
    ):
        """A simple example endpoint that greets the user by name."""
        data = {"message": f"Hello, {name}!"}

        return data
