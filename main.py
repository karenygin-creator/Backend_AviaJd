from fastapi import FastAPI
from app.models.models import Base
from app.routers.auth import router as auth_router
from app.routers.bookings import router as bookings_router

from database import engine
app=FastAPI()
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth_router)
app.include_router(bookings_router)