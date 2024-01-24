import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


# Sample User model
class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=50)
    capacity = models.IntegerField()


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    reserved_num = models.IntegerField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
