from sqlalchemy.orm import Session
from app.models import body_part as body_part_models
from app.schemas import body_part as body_part_schemas

def create_body_part(db: Session, body_part: body_part_schemas.BodyPartCreate):
    body_part_value = body_part_schemas.BodyPartEnum[body_part.name].value
    db_body_part = body_part_models.BodyPart(name=body_part_value)

    db.add(db_body_part)
    db.commit()
    db.refresh(db_body_part)
    response_data = {
        "id": db_body_part.id,
        "name": db_body_part.name.name 
    }
    
    return response_data

def get_body_part(db: Session, body_part_id: int):
    body_part = db.query(body_part_models.BodyPart).filter(body_part_models.BodyPart.id == body_part_id).first()
    if body_part is None:
        return None 
    return body_part_schemas.BodyPart(
        id=body_part.id,
        name=body_part_models.BodyPartEnum(body_part.name).name  
    )

def get_body_parts(db: Session, skip: int = 0, limit: int = 10):
    body_parts = db.query(body_part_models.BodyPart).offset(skip).limit(limit).all()
    return [
        body_part_schemas.BodyPart(
            id=bp.id,
            name=body_part_models.BodyPartEnum(bp.name).name  
        )
        for bp in body_parts
    ]

def update_body_part(db: Session, body_part_id: int, body_part_data: body_part_schemas.BodyPartUpdate):
    db_body_part = db.query(body_part_models.BodyPart).filter(body_part_models.BodyPart.id == body_part_id).first()
    if not db_body_part:
        return None
    for key, value in body_part_data.dict(exclude_unset=True).items():
        if key == "name" and isinstance(value, str):
            value = body_part_models.BodyPartEnum[value]
        setattr(db_body_part, key, value)
    db.commit()
    db.refresh(db_body_part)
    response_data = {
        "id": db_body_part.id,
        "name": db_body_part.name.name 
    }
    
    return response_data

def delete_body_part(db: Session, body_part_id: int):
    db_body_part = db.query(body_part_models.BodyPart).filter(body_part_models.BodyPart.id == body_part_id).first()
    if db_body_part:
        db.delete(db_body_part)
        db.commit()
    response_data = {
        "id": db_body_part.id,
        "name": db_body_part.name.name 
    }
    
    return response_data
