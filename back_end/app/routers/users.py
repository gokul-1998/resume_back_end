# routers/users.py
from fastapi import APIRouter, HTTPException, status
from datetime import datetime
import json
from pydantic import BaseModel
from sqlalchemy.orm import Session 
from .. import models, schemas, database
from fastapi import Depends
from typing import List

router = APIRouter(tags=['Users'])

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

# define a get method to check if username is available
@router.get("/users/check-name/{name}")
def check_name_availability(name: str, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.name == name).first()
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Name is already taken.")
    return {"available": True}


from datetime import datetime
import json

@router.put("/users/{username}", response_model=schemas.User)
def update_profile(username: str, profile: schemas.Profile, db: Session = Depends(database.get_db)):
    user_db = db.query(models.User).filter(models.User.name == username).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    profile = profile.dict()
    profile['updated_at'] = datetime.utcnow().isoformat()  # Convert datetime to ISO format string
    
    print(type(profile))    
    
    profile = json.dumps(profile)  # Now, it should be JSON serializable
    user_db.profile = profile
    
    db.commit()
    db.refresh(user_db)
    return user_db


# # Define a POST route to create a user
# @router.post("/users/")
# def create_user(user: User):
#     # Here you can implement logic to save the user to the database
#     return {"message": f"User {user.name} created successfully!", "user": user}
