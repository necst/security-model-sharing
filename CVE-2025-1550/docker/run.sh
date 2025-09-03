#!/usr/bin/env bash
set -e

IMAGE_NAME="kv1"

echo ">>> Building image $IMAGE_NAME..."
docker build -f Dockerfile -t $IMAGE_NAME .. || {
  echo "Build failed!"
  exit 1
}

# Run container with interactive shell
echo ">>> Starting container shell..."
docker run --rm -it \
  -w /poc \
  $IMAGE_NAME bash