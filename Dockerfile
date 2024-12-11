# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1  # Prevent Python from writing .pyc files
ENV PYTHONUNBUFFERED 1        # Force the stdout and stderr streams to be unbuffered

# Install postgresl client utility
RUN apt-get update && apt-get install -y postgresql-client

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose port 3000 for Django development server
EXPOSE 3000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:3000"]