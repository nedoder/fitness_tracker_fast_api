from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List
from app.schemas.user import User
from app.schemas.exercise import ExerciseInstance
class TrainingBase(BaseModel):
    user_id: int
    name: str
    description: Optional[str]
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: Optional[float]
    calories_burned: Optional[float]

class TrainingCreate(TrainingBase):
    pass

class TrainingUpdate(TrainingBase):
    pass

class Training(TrainingBase):
    id: int
    user: User
    exercises: List['ExerciseInstance'] = []

    class Config:
        orm_mode = True
