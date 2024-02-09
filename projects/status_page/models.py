from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class StatusEvent(Base):
    __tablename__ = 'status_events'

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, index=True)
    detail = Column(String)
    time_created = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String)
    time_resolved = Column(DateTime, nullable=True)
