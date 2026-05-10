from sqlalchemy import Column, Integer, String
from ghmap_api.database import Base


class ContentLogEntry(Base):
    __tablename__ = "content_log"

    id = Column(Integer, primary_key=True, index=True)
    action = Column(Integer, nullable=False)
    ip = Column(String, nullable=False)
    fecha = Column(String, nullable=False)
    puerto = Column(Integer, nullable=False)
    file = Column(String, nullable=False)
    bounce_ip = Column(String, nullable=False)
