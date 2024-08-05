from fastapi import FastAPI
from app.routers import user, level, training, exercise, body_part
app = FastAPI()

app.include_router(user.router)
app.include_router(level.router)
app.include_router(training.router)
app.include_router(exercise.router)
app.include_router(body_part.router)
