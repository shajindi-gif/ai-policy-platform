from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    command = Column(Text, nullable=False)
    status = Column(String(50), default="pending", nullable=False)
    result = Column(Text, nullable=True)
    agent_name = Column(String(100), default="general_agent", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
