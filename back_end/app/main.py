# main.py
from fastapi import FastAPI
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .routers import users, resumes, auth  # Import the routers

app = FastAPI()

origins = [
    "http://localhost:5173",  # Your frontend origin
    "http://127.0.0.1:8000",  # Alternative frontend origin
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from your frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


# Create all the database tables
models.Base.metadata.create_all(bind=engine)

# Include the routers
app.include_router(users.router)  # Users router
app.include_router(resumes.router)  # Resumes router
app.include_router(auth.router)  # Auth router



