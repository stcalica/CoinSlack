FROM ubuntu:latest
MAINTAINER Kyle Calica "Kyle Calica"
RUN apt-get update -y
RUN apt-get install -y python3-dev  build-essential python-pip gunicorn
RUN pip install --upgrade setuptools
RUN pip install ez_setup
COPY . /app
WORKDIR /app
RUN pip install -r ./app/requirements.txt
CMD [ "gunicorn", "-b", ":8000", "app:app" ]
