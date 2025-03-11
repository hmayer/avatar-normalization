FROM python:3.13-alpine

# Installing dependencies to build opencv wrappers
RUN apk add --no-cache cmake python3-dev build-base linux-headers

COPY ./ /app
WORKDIR /app

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools pip wheel \
    && CMAKE_BUILD_PARALLEL_LEVEL=$(nproc) pip install -r requirements.txt

COPY ./docker/start-server.sh /start-server.sh
RUN chmod +x /start-server.sh

EXPOSE 5000
ENTRYPOINT /start-server.sh
