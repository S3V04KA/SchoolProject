#!/bin/sh

SECTION=$1

if [ "$SECTION" == "prod" ]
then
  echo "Running in production mode..."
  docker compose -f docker-compose.prod.yaml up
else
  if [ "$SECTION" == "dev" ]
  then
    echo "Running in development mode..."
    export DOMAIN="localhost"
    docker compose -f docker-compose.dev.yaml up -d
  else
    echo "Error: Invalid section. Please specify 'prod' or 'dev'."
  fi
fi
