# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /application

# Copy the current directory contents into the container at /app
COPY temperature_converter.py .
COPY history.txt .

# # Ensure /data directory exists for volume mounting
# RUN mkdir -p /data

# Command to run the application
CMD ["python", "temperature_converter.py"]