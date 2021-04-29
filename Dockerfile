FROM python:3.9-slim
RUN apt update

WORKDIR /opt
COPY requirements.txt .
RUN pip install --upgrade pip==21.0.1 &&\
  pip install -r requirements.txt &&\
  rm requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/opt"

COPY emoji_writer ./emoji_writer
COPY main.py main.py
COPY test ./test
