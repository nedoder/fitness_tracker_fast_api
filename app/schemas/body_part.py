from pydantic import BaseModel
from typing import Optional
from enum import Enum

class BodyPartEnum(str, Enum):
    UPPER_BODY = "UPPER_BODY"
    LOWER_BODY = "LOWER_BODY"
    FULL_BODY = "FULL_BODY"
    CORE = "CORE"
    ARMS = "ARMS"
    LEGS = "LEGS"
    BACK = "BACK"
    SHOULDERS = "SHOULDERS"


class BodyPartBase(BaseModel):
    name: BodyPartEnum

class BodyPartCreate(BodyPartBase):
    pass

class BodyPartUpdate(BodyPartBase):
    pass

class BodyPart(BodyPartBase):
    id: int

    class Config:
        orm_mode = True
