from typing import List
from fastapi import FastAPI
from db import crud, schemas
import json

# from db.schemas import User, Room, Booking
# from db.crud import create_user, create_room, create_booking

app = FastAPI()


@app.get("/")
def index():
    return {"status": "OK"}


@app.get("/users", response_model=List[schemas.User])
def index_users():
    users = crud.get_users()
    return users


@app.get("/rooms", response_model=List[schemas.Room])
def index_rooms():
    rooms = crud.get_rooms()
    return rooms


@app.get("/bookings", response_model=List[schemas.Booking])
def index_bookings():
    bookings = crud.get_bookings()
    return bookings


@app.post("/users", response_model=schemas.User)
def create_users(user: schemas.User):
    user = crud.create_user(user_name=user.user_name)
    return user


@app.post("/rooms", response_model=schemas.Room)
def create_rooms(room: schemas.Room):
    room = crud.create_room(room_name=room.room_name, capacity=room.capacity)
    return room


@app.post("/bookings", response_model=schemas.Booking)
def create_bookings(booking: schemas.Booking):
    booking = crud.create_booking(
        user_id=booking.user_id,
        room_id=booking.room_id,
        reserved_num=booking.reserved_num,
        start_datetime=booking.start_datetime,
        end_datetime=booking.end_datetime,
    )
    return booking
