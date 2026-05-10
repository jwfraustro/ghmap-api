from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from ghmap_api.database import get_db
from ghmap_api.models import ContentLogEntry, Submission
from ghmap_api.schemas import ContentLogRequest

router = APIRouter()


@router.post("/content-log", status_code=201)
def ingest_content_log(request: Request, payload: ContentLogRequest, db: Session = Depends(get_db)):
    submission = Submission(client_ip=request.client.host)
    db.add(submission)
    db.flush()

    entries = [
        ContentLogEntry(
            submission_id=submission.id,
            action=entry.action,
            ip=entry.ip,
            fecha=entry.fecha,
            puerto=entry.puerto,
            file=entry.file,
            bounce_ip=entry.bounceIp,
            player_net_id=entry.playerNetID,
            tutorial=entry.tutorial,
            token_trace=entry.tokenTrace,
        )
        for entry in payload.contentLog
    ]
    db.add_all(entries)
    db.commit()
    return {"submission_id": submission.id, "inserted": len(entries)}
