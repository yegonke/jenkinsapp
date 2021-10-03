#!/bin/sh

# python manage.py migrate --no-input
# python manage.py collectstatic --no-input
python manage.py migrate totp --no-input
python manage.py migrate drfpasswordless --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn mobileotp.wsgi:application --bind 0.0.0.0:8000
