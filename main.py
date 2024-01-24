############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys

sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django

django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

from typing import List, Optional
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel, Field


app = FastAPI()


class Booking(BaseModel):
    id: int
    user_id: str
    room_id: str
    reserved_num: int
    start_datetime: datetime
    end_datetime: str


class User(BaseModel):
    id: int
    user_name: str = Field(max_length=12)


class Room(BaseModel):
    id: int
    room_name: str
    capacity: int = Field(max_length=12)


app = FastAPI()


@app.get("/")
def index():
    return {"status": "OK"}


@app.post("/users")
def create_user(user: User):
    return {"user": user}


@app.post("/rooms")
def create_room(room: Room):
    return {"room": room}


@app.post("/bookings")
def create_booking(booking: Booking):
    return {"booking": booking}
