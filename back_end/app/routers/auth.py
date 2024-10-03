from fastapi import APIRouter

from .. import database, schemas, models, utils
from sqlalchemy.orm import Session
from fastapi import Depends, status,HTTPException
from app import models, oauth2, schemas


router = APIRouter (tags=['Authentication'])


# @router.post("/login/")
# def login(user: dict):
#     return {"message": f"User {user['username']} logged in!"}

# @router.post("/register/")
# def register(user: dict):
#     return {"message": f"User {user['username']} registered successfully!"}


@router.post('/login', response_model=schemas.token)
def login(user_credentials:schemas.LoginRequest,db: Session = Depends(database.get_db)):

    User = db.query(models.User).filter(models.User.email == user_credentials.email).first()

    if not User:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password,User.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    

    access_token = oauth2.create_access_token(data ={"employee_id": User.id})

    return {"access_token": access_token, "token_type": "bearer","username": User.name}



@router.post("/register/", status_code=status.HTTP_201_CREATED)
def register(user: schemas.usercreate, db: Session = Depends(database.get_db)):
    try:
        hashed_password = utils.hash(user.password)
        user.password = hashed_password
        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise e