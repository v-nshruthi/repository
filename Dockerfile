# Use official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the app code
COPY app.py .

EXPOSE 5003
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5003"]
