from fastapi import FastAPI
from routes.auth import authRouter

app = FastAPI()

app.include_router(authRouter , prefix="/auth")


