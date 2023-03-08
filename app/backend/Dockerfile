FROM python:3.9

ENV PYTHONUNBUFFERED=1

ARG DOCKERIZE_VERSION=v0.6.1

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apt-get update && apt-get install -y gcc fonts-freefont-ttf

RUN pip install gunicorn

RUN pip install daphne

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./ /app/

ENTRYPOINT ["make"]
