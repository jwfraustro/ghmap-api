from pydantic import BaseModel, Field


class ContentLogEntrySchema(BaseModel):
    action: int
    ip: str
    fecha: str
    puerto: int
    file: str
    bounceIp: str = Field(alias="bounceIp")

    model_config = {"populate_by_name": True}


class ContentLogRequest(BaseModel):
    contentLog: list[ContentLogEntrySchema]
