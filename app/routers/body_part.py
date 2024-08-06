from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal, engine
from app.crud.body_part import create_body_part, update_body_part, get_body_part, get_body_parts, delete_body_part
from app.schemas.body_part import BodyPart, BodyPartCreate, BodyPartUpdate
from app.models import body_part as body_part_models

body_part_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/body_part/", response_model=BodyPart)
def create_body_part(body_part: BodyPartCreate, db: Session = Depends(get_db)):
    return create_body_part(db=db, body_part=body_part)

@router.get("/body_parts/", response_model=List[BodyPart])
def read_body_parts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    body_parts = get_body_parts(db, skip=skip, limit=limit)
    return body_parts

@router.get("/body_part/{body_part_id}", response_model=BodyPart)
def read_body_part(body_part_id: int, db: Session = Depends(get_db)):
    db_body_part = get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return db_body_part

@router.put("/body_part/{body_part_id}", response_model=BodyPart)
def update_body_part(body_part_id: int, body_part: BodyPartCreate, db: Session = Depends(get_db)):
    db_body_part = get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return update_body_part(db=db, body_part_id=body_part_id, body_part=body_part)

@router.delete("/body_part/{body_part_id}", response_model=BodyPart)
def delete_body_part(body_part_id: int, db: Session = Depends(get_db)):
    db_body_part = get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    delete_body_part(db=db, body_part_id=body_part_id)
    return db_body_part