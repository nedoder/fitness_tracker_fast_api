from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db import engine
from app.crud import user as user_crud
from app.schemas import user as user_schemas
from app.models import user as user_models
from app.utils.authentication import create_access_token
from app.dependencies import get_db, get_current_user

user_models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/users/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)

@router.get("/users/", response_model=List[user_schemas.User])
def read_users(skip: int = 0, limit: int = 10, users: user_schemas.User = Depends(get_current_user)):
    _, db = users
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/users/me", response_model=user_schemas.User)
def read_users_me(current_user: user_schemas.User = Depends(get_current_user)):
    current_user, _ = current_user
    return current_user

@router.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    current_user, db = current_user
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/users/{user_id}", response_model=user_schemas.User)
def update_user(user_id: int, user: user_schemas.UserUpdate , current_user: user_schemas.User = Depends(get_current_user)):
    _, db = current_user
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_crud.update_user(db=db, user_id=user_id, user_data=user)

@router.delete("/users/{user_id}", response_model=user_schemas.User)
def delete_user(user_id: int, current_user: user_schemas.User = Depends(get_current_user)):
    _, db = current_user
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_crud.delete_user(db=db, user_id=user_id)
    return db_user

@router.post("/login", response_model=user_schemas.Token)
def login(login_request: user_schemas.LoginRequest, db: Session = Depends(get_db)):
    user = user_crud.authenticate_user(db, login_request.username, login_request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

