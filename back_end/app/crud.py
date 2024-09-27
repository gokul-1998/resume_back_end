# crud.py
from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime

def create_resume(db: Session, resume: schemas.ResumeCreate):
    db_resume = models.Resume(
        name=resume.name,
        title=resume.title,
        summary=resume.summary,
        created_at=datetime.utcnow(),
    )
    db.add(db_resume)
    db.commit()
    db.refresh(db_resume)
    return db_resume

def get_resume(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()

def get_resumes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Resume).offset(skip).limit(limit).all()
