from typing import Optional

from fastapi import APIRouter, Depends, Query, Request
from sqlalchemy.orm import Session

from ghmap_api.database import get_db
from ghmap_api.models import ContentLogEntry, Submission
from ghmap_api.schemas import ContentLogRequest, SubmissionResponse

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


@router.get("/submissions", response_model=list[SubmissionResponse])
def get_submissions(
    request: Request,
    ip: Optional[str] = Query(None, description="IP address that submitted the logs. Defaults to the requester's IP."),
    db: Session = Depends(get_db),
):
    filter_ip = ip or request.client.host
    return db.query(Submission).filter(Submission.client_ip == filter_ip).all()
