# routers/users.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session 
from .. import models, schemas, database
from fastapi import Depends
from typing import List

router = APIRouter()

# Define a Pydantic model for User
class User(BaseModel):
    name: str
    email: str
    password: str

# Define a GET route to fetch user data
@router.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(database.get_db)):

    users = db.query(models.User).all()
    return users

@router.get("/users/{username}", response_model=schemas.User)
def get_user(username: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# define a get method to check if username and email is available
@router.get("/users/check/{email}")
def check_user(email: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        raise HTTPException(status_code=409, detail="User already exists")
    else:
        return {"message": "User does not exist"}


# # Define a POST route to create a user
# @router.post("/users/")
# def create_user(user: User):
#     # Here you can implement logic to save the user to the database
#     return {"message": f"User {user.name} created successfully!", "user": user}
