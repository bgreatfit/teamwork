[![Build Status](https://travis-ci.org/bgreatfit/teamwork.svg?branch=master)](https://travis-ci.org/bgreatfit/teamwork) [![Coverage Status](https://coveralls.io/repos/github/bgreatfit/teamwork/badge.svg)](https://coveralls.io/github/bgreatfit/teamwork)
Docker environment for  Teamwork project, Django restframework with JWT , React
===========================================
# API Documentation:
# How to run
Dependencies:
  * Docker engine v19.03.1, or higher. Your OS provided package might be a little old, if you encounter problems, do upgrade. See [https://docs.docker.com/engine/installation](https://docs.docker.com/engine/installation)
  * Docker compose v1.24 or higher. See [docs.docker.com/compose/install](https://docs.docker.com/compose/install/)
  
Use git clone [https://github.com/bgreatfit/teamwork.git](https://github.com/bgreatfit/teamwork.git) to download project

Once you're done, simply `cd` to your project and run `docker-compose up -d`. This will initialise and start all the containers,
 and also run database migrations,collectstatic files see .entrypoint.sh for more info.
 then leave them running in the background.

## Services exposed outside your environment

You can access your application via **`127.0.0.1:8000`**, if you're running the containers directly.

## Hosts within your environment

username: **`root`**
password: **`root`**

Service|Hostname |Port number
-------|---------|-----------
web    |django   |8000
postgres|postgres |5432
nginx  |nginx    |8000


# Development hints

Customize the project name, database credentials in the .env file

# Docker compose cheatsheet

**Note:** you need to cd first to where your docker-compose.yml file lives.

  * Start containers in the background: `docker-compose up -d`
  * Start containers on the foreground: `docker-compose up`. You will see a stream of logs for every container running.
  * Stop containers: `docker-compose stop`
  * Kill containers: `docker-compose kill`
  * View container logs: `docker-compose logs`
  * Execute command inside of container: `docker-compose exec SERVICE_NAME COMMAND` where `COMMAND` is whatever you want to run. Examples:
    * Shell into the django container, `docker-compose exec django bash`
    * Open a mysql shell, `docker-compose exec mysql mysql -uroot -pCHOSEN_ROOT_PASSWORD`

# Docker general cheatsheet

**Note:** these are global commands and you can run them from anywhere.

  * To clear containers: `docker rm -f $(docker ps -a -q)`
  * To clear images: `docker rmi -f $(docker images -a -q)`
  * To clear volumes: `docker volume rm $(docker volume ls -q)`
  * To clear networks: `docker network rm $(docker network ls | tail -n+2 | awk '{if($2 !~ /bridge|none|host/){ print $1 }}')`
  
