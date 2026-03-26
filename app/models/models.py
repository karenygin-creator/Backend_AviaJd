from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column
class Base(DeclarativeBase): pass
class User(Base):
    __tablename__ = 'users'
    id:Mapped[int]=mapped_column(primary_key=True)
    email:Mapped[str]=mapped_column(String,unique=True)
    password:Mapped[str]=mapped_column(String)
class Trip(Base):
    __tablename__ = 'trips'
    id:Mapped[int]=mapped_column(primary_key=True)
    from_city:Mapped[str]=mapped_column(String)
    to_city:Mapped[str]=mapped_column(String)
    price:Mapped[float]=mapped_column(Float)
class Booking(Base):
    __tablename__ = 'bookings'
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(ForeignKey('users.id'))
    trip_id:Mapped[int]=mapped_column(ForeignKey('trips.id'))
