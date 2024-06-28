#!/usr/bin/env bash

set -e

HOST=$1
PORT=$2
shift 2
cmd="$@"

echo "Waiting for $HOST:$PORT to be available..."

while ! nc -z $HOST $PORT; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

echo "$HOST:$PORT is available. Starting the service..."
exec $cmd
