#!/bin/bash

# Collect static files
echo "Collect static files"

#python manage.py makemigrations
##
python manage.py migrate
#
python manage.py collectstatic --no-input --clear
#$ celery worker -A cowrywise --loglevel=debug --concurrency=4
#celery -A cowrywise worker
#celery -A cowrywise beat
## Start server
echo "Starting server"
#
#python manage.py flush --no-input
#python manage.py collectstatic --no-input
gunicorn --timeout=30 --workers=2 --bind 0.0.0.0:$PORT teamwork.wsgi:application
exec "$@"
