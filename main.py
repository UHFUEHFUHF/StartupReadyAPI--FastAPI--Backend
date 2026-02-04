from fastapi import FastAPI
from routes.auth import authRouter
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

app.include_router(authRouter , prefix="/auth" , tags=["Auth"])



