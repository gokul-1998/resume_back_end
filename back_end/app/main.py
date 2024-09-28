# main.py
from fastapi import FastAPI
from .database import engine
from . import models
from .routers import users, resumes, auth  # Import the routers

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your frontend origin
    "http://127.0.0.1:8000",  # Alternative frontend origin
]

# Create all the database tables
models.Base.metadata.create_all(bind=engine)

# Include the routers
app.include_router(users.router)  # Users router
app.include_router(resumes.router)  # Resumes router
app.include_router(auth.router)  # Auth router



