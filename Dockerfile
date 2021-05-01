FROM python:3.9-slim

ARG debug
ARG mode="writer"

RUN echo $debug
RUN apt update

WORKDIR /opt
COPY requirements.txt .
COPY requirements_server.txt .

RUN pip install --upgrade pip==21.0.1 \
  && pip install -r requirements.txt \
  && rm requirements.txt \
  && if [ "${debug}" = "true" ]; then pip install ipdb; fi \
  && if [ "${mode}" = "server" ]; then pip install --upgrade -r  requirements_server.txt; fi


ENV PYTHONPATH "${PYTHONPATH}:/opt"

COPY emoji_writer ./emoji_writer
COPY main.py main.py
COPY app.py app.py
COPY test ./test
