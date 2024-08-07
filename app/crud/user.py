from sqlalchemy.orm import Session
from app.models import user as user_models
from app.schemas import user as user_schemas
from app.utils import hash_password


def create_user(db: Session, user: user_schemas.UserCreate):
    hashed_password = hash_password.hash(user.password)
    user.password = hashed_password
    gender_enum = user_schemas.GenderEnum[user.gender]
    db_user = user_models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        gender=gender_enum
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    response_data = {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "date_joined": db_user.date_joined,
        "last_login": db_user.last_login,
        "gender": db_user.gender.name
    }
    
    return response_data

def get_user(db: Session, user_id: int):
    user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if user is None:
        return None 
    return user_schemas.User(
        id=user.id,
        username=user.username,
        gender=user_models.GenderEnum(user.gender).name,
        email=user.email,
        date_joined=user.date_joined,
        last_login=user.last_login
    )

def get_users(db: Session, skip: int = 0, limit: int = 10):
    users = db.query(user_models.User).offset(skip).limit(limit).all()
    return [
        user_schemas.User(
        id=user.id,
        username=user.username,
        gender=user_models.GenderEnum(user.gender).name,
        email=user.email,
        date_joined=user.date_joined,
        last_login=user.last_login
        ) for user in users
    ]

def update_user(db: Session, user_id: int, user_data: user_schemas.UserUpdate):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user:
        for key, value in user_data.dict(exclude_unset=True).items():
            if key == "gender" and isinstance(value, str):
                value = user_models.GenderEnum[value]
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    response_data = {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "date_joined": db_user.date_joined,
        "last_login": db_user.last_login,
        "gender": db_user.gender.name
    }
    
    return response_data

def delete_user(db: Session, user_id: int):
    db_user = db.query(user_models.User).filter(user_models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    response_data = {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "date_joined": db_user.date_joined,
        "last_login": db_user.last_login,
        "gender": db_user.gender.name
    }
    
    return response_data

def verify_password(plain_password, hashed_password):
    return hash_password.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(user_models.User).filter(user_models.User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user