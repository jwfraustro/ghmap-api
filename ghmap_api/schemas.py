from datetime import datetime
from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field


class StatusLog(IntEnum):
    open = 0
    close = 1
    shell = 2
    remove = 3
    bounce = 4
    download = 5
    upload = 6


class ContentLogEntrySchema(BaseModel):
    action: StatusLog = Field(..., examples=[StatusLog.shell])
    ip: str = Field(..., examples=["135.187.88.229"])
    fecha: str = Field(..., examples=["25/Mar/2000 - 14:37"])
    puerto: int = Field(..., examples=[0])
    file: str = Field(..., examples=["/var/log/syslog"])
    bounceIp: str = Field(..., examples=["1.2.3.4"])
    playerNetID: Optional[str] = Field(None, examples=["76561198000000000"])
    tutorial: Optional[bool] = Field(None, examples=[False])
    tokenTrace: Optional[str] = Field("", examples=[""])

    model_config = {"populate_by_name": True}


class ContentLogRequest(BaseModel):
    contentLog: list[ContentLogEntrySchema]


# --- Response schemas ---

class ContentLogEntryResponse(BaseModel):
    id: int
    action: Optional[int]
    ip: Optional[str]
    fecha: Optional[str]
    puerto: Optional[int]
    file: Optional[str]
    bounce_ip: Optional[str]
    player_net_id: Optional[str]
    tutorial: Optional[bool]
    token_trace: Optional[str]

    model_config = {"from_attributes": True}


class SubmissionResponse(BaseModel):
    id: int
    submitted_at: datetime
    entries: list[ContentLogEntryResponse]

    model_config = {"from_attributes": True}
