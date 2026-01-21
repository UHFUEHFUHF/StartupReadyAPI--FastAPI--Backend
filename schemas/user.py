from pydantic import BaseModel , EmailStr


class UserCreate(BaseModel):
    name : str
    password : str
    email : EmailStr


class UserLogin(BaseModel):
    email : EmailStr
    password : str

class UserToken(BaseModel):
    token : str






