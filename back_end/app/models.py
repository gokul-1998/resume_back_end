# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base

class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    title = Column(String)
    summary = Column(Text)
    created_at = Column(DateTime)
