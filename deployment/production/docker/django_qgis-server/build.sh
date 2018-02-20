#!/usr/bin/env bash
IMAGE_NAME=geonode_django_qgis-server
TAG_NAME=integration
docker build -t vasuse7en/${IMAGE_NAME}:integration .
docker push vasuse7en/${IMAGE_NAME}:${TAG_NAME}
