from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.booking import BookingCreate
from app.services.booking_service import BookingService
from database import get_db

router = APIRouter(prefix="/bookings", tags=["Bookings"])
@router.post("/")
async def create_booking(data:BookingCreate,db:AsyncSession=Depends(get_db)):
    booking = await BookingService.create_booking(db,data)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
@router.get("/")
async def get_booking(db:AsyncSession=Depends(get_db)):
    return await BookingService.get_all(db)
@router.delete("/{booking_id}")
async def delete_booking(booking_id:int,db:AsyncSession=Depends(get_db)):
    booking=await BookingService.delete_booking(db,booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return{
        "message": "Booking cancelled",
        "booking": booking
    }
@router.get("/user/{user_id}")
async def get_user_booking(user_id:int,db:AsyncSession=Depends(get_db)):
    return await BookingService.get_user_bookings(db,user_id)
@router.post("/{booking_id}/pay")
async def pay_booking(booking_id:int,db:AsyncSession=Depends(get_db)):
    booking = await BookingService.pay_booking(db,booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {
        "message": "Booking paid",
        "booking": booking
    }