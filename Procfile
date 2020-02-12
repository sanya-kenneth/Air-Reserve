release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn air_reserve.wsgi --log-file -