FROM python:3.7.5-slim-buster
MAINTAINER Roman Kojnok <roman.kojnok@protonmail.com>

ENV INSTALL_PATH /fitness
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "fitness.app:create_app()"
