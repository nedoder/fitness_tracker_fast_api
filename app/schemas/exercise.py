from pydantic import BaseModel
from typing import Optional
class ExerciseBase(BaseModel):
    name: str
    description: Optional[str]
    level_id: int
    body_part_id: int
    calories_burned_per_minute: float

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseUpdate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int

    class Config:
        orm_mode = True

class ExerciseInstanceBase(BaseModel):
    training_id: int
    exercise_id: int
    reps: Optional[int]
    sets: Optional[int]
    weight: Optional[float]
    duration: Optional[float]

class ExerciseInstanceCreate(ExerciseInstanceBase):
    pass

class ExerciseInstanceUpdate(ExerciseInstanceBase):
    pass


class ExerciseInstance(ExerciseInstanceBase):
    id: int

    class Config:
        orm_mode = True