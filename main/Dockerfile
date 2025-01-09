FROM python:3.9-slim-bullseye
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    gcc \
    && apt-get clean

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app