FROM ubuntu:latest
MAINTAINER Willian de Morais <williandmorais@gmail.com>

RUN apt-get update && apt-get install -y python3-pip postgresql-client-9.5 libpq-dev python3-dev libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev
RUN pip3 install --upgrade pip

ADD . /code
WORKDIR /code

RUN pip3 install -r requirements.txt