# base image  
FROM python:3.11-slim-bullseye

# update server software
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENV APPDIR=/usr/src/app

# where your code lives  
WORKDIR $APPDIR

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip

# copy whole project to your docker home directory. 
COPY . $APPDIR

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# port where the Django app runs  
EXPOSE 8000  

# start server 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
