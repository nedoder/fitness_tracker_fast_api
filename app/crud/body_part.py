from sqlalchemy.orm import Session
from app.models.body_part import BodyPart
from app.schemas.body_part import BodyPartCreate, BodyPartUpdate

def create_body_part(db: Session, user: BodyPartCreate):
    db_body_part = BodyPart(username=user.username, email=user.email, hashed_password=hashed_password)

    db.add(db_body_part)
    db.commit()
    db.refresh(db_body_part)
    return db_body_part

def get_body_part(db: Session, body_part_id: int):
    return db.query(BodyPart).filter(BodyPart.id == body_part_id).first()

def get_body_parts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(BodyPart).offset(skip).limit(limit).all()

def update_body_part(db: Session, body_part_id: int, body_part_data: BodyPartUpdate):
    db_body_part = db.query(BodyPart).filter(BodyPart.id == body_part_id).first()
    if db_body_part:
        for key, value in body_part_data.dict(exclude_unset=True).items():
            setattr(db_body_part, key, value)
        db.commit()
        db.refresh(db_body_part)
    return db_body_part

def delete_body_part(db: Session, body_part_id: int):
    db_body_part = db.query(BodyPart).filter(BodyPart.id == body_part_id).first()
    if db_body_part:
        db.delete(db_body_part)
        db.commit()
    return db_body_part