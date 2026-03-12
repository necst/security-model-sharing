FROM python:3.12-slim

WORKDIR /poc

RUN apt-get update && apt-get install -y --no-install-recommends bash

RUN pip install --upgrade pip

RUN pip install keras==3.8.0 tensorflow==2.19.0

COPY poc.keras /poc
COPY poc_load.py /poc