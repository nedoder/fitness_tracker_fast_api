from sqlalchemy import Column, Integer, Enum as SqlEnum
from enum import Enum
from sqlalchemy.orm import relationship
from app.db import Base

class LevelEnum(Enum):
    BEGINNER = 0
    INTERMEDIATE = 1
    ADVANCED = 2
    EXPERT = 3
    
class Level(Base):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(SqlEnum(LevelEnum), unique=True, index=True)

    exercises = relationship("Exercise", back_populates="level")