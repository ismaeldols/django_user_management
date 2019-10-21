# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000

# Copy project
COPY . /code/

# Set work directory
WORKDIR /code/

#Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install pipenv

# Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock

#COPY Pipfile Pipfile.lock /code/
RUN pipenv install --skip-lock --system --dev

RUN apt-get update --allow-releaseinfo-change && apt-get install -y netcat
ENTRYPOINT ["/code/entrypoint.sh"]
