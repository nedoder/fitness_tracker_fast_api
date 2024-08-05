from pydantic import BaseModel
from enum import Enum

class LevelEnum(str, Enum):
    BEGINNER = "BEGINNER"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"
    EXPERT = "EXPERT"

class LevelBase(BaseModel):
    name: LevelEnum

class LevelCreate(LevelBase):
    pass

class LevelUpdate(LevelBase):
    pass


class Level(LevelBase):
    id: int

    class Config:
        orm_mode = True


