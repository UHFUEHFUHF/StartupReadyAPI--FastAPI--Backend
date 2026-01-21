from  passlib.context import CryptContext
import hashlib

pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

def hashing_pass(password : str) -> str:
    small_pass = hashlib.sha256(password.encode("utf-8")).hexdigest()

    return pwd_context.hash(small_pass)


def Check_pass(plain_pass : str , hash_pass : str) -> bool:
    small_plain_pass = hashlib.sha256(plain_pass.encode("utf-8")).hexdigest()

    return pwd_context.verify(small_plain_pass , hash_pass)



