FROM python:latest


WORKDIR /src
COPY . /src

RUN pip install -r requirements.txt
