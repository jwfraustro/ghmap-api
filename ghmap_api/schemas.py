from typing import Optional
from pydantic import BaseModel, Field


class ContentLogEntrySchema(BaseModel):
    action: int
    ip: str
    fecha: str
    puerto: int
    file: str
    bounceIp: str
    playerNetID: Optional[str] = None
    tutorial: Optional[bool] = None
    tokenTrace: Optional[str] = ""

    model_config = {"populate_by_name": True}


class ContentLogRequest(BaseModel):
    contentLog: list[ContentLogEntrySchema]
