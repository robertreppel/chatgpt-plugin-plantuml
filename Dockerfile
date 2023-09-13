# Use an official Python runtime based on Debian Buster as the base image
FROM python:3.11-buster

# Set the working directory in the container to /app
WORKDIR /app

# Install Java, wget, and Graphviz
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless wget graphviz && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download the PlantUML JAR
RUN wget "https://sourceforge.net/projects/plantuml/files/plantuml.jar/download" -O plantuml.jar

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5003

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Run the application when the container launches
CMD ["python", "main.py"]
