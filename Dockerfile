FROM python:3.7-alpine
# MAINTAINER London App Developer Ltd.

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app /app


#adding new user to not let running the rogram from root
# RUN adduser -D user 
# #running the user
# USER user


