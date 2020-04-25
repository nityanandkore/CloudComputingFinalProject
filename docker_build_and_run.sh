#!/usr/bin/env bash

# Build image

docker build --tag=cloudcomputingfinalproject .


# List docker images

docker image ls


# Run flask app

docker run -p 8000:80 cloudcomputingfinalproject


dockerpath="nityanandkore/cloudcomputingfinalproject"

# Authenticate & Tag

echo "Docker ID and Image: $dockerpath"

docker login &&\

    docker image tag cloudcomputingfinalproject $dockerpath

# Push Image

docker image push $dockerpath 