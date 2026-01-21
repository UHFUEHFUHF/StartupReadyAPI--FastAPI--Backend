from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from models.model import User as UserModel
from Database.session import get_db
from utils.security import hashing_pass , Check_pass


authRouter = APIRouter()

@authRouter.post("/login")
def login(userLogin: UserLogin):
    return userLogin.email


@authRouter.post("/signup")
def signup(signupDetails: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(UserModel).filter(
        UserModel.email == signupDetails.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = UserModel(
        name=signupDetails.name,
        email=signupDetails.email,
        password= hashing_pass(signupDetails.password)
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Something went wrong")

    return {
        "message": "User created successfully",
        "user_id": new_user.id
    }
