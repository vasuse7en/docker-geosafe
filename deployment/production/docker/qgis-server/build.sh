#!/usr/bin/env bash
IMAGE_NAME=geonode_qgis-server
TAG_NAME=latest
docker build -t vasuse7en/${IMAGE_NAME} .
docker tag vasuse7en/${IMAGE_NAME}:latest vasuse7en/${IMAGE_NAME}:${TAG_NAME}
docker push vasuse7en/${IMAGE_NAME}:${TAG_NAME}
