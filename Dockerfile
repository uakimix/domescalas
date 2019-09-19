
# pull official base image
FROM python:3

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
WORKDIR /code


COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


