from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud.exercise import create_exercise, update_exercise, get_exercise, get_exercises, delete_exercise, create_exercise_instance, update_exercise_instance, get_exercise_instance, get_exercise_instances, delete_exercise_instance
from app.schemas.exercise import Exercise, ExerciseCreate, ExerciseUpdate, ExerciseInstance, ExerciseInstanceCreate, ExerciseInstanceUpdate
from app.models.exercise import Exercise as ExerciseModel
from app.models.exercise import ExerciseInstance as ExerciseInstanceModel

ExerciseModel.Base.metadata.create_all(bind=engine)
ExerciseInstanceModel.Base.metadata.create_all(bind=engine)


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/exercise/", response_model=Exercise)
def create_user(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    return create_exercise(db=db, exercise=exercise)

@router.get("/exercises/", response_model=List[Exercise])
def read_exercises(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    exercises = get_exercises(db, skip=skip, limit=limit)
    return exercises

@router.get("/exercise/{exercise_id}", response_model=Exercise)
def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise

@router.put("/exercise/{exercise_id}", response_model=Exercise)
def update_exercise(exercise_id: int, exercise: ExerciseCreate, db: Session = Depends(get_db)):
    db_exercise = get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return update_exercise(db=db, exercise_id=exercise_id, exercise=exercise)

@router.delete("/exercise/{exercise_id}", response_model=Exercise)
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    delete_exercise(db=db, exercise_id=exercise_id)
    return db_exercise

@router.post("/exercise_instance/", response_model=ExerciseInstance)
def create_exercise_instance(exercise_instance: ExerciseInstanceCreate, db: Session = Depends(get_db)):
    return create_exercise_instance(db=db, exercise_instance=exercise_instance)

@router.get("/exercise_instances/", response_model=List[ExerciseInstance])
def read_exercise_instances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    exercise_instances = get_exercise_instances(db, skip=skip, limit=limit)
    return exercise_instances

@router.get("/exercise_instance/{exercise_instance_id}", response_model=ExerciseInstance)
def read_exercise_instance(exercise_instance_id: int, db: Session = Depends(get_db)):
    db_exercise_instance = get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return db_exercise_instance

@router.put("/exercise_instance/{exercise_instance_id}", response_model=ExerciseInstance)
def update_exercise_instance(exercise_instance_id: int, exercise_instance: ExerciseInstanceUpdate, db: Session = Depends(get_db)):
    db_exercise_instance = get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return update_exercise_instance(db=db, exercise_instance_id=exercise_instance_id, exercise_instance_data=exercise_instance)

@router.delete("/exercise_instance/{exercise_instance_id}", response_model=ExerciseInstance)
def delete_exercise_instance(exercise_instance_id: int, db: Session = Depends(get_db)):
    db_exercise_instance = get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return delete_exercise_instance(db=db, exercise_instance_id=exercise_instance_id)