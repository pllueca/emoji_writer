FROM python:3.8-slim
RUN apt update

WORKDIR /opt
COPY . .
RUN pip3 install -r requirements.txt
