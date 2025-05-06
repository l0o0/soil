from fastapi import FastAPI
from app.routers import users, journals
import os

app = FastAPI()


# Include the routers
app.include_router(users.router)
# app.include_router(auth.router, prefix="/auth")
app.include_router(journals.router)