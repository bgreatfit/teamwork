FROM python:3.7
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
RUN apt-get update \
    && apt-get -y install postgresql \
    && apt-get -y install zlib \
    && apt-get -y install jpeg \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
# un-comment the following two dependecies if you want to add library like pandas, scipy and numpy
# openblas \
# libstdc++

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
COPY /app/package.json /app/package.json
RUN npm install


# copy project
COPY /app/ /app/
# run entrypoint.sh
COPY app/entrypoint.dev.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
#ENTRYPOINT ["sh","/app/entrypoint.dev.sh"]
CMD gunicorn teamwork.wsgi:application --bind 0.0.0.0:$PORT
