from passlib.context import CryptContext
from jose import JWTError , jwt
from dotenv import load_dotenv
from datetime import datetime , timedelta
import os
import hashlib

load_dotenv()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing_pass(password: str) -> str:
    small_pass = hashlib.sha256(password.encode("utf-8")).digest()
    return pwd_context.hash(small_pass)

def Check_pass(plain_pass: str, hash_pass: str) -> bool:
    small_plain_pass = hashlib.sha256(plain_pass.encode("utf-8")).digest()
    return pwd_context.verify(small_plain_pass, hash_pass)

Algorithm = "HS256"
TOKEN_EXPIRE_TIME = 60

def create_access_token(data : dict):

    payload = {
        "user" : data,
        "exp" : datetime.utcnow() + timedelta(minutes=60)
    }

    encode_jwt = jwt.encode(payload , os.getenv("SECRET_KEY") , algorithm=Algorithm)
    return encode_jwt



