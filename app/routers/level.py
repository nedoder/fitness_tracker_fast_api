from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud.level import create_level, update_level, get_level, get_levels, delete_level
from app.schemas.level import Level, LevelCreate, LevelUpdate
from app.models.level import Level as LevelModel

LevelModel.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/level/", response_model=Level)
def create_level(level: LevelCreate, db: Session = Depends(get_db)):
    return create_level(db=db, level=level)

@router.get("/levels/", response_model=List[Level])
def read_levels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    levels = get_levels(db, skip=skip, limit=limit)
    return levels

@router.get("/level/{level_id}", response_model=Level)
def read_level(level_id: int, db: Session = Depends(get_db)):
    db_level = get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return db_level

@router.put("/level/{level_id}", response_model=Level)
def update_level(level_id: int, user: LevelCreate, db: Session = Depends(get_db)):
    db_level = get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return update_level(db=db, level_id=level_id, user=user)

@router.delete("/level/{level_id}", response_model=Level)
def delete_level(level_id: int, db: Session = Depends(get_db)):
    db_level = get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    delete_level(db=db, level_id=level_id)
    return db_level