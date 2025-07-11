# Use official Python image as base
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . .

# Collect static files (if needed)
RUN python manage.py collectstatic --noinput

# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Remove default nginx site config
RUN rm /etc/nginx/sites-enabled/default || true

# Expose port 80
EXPOSE 80

# Start Gunicorn and nginx
CMD service nginx start && gunicorn corruption_portal.wsgi:application --bind 127.0.0.1:8000 --workers 3