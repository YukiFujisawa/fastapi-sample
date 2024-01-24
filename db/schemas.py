from datetime import datetime
from pydantic import BaseModel, Field


class Booking(BaseModel):
    id: int
    user_id: str
    room_id: str
    reserved_num: int
    start_datetime: datetime
    end_datetime: str

    class Config:
        from_attributes = True


class User(BaseModel):
    id: int
    user_name: str = Field(max_length=12)

    class Config:
        from_attributes = True


class Room(BaseModel):
    id: int
    room_name: str
    capacity: int

    class Config:
        from_attributes = True
