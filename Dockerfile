FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --update --no-cache postgresql-client

# Install build dependencies and libraries
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc \
    libc-dev \
    libpq \
    musl-dev \
    linux-headers \
    postgresql-dev

# Copy and install Python dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Delete dependencies and libraries
RUN apk del .tmp-build-deps

# Create and set working directory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# Create a non-root user
RUN adduser -D user
USER user
