FROM python:3.9-slim
RUN apt update

WORKDIR /opt
COPY requirements.txt .
RUN pip3 install -r requirements.txt && rm requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/opt"

COPY emoji_writer ./emoji_writer
COPY test ./test
