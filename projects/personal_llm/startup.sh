#!/bin/bash
echo "[STARTUP] Booting up LLM..."

export PYTHONPATH=/app

# Ensure database exists
python3 scripts/chat_manager.py --init

# Start FastAPI UI in background
nohup python3 ui/main.py > ui.log 2>&1 &

# Launch CLI
python3 scripts/inference.py
