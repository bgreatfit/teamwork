
#!/bin/bash

#echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
#docker push USER/REPO


docker ps
docker container ls
sudo docker login --username $HEROKU_DOCKER_USERNAME --password $HEROKU_AUTH_TOKEN registry.heroku.com
sudo docker tag teamwork_web:latest registry.heroku.com/teamworka/web
sudo docker inspect --format='{{.Id}}' registry.heroku.com/teamworka/web
if [ $TRAVIS_BRANCH == "master" ] && [ $TRAVIS_PULL_REQUEST == "false" ]; then sudo docker push registry.heroku.com/teamworka/web; fi

#    - heroku addons:create heroku-postgresql:hobby-dev -a mywebapp0

#heroku run container:release web -a teamworka
#heroku run python manage.py makemigrations -a teamworka
#heroku run python manage.py migrate -a teamworka
chmod +x heroku-container-release.sh

sudo chown $USER:docker ~/.docker
sudo chown $USER:docker ~/.docker/config.json
sudo chmod g+rw ~/.docker/config.json
