from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import engine
from app.crud import training as training_crud
from app.schemas import training as training_schemas
from app.models import training as training_models
from app.dependencies import get_db

training_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/trainings/", response_model=training_schemas.Training)
def create_training(training: training_schemas.TrainingCreate, db: Session = Depends(get_db)):
    return training_crud.create_training(db=db, training=training)

@router.get("/trainings/", response_model=List[training_schemas.Training])
def read_trainings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trainings = training_crud.get_trainings(db, skip=skip, limit=limit)
    return trainings

@router.get("/trainings/{training_id}", response_model=training_schemas.Training)
def read_training(training_id: int, db: Session = Depends(get_db)):
    db_training = training_crud.get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return db_training

@router.put("/trainings/{training_id}", response_model=training_schemas.Training)
def update_training(training_id: int, training: training_schemas.TrainingCreate, db: Session = Depends(get_db)):
    db_training = training_crud.get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return training_crud.update_training(db=db, training_id=training_id, training=training)

@router.delete("/trainings/{training_id}", response_model=training_schemas.Training)
def delete_training(training_id: int, db: Session = Depends(get_db)):
    db_training = training_crud.get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    training_crud.delete_training(db=db, training_id=training_id)
    return db_training