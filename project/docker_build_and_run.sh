#!/usr/bin/env bash



# Build image

docker build --tag=CloudComputingFinalProject .



# List docker images

docker image ls



# Run flask app

docker run -p 8000:80 CloudComputingFinalProject


# Push Image

docker image push $dockerpath 