from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud import level as level_crud
from app.schemas import level as level_schemas
from app.models import level as level_models

level_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/levels/", response_model=level_schemas.Level)
def create_level(level: level_schemas.LevelCreate, db: Session = Depends(get_db)):
    return level_crud.create_level(db=db, level=level)

@router.get("/levels/", response_model=List[level_schemas.Level])
def read_levels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    levels = level_crud.get_levels(db, skip=skip, limit=limit)
    return levels

@router.get("/levels/{level_id}", response_model=level_schemas.Level)
def read_level(level_id: int, db: Session = Depends(get_db)):
    db_level = level_crud.get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return db_level

@router.put("/levels/{level_id}", response_model=level_schemas.Level)
def update_level(level_id: int, level: level_schemas.LevelUpdate, db: Session = Depends(get_db)):
    db_level = level_crud.get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    return level_crud.update_level(db=db, level_id=level_id, level=level)

@router.delete("/levels/{level_id}", response_model=level_schemas.Level)
def delete_level(level_id: int, db: Session = Depends(get_db)):
    db_level = level_crud.get_level(db, level_id=level_id)
    if db_level is None:
        raise HTTPException(status_code=404, detail="Level not found")
    level_crud.delete_level(db=db, level_id=level_id)
    return db_level