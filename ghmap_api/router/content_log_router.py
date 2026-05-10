from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ghmap_api.database import get_db
from ghmap_api.models import ContentLogEntry
from ghmap_api.schemas import ContentLogRequest

router = APIRouter()


@router.post("/content-log", status_code=201)
def ingest_content_log(payload: ContentLogRequest, db: Session = Depends(get_db)):
    entries = [
        ContentLogEntry(
            action=entry.action,
            ip=entry.ip,
            fecha=entry.fecha,
            puerto=entry.puerto,
            file=entry.file,
            bounce_ip=entry.bounceIp,
        )
        for entry in payload.contentLog
    ]
    db.add_all(entries)
    db.commit()
    return {"inserted": len(entries)}
