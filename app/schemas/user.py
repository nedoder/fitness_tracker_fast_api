from datetime import datetime
from pydantic import BaseModel
from typing import Optional
class UserBase(BaseModel):
    username: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    date_of_birth: Optional[datetime]
    gender: Optional[str]
    height: Optional[float]
    weight: Optional[float]
    profile_picture: Optional[str]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class User(UserBase):
    id: int
    date_joined: datetime
    last_login: datetime

    class Config:
        orm_mode = True