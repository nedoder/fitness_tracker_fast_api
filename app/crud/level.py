from sqlalchemy.orm import Session
from app.models import level as level_models
from app.schemas import level as level_schemas

def create_level(db: Session, level: level_schemas.LevelCreate):
    level_enum_value = level_schemas.LevelEnum[level.name].value
    db_level = level_models.Level(name=level_enum_value)

    db.add(db_level)
    db.commit()
    db.refresh(db_level)
    response_data = {
        "id": db_level.id,
        "name": db_level.name.name 
    }
    
    return response_data

def get_level(db: Session, level_id: int):
    level =  db.query(level_models.Level).filter(level_models.Level.id == level_id).first()
    if level is None:
        return None 
    return level_schemas.Level(
        id=level.id,
        name=level_models.LevelEnum(level.name).name  
    )

def get_levels(db: Session, skip: int = 0, limit: int = 10):
    levels =  db.query(level_models.Level).offset(skip).limit(limit).all()
    return [
        level_schemas.Level(
            id=bp.id,
            name=level_models.LevelEnum(bp.name).name  
        )
        for bp in levels
    ]

def update_level(db: Session, level_id: int, level: level_schemas.LevelUpdate):
    db_level = db.query(level_models.Level).filter(level_models.Level.id == level_id).first()
    if not db_level:
        return None
    for key, value in level.dict(exclude_unset=True).items():
        if key == "name" and isinstance(value, str):
            value = level_models.LevelEnum[value]
        setattr(db_level, key, value)
    db.commit()
    db.refresh(db_level)
    response_data = {
        "id": db_level.id,
        "name": db_level.name.name 
    }
    
    return response_data

def delete_level(db: Session, level_id: int):
    db_level = db.query(level_models.Level).filter(level_models.Level.id == level_id).first()
    if db_level:
        db.delete(db_level)
        db.commit()
    response_data = {
        "id": db_level.id,
        "name": db_level.name.name 
    }
    
    return response_data