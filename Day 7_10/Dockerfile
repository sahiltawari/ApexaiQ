# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port 5000 for external access
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]