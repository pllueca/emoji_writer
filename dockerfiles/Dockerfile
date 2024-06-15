FROM python:3.12-slim

ARG debug
ARG mode="writer"

RUN echo $debug
RUN apt update

WORKDIR /pip
COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install -r requirements.txt \
  && rm requirements.txt \
  && if [ "${debug}" = "true" ]; then pip install ipdb; fi


WORKDIR /opt
ENV PYTHONPATH "${PYTHONPATH}:/opt"

COPY emoji_writer ./emoji_writer
COPY scripts/main.py main.py
COPY test ./test
