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

from db.models import Booking, Room, User


def get_users():
    return User.objects.all()


def get_rooms():
    return Room.objects.all()


def get_bookings():
    return Booking.objects.all()


# ユーザの作成
def create_user(user_name: str):
    user = User(user_name=user_name)
    user.save()
    return user


# ルームの作成
def create_room(room_name: str, capacity: int):
    room = Room(room_name=room_name, capacity=capacity)
    room.save()
    return room


# 予約の作成
def create_booking(
    user_id: int,
    room_id: int,
    reserved_num: int,
    start_datetime: str,
    end_datetime: str,
):
    user = User.objects.get(id=user_id)
    room = Room.objects.get(id=room_id)

    booking = Booking(
        user_id=user.id,
        room_id=room.id,
        reserved_num=reserved_num,
        start_datetime=start_datetime,
        end_datetime=end_datetime,
    )
    booking.save()
    return booking
