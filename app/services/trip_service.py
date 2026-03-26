from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.models import Booking, Trip


class TripService:
    @staticmethod
    async def create_trip(db:AsyncSession,data):
        trip = Trip(**data.dict())
        db.add(trip)
        await db.commit()
        return trip
    @staticmethod
    async def get_all(db:AsyncSession):
        result = await db.execute(select(Trip))
        return bookings.scalars().all()
