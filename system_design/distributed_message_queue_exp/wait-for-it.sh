#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available

set -e

TIMEOUT=15
QUIET=0
HOST="$1"
PORT="$2"

echo "Checking $HOST:$PORT..."
for i in $(seq $TIMEOUT) ; do
    if nc -z "$HOST" "$PORT" ; then
        echo "$HOST:$PORT is available after $i seconds."
        exit 0
    fi
    echo "$HOST:$PORT is not available yet..."
    sleep 1
done

echo "$HOST:$PORT is still not available after $TIMEOUT seconds, giving up."
exit 1
