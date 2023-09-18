# Use an official Python runtime based on Debian Buster as the base image
FROM python:3.11-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install Graphviz only
RUN apt-get update && \
    apt-get install -y graphviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5003 available to the world outside this container
EXPOSE 5003

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run the application when the container launches
CMD ["python", "main.py"]
