#!/bin/bash

# Collect static files
echo "Collect static files"

#python manage.py makemigrations
##
#HOST=db
#PORT=5432
#RETRIES=10
#DATABASE=teamwork_db
#USER=root

#while !</dev/tcp/db/5432; do sleep 1; done
#until d bash -c '(echo > /dev/tcp/$HOST/$PORT) > /dev/null 2>&1' || [ $RETRIES -eq 0 ]; do
#    echo "Waiting for Postgres server, $((RETRIES--)) remaining attempts..."
#        sleep 1
#
python manage.py migrate
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
