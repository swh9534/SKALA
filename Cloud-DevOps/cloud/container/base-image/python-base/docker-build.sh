#!/bin/bash
IMAGE_NAME="skala-k8s.base"
VERSION="1.0.1"

# Docker 이미지 빌드
docker build \
  --build-arg CPU_PLATFORM=${CPU_PLATFORM} \
  --tag ${IMAGE_NAME}:${VERSION} \
  --file Dockerfile \
  ${IS_CACHE} .
