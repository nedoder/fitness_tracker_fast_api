from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import engine
from app.crud import body_part as body_part_crud
from app.schemas import body_part as body_part_schemas
from app.models import body_part as body_part_models
from app.dependencies import get_db

body_part_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/body_parts/", response_model=body_part_schemas.BodyPart)
def create_body_part(body_part: body_part_schemas.BodyPartCreate, db: Session = Depends(get_db)):
    return body_part_crud.create_body_part(db=db, body_part=body_part)

@router.get("/body_parts/", response_model=List[body_part_schemas.BodyPart])
def read_body_parts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    body_parts = body_part_crud.get_body_parts(db, skip=skip, limit=limit)
    return body_parts

@router.get("/body_parts/{body_part_id}", response_model=body_part_schemas.BodyPart)
def read_body_part(body_part_id: int, db: Session = Depends(get_db)):
    db_body_part = body_part_crud.get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return db_body_part

@router.put("/body_parts/{body_part_id}", response_model=body_part_schemas.BodyPart)
def update_body_part(body_part_id: int, body_part: body_part_schemas.BodyPartUpdate, db: Session = Depends(get_db)):
    db_body_part = body_part_crud.get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    return body_part_crud.update_body_part(db=db, body_part_id=body_part_id, body_part_data=body_part)

@router.delete("/body_parts/{body_part_id}", response_model=body_part_schemas.BodyPart)
def delete_body_part(body_part_id: int, db: Session = Depends(get_db)):
    db_body_part = body_part_crud.get_body_part(db, body_part_id=body_part_id)
    if db_body_part is None:
        raise HTTPException(status_code=404, detail="Body part not found")
    body_part_crud.delete_body_part(db=db, body_part_id=body_part_id)
    return db_body_part