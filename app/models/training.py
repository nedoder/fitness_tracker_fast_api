from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.db import Base

class Training(Base):
    __tablename__ = 'trainings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    duration = Column(Float)
    calories_burned = Column(Float)

    user = relationship("User", back_populates="trainings")
    exercises = relationship("ExerciseInstance", back_populates="training")