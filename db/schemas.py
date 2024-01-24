from datetime import datetime
from pydantic import BaseModel, Field


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


class Booking(BaseModel):
    id: int
    user_id: int
    room_id: int
    reserved_num: int
    start_datetime: datetime
    end_datetime: datetime

    class Config:
        from_attributes = True
