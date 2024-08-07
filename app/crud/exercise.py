from sqlalchemy.orm import Session
from app.models import exercise as exercise_models
from app.schemas import exercise as exercise_schemas

def create_exercise(db: Session, exercise: exercise_schemas.ExerciseCreate):
    db_exercise= exercise_models.Exercise(
        name=exercise.name,
        description=exercise.description,
        level_id=exercise.level_id,
        body_part_id=exercise.body_part_id,
        calories_burned_per_minute=exercise.calories_burned_per_minute
    )

    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def get_exercise(db: Session, exercise_id: int):
    return db.query(exercise_models.Exercise).filter(exercise_models.Exercise.id == exercise_id).first()

def get_exercises(db: Session, skip: int = 0, limit: int = 10):
    return db.query(exercise_models.Exercise).offset(skip).limit(limit).all()

def update_exercise(db: Session, exercise_id: int, exercise: exercise_schemas.ExerciseUpdate):
    db_exercise = db.query(exercise_models.Exercise).filter(exercise_models.Exercise.id == exercise_id).first()
    if db_exercise:
        for key, value in exercise.dict(exclude_unset=True).items():
            setattr(db_exercise, key, value)
        db.commit()
        db.refresh(db_exercise)
    return db_exercise

def delete_exercise(db: Session, exercise_id: int):
    db_exercise = db.query(exercise_models.Exercise).filter(exercise_models.Exercise.id == exercise_id).first()
    if db_exercise:
        db.delete(db_exercise)
        db.commit()
    return db_exercise


def create_exercise_instance(db: Session, exercise_instance: exercise_schemas.ExerciseInstanceCreate):
    db_exercise_instance = exercise_models.ExerciseInstance(
        training_id=exercise_instance.training_id,
        exercise_id=exercise_instance.exercise_id,
        reps=exercise_instance.reps,
        sets=exercise_instance.sets,
        weight=exercise_instance.weight,
        duration=exercise_instance.duration
    )
    db.add(db_exercise_instance)
    db.commit()
    db.refresh(db_exercise_instance)
    return db_exercise_instance

def get_exercise_instance(db: Session, exercise_instance_id: int):
    return db.query(exercise_models.ExerciseInstance).filter(exercise_models.ExerciseInstance.id == exercise_instance_id).first()

def get_exercise_instances(db: Session, skip: int = 0, limit: int = 10):
    return db.query(exercise_models.ExerciseInstance).offset(skip).limit(limit).all()

def update_exercise_instance(db: Session, exercise_instance_id: int, exercise_instance_data: exercise_schemas.ExerciseInstanceUpdate):
    db_exercise_instance = db.query(exercise_models.ExerciseInstance).filter(exercise_models.ExerciseInstance.id == exercise_instance_id).first()
    if db_exercise_instance:
        for key, value in exercise_instance_data.dict(exclude_unset=True).items():
            setattr(db_exercise_instance, key, value)
        db.commit()
        db.refresh(db_exercise_instance)
    return db_exercise_instance

def delete_exercise_instance(db: Session, exercise_instance_id: int):
    db_exercise_instance = db.query(exercise_models.ExerciseInstance).filter(exercise_models.ExerciseInstance.id == exercise_instance_id).first()
    if db_exercise_instance:
        db.delete(db_exercise_instance)
        db.commit()
    return db_exercise_instance