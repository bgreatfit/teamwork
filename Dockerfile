FROM python:3.7-alpine
# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

# Making source and static directory
RUN mkdir /app
RUN mkdir /static

# set work directory
WORKDIR /app

# Adding mandatory packages to docker
RUN apk update && apk add --no-cache \
    postgresql \
    zlib \
    jpeg
# un-comment the following two dependecies if you want to add library like pandas, scipy and numpy
# openblas \
# libstdc++

# Installing temporary packages required for installing requirements.pip
RUN apk add --no-cache --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev\
    zlib-dev \
    jpeg-dev
# un-comment if you want to install numpy, pandas, scipy etc and their supported dependencies
# g++ \
# openblas-dev \
# cmake \
# && ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN  curl -sL https://deb.nodesource.com/setup_12.x |  bash
RUN apt-get install -y nodejs

# Update pip
RUN pip install --upgrade pip

# **if you want to install scipy uncomment the following file**
# RUN pip3 install --no-cache-dir --disable-pip-version-check scipy==1.3.1

# install dependencies python
COPY /app/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# install dependencies nodejs
COPY /app/package.json /app/
RUN npm install

# removing temporary packages from docker and removing cache
RUN apk del build-deps && \
    find -type d -name __pycache__ -prune -exec rm -rf {} \; && \
    rm -rf ~/.cache/pip

EXPOSE 8000
# copy project
COPY /app/ /app/
# run entrypoint.sh
COPY app/entrypoint.dev.sh /app/entrypoint.dev.sh
RUN chmod +x /app/entrypoint.dev.sh
#ENTRYPOINT ["/app/entrypoint.dev.sh"]
CMD ["sh","/entrypoint.dev.sh"]

