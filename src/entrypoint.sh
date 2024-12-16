#!/bin/sh
#entrypoint specific for django that is used to automate some routine at startup

poetry run python manage.py makemigrations --no-input
poetry run python manage.py migrate --no-input
poetry run python manage.py collectstatic --no-input

DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME} DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL} poetry run python manage.py createsuperuser --noinput

#without this check celery throws a psycopg2 error despite connecting to Redis container
echo "Waiting for PostgreSQL"
while ! nc -z $DATABASE_HOST $DATABASE_PORT; do 
    sleep 0.1
done
echo "PostgreSQL is ready"

poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000

exec "$@"