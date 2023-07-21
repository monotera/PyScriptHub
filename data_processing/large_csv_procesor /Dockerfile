# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask application runs
EXPOSE 5000

# Set the environment variables
ENV FLASK_APP=app.py

# Run the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
