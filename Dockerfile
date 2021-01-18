FROM python:3.7-alpine

# Update packages
RUN apk update 

# Install python3 libs and pip3
RUN apk add python3-dev libffi-dev libressl-dev openldap-dev

# Add bash
RUN apk add --no-cache bash

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip \
&& pip3 install --upgrade setuptools

# Install certificates store
RUN apk add ca-certificates \
&& rm -rf /var/cache/apk/*

# Expose the flask port
EXPOSE 5000

# Set the environment variables
ENV FLASK_ENV=production
ENV FLASK_APP=app
ENV PYTHONUNBUFFERED=TRUE

# Install app dependencies
COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.diesel.net --extra-index-url https://pypi.diesel.net/ -r requirements.txt

# WSGI integration
COPY gunicorn.py gunicorn.py

# Bundle app source
COPY config.py config.py
COPY util.py util.py
COPY app.py app.py
COPY github.py github.py

ENTRYPOINT ["gunicorn", "--preload", "--config", "gunicorn.py", "app:app"]
