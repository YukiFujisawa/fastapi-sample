web: python manage.py makemigrations db
web: python manage.py migrate
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}