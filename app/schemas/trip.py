from pydantic import BaseModel

class TripCreate(BaseModel):
    from_city:str
    to_city:str
    price:float