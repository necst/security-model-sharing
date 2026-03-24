#!/usr/bin/env bash
set -e

IMAGE_NAME="survey-plot"

echo ">>> Building image $IMAGE_NAME..."
docker build -f Dockerfile -t $IMAGE_NAME .. || {
  echo "Build failed!"
  exit 1
}

echo ">>> Running survey plot generation..."
docker run --rm \
  -v "$(cd .. && pwd):/app/output" \
  -w /app \
  $IMAGE_NAME bash -c "python plot_survey.py && cp boxplot_updated.pdf output/ && python survey_script.py"
