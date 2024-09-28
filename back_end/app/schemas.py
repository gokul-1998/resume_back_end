# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ResumeBase(BaseModel):
    name: str
    title: str
    summary: str

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class usercreate(BaseModel):
    name: str
    email: str
    password: str

class token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    id: Optional[str] = None