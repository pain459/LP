#!/bin/bash
echo "[SHUTDOWN] Stopping LLM..."

# Optionally flush buffer to DB here

docker stop llama-llm
docker rm llama-llm
