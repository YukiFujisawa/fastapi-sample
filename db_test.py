# Seed a few users in the database
# User.objects.create(user_name="Dan")
# User.objects.create(user_name="Robert")

from db.crud import get_users

users = get_users()

for u in users:
    print(f"ID: {u.id} \tUsername: {u.user_name}")
