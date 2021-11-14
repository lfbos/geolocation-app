FROM python:3.8-slim
MAINTAINER Luis Boscan <lboscannava@gmail.com>

# Set environment variables
ENV HOME=/home/app
ENV APP_HOME=/home/app/web

# Create the appropriate directories
RUN mkdir -p $APP_HOME

RUN mkdir $APP_HOME/static
RUN mkdir $APP_HOME/media
RUN mkdir $APP_HOME/media/audio

# Copy project
COPY . $APP_HOME
WORKDIR $APP_HOME

# Install dependencies
RUN apt-get update -y && apt-get install libgdal-dev g++ postgresql-client -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache

CMD sh $APP_HOME/run.sh
