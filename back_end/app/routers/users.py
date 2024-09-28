# routers/users.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Define a Pydantic model for User
class User(BaseModel):
    name: str
    email: str
    password: str

# Define a GET route to fetch user data
@router.get("/users/")
def get_users():
    return [{"user_id": 1, "name": "John Doe"}, {"user_id": 2, "name": "Jane Doe"}]

# # Define a POST route to create a user
# @router.post("/users/")
# def create_user(user: User):
#     # Here you can implement logic to save the user to the database
#     return {"message": f"User {user.name} created successfully!", "user": user}
