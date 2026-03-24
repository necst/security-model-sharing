#!/usr/bin/env bash
set -e

IMAGE_NAME="version-adoption-keras"

echo ">>> Building image $IMAGE_NAME..."
docker build -f Dockerfile -t $IMAGE_NAME .. || {
  echo "Build failed!"
  exit 1
}

echo ">>> Running version adoption plot generation..."
docker run --rm \
  -v "$(cd .. && pwd):/app/output" \
  -w /app \
  $IMAGE_NAME bash -c "python plot_generator.py && cp keras_versions.pdf output/"
