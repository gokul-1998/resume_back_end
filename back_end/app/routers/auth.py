from fastapi import APIRouter

router = APIRouter (tags=['Authentication'])


@router.post("/login/")
def login(user: dict):
    return {"message": f"User {user['username']} logged in!"}

@router.post("/register/")
def register(user: dict):
    return {"message": f"User {user['username']} registered successfully!"}
