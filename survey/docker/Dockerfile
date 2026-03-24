FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends bash

RUN pip install --upgrade pip

RUN pip install pandas==3.0.1 matplotlib==3.10.8

COPY plot_survey.py /app
COPY ["Survey - Model Sharing (Responses) - Form Responses.csv", "/app/"]
COPY survey_script.py /app
