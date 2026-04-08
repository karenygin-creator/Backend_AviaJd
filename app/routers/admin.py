from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_only

from app.services.user_service import UserService
from database import get_db

router=APIRouter(prefix="/admin",tags=["Admin"])
async def check_admin(db:AsyncSession,admin_id:int):
    admin=await UserService.get_user_by_id(db,admin_id)
    if not admin or admin.role!="admin":
        return None
    return admin
@router.get("/users")
async def get_users(admin_id:int,db:AsyncSession=Depends(get_db)):
    admin=await check_admin(db,admin_id)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return await UserService.get_user_all(db)