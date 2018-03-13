#!/usr/bin/env bash

if [ -z "$REPO_NAME" ]; then
	REPO_NAME=vasuse7en
fi

if [ -z "$IMAGE_NAME" ]; then
	IMAGE_NAME=geonode_inasafe-headless
fi

if [ -z "$TAG_NAME" ]; then
	TAG_NAME=latest
fi

if [ -z "$BUILD_ARGS" ]; then
	BUILD_ARGS="--pull --no-cache"
fi

# Build Args Environment

if [ -z "$INASAFE_HEADLESS_TAG" ]; then
	INASAFE_HEADLESS_TAG=realtime-backport-cherry-pick
fi

echo "INASAFE_HEADLESS_TAG=${INASAFE_HEADLESS_TAG}"

echo "Build: $REPO_NAME/$IMAGE_NAME:$TAG_NAME"

docker build -t ${REPO_NAME}/${IMAGE_NAME} \
	--build-arg INASAFE_HEADLESS_TAG=${INASAFE_HEADLESS_TAG} \
	${BUILD_ARGS} .
docker tag ${REPO_NAME}/${IMAGE_NAME}:latest ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
docker push ${REPO_NAME}/${IMAGE_NAME}:${TAG_NAME}
