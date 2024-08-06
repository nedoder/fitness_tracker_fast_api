from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum
class GenderEnum(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
class UserBase(BaseModel):
    username: str
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    gender: GenderEnum
    height: Optional[float] = None
    weight: Optional[float] = None

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class User(UserBase):
    id: int
    date_joined: datetime
    last_login: datetime

    class Config:
        orm_mode = True