FROM python:3.10-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3-pip git build-essential libssl-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

RUN apt update && apt upgrade -y && apt install ffmpeg python3 python3-pip apt-utils -y 

RUN mkdir /Insta-DL
WORKDIR /Insta-DL


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

COPY . .


CMD ["python3", "bot.py"]
