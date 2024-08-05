from sqlalchemy import Column, Integer, Enum as SqlEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from enum import Enum
from app.db import Base

class BodyPartEnum(Enum):
    UPPER_BODY = 0
    LOWER_BODY = 1
    FULL_BODY = 2
    CORE = 3
    ARMS = 4
    LEGS = 5
    BACK = 6
    SHOULDERS = 7

class BodyPart(Base):
    __tablename__ = 'body_parts'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(SqlEnum(BodyPartEnum), unique=True, index=True)

    exercises = relationship("Exercise", back_populates="body_part")