from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SessionMemory(BaseModel):
    session_id: str
    content: str
    created_at: datetime = datetime.utcnow()


class TaskMemory(BaseModel):
    task_id: str
    state: dict
    created_at: datetime = datetime.utcnow()


class VerifiedMemory(BaseModel):
    fact: str
    approved_by: str
    approved_at: datetime = datetime.utcnow()
