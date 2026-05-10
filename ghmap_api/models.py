from sqlalchemy import Boolean, Column, Integer, String
from ghmap_api.database import Base


class ContentLogEntry(Base):
    __tablename__ = "content_log"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(Integer, nullable=True)
    ip = Column(String, nullable=True)
    fecha = Column(String, nullable=True)
    puerto = Column(Integer, nullable=True)
    file = Column(String, nullable=True)
    bounce_ip = Column(String, nullable=True)
    player_net_id = Column(String, nullable=True)
    tutorial = Column(Boolean, nullable=True)
    token_trace = Column(String, nullable=True)
