#!/bin/bash

# Create Kafka topic
kafka-topics.sh --create --topic chatroom-1 --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
