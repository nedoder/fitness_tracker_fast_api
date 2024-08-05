from sqlalchemy.orm import Session
from app.models.level import Level
from app.schemas.level import LevelCreate, LevelUpdate

def create_level(db: Session, user: LevelCreate):
    db_level = Level(username=user.username, email=user.email, hashed_password=hashed_password)

    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    return db_level

def get_level(db: Session, level_id: int):
    return db.query(Level).filter(Level.id == level_id).first()

def get_levels(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Level).offset(skip).limit(limit).all()

def update_level(db: Session, level_id: int, level_data: LevelUpdate):
    db_level = db.query(Level).filter(Level.id == level_id).first()
    if db_level:
        for key, value in level_data.dict(exclude_unset=True).items():
            setattr(db_level, key, value)
        db.commit()
        db.refresh(db_level)
    return db_level

def delete_level(db: Session, level_id: int):
    db_level = db.query(Level).filter(Level.id == level_id).first()
    if db_level:
        db.delete(db_level)
        db.commit()
    return db_level