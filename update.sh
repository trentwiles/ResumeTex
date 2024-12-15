#!/bin/bash

# Variables
IMAGE_NAME="fastapi-resume"
CONTAINER_NAME="fastapi-resume-container"
PORT=5005

# Stop and remove the existing container
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

# Pull the latest changes from Git
git pull

# Rebuild the Docker image
docker build -t $IMAGE_NAME:latest .

# Run the updated container
docker run -d --name $CONTAINER_NAME -p $PORT:8000 $IMAGE_NAME:latest

echo "Container $CONTAINER_NAME is running on port $PORT with the latest updates."
