FROM debian:11
FROM python:3-slim-buster
FROM nikolaik/python-nodejs:latest

WORKDIR /EnmuBot/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get -y install git
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get install libxml2-dev libxslt-dev 

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3", "-m", "EnmuBot"]
