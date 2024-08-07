from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud import exercise as exercise_crud
from app.schemas import exercise as exercise_schemas
from app.models import exercise as exercise_models

exercise_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/exercises/", response_model=exercise_schemas.Exercise)
def create_user(exercise: exercise_schemas.ExerciseCreate, db: Session = Depends(get_db)):
    return exercise_crud.create_exercise(db=db, exercise=exercise)

@router.get("/exercises/", response_model=List[exercise_schemas.Exercise])
def read_exercises(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    exercises = exercise_crud.get_exercises(db, skip=skip, limit=limit)
    return exercises

@router.get("/exercises/{exercise_id}", response_model=exercise_schemas.Exercise)
def read_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = exercise_crud.get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return db_exercise

@router.put("/exercises/{exercise_id}", response_model=exercise_schemas.Exercise)
def update_exercise(exercise_id: int, exercise: exercise_schemas.ExerciseCreate, db: Session = Depends(get_db)):
    db_exercise = exercise_crud.get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return exercise_crud.update_exercise(db=db, exercise_id=exercise_id, exercise=exercise)

@router.delete("/exercises/{exercise_id}", response_model=exercise_schemas.Exercise)
def delete_exercise(exercise_id: int, db: Session = Depends(get_db)):
    db_exercise = exercise_crud.get_exercise(db, exercise_id=exercise_id)
    if db_exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    exercise_crud.delete_exercise(db=db, exercise_id=exercise_id)
    return db_exercise

@router.post("/exercise_instances/", response_model=exercise_schemas.ExerciseInstance)
def create_exercise_instance(exercise_instance: exercise_schemas.ExerciseInstanceCreate, db: Session = Depends(get_db)):
    return exercise_crud.create_exercise_instance(db=db, exercise_instance=exercise_instance)

@router.get("/exercise_instances/", response_model=List[exercise_schemas.ExerciseInstance])
def read_exercise_instances(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    exercise_instances = exercise_crud.get_exercise_instances(db, skip=skip, limit=limit)
    return exercise_instances

@router.get("/exercise_instances/{exercise_instance_id}", response_model=exercise_schemas.ExerciseInstance)
def read_exercise_instance(exercise_instance_id: int, db: Session = Depends(get_db)):
    db_exercise_instance = exercise_crud.get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return db_exercise_instance

@router.put("/exercise_instances/{exercise_instance_id}", response_model=exercise_schemas.ExerciseInstance)
def update_exercise_instance(exercise_instance_id: int, exercise_instance: exercise_schemas.ExerciseInstanceUpdate, db: Session = Depends(get_db)):
    db_exercise_instance = exercise_crud.get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return exercise_crud.update_exercise_instance(db=db, exercise_instance_id=exercise_instance_id, exercise_instance_data=exercise_instance)

@router.delete("/exercise_instances/{exercise_instance_id}", response_model=exercise_schemas.ExerciseInstance)
def delete_exercise_instance(exercise_instance_id: int, db: Session = Depends(get_db)):
    db_exercise_instance = exercise_crud.get_exercise_instance(db, exercise_instance_id=exercise_instance_id)
    if db_exercise_instance is None:
        raise HTTPException(status_code=404, detail="Exercise instance not found")
    return exercise_crud.delete_exercise_instance(db=db, exercise_instance_id=exercise_instance_id)