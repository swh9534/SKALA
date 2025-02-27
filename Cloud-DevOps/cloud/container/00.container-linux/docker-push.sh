#!/bin/bash

DOCKER_REGISTRY="amdp-registry.skala-ai.com/skala25a"
DOCKER_REGISTRY_USER="robot\$skala25a"
DOCKER_REGISTRY_PASSWORD="1qB9cyusbNComZPHAdjNIFWinf52xaBJ"
DOCKER_CACHE="--no-cache"

IMAGE_NAME="container-linux"
VERSION="1.0"

# 1. Docker 레지스트리에 로그인 (옵션: 이 스크립트를 실행하기 전에 미리 로그인해두어도 됩니다)
echo ${DOCKER_REGISTRY_PASSWORD} | docker login ${DOCKER_REGISTRY} \
	-u ${DOCKER_REGISTRY_USER}  --password-stdin \
   	|| { echo "Docker 로그인 실패"; exit 1; }

# 2. harbor 로 push 하기 위해 tag 추가
docker tag  ${IMAGE_NAME}:${VERSION} ${DOCKER_REGISTRY}/${IMAGE_NAME}:${VERSION}


# Docker 이미지 푸시
# docker push amdp-registry.skala-ai.com/skala25/skala-k8s.base:1.0.0
docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${VERSION} \
	|| { echo "Docker 이미지 푸시 실패"; exit 1; }
