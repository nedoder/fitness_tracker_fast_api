from sqlalchemy.orm import Session
from app.models.exercise import Exercise, ExerciseInstance
from app.schemas.exercise import ExerciseCreate, ExerciseUpdate, ExerciseInstanceCreate, ExerciseInstanceUpdate

def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise= Exercise()

    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def get_exercise(db: Session, exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()

def get_exercises(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Exercise).offset(skip).limit(limit).all()

def update_exercise(db: Session, exercise_id: int, exercise_data: ExerciseUpdate):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if db_exercise:
        for key, value in exercise_data.dict(exclude_unset=True).items():
            setattr(db_exercise, key, value)
        db.commit()
        db.refresh(db_exercise)
    return db_exercise

def delete_exercise(db: Session, exercise_id: int):
    db_exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if db_exercise:
        db.delete(db_exercise)
        db.commit()
    return db_exercise


def create_exercise_instance(db: Session, exercise_instance: ExerciseInstanceCreate):
    db_exercise_instance = ExerciseInstance()
    db.add(db_exercise_instance)
    db.commit()
    db.refresh(db_exercise_instance)
    return db_exercise_instance

def get_exercise_instance(db: Session, exercise_instance_id: int):
    return db.query(ExerciseInstance).filter(ExerciseInstance.id == exercise_instance_id).first()

def get_exercise_instances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ExerciseInstance).offset(skip).limit(limit).all()

def update_exercise_instance(db: Session, exercise_instance_id: int, exercise_instance_data: ExerciseInstanceUpdate):
    db_exercise_instance = db.query(ExerciseInstance).filter(ExerciseInstance.id == exercise_instance_id).first()
    if db_exercise_instance:
        for key, value in exercise_instance_data.dict(exclude_unset=True).items():
            setattr(db_exercise_instance, key, value)
        db.commit()
        db.refresh(db_exercise_instance)
    return db_exercise_instance

def delete_exercise_instance(db: Session, exercise_instance_id: int):
    db_exercise_instance = db.query(ExerciseInstance).filter(ExerciseInstance.id == exercise_instance_id).first()
    if db_exercise_instance:
        db.delete(db_exercise_instance)
        db.commit()
    return db_exercise_instance