from sqlalchemy.orm import Session
from app.models import training as training_models
from app.schemas import training as training_schemas

def create_training(db: Session, training: training_schemas.TrainingCreate):
    db_training = training_models.Training(
        user_id=training.user_id,
        name=training.name,
        description=training.description,
        duration=training.duration,
        calories_burned=training.calories_burned,
        start_time=training.start_time,
        end_time=training.end_time
    )

    db.add(db_training)
    db.commit()
    db.refresh(db_training)
    response_data = {
        "id": db_training.id,
        "user_id": db_training.user_id,
        "user": {
            "id": db_training.user.id,
            "email": db_training.user.email,
            "username": db_training.user.username,
            "last_login": db_training.user.last_login,
            "date_joined": db_training.user.date_joined

        },
        "name": db_training.name,
        "description": db_training.description,
        "duration": db_training.duration,
        "calories_burned": db_training.calories_burned,
        "start_time": db_training.start_time,
        "end_time": db_training.end_time
    }
    
    return response_data


def get_training(db: Session, training_id: int):
    training = db.query(training_models.Training).filter(training_models.Training.id == training_id).first()
    if training is None:
        return None 
    response_data = {
        "id": training.id,
        "user_id": training.user_id,
        "user": {
            "id": training.user.id,
            "email": training.user.email,
            "username": training.user.username,
            "last_login": training.user.last_login,
            "date_joined": training.user.date_joined

        },
        "name": training.name,
        "description": training.description,
        "duration": training.duration,
        "calories_burned": training.calories_burned,
        "start_time": training.start_time,
        "end_time": training.end_time
    }
    
    return response_data
def get_trainings(db: Session, skip: int = 0, limit: int = 10):
    trainings = db.query(training_models.Training).offset(skip).limit(limit).all()
    response_data = [{
        "id": training.id,
        "user_id": training.user_id,
        "user": {
            "id": training.user.id,
            "email": training.user.email,
            "username": training.user.username,
            "last_login": training.user.last_login,
            "date_joined": training.user.date_joined

        },
        "name": training.name,
        "description": training.description,
        "duration": training.duration,
        "calories_burned": training.calories_burned,
        "start_time": training.start_time,
        "end_time": training.end_time
    } for training in trainings] 
    
    return response_data
def update_training(db: Session, training_id: int, training: training_schemas.TrainingUpdate):
    db_training = db.query(training_models.Training).filter(training_models.Training.id == training_id).first()
    if db_training:
        for key, value in training.dict(exclude_unset=True).items():
            setattr(db_training, key, value)
        db.commit()
        db.refresh(db_training)
    response_data = {
        "id": db_training.id,
        "user_id": db_training.user_id,
        "user": {
            "id": db_training.user.id,
            "email": db_training.user.email,
            "username": db_training.user.username,
            "last_login": db_training.user.last_login,
            "date_joined": db_training.user.date_joined

        },
        "name": db_training.name,
        "description": db_training.description,
        "duration": db_training.duration,
        "calories_burned": db_training.calories_burned,
        "start_time": db_training.start_time,
        "end_time": db_training.end_time
    }
    
    return response_data


def delete_training(db: Session, training_id: int):
    db_training = db.query(training_models.Training).filter(training_models.Training.id == training_id).first()
    if db_training:
        db.delete(db_training)
        db.commit()
    response_data = {
        "id": db_training.id
    }
    
    return response_data