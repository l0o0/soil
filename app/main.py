from fastapi import FastAPI
from app.routers import users, journals

app = FastAPI()


# Include the routers
app.include_router(users.router, prefix="/v1")
# app.include_router(auth.router, prefix="/auth")
app.include_router(journals.router, prefix="/v1")