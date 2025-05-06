from fastapi import APIRouter
from app.services.user import create_user
from app.schemas.user import UserCreate, UserResponse
from app.core.deps import DBSessionDep

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: DBSessionDep):
    return await create_user(db=db, user=user)