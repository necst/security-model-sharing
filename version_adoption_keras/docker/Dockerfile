FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends bash

RUN pip install --upgrade pip

RUN pip install pandas==3.0.1 matplotlib==3.10.8

COPY plot_generator.py /app
COPY bquxjob_7e772f9e_1985d03a1ba.csv /app/
