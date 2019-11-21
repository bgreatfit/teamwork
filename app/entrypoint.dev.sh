#!/bin/bash

# Collect static files
echo "Collectingggggg static files"

#python manage.py makemigrations
##
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done


python manage.py collectstatic --no-input

python manage.py runserver 0.0.0.0:9000

#

#$ celery worker -A cowrywise --loglevel=debug --concurrency=4
#celery -A cowrywise worker
#celery -A cowrywise beat
## Start server
echo "Starting server"
#
#python manage.py flush --no-input
#python manage.py collectstatic --no-input
#python manage.py runserver 0.0.0.0:9000
#exec "$@"
