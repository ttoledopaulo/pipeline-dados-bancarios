FROM apache/spark:3.5.1-python3

USER root

WORKDIR /app

COPY src /app/src
COPY data /app/data

ENV PYTHONPATH=/app/src
