from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud.training import create_training, update_training, get_training, get_trainings, delete_training
from app.schemas. training import Training, TrainingCreate, TrainingUpdate
from app.models.training import Training as TrainingModel

TrainingModel.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/training/", response_model=Training)
def create_training(training: TrainingCreate, db: Session = Depends(get_db)):
    return create_training(db=db, training=training)

@router.get("/trainings/", response_model=List[Training])
def read_trainings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    trainings = get_trainings(db, skip=skip, limit=limit)
    return trainings

@router.get("/training/{training_id}", response_model=Training)
def read_training(training_id: int, db: Session = Depends(get_db)):
    db_training = get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return db_training

@router.put("/training/{training_id}", response_model=Training)
def update_training(training_id: int, training: TrainingCreate, db: Session = Depends(get_db)):
    db_training = get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    return update_training(db=db, training_id=training_id, training=training)

@router.delete("/training/{training_id}", response_model=Training)
def delete_training(training_id: int, db: Session = Depends(get_db)):
    db_training = get_training(db, training_id=training_id)
    if db_training is None:
        raise HTTPException(status_code=404, detail="Training not found")
    delete_training(db=db, training_id=training_id)
    return db_training