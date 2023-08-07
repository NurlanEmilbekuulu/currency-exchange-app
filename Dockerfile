# Use the official Python Alpine image as the base image
FROM python:3.8-alpine

# Set environment variables for Python buffering and Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for building some Python packages
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install the Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Run Django migrations
RUN python manage.py migrate

# Install supervisor
RUN apk add supervisor

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose Gunicorn port
EXPOSE 8000

# Start supervisord to manage Gunicorn, Celery worker, and Celery beat
CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
