# schemas.py
import json
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ResumeBase(BaseModel):
    name: str
    title: str
    summary: str

class ResumeCreate(ResumeBase):
    pass

class Profile(BaseModel):
    profile:dict

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
    username: str

class LoginRequest(BaseModel):
    email: str
    password: str

class TokenData(BaseModel):
    id: Optional[str] = None

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: datetime
    profile: str
    resumes: List[Resume] = []

    class Config:
        orm_mode = True