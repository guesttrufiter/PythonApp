# Use a lightweight official Python runtime image as our base environment
FROM python:3.11-slim

# Set the working directory inside the container container filesystem
WORKDIR /app

# Copy the project dependencies file into the container workspace
COPY requirements.txt .

# Install the Python dependencies specified in requirements.txt without caching
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code into the container
COPY . .

# Expose port 5001 to allow network traffic to the Flask application
EXPOSE 5001

# Specify the default command to run the Python application when container starts
CMD ["python3", "app.py"]