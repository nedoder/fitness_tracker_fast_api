from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    level_id = Column(Integer, ForeignKey('levels.id'))
    body_part_id = Column(Integer, ForeignKey('body_parts.id'))
    calories_burned_per_minute = Column(Float)

    level = relationship("Level", back_populates="exercises")
    body_part = relationship("BodyPart", back_populates="exercises")

class ExerciseInstance(Base):
    __tablename__ = 'exercise_instances'
    id = Column(Integer, primary_key=True, index=True)
    training_id = Column(Integer, ForeignKey('trainings.id'))
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    reps = Column(Integer)
    sets = Column(Integer)
    weight = Column(Float)
    duration = Column(Float)

    training = relationship("Training", back_populates="exercises")
    exercise = relationship("Exercise")