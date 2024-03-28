FROM python:3.10.10-alpine

RUN apk update && \
    apk add --no-cache wget && \
    apk add --no-cache build-base libffi-dev openssl-dev && \
    apk add python3 py3-pip gcc musl-dev

WORKDIR /app
COPY . /app
ENV PYTHONPATH "${PYTHONPATH}:/app/src"
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt
RUN bash start.sh