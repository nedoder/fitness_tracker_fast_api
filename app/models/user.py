from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SqlEnum, Float
from enum import Enum
from sqlalchemy.orm import relationship
from app.db import Base

class GenderEnum(Enum):
    MALE = 0
    FEMALE = 1
    OTHER = 2
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    date_of_birth = Column(DateTime)
    gender = Column(SqlEnum(GenderEnum))
    height = Column(Float)
    weight = Column(Float)
    date_joined = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, default=datetime.utcnow)

    training = relationship("Training", back_populates="user")