FROM python:3.13-alpine

# Installing dependencies to build opencv wrappers
RUN apk add --no-cache cmake python3-dev build-base linux-headers
RUN pip install Flask opencv-python-headless

COPY ./ /app

COPY ./docker/start-server.sh /start-server.sh
RUN chmod +x /start-server.sh

WORKDIR /app
EXPOSE 5000
ENTRYPOINT /start-server.sh
