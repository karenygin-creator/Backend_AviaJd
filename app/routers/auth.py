from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate
from app.services.user_service import UserService
from database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(data:UserCreate,db:AsyncSession=Depends(get_db)):
    return await UserService.create_user(db,data.email,data.password)