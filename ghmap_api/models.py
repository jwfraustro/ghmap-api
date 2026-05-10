from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ghmap_api.database import Base


class Submission(Base):
    __tablename__ = "submission"

    id = Column(Integer, primary_key=True, index=True)
    submitted_at = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    client_ip = Column(String, nullable=False)

    entries = relationship("ContentLogEntry", back_populates="submission", cascade="all, delete-orphan")


class ContentLogEntry(Base):
    __tablename__ = "content_log"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submission.id", ondelete="CASCADE"), nullable=False)
    action = Column(Integer, nullable=True)
    ip = Column(String, nullable=True)
    fecha = Column(String, nullable=True)
    puerto = Column(Integer, nullable=True)
    file = Column(String, nullable=True)
    bounce_ip = Column(String, nullable=True)
    player_net_id = Column(String, nullable=True)
    tutorial = Column(Boolean, nullable=True)
    token_trace = Column(String, nullable=True)

    submission = relationship("Submission", back_populates="entries")
