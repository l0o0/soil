from fastapi import FastAPI
from app.middleware.logging import logging_middleware
from app.routers import users, journals

app = FastAPI()

# Middlewares
app.middleware("http")(logging_middleware)


# Include the routers
app.include_router(users.router)
# app.include_router(auth.router, prefix="/auth")
app.include_router(journals.router)